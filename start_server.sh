#!/bin/sh

# Check that screen is running
if screen -ls | grep -q "server" ;
then
  echo "Screen OK! "
else
  echo "Screen is NOT running!"
  echo "Creating screen 'server'"
  screen -dmS server
  sleep 0.5
fi

# Check that server is running
if curl -stderr /dev/null -I http://localhost:5000 | grep -1 "200 OK" ;
then
  echo "Server OK!"
else
  echo "Server is NOT running!"
  screen -S server -X stuff  "workon mlf^M"
  sleep 0.5
  screen -S server -X stuff  "cd $HOME/mlf-service^M"
  sleep 0.5
  echo "Starting server..."
  screen -S server -X stuff  "python core/server.py^M"
  sleep 8
  curl -I http://localhost:5000
fi

# Check that screen is running
if screen -ls | grep -q "webcam" ;
then
  echo "Screen OK! "
else
  echo "Screen is NOT running!"
  echo "Creating screen 'webcam'"
  screen -dmS webcam
  sleep 0.5
fi

# Check if webcam is running
if curl -stderr /dev/null -I http://localhost:8080 | grep -1 "200 OK" ;
then
 echo "Webcam OK!"
else
 echo "Webcam is NOT running!"
 screen -S webcam -X stuff "workon mlf^M"
 sleep 0.5
 screen -S webcam -X stuff "cd $HOME/mlf-service^M"
 sleep 0.5
 echo "Starting webcam..."
 screen -S webcam -X stuff "python core/webcam.py^M"
 sleep 8
 curl -I http://localhost:8080
fi

echo "done"
