#!/bin/sh

# Get info for new tarball
DAY="$(date -I)"
BACKUPDIR="./companyA/IA"
NAME="$DAY-backup-companyA.tar.gz"
TARBALL="$NAME"

# Get checksums of existing backups
EXISTING="$(cksum ./companyA/IA/*backup-companyA.tar.gz)"

# Prepare tarball
tar --exclude=./companyA/IA/*backup-companyA.tar.gz -cpzf "$TARBALL" ./companyA/

# Compare new tarball against existing backups
NEWCK="$(cksum "$TARBALL" | cut -d " " -f 1)"
MATCH="$(echo "$EXISTING" | grep "$NEWCK")"
if [ -z "$MATCH" ] ; then
    cp "$TARBALL" "$BACKUPDIR"
    echo "Created backup $NAME in $BACKUPDIR"
else
    echo "No new changes to companyA. Backup not needed."
fi
