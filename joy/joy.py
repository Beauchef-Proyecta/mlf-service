import sys
 
# setting path
sys.path.append('/home/pi/mlf-service')

import time

import numpy as np

from evdev import InputDevice, categorize, ecodes
from core.serial_wrapper.mk2_serial import MK2Serial
from core.model.mk2_robot import MK2Model



class RobotJoy():
    def __init__(self, q0=0, q1=0, q2=90, q3=120, dt = 0.1):
        self.serial = MK2Serial()
        time.sleep(5)
        self.model = MK2Model
        self.q  = [q0, q1, q2, q3]
        self.dq = [2, 2, 2, 2]
        self.delay = dt

        # Magnet and relay parameters
        self.state = 0
        self.relay = 1
        self.set_magnet()

        self.device_path = "/dev/input/event0"
        try:
            self.controller = InputDevice(self.device_path)
            print(f"Found {self.controller.name}")

            if self.controller.name == "Microsoft X-Box 360 pad":
                self.analog_max_x = 32512
                self.analog_min_x = -32768
                self.analog_max_y = -32513
                self.analog_min_y = 32767
                self.RZ_max = 255
                self.Z_max = 255

                self.a_button = ecodes.BTN_SOUTH
            else:
                self.analog_max_x = 255
                self.analog_min_x = 0
                self.analog_max_y = 255
                self.analog_min_y = 0

                self.a_button = ecodes.BTN_C

        except FileNotFoundError:
            print(f"Device not found at {self.device_path}. Check the correct event path for your ZD-V+ controller.")
    
    def start(self):
        for event in self.controller.read_loop():
            if event != None:
                if event.type == ecodes.EV_KEY:
                    key_event = categorize(event)
                    self.button_handler(key_event)
                
                elif event.type == ecodes.EV_ABS:
                    abs_event = categorize(event)
                    self.analog_handler(abs_event)
            else:
                continue
    
    def button_handler(self, key_event):
        event = key_event.event

        # MAGNET CODE
        if event.code == self.a_button:
            value = event.value
            if value == 1:
                self.switch_magnet_state()
                print(f"Switch magnet state. Current state: {'Encendido' if self.state == 1 else 'Apagado' }")
                time.sleep(self.delay)
        # Q2 CODE
        if event.code == ecodes.BTN_TR:
            value = event.value
            if value == 1:
                while value == 1:
                    time.sleep(self.delay)
                    if self.q[2] - self.dq[2] > 65 and self.q[2] - self.dq[2] < 145:
                        self.q[2] -= self.dq[2]
                    self.set_joints()
                    print(f"q2 moved up! q2:{self.q[2]}")
                    event = self.controller.read_one()
                    if event != None:
                        break

        if event.code == ecodes.BTN_TL:
            value = event.value
            if value == 1:
                while value == 1:
                    time.sleep(self.delay)
                    if self.q[2] + self.dq[2] > 65 and self.q[2] + self.dq[2] < 145:
                        self.q[2] += self.dq[2]
                    self.set_joints()
                    print(f"q2 moved down! q2:{self.q[2]}")
                    event = self.controller.read_one()
                    if event != None:
                        break

        # Q3 CODE
        if self.controller.name == "Microsoft X-Box 360 pad":
            pass
        else:
            if event.code == ecodes.BTN_Z:
                value = event.value
                if value == 1:
                    while value == 1:
                        time.sleep(self.delay)
                        if self.q[3] + self.dq[3] > 10 and self.q[3] + self.dq[3] < 170:
                            self.q[3] += self.dq[3]
                        self.set_joints()
                        print(f"q3 moved right! q3:{self.q[3]}")
                        event = self.controller.read_one()
                        if event != None:
                            break
            if event.code == ecodes.BTN_WEST:
                value = event.value
                if value == 1:
                    while value == 1:
                        time.sleep(self.delay)
                        if self.q[3] - self.dq[3] > 10 and self.q[3] - self.dq[3] < 170:
                            self.q[3] -= self.dq[3]
                        self.set_joints()
                        print(f"q3 moved down! q3:{self.q[3]}")
                        event = self.controller.read_one()
                        if event != None:
                            break

    def analog_handler(self, abs_event):
        event = abs_event.event

        if event.code == ecodes.ABS_X:
            x_value = event.value

            if x_value == self.analog_max_x:
                while x_value == self.analog_max_x:
                    time.sleep(self.delay)
                    if self.q[0] - self.dq[0] > -45 and self.q[0] - self.dq[0] < 45:
                        self.q[0] -= self.dq[0]
                    self.set_joints()
                    print(f"Moved to the left! q0:{self.q[0]}")
                    abs_event = self.controller.read_one()
                    if abs_event:
                        if abs_event.type == ecodes.EV_ABS:
                            abs_event = categorize(abs_event)
                            event = abs_event.event
                            x_value = event.value

            elif x_value == self.analog_min_x:
                while x_value == self.analog_min_x:
                    time.sleep(self.delay)
                    if self.q[0] + self.dq[0] > -45 and self.q[0] + self.dq[0] < 45:
                        self.q[0] += self.dq[0]
                    self.set_joints()
                    print(f"Moved to the right! q0:{self.q[0]}")
                    abs_event = self.controller.read_one()
                    if abs_event != None:
                        if abs_event.type == ecodes.EV_ABS:
                            abs_event = categorize(abs_event)
                            event = abs_event.event
                            x_value = event.value
        if event.code == ecodes.ABS_Y:
            y_value = abs_event.event.value
            if y_value == self.analog_max_y:
                while y_value == self.analog_max_y:
                    time.sleep(self.delay)
                    if self.q[1] - self.dq[1] > -30 and self.q[1] - self.dq[1] < 62:
                        self.q[1] -= self.dq[1]
                    self.set_joints()
                    print(f"Moved to the left! q1:{self.q[1]}")
                    abs_event = self.controller.read_one()
                    if abs_event != None:
                        if abs_event.type == ecodes.EV_ABS:
                            abs_event = categorize(abs_event)
                            event = abs_event.event
                            y_value = event.value

            elif y_value == self.analog_min_y:
                while y_value == self.analog_min_y:
                    time.sleep(self.delay)
                    if self.q[1] + self.dq[1]> -30 and self.q[1] + self.dq[1] < 62:
                        self.q[1] += self.dq[1]
                    self.set_joints()
                    print(f"Moved to the right! q1:{self.q[1]}")
                    abs_event = self.controller.read_one()
                    if abs_event != None:
                        if abs_event.type == ecodes.EV_ABS:
                            abs_event = categorize(abs_event)
                            event = abs_event.event
                            y_value = event.value

        if self.controller.name == "Microsoft X-Box 360 pad":
            if event.code == ecodes.ABS_RZ:
                tr_value = event.value

                if tr_value == self.RZ_max:
                    while tr_value == self.RZ_max:
                        time.sleep(self.delay)
                        if self.q[3] + self.dq[3] > 10 and self.q[3] + self.dq[3] < 170:
                            self.q[3] += self.dq[3]
                        self.set_joints()
                        print(f"Moved to the left! q3:{self.q[3]}")
                        abs_event = self.controller.read_one()
                        if abs_event:
                            abs_event = categorize(abs_event)
                            event = abs_event.event
                            tr_value = event.value
            elif event.code == ecodes.ABS_Z:
                tr_value = event.value

                if tr_value == self.Z_max:
                    while tr_value == self.Z_max:
                        time.sleep(self.delay)
                        if self.q[3] - self.dq[3] > 10 and self.q[3] - self.dq[3] < 170:
                            self.q[3] -= self.dq[3]
                        self.set_joints()
                        print(f"Moved to the left! q3:{self.q[3]}")
                        abs_event = self.controller.read_one()
                        if abs_event:
                            abs_event = categorize(abs_event)
                            event = abs_event.event
                            tr_value = event.value
    
    def set_joints(self):
        s0 = (90 - int(self.q[0]) * 2) & 0xFF
        s1 = (90 + int(self.q[1])) & 0xFF
        s2 = (180 - int(self.q[2]) - int(self.q[1])) & 0xFF
        s3 = int(self.q[3]) & 0xFF
        self.serial.set_joints([s0, s1, s2, s3])
    
    def switch_magnet_state(self):
        if self.state == 1:
            self.state = 0
            self.set_magnet()
        elif self.state == 0:
            self.state = 1
            self.set_magnet()

    def set_magnet(self):
        s = int(self.state) & 0xFF 
        n = int(self.relay)
        self.serial.set_relay_status([s], n)



if __name__ == "__main__":
    joy = RobotJoy(dt=0.1)
    joy.start()
