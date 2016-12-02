# Peeler - the scenemusic.net database rip engine.
# ©2016 Artur Szcześniak

import requests
import time
import threading

def start():
    nectarine_url = "http://www.scenemusic.net/demovibes/xml/song/"
    songsdir = "songs"
    songstart = 1
    songend = 44000
    for song_number in range(songstart, songend):
        while True:
            try:
                response = requests.get(nectarine_url + str(song_number))
                response.raise_for_status()
                print("Current song: {}".format(song_number))
                with open(songsdir + "/" + str(song_number) + ".xml", "w+") as xml_file:
                    xml_file.write(response.text.replace("&#39;","\'").replace("&lt;","\<").replace("&gt;","\>"))
            except requests.ConnectionError as e:
                print("Connection error: \"{}(...)\", retrying in 5s...".format(str(e.args)[0:50]))
                time.sleep(5)
                continue
            except requests.HTTPError as he:
                print("HTTP error: \"{}(...)\", skipping song {}.".format(str(he.args)[0:50], song_number))
                break
            break

def welcome_menu():
    made_choice = False
    print("Welcome to Peeler!",
          "Do you want to start this script? (y/n)\n")
    while not made_choice:
        choice = input()
        if choice in ("y", "Y", "yes", "ye"):
            made_choice = True
            start()
        elif choice in ("n", "N", "no"):
            made_choice = True
            print("Bye!")
            exit()
        else:
            print("Please type \"y\" or \"n\".")

if __name__ == "__main__":
    welcome_menu()
