#!/usr/bin/python3
import urllib
from urllib.parse import unquote
from urllib.parse import urlparse
import re
import sys
#from cymon import Cymon
#import domaincytrack

getURL = re.compile(r'url=.*?amp')

decode1 = sys.argv[1]

#test3 = urllib.parse.unquote(decode1)

#print(test3)

decodeSearch = getURL.search(decode1)

str = decodeSearch.group();

strip1 = str.strip('url=')

str = strip1

strip2 = str.strip('&amp')

#print(strip2)

test = urllib.parse.unquote(strip2)
print("\n")
print(test)
print("\n")

