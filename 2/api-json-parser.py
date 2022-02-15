"""
Lab 2-2
Marko Ruzak CS-1

Module which parses json date recieved from Twitter API
endpoints.
"""
import json


def main_menu(data):
    while True:

        print("Hello! I'm here because I know how to get you\n"
              "info you need from that json fast and safe.\n"
              "Just tell me what are you looking for and I'm gonna take care"
              " about the rest.\n\nSo what you want to do?\n"
              "\t1. Show me a list of all keys in JSON!\n"
              "\t2. Recieve data by given key.\nYour choice: ")
        try:
            choice = int(input())
            if choice == 1:
                display_all_keys(data)
                break
            elif choice == 2:
                pass
            else:
                break
        except ValueError:
            print("It's either 1 or 2 :(")


def display_all_keys(data):
    print("\nHere is the list of all keys in this JSON object.")
    for key in data:
        print(f"\t • {key}")


if __name__ == "__main__":
    file = open("twtdata.json", "r")
    _json = json.load(file)
    file.close()
    main_menu(_json["users"][0])  # we take only one json object.
