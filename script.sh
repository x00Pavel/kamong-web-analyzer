#!/bin/bash

while true; do
    curl http://flask:8008 >> /tmp/script-log
    sleep $[ $RANDOM % 20 ]
done