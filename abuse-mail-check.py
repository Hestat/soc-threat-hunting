#!/usr/bin/python3
import urllib
from urllib.parse import unquote
from urllib.parse import urlparse
import re
import sys
import os
import argparse
import subprocess
import webbrowser
import datetime
from tkinter import Tk
from colorama import Fore, Back, Style

#regex for safelink
getURL = re.compile('(?i)https://[^./\r\n]*\.safelinks\.protection\.outlook\.com/\?url=(.*?)&(?:amp;)?data=[0-9]{1,2}%7c[0-9]{1,2}.*?reserved=[0-9]')

#option to include safelink url via sysargs
#decode1 = sys.argv[1]

__authors__ = [ "Brian Laskowski" ]

__date__ = "02-03-19"

__description__ = "Script to scrap safelinks from emails and scan via Urlscan.io Virustotal and Talos Reputation Database. Takes input from the Copy/Paste Buffer, no aruments necessary"

parser = argparse.ArgumentParser(
        description=__description__,
        epilog="Developed by {} on {}".format(", ".join(__authors__), __date__)
)
args = parser.parse_args()


try:
    #hide Tk window
    root =Tk()
    root.withdraw()
    #get safelink from current clipboard content
    getClip = root.clipboard_get()
except:
    print("\nNothing in Clipboard yet\n")

#extract safelink
decodeSearch = getURL.search(getClip)

#set log path via user home dir
homedir = os.path.expanduser('~')

#create log file in append mode
urlReporting = open(homedir+"/abuse-reporting.log", "a+")
urlReporting.close()

try:
    #not sure can't remember
    decodeGroup = decodeSearch.group();
except:
    print('\nNo Safelink found or Copy/Paste buffer is empty, please recopy the safelink or message\n')


#make url human readable
urlDecode = urllib.parse.unquote(decodeGroup)

#remove safelink wrappers
final = urlDecode.split('url=')

#remove safelink wrappers
final2 = final[1].split('&data')

#show unsafety link
print(Fore.GREEN +"Url Extracted:")
print(final2[0])

#save unsafe link
scanTarget = final2[0]

#extract base domain
getDomain = scanTarget.split("//")[-1].split("/")[0]
print(Fore.GREEN +"\nBase Domain:")
print(getDomain)
    
print(Fore.RED + "\nForcepoint Check:")
subprocess.call(["virustotal","-f" +getDomain])

checkLocal = re.compile(getDomain)
logLocal = open(homedir+"/abuse-master.log", "r")
for line in logLocal:
    if re.search(checkLocal, line):
        print(Fore.YELLOW +'\nMatch found, previously reported:')
        print(line),
        matchHit = input(Fore.YELLOW +'\nDo you want to proceed? If not press x to exit.')
        if matchHit == "x" or matchHit == "X":
            sys.exit(1)
        else:
            pass

urlReporting = open(homedir+"/abuse-reporting.log", "r")

for line in urlReporting:
    if re.search(checkLocal, line):
        print(Fore.YELLOW +'\nMatch found, previously reported:')
        print(line),
        matchHit = input(Fore.YELLOW +'\nDo you want to proceed? If not press x to exit.')
        if matchHit == "x" or matchHit == "X":
            sys.exit(1)
        else:
            pass
urlReporting.close()

#check that safelink decode worked and if not allow analyst to add proper url
urlConfirm = input(Fore.WHITE +'\nIs this the URL to check? [y/n]')
if urlConfirm == "n" or urlConfirm == "N":
    scanTarget = input('Please enter the URL you want to scan now:\n')
else:
    pass

#set Talos Rep DB site url
talosSite = str('https://www.talosintelligence.com/reputation_center/lookup?search=')

#Create search string for talos check
talosSearch=talosSite+scanTarget
    
choice = input('\nDo you want to scan with Urlscan.io? [y/n]\nOutput to cmd line\n') 
if choice == "y" or choice == "Y":
    #pass url to urlscan
        subprocess.call(["urlscan %s %s %s %s" %("scan","--url ",scanTarget," --public")], shell=True)
else:
    pass

choice1 = input('\nDo you want to scan with Virustotal? [y/n]\nOutput to cmd line\n')
if choice1 == "y" or choice1 == "Y":
    #pass url to virustotal
    subprocess.call(["virustotal", "-u" +scanTarget])
else:
    pass

choice2 = input('\nDo you want to pull up in Talos Reputation Database? [y/n]\nOpens in browser\n')
if choice2 == "y" or choice2 == "Y":
    #pass url to Talos for check in their reputation database
    webbrowser.open_new(talosSearch)
else:
    pass
    
choice3 = input("\nIs this a true positive? [y/n]")
if choice3 == "y" or choice3 == "Y":
    urlReporting = open(homedir+"/abuse-reporting.log", "a+")
    now = datetime.datetime.now()
    print("writing to file ...")
    print(homedir+"/abuse-reporting.log\n")
    urlReporting.write(scanTarget + " ")
    urlReporting.write(str(now) + "\n")
    urlReporting.close()
else:
    pass

