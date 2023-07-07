# READ ME
This repository is meant to send frames from a robot webcam to a browser through webrtc. Other webrtc connections are available.


## Proyect Description
`webcam.py`: Run the server for the signaling and streaming.

`index.html`: Webpage that show the video stream.

`client.js`: Manage the WebRTC connection in the client.

`server.py`: Run the server for robot actions.

# Setting up a new Raspberry Pi

## Upload the OS

Download the Raspberry PI OS installer from the [official page]([https://link-url-here.org](https://www.raspberrypi.com/software/)). Then, grab an empty Micro SD Card and upload the Raspberry Pi OS lite (64 bit) image to the card. Make sure that this OS uses Python 3.9.2!

### Important settings 

Once you have already selected the OS image to upload to the Micro SD, go to the wheel on the bottom left. Perform the following steps:

- [ ] Set hostname to `{ROBOT NAME}.local`
- [ ] Enable SSH and then select `Use password authentication`
- [ ] Select `Set username and password` and then set `Username: pi` and your preferred password (Make sure to remember it!)

Save changes and then upload the OS image to the Micro SD Card.

## Inside the Raspberry Pi

### Connect to your Pi via SSH
Load the card in the Raspberry Pi, connect it to a LAN (we recomend using an ethernet cable) and turn it on. Log into the Raspberry Pi through SSH:

In your own terminal type:
```sh
ssh pi@{ROBOT NAME}.local
```
Enter the password that you selected.

## System settings
Run the `raspi-config` tool as super user:
```sh
sudo raspi-config
```

Perform the following changes (you may want to check the boxes):
- [ ] Update this tool
- [ ] Expand the System
- [ ] Enable Camera (legacy)
- [ ] Change TimeZone

Apply changes, reboot and log again through SSH.

## Install libraries


First of all, update and upgrade `apt`, our package manager:
```sh
sudo apt update
sudo apt upgrade
```
The update part is fast; the upgrade part may take a while, so go grab some coffe if you want :)

Then, install these bad boys:
```sh
sudo apt install build-essential cmake pkg-config git python3-pip python3-dev screen
```

### Install Python3 virtual environments

We will stay with Python 3.9.2 (the default 3.x version that comes with the OS). We now need one of the most important tools to mantain everything stable: virtual environments. This is accomplished by installing `virtualenv` and `virtualenvwrapper`:

```sh
sudo pip3 install virtualenv virtualenvwrapper
```

Now we need to append some environment variables to our `.bashrc` file
```sh
echo "# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh " >> ~/.bashrc
```

now we source them!
```sh
source ~/.bashrc
```
On first run, `virtualenvwrapper` will create some folders
```sh
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/premkproject
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/postmkproject
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/initialize
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/premkvirtualenv
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/postmkvirtualenv
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/prermvirtualenv
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/postrmvirtualenv
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/predeactivate
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/postdeactivate
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/preactivate
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/postactivate
virtualenvwrapper.user_scripts creating /home/student/.virtualenvs/get_env_details
```
Now we are ready to create our virtualenvironment:
```sh
mkvirtualenv mlf -p python3
```
I everything is ok, our terminal shoul have `(mlf)` at the beginning of each line, which meand that the environment has been created and activated.

### Install some Python packages in our environment

Make sure the `mlf` environment is activated. If not, you can type:
```sh
workon mlf
```
`(mlf)` should append to the left of your terminal.

Upgrade pip with the following command:
```sh
pip install --upgrade pip
```
Now, clone this repo in the default folder of your Raspberry Pi.
```sh
git clone https://github.com/Beauchef-Proyecta/mlf-service
```
Execute the next lines:
```sh
cd mlf-service
pip install -r requirements.txt
```

Now everything should work!

## Running 

When you start the example, it will create an HTTP server which you can connect to from your browser or other application:

    $ python webcam.py

### From browser

You can then browse to the following page with your browser:

http://{nombre-pony}.local:8080

Once you click Start the server will send video from its webcam to the browser.

> **Warning** Due to the timing of when Firefox starts responding to mDNS requests and the current lack of ICE trickle support in aiortc, this example may not work with Firefox.

### From other aplication

You can start a webrtc connection sending your RTCSessionDescription to the following page:

    http://{ROBOT NAME}.local:8080/offer

And saving the RTCSessionDescription that it will respond.

For an example see https://github.com/Beauchef-Proyecta/mlf-api


