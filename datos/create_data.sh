#!/bin/bash
process_files(){                                                                                                
    while IFS= read -r line
    do
        ./get_subs.sh "$line"
        if [ -e peliculas/"$line subs.srt" ]
        then 
            ./process_sub.sh peliculas/"$line subs.srt"
        fi
    done < "$1"
}

mkdir peliculas
process_files "$1"
