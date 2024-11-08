
import serial
from serial import Serial
import struct
import time
import numpy as np

HEADER          = 0xA0
CMD_JOINT       = 0x10
CMD_BELT        = 0x20
CMD_GRIPPER     = 0x30
CMD_MAGNET      = 0x40
CMD_PROXIMITY   = 0xA0
CMD_LASER       = 0xB0
CMD_WEIGHT      = 0x80

class SerialControl:

    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port
        self.serial = None

    def open_serial(self):
        try:
            self.serial = Serial(self.port, 115200)
            print("The port is available")
            serial_port = "Open"
            time.sleep(2)
        except serial.serialutil.SerialException:
            print("The port is at use")
            self.serial.close()
            self.serial.open()

    def close_serial(self):
        self.serial.close()

    def send_data(self, data, CMD = CMD_JOINT):
        self.serial.write(data)
        time.sleep(0.01)

        if CMD == CMD_WEIGHT:
            response = self.serial.read_until(b'\r\n')
            _ = self.serial.read_until(b'\r\n')
        else:
            response = self.serial.read_until(b'\r\n')
        return response

    def build_serial_msg(self, cmd: int, params: list):
        data = [HEADER, len(params) + 1, cmd]
        for p in params:
            data.append(p)
        return bytearray(data)


if __name__ == "__main__":
    ser = SerialControl("COM4")
    ser.open_serial()

    for i in range(5):
            data = ser.build_serial_msg(0x80, [])
            s = ser.send_data(data, CMD_WEIGHT)
            print(f"Command: 0x80.")
            print(f"Response should be: 23.5")
            print(f"Response: {s.decode().strip()}")
            time.sleep(1)

    for i in range(5):

        angle1 = np.random.randint(0, 180)
        angle2 = np.random.randint(0, 180)
        angle3 = np.random.randint(0, 180)
        angle4 = np.random.randint(0, 180)

        data = ser.build_serial_msg(0x10, [angle1, angle2, angle3, angle4])
        s = ser.send_data(data)
        print(f"Angles: {angle1}, {angle2}, {angle3}, {angle4}")
        print("Response should be: ", (angle1 + angle2 + angle3 + angle4))
        print(f"Response: {s.decode().strip()}")
        time.sleep(1)
    
    for i in range(2):

        data = ser.build_serial_msg(0x50, [i%2])
        s = ser.send_data(data)
        print(f"Command: 0x50. Switch: {i%2}")
        print(f"Response: {s.decode().strip()}")
        time.sleep(1)

    for i in range(2):

        data = ser.build_serial_msg(0x60, [i%2])
        s = ser.send_data(data)
        print(f"Command: 0x60. Switch: {i%2}")
        print(f"Response: {s.decode().strip()}")
        time.sleep(1)


    ser.close_serial()