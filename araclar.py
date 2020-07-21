#!/usr/bin/python3

import os,sys
def check_modules():
    try:
        from colorama import Fore, Back, Style
    except:
        print("colorama module is not found ! installion: 'pip3 install colorama' ")
        sys.exit()
check_modules()
def success(message):
    print(Fore.GREEN + "[+] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end="\n")

def error(message):
    print(Fore.RED + "[!] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end="\n")

def status(message):
    print(Fore.BLUE + "[*] " + Style.RESET_ALL + Style.BRIGHT, end="")
    print(message, end="\n")
