#!/bin/sh

# Check that screen is running
if screen -ls | grep -q "server" ;
then
  echo "Stoping server"
  screen -S server -X stuff  "^C"
  sleep 0.5
  echo "Terminating screen"
  screen -S server -X stuff  "exit^M"
  sleep 0.5
else
  echo "Screen is not running :)!"
fi

if screen -ls | grep -q "webcam" ;
then
  echo "Stoping webcam"
  screen -S webcam -X stuff  "^C"
  sleep 0.5
  echo "Terminating screen"
  screen -S webcam -X stuff  "exit^M"
  sleep 0.5
else
  echo "Webcam is not running :)!"
fi