# Thread executor of Peeler - the scenemusic.net database rip engine.
# ©2017 Artur Szcześniak
# -*- coding: utf-8 -*-

import threading
import requests
import logging as log
import os.path as op

log.basicConfig(filename="logs/log",
                format='%(asctime)s %(message)s',
                level=20)



class Blade(threading.Thread):
    def __init__(self, song_number, url, songsdir):
        super().__init__()
        self.song_number = song_number
        self.url = url
        self.songsdir = songsdir


    def html_replace(self, unfixed):
        fixed = unfixed.replace("&#39;", "'").replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")
        return fixed


    def run(self):
        while True:
            try:
                if op.isfile(self.songsdir + "/" + str(self.song_number) + ".xml"):
                    log.info("INFO: {}: file exists, skipping.".format(self.song_number))
                    return 0
                else:
                    response = requests.get(self.url + str(self.song_number))
                    response.raise_for_status()
                    with open(self.songsdir + "/" + str(self.song_number) + ".xml", "w+") as xml_file:
                        xml_file.write(self.html_replace(response.text))
                    log.info("INFO: Song {} ripped.".format(self.song_number))
                    return 0
            except requests.ConnectionError as e:
                log.error("ERROR: Connection error.")
                return e
            except requests.HTTPError as he:
                if str(he)[0:3] == "503":
                    log.error("ERROR: Song {}: Received 503.".format(self.song_number))
                    return he
                if str(he)[0:3] == "404":
                    log.error("ERROR: Song {}: Received 404.".format(self.song_number))
                    return he
