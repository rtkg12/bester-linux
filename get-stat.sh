#!/bin/bash

STAT_DIRECTORY="./stats"

rm -rf $STAT_DIRECTORY

mkdir -p $STAT_DIRECTORY

input="machines.txt"
while IFS= read -r var
do
  if [ "$var" != "" ]
  then
    echo "$var"
    #SSHs into all the servers in machines.txt and cats /proc/stat
    ssh -n $USER@$var.cs.wisc.edu cat /proc/stat > $STAT_DIRECTORY/stat-$var
  fi
done < "$input"


