#!/bin/bash

[[ -z $SNIPPETS ]] && echo "SNIPPETS dir undefined" && exit 1

echo "$SNIPPETS"

snip() {
    local name="$1"
    local path="$SNIPPETS/$name"
    if [[ -r $path ]] ; then
        local buffer=$(<$path)
        local -i n=1
        echo "$buffer"
        
    fi
}

snip "$@"
