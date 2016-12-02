# Thread executor of Peeler - the scenemusic.net database rip engine.
# ©2016 Artur Szcześniak

import threading
import requests
import time
import random


class Blade(threading.Thread):
    def __init__(self, song_number, songstart, songend, url, songsdir):
        super().__init__()
        self.song_number = song_number
        self.songstart = songstart
        self.songend = songend
        self.url = url
        self.songsdir = songsdir

    def html_replace(self, unfixed):
        fixed = unfixed.replace("&#39;", "'").replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
        return fixed

    def run(self):
            while True:
                try:
                    response = requests.get(self.url + str(self.song_number))
                    response.raise_for_status()
                    print("Current song: {}".format(self.song_number))
                    with open(self.songsdir + "/" + str(self.song_number) + ".xml", "w+") as xml_file:
                        xml_file.write(self.html_replace(response.text))
                except requests.ConnectionError as e:
                    print("Connection error: \"{}(...)\", retrying in 5s...".format(str(e.args)[0:50]))
                    time.sleep(5)
                    continue
                except requests.HTTPError as he:
                    #print("HTTP error: \"{}(...)\", skipping song {}.".format(str(he.args)[0:50], self.song_number))
                    print(he)
                    break
                break
