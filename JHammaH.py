import requests
import os
import time
import sys
import subprocess
import datetime
import streamlink

print("\n--------------------------------------------------\n")
print("JHammaH's Twitch View Spoofer\n")
print("--------------------------------------------------\n")
input("Press enter to get all the ducks in a row...")
print("\n")


while True:
    dec1 = input("First off. Is your updated 'proxy_list.txt' file in the same folder as this\nprogram? (y/n):")
    if dec1 == "y":
        break
    elif dec1 != 'y':
        input("\nYou will need to move it there and restart this program. Press Enter\n")
        exit(1)

while True:
    handle = input("\nNext. Enter the twitch channel you want to record:\nwww.twitch.tv/")
    print("")
    dec2 = input("Are you sure you entered '" + handle + "' correctly? (y/n):")
    if dec2 == "y":
        break
    elif dec2 != 'y':
        print("\nLet's try typing that again.\n")

num_viewers = 0
print("\nHow many viewers are you wanting to spoof?")

while 1 > num_viewers or 101 < num_viewers:
        try:
            num_viewers = int(input("Enter a number between 1-100: "))
        except ValueError:
            print("\nI'm pretty sure that isn't a valid number. Try again.")
        if num_viewers >= 101:
            print("\nCan't spoof over 100 viewers! Try again.\n")
        elif num_viewers == 0:
            print("\nWhy would you want to spoof zero viewers? Try again.\n")

print("\n")
print("Ok then. Lets go over the details.\n")
print("You are wanting to make it look like " + str(num_viewers) + " people are watching " + handle + "'s stream.\n")

while True:
    dec3 = input("Does this look right? (y/n)")
    if dec3 == "y":
        break
    elif dec3 != "y":
        input("You're gonna have to re-enter this information then since you messed up. Press Enter")
        exit(1)
