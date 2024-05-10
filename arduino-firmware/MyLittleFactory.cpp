/**
Library for MK2Robot control and some effectors we use in The Little Factory
see project repo @ https://github.com/Beauchef-Proyecta/mlf

This library has been written following the Arduino documentation and guidelines
https://www.arduino.cc/en/Hacking/LibraryTutorial
https://www.arduino.cc/en/Reference/APIStyleGuide
*/

#include "MyLittleFactory.h"

#include <Arduino.h>
#include <Servo.h>

#include "component_joints.h"

/** Components */

Joint joints[4];
Joint gripper;
Joint extra;
Relay relay_1;
Relay relay_2;
LoadCell load_cell;

void setup_components() {
    joints[0] = Joint(SERVO_J0, HOME_J0);
    joints[1] = Joint(SERVO_J1, HOME_J1);
    joints[2] = Joint(SERVO_J2, HOME_J2);
    joints[3] = Joint(SERVO_J3, HOME_J3);
    relay_1   = Relay(RELAY_1, HOME_RELAY_1);
    relay_2   = Relay(RELAY_2, HOME_RELAY_2);
    load_cell   = LoadCell(CELL_DOUT, CELL_CLK);
    extra     = Joint(EXTRA_SERVO, HOME_EXTRA);
    gripper   = Joint(GRIPPER_SERVO, HOME_GRIPPER);
};

/** Wrapper functions */

int set_joint_position(char params[]) {
    byte res = 0;
    for (int id = 0; id < 4; id++) {
        res += joints[id].set_position((uint8_t)params[id + 1]);
    }
    return (int)res;
};

int set_gripper_position(char params[]) {
    byte res = 0;
    res = gripper.set_position((uint8_t)params[1]);
    return (int)res;
};

int set_extra_position(char params[]) {
    byte res = 0;
    res = extra.set_position((uint8_t)params[1]);
    return (int)res;
};

int set_relay_1_status(char params[]) {
    byte res = 0;
    res = relay_1.set_status((uint8_t)params[1]);
    return (int)res;
};

int set_relay_2_status(char params[]) {
    byte res = 0;
    res = relay_2.set_status((uint8_t)params[1]);
    return (int)res;
};

int get_weight(char _params[]) {
    byte res = 0;
    res = load_cell.get_weight();
    return (int)res; 
}

/** Command List */

func_ptr_t command_list[256] = {};

void build_command_list() { 
    command_list[CMD_JOINT]   = set_joint_position;
    command_list[CMD_RELAY_1] = set_relay_1_status;
    command_list[CMD_RELAY_2] = set_relay_2_status;
    command_list[CMD_EXTRA]   = set_extra_position;
    command_list[CMD_GRIPPER] = set_gripper_position;
    command_list[CMD_WEIGHT] = get_weight;
    
 };

/** COMMUNICATIONS¡ */

void setup_serial() {
    Serial.begin(115200);
    Serial.flush();
    delay(100);
};

bool read_command(char buffer[]) {  // send data only when you receive data:
    int n;
    memset(buffer, 0, 16);
    if (Serial.available() > 1) {
        if (Serial.read() == HEADER) {
            n = Serial.read();
            Serial.readBytes(buffer, n);
            return true;
        }
    }
    return false;
};

int execute_command(char cmd[]) {
    int response = 0xFF;
    if (command_list[cmd[0]] != 0) {
        response = command_list[cmd[0]](cmd);
    }
    Serial.print(cmd[0], HEX);
    Serial.print(response, HEX);
};
