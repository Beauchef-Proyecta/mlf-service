#include "Arduino.h"
#include "component_joints.h"


/** JOINT CLASS */
Joint::Joint(){};

Joint::Joint(int pin, uint8_t position) {
    this->servo.attach(pin);
    int params[] = {pin, position};
    this->set_position(position);
};

uint8_t Joint::set_position(uint8_t position) {
    this->position = position;
    this->servo.write(position);
    return this->position;
};


/** MAGNET CLASS */
Magnet::Magnet(){};

Magnet::Magnet(int pin, int status){
    this->status = status;
    this->pin = pin;
    this->begin();
    this->set_status(this->status);
};

void Magnet::begin(){
    pinMode(this->pin, OUTPUT);
};

uint8_t Magnet::set_status(uint8_t status){
    this->status = status;
    digitalWrite(this->pin, this->status);
    return this->status;
};