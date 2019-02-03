#!/bin/bash

###############################setup##################################
#choose y/N
yesno(){ read -p "$question " choice;case "$choice" in y|Y|yes|Yes|YES ) decision=1;; n|N|no|No|NO ) decision=0;; * ) echo "invalid" && yesno; esac; }



######################   create formatting #################################
#Creates variable for red color
red='\e[0;31m'
#Creates variable for bold red color
redbold='\e[1;31m'
#Creates variable for green color
green='\e[0;32m'
#Creates variable for yellow color
yellow='\e[1;33m'
#Creates variable for purple color
purple='\e[1;35m'
#Creates variable for no color
whi='\e[0m'
#blue
blue='\e[34m'

div(){
  for ((i=0;i<$1;i++)); do printf '='; done;
}

header(){
	echo -e "\n$(div 80)\n"
}

header2=$(echo -e "$(div 3)")



########################################################################


while getopts "f:F:" opt;do
	case ${opt} in

		f ) #echo -e "Provide the full path of the file to analyze\n"
			#read FILE
			FILE=$OPTARG
			echo
			file $FILE
			HASH1=$(md5sum $FILE)
			HASH2=$(sha1sum $FILE)
			HASH3=$(sha256sum $FILE)
			HASH4=$(ssdeep -s $FILE)
			DATE=$(date)
			echo -e "\nmd5:$HASH1"
			echo -e "sha1:$HASH2"
			echo -e "sha256:$HASH3"
			echo -e "\n$HASH4\n"
			echo -e "File analysis completed on $DATE"
			exit 0;;

		
		F ) #echo "2"
			FILE=$OPTARG
			ENT=$(binwalk -NFE $FILE)
			echo -e "$ENT\n"
		 	exit 0;;

	
	esac
done
