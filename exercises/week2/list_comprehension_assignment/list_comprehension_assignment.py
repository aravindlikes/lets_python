import os
import re
import sys


def print_items():
    print("\rPrint Items with Folders: ")
    mydir = input("\rEnter Directory: ")
    try:
        paths = os.listdir(mydir)
        if (mydir[len(mydir) - 1] != "\\"):
            mydir += "\\"
        for i in paths:
            print(mydir + i)
    except:
        print("Directory not Found (or) inaccessabile")


def print_items_no_dir():
    print("Print Items without Folders")
    paths = []
    mydir = input("\rEnter Directory: ")
    try:
        for (dirpath, dirnames, filenames) in os.walk(mydir):
            dir = dirpath + "\\"
            paths.extend(filenames)
            break
        for i in paths:
            print(dir + i)
    except:
        print("Directory not Found (or) inaccessabile")


def print_pics():
    print("Print all .png and .jpg files")
    paths = []
    mydir = input("\rEnter Directory: ")
    try:
        for (dirpath, dirnames, filenames) in os.walk(mydir):
            dir = dirpath + "\\"
            paths.extend(filenames)
            break
        for i in paths:
            if i.endswith(".png") or i.endswith(".jpg"):
                print(dir + i)
    except:
        print("Directory not Found (or) inaccessabile")


def print_no_spaces():
    print("Count of number of spaces in a string")
    string = input("\rEnter string: ")
    print("Count of Spaces: ", string.count(' '))


def remove_vowels():
    print("Remove Vowels and Print the String")
    string = input("\rEnter string: ")
    string = re.sub(r'[AEIOU]', '', string, flags=re.IGNORECASE)
    print(string)


def print_less_4():
    print("Print Less 4")
    string = input("\rEnter string: ")
    for word in string.split():
        if (len(word) < 4):
            print(word)


def print_len_of_word():
    print("Print Length of Each Word")
    sentence = input("\rEnter sentence: ")
    for word in sentence.split():
        print(word, "\t", len(word))


def menu():
    print("1. Print Items with Folders\n"
          "2. Print Items without Folders\n"
          "3. Print all .png and .jpg files\n"
          "4. Remove Vowels and Print the String\n"
          "5. Print Less 4\n"
          "6. Count of number of spaces in a string\n"
          "7. Print Length of Each Word\n"
          "8. Exit")
    argument = input("\nEnter Choice: ")
    if argument == '1':
        print_items()
    elif argument == '2':
        print_items_no_dir()
    elif argument == '3':
        print_pics()
    elif argument == '4':
        remove_vowels()
    elif argument == '5':
        print_less_4()
    elif argument == '6':
        print_no_spaces()
    elif argument == '7':
        print_len_of_word()
    elif argument == '8':
        sys.exit()
    else:
        print("Invalid Input")


# Driver program
if __name__ == '__main__':
    menu()
