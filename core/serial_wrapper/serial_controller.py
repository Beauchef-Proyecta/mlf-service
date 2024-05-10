import time

from serial import Serial
from serial.serialutil import SerialException

class SerialController:
    def __init__(self, port):
        self.port = port
        self.serial = None

    def open(self):
        try:
            self.serial = Serial(self.port, 115200)
            print("The port is available")
        except SerialException:
            print("The port is at use")
            self.serial.close()
            self.serial.open()

    def close(self):
        self.serial.close()

    def send_data(self, data):
        self.serial.write(data)
        time.sleep(0.01)
        return self.serial.read(2)

    def recv_data(self, cmd, len_data):
        self.serial.write(cmd)
        time.sleep(0.01)
        return self.serial.read(2 + len_data)