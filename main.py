# Peeler - the scenemusic.net database rip engine.
# ©2017 Artur Szcześniak

import blade
import os
import requests
import multiprocessing

cpucont = multiprocessing.cpu_count()

def checksong():
    pass

def main():
    os.system("cls")
    print("Logical cores found: {}".format(cpucont))
    nectarine_url = "http://www.scenemusic.net/demovibes/xml/song/"
    songsdir = "songs"
    songchecknumber = 0
    consecutive404 = 0
    songsnumberlist = []
    while consecutive404 < 10:
        response = requests.get(nectarine_url + str(songchecknumber))
        print("Checking song no. {} ....\r".format(songchecknumber))
        if response.status_code == 404:
            consecutive404 += 1
            songchecknumber += 1
        else:
            songchecknumber += 1
            songsnumberlist.append(songchecknumber)
    print("Reached 10 consecutive 404's.")




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
