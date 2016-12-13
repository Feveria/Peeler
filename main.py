# Peeler - the scenemusic.net database rip engine.
# ©2016 Artur Szcześniak

import blade
import juicelog as jl
import os


def main():
    os.system("cls")
    nectarine_url = "http://www.scenemusic.net/demovibes/xml/song/"
    songsdir = "songs"
    songstart = 1
    songend = 43602
    l = jl.Juicelog()
    l.logstart()
    for spawn_number in range(songstart, songend + 1):
        razor = blade.Blade(spawn_number, songstart, songend, nectarine_url, songsdir)
        razor.start()


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
