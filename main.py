# Peeler - the scenemusic.net database rip engine.
# ©2017 Artur Szcześniak
# -*- coding: utf-8 -*-

import blade
import os

import math
import time
from multiprocessing import cpu_count

nectarine_url = "http://www.scenemusic.net/demovibes/xml/song/"
cpucount = cpu_count()
maxsong = 48000


def main():
    os.system("cls")
    songsdir = "songs"
    for i in range(math.floor(maxsong / cpucount)):
        for j in range(1, cpucount+1):
            worker = blade.Blade(i*j,
                                 nectarine_url,
                                 songsdir)
            worker.start()
            print("Ripping song {}".format(i*j), end='\r')
        time.sleep(0.2)

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
