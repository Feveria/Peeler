# Peeler - the scenemusic.net database rip engine.
# ©2016 Artur Szczesniak

def start():
    print("/start placeholder/")


def welcome_message():
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
    welcome_message()
