This is a collection of scripts to help SOC analysts perform their duties which often have them querying information from many different sources which can be a strain on time and resources.

Not everything is currently documented here, and many of the scripts require API keys or other external tools to be installed to get fully up and running, will look to make a better install package later, but for now if you can benefit please take and use what you can. Also not all scripts here are in completed form yet.


####################################################

usage: alienvault-check [-h] [-ip IP] [-host HOST] [-url URL] [-hash HASH]
                        [-file FILE]

OTX CLI Example

optional arguments:
  -h, --help  show this help message and exit
  -ip IP      IP eg; 4.4.4.4
  -host HOST  Hostname eg; www.alienvault.com
  -url URL    URL eg; http://www.alienvault.com
  -hash HASH  Hash of a file eg; 7b42b35832855ab4ff37ae9b8fa9e571
  -file FILE  Path to a file, eg; malware.exe

####################################################

usage: cymon-check [-h] [-u URL] [-i IP] [-ha HASH] [-d DOMAIN]

Script to check Cymon for IoC's

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Url to scan in cymon
  -i IP, --ip IP        IP to check in cymon
  -ha HASH, --hash HASH
                        Search a hash in cymon
  -d DOMAIN, --domain DOMAIN
                        Domain to check in cymon

Developed by Brian Laskowski on 09-05-18

####################################################

usage: virustotal [-h] [-u URL] [-i IP] [-ha HASH] [-d DOMAIN]

Script to check Virustotal for IoC's

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Url to submit to Virustotal
  -i IP, --ip IP        IP to check in Virustotal
  -ha HASH, --hash HASH
                        Search a hash in Virustotal
  -d DOMAIN, --domain DOMAIN
                        Domain to check in Virustotal

Developed by Brian Laskowski on 09-04-18

####################################################

usage: urlscan [-h] {init,scan,search,retrieve} ...

Wrapper for urlscan.io's API

positional arguments:
  {init,scan,search,retrieve}
                        commands
    init                initialize urlscan-py with API key
    scan                scan a url
    search              search database for UUID of url
    retrieve            retrieve scan results

optional arguments:
  -h, --help            show this help message and exit

####################################################

usage: shodan [-h] [-i IP]

Script to check against Shodan

optional arguments:
  -h, --help      show this help message and exit
  -i IP, --ip IP  IP to check in Shodan

Developed by Brian Laskowski on 11-8-18

####################################################
