#!/usr/bin/python3

from __future__ import print_function
import argparse
import hashlib
import os
import requests
import urllib
import json
import simplejson

#def pp_json(json_thing, sort=True, indents=2):
#    if type(json_thing) is str:
#        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
#    else:
#        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
#    return None


vtKey=""
__authors__ = [ "Brian Laskowski" ]

__date__ = "09-04-18"

__description__ = "Script to check Virustotal for IoC's"

parser = argparse.ArgumentParser(
	description=__description__,
	epilog="Developed by {} on {}".format(", ".join(__authors__), __date__)
)

parser.add_argument("-u","--url", help="Url to submit to Virustotal")
parser.add_argument("-i","--ip", help="IP to check in Virustotal")
parser.add_argument("-ha","--hash", help="Search a hash in Virustotal")
parser.add_argument("-d","--domain", help="Domain to check in Virustotal")
args = parser.parse_args()

###IP lookup
if args.ip:
    ipUrl='https://www.virustotal.com/vtapi/v2/ip-address/report'
    parameters = {'ip': '', 'apikey': vtKey}
    parameters["ip"]=args.ip
    response = urllib.request.urlopen('%s?%s' % (ipUrl, urllib.parse.urlencode(parameters))).read()
    response_dict = json.loads(response)
    print(simplejson.dumps(response_dict, indent=4))

###URL Scanning
if args.url:
    params = {'apikey': vtKey, 'url':""}
    params["url"] = args.url
    response = requests.post('https://www.virustotal.com/vtapi/v2/url/scan', data=params)
    json_response = response.json()
    print(simplejson.dumps(json_response, indent=4))

###Hash search
if args.hash:
    params = {'apikey': vtKey, 'resource': ""}
    params["resource"] = args.hash
    headers = {
    "Accept-Encoding": "gzip, deflate",
    "User-Agent" : "gzip,  My Python requests library example client or username"
    }
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',
    params=params, headers=headers)
    json_response = response.json()
    print(simplejson.dumps(json_response, indent=4))

###Domain search
if args.domain:
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    parameters = {'domain': "", 'apikey': vtKey}
    parameters["domain"]= args.domain
    response = urllib.request.urlopen('%s?%s' % (url, urllib.parse.urlencode(parameters))).read()
    response_dict = json.loads(response)
    print(simplejson.dumps(response_dict, indent=4))
