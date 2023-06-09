
import serial
from serial import Serial
import time
import numpy as np

HEADER          = 0xA0
CMD_JOINT       = 0x10
CMD_BELT        = 0x20
CMD_GRIPPER     = 0x30
CMD_MAGNET      = 0x40
CMD_PROXIMITY   = 0xA0
CMD_LASER       = 0xB0

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

    def send_data(self, data):
        self.serial.write(data)
        time.sleep(0.01)
        return self.serial.read(2)

    def build_serial_msg(self, cmd: int, params: list):
        data = [HEADER, len(params) + 1, cmd]
        for p in params:
            data.append(p)
        return bytearray(data)


if __name__ == "__main__":
    ser = SerialControl()
    ser.open_serial()
    i=0
    while True:
        i += 2
        angle1 = int((90 * np.sin(i* np.pi/180))+90) & 0xFF
        angle2 = int((30 * np.sin(2*i* np.pi/180))+90) & 0xFF
        angle3 = int((30 * np.sin(i* np.pi/180))+90) & 0xFF
        i %= 360

        data = ser.build_serial_msg(0x10, [angle1, angle2, angle3])
        s = ser.send_data(data)
        print(f"[{i}: {angle1}]->{s}")