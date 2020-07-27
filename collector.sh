#!/bin/bash

collect(){
wget -U "$UA" "$URL"
}

helpmenu(){
echo -e "\n===========Download Malware Samples with Spoofed User Agent===========\n"
echo -e "-h --help get this help menu"
echo -e "-u --url provide url you wish to wget"
echo -e "======================================================"
}

# read the options
TEMP=`getopt -o u:U:h:: --long url:,useragent:,help:: -- "$@"`

eval set -- "$TEMP"

while true; do
  case "$1" in
    -h|--help)
      helpmenu
      exit 0;;
    -u|--url)
      URL=$2; shift 2
      echo -e "=== Select a User Agent to Mask as ===\n"
      select opt in win10edge bitsadmin powershell emotet meterpreter quit;do
	      case $opt in 
		      	win10edge)
			UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
			break;;
		      	bitsadmin)
		      	UA="Microsoft BITS/7.8"
			break;;
			powershell)
			UA="Mozilla/5.0 (Windows NT 10.0; Microsoft Windows 10.0.15063; en-US) PowerShell/6.0.0"
			break;;
			emotet)
			UA="Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E)"
			break;;
			meterpreter)
			UA="Mozilla/4.0 (compatible; MSIE 6.1; Windows NT)"
			break;;
			quit)
			exit 0;;
			*)
			echo "Invalid option $RELPY";;
		esac
	done
      collect
      exit 0;;
    -U|--useragent)
      URL=$2; shift 2
      UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
      collect
      exit 0;;
    *) break;;
esac
done
