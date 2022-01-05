#!/bin/bash

get_link(){
    movie_name_search=$(printf "$1" | sed -e 's\ \+\g')
    movie_name_grep=$(printf "$1" | sed -e 's\ \-\g')

    link=$(curl -s "https://www.subdivx.com/index.php?accion=5&masdesc=&buscar2=$1&oxdown=1" | 
        grep -o "https://www.subdivx.com/[^']*-$movie_name_grep[^']*.html")
    read link <<< "$link"

    link=$(curl -s "$link" | grep -o "bajar.php?id=[^']*&u=[^']")

    printf "$link"
    return 0
} 

uncompress(){
    mkdir "$1 subs dir"
    mv "$1 subs" "$1 subs dir"

    cd "$1 subs dir"
    if [ $extension == "application/x-rar" ];then
        unrar x "$1 subs"
    else
        unzip "$1 subs"
    fi

     cd ..
     return 0
}

create_subs(){
    cd tmp
    declare -i count
    count=0

    for file in ./*.srt
    do
        if [ $count -eq 0 ]
        then
            mv "$file" "$1 subs.srt"
        else
            cat "$file" >> "$1 subs.srt"
        fi

        count+=1

    done

    mv "$1 subs.srt" ..

    cd ..
    rm -r tmp

}


get_file(){
    wget -O "$2 subs" --referer https://subdivx.com/ "https://www.subdivx.com/$1"
    extension=$(file --mime-type -b "$2 subs")

    uncompress "$2"

    mkdir tmp
    mv "$2 subs dir"/*.srt tmp

    create_subs "$2"

    mv "$2 subs".srt peliculas

    rm -r "$2 subs dir"

     # mkdir "$2 subs dir"
     # mv "$2 subs.srt" "$2 subs dir"
}

link=$(get_link "$1")
if [ ! -z "$link" ]
then
    get_file "$link" "$1"
fi


