# mlf-service
Send frames from a robot webcam to a browser through webrtc. Other webrtc connections are available.

## Running 

First install the requirements 

    $ pip install -r requirements.txt

When you start the example, it will create an HTTP server which you can connect to from your browser or other application:

    $ python webcam.py

### From browser

You can then browse to the following page with your browser:

http://{nombre-pony}.local:8080

Once you click Start the server will send video from its webcam to the browser.

Warning

Due to the timing of when Firefox starts responding to mDNS requests and the current lack of ICE trickle support in aiortc, this example may not work with Firefox.

### From other aplication

You can start a webrtc connection sending your RTCSessionDescription to the following page:

    http://{nombre-pony}.local:8080/offer

And saving the RTCSessionDescription that it will respond.

For an example see https://github.com/Beauchef-Proyecta/mlf-api

## Proyect Description
webcam.py: Run the server for the signaling and streaming.

index.html: Webpage that show the video stream.

client.js: Manage the WebRTC connection in the client.

## Agregar offsets
ejecutar el siguiente comando

    $ echo 'export OFFSETS = "<offset1>,<offset2>,<offset3>,<offset4>"' >> ~/.bashrc
Para editar o eliminarlas

    $ nano ~/.bashrc
y al final del archivo hay que editarlas.