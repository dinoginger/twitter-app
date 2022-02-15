"""
Lab 2-2
Marko Ruzak CS-1

Module which parses json date recieved from Twitter API
endpoints.
"""
import json
from time import sleep


def menu(data, depth, obj):
    data = data
    depth = depth
    obj = obj
    while True:
        try:
            print(f"!!!CURENT DEPTH : {depth}!!!\n!!!CURRENT OBJECT: {obj}!!!")
            print("\nWhat's next?\n"
                  "\t1. Show me a list of all keys in this object!!\n"
                  "\t2. Recieve data by given key.\n"
                  f"\t3. Exit level {depth}\n"
                  "Your choice: ")
            choice = int(input())
            if choice == 1:
                print("\nHere is the list of all keys in this JSON object.")
                display_items(data)
            elif choice == 2:
                get_info(data, depth, obj)
            elif choice == 3:
                return
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


def display_items(data):
    if type(data) == dict:
        for key in data.keys():
            print(f"\t • {key}")
    elif type(data) == list:
        for value in data:
            print(f"\t • {value} ({type(value)})")


def get_info(data, depth, obj):
    print(f"\tCURRENT DEPTH {depth}\nCURRENT OBJECT: {obj}\nOkay, input the key you want to get value of:\n")
    try:
        key = input()

        if type(data[key]) == list:
            print("Value is a list.")
            if len(data[key]) == 0:
                print("\t", data[key])

            display_items(data[key])
            print("")

        elif type(data[key]) == dict:
            print("Value is an object.\nDo you want to see the list of its keys?\n"
                  "\t1. Yes\n"
                  "\t2. No\nYour choice:")
            try:
                choice = int(input())
            except ValueError:
                print("Wrong choice. Returning to menu...")
                return

            if choice == 1:
                display_items(data[key])
                menu(data[key], depth + 1, key)

            elif choice == 2:
                print("Returning to menu....")
                return
            else:
                print("Wrong choice. Returning to menu...")
                return
        else:
            print(f"Value by key \"{key}\":")
            print(f"\t{data[key]}")
    except KeyError:
        print("Wrong key entered.")
        return


def main():
    depth = 0
    file = open("twtdata.json", "r")
    _json = json.load(file)
    file.close()
    data = _json["users"][0]
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
                display_items(data)
            elif choice == 2:
                get_info(data, depth, "main")
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


if __name__ == "__main__":
    main()
