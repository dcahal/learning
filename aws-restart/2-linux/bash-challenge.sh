#!/bin/bash

if [ -e ./grok00 ] ; then
    first=$(find grok* | tail -n 1 | cut -c 6-9)
else
    first="00"
fi
last=$((first+25))
eval touch grok{$first..$last}
