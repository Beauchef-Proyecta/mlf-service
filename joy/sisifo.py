import sys
 
# setting path
sys.path.append('/home/pi/mlf-service')

from core.serial_wrapper.mk2_serial import MK2Serial
import pickle
import time

def set_magnet(serial, state,relay):
    s = int(state) & 0xFF 
    n = int(relay)

    serial.set_relay_status([s], n)

def set_joints(serial, q):
    s0 = (90 - int(q[0]) * 2) & 0xFF
    s1 = (90 + int(q[1])) & 0xFF
    s2 = (180 - int(q[2]) - int(q[1])) & 0xFF
    s3 = int(q[3]) & 0xFF

    serial.set_joints([s0, s1, s2, s3])


if __name__ == "__main__":
    serial = MK2Serial()
    time.sleep(5)
    # Load the list of joints from the file
    with open('path_joints.pkl', 'rb') as file:
        loaded_path_joints = pickle.load(file)

    # Print the loaded list
    print("Loaded List of Joints")
    while True:
        time.sleep(3)
        for joints in loaded_path_joints:
            if len(joints) == 2:
                state, relay = joints
                time.sleep(1)
                set_magnet(serial, state, relay)
                time.sleep(1)
            else:
                q = joints
                set_joints(serial, q)
                time.sleep(0.2)


        


