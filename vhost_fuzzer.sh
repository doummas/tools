#!/bin/bash

show_help(){
	echo "usage for the vhost fuzzer"
	echo " $0 <wordlists> <url> <domain> <fs filter>"
	echo " set the fs filter in the beginnig any number then change it"
	echo " -h, --help show help"
	echo " github repo => 'https://github.com/doummas'"
}
if [[ "$1" == "-h" || "$1" == "--help" ]]; then
	show_help
	exit 0 
fi

if [ "$#" -ne 4 ]; then
    echo "Error: Missing or incorrect arguments."
    show_help
    exit 1
fi
wordlists="$1"
url="$2"
domain="$3"
fs="$4"

ffuf -w "$wordlists" -u "$url" -H "HOST: FUZZ.$domain" -fs "$fs"
