# Peeler - the scenemusic.net database rip engine.
# ©2017 Artur Szcześniak

import blade
import threading
import os
import urllib.request as req
import urllib.error as urlerr
import queue
from multiprocessing import cpu_count

nectarine_url = "http://www.scenemusic.net/demovibes/xml/song/"
cpucount = cpu_count()
songsnumberlist = []


class CheckWorker(threading.Thread):
    """Class that defines thread worker for performsongcheck function"""

    def __init__(self, songchecknumber, queue):
        self.songchecknumber = songchecknumber
        super().__init__()
        self.queue = queue

    def run(self):
        try:
            response = req.urlopen(nectarine_url + str(self.songchecknumber))
            print("Checking song no. {} ....\r".format(self.songchecknumber))
            songsnumberlist.append(self.songchecknumber)
        except urlerr.HTTPError as e:
            print("Song: {} Error: {}\r".format(self.songchecknumber, e.code))
            self.queue.put(0)


def getsonglist():
    """Function that allows to check which songs are available"""
    currentsong = 0
    threads = []
    kolejka = queue.Queue()
    while True:
        for x in range(currentsong, currentsong + cpucount):
            t = CheckWorker(x, kolejka)
            threads.append(t)

        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        if kolejka.qsize() >= cpucount:
            break
        else:
            currentsong += cpucount
            threads = []
            while not kolejka.empty():
                kolejka.get()
    print(songsnumberlist)


def main():
    os.system("cls")
    songsdir = "songs"
    getsonglist()


def welcome_menu():
    os.system("cls")
    made_choice = False
    print("Welcome to Peeler!",
          "Do you want to start this script? (y/n)\n")
    while not made_choice:
        choice = input()
        if choice in ("y", "Y", "yes", "ye"):
            made_choice = True
            main()
        elif choice in ("n", "N", "no"):
            made_choice = True
            os.system("cls")
            print("Bye!")
            exit()
        else:
            print("\nPlease type \"y\" or \"n\".")


if __name__ == "__main__":
    welcome_menu()
