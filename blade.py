# Thread executor of Peeler - the scenemusic.net database rip engine.
# ©2016 Artur Szcześniak

import threading
import requests
import time
import random
import juicelog as jl
import os.path as op


class Blade(threading.Thread):
    def __init__(self, song_number, songstart, songend, url, songsdir):
        super().__init__()
        self.song_number = song_number
        self.songstart = songstart
        self.songend = songend
        self.url = url
        self.songsdir = songsdir
        self.log = jl.Juicelog()

    def html_replace(self, unfixed):
        fixed = unfixed.replace("&#39;", "'").replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
        return fixed

    def run(self):
        while True:
            try:
                response = requests.get(self.url + str(self.song_number))
                response.raise_for_status()
                self.log.logsong(self.song_number)
                if op.isfile(self.songsdir + "/" + str(self.song_number) + ".xml"):
                    self.log.logerror("{}: file exists, skipping.".format(self.song_number))
                    break
                else:
                    with open(self.songsdir + "/" + str(self.song_number) + ".xml", "w+") as xml_file:
                        xml_file.write(self.html_replace(response.text))
                    print("Ripped song: {}                                         ".format(self.song_number), end="\r")

                    break
            except requests.ConnectionError as e:
                #print("Connection error: \"{}(...)\", retrying in 5s...".format(str(e.args)[0:50]), end="\r")
                self.log.logerror("Connection error: \"{}(...)\", retrying in 5s...".format(str(e.args)[0:50]))
                time.sleep(5)
                continue
            except requests.HTTPError as he:
                #print("HTTP error: \"{}(...)\", skipping song {}.".format(str(he.args)[0:50], self.song_number))
                if str(he)[0:3] == "503":
                    wait_time = random.randrange(0, 10)
                    #print("{}: Received 503, retrying in {}...".format(self.song_number, wait_time))
                    self.log.logerror("{}: Received 503, retrying in {}...".format(self.song_number, wait_time))
                    time.sleep(wait_time)
                    continue
                if str(he)[0:3] == "404":
                    print("Received 404, skipping song {}.".format(self.song_number))
                    break


