import time

from serial import Serial
from serial.serialutil import SerialException
import struct

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
    
    def recv_response(self, cmd, payload):
        assert cmd.to_bytes(1, 'big') == self.serial.read(1)
        len_data = struct.unpack('b',self.serial.read(1))[0]
        response = self.serial.read(len_data)
        self.serial.read(1) == payload.to_bytes(1, 'big')
        return response
        