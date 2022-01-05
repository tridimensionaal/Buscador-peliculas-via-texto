#!/bin/bash

process_sub(){
    type_f=$(file "$1" | grep -o "ISO-8859")

    if [ ! -z "$type_f" ]
    then
        mv "$1" "$1.tmp"
        iconv -f ISO-8859-1 -t UTF-8//TRANSLIT "$1.tmp" > "$1"
        rm "$1.tmp"
        dos2unix "$1"

        sub_time="[0-9][0-9]:[0-9][0-9]:[0-9][0-9],[0-9][0-9][0-9]"
        # remove time sub

        sed -i "/$sub_time --> $sub_time/d" "$1"
        # remove number sub
        sed -i "/[0-9]\+/d" "$1"

        # remove number sub
        sed -i "s/<i>//g" "$1"
        sed -i "s/<\/i>//g" "$1"

    else
        rm "$1"
    fi

}

process_sub "$1"


