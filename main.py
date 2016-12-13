# Peeler - the scenemusic.net database rip engine.
# ©2016 Artur Szcześniak

import blade
import juicelog as jl




def main():
    nectarine_url = "http://www.scenemusic.net/demovibes/xml/song/"
    songsdir = "songs"
    songstart = 1
    songend = 1000
    l = jl.Juicelog()
    l.logstart()
    for spawn_number in range(songstart, songend):
        razor = blade.Blade(spawn_number, songstart, songend, nectarine_url, songsdir)
        razor.start()



def welcome_menu():
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
            print("Bye!")
            exit()
        else:
            print("Please type \"y\" or \"n\".")


if __name__ == "__main__":
    welcome_menu()
