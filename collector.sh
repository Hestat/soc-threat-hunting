#!/bin/bash



collect(){
wget -U "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246" "$URL"
}

helpmenu(){
echo -e "\n===========Download Malware Samples with Spoofed User Agent===========\n"
echo -e "-h --help get this help menu"
echo -e "-u --url provide url you wish to wget"
echo -e "======================================================"
}

# read the options
TEMP=`getopt -o u:h:: --long url:,help:: -- "$@"`

eval set -- "$TEMP"

while true; do
  case "$1" in
    -h|--help)
      helpmenu
      exit 0;;
    -u|--url)
      URL=$2; shift 2
      collect
      exit 0;;
    *) break;;
esac
done
