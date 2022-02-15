"""
Lab 2-2
Marko Ruzak CS-1

Module which parses json date recieved from Twitter API
endpoints.
"""
import json
from time import sleep

def main_menu(data):


    print("Hello! I'm here because I know how to get you\n"
          "info you need from that json fast and safe.\n"
          "Just tell me what are you looking for and I'm gonna take care"
          " about the rest.\n\nSo what you want to do?\n"
          "\t1. Show me a list of all keys in JSON!\n"
          "\t2. Recieve data by given key.\n"
          "\t3. Exit program."
          "Your choice: ")
    while True:
        try:
            choice = int(input())
            if choice == 1:
                print("\nHere is the list of all keys in this JSON object.")
                display_all_keys(data)
                break
            elif choice == 2:
                get_info(data)
            elif choice == 3:
                quit()
            else:
                print("It's either 1, 2 or 3 :(")
            sleep(1.25)
            print("\nWhat's next?\n"
                    "\t1. Show me a list of all keys in JSON!\n"
                    "\t2. Recieve data by given key.\n"
                  "\t3. Exit\n"
                  "Your choice: ")
        except ValueError:
            print("It's either 1, 2 or 3 :(")


def display_all_keys(data):
    for key in data:
        print(f"\t • {key}")


def get_info(data):
    print("Okay, input the key you want to get value of:\n")
    try:
        key = input()
    except KeyError:
        print("Wrong key entered.")
        return

    if type(data[key]) == list:
        pass
    elif type(data[key]) == dict:
        pass
    else:
        print(f"Value by key \"{key}\":")
        print(f"\t{data[key]}")



if __name__ == "__main__":
    file = open("twtdata.json", "r")
    _json = json.load(file)
    file.close()
    main_menu(_json["users"][0])  # we take only one json object.
