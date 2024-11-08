#include "Arduino.h"
#include "component_joints.h"
#include <string.h>  // Para memcpy

/** JOINT CLASS */
Joint::Joint(){};

Joint::Joint(int pin, int position) {
    this->servo.attach(pin);
    int params[] = {pin, position};
    this->set_position(position);
};

int Joint::set_position(int position) {
    this->position = position;
    this->servo.write(position);
    return this->position;
};


/** RELAY CLASS */
Relay::Relay(){};

Relay::Relay(int pin, int status){
    this->status = status;
    this->pin = pin;
    this->begin();
    this->set_status(this->status);
};

void Relay::begin(){
    pinMode(this->pin, OUTPUT);
};

int Relay::set_status(int status){
    this->status = status;
    digitalWrite(this->pin, this->status);
    return this->status;
};


/** LOAD CELL CLASS */
LoadCell::LoadCell(){};

LoadCell::LoadCell(int dout, int clk) {
    this->dout = dout;
    this->clk =clk;
    this->cell.begin(dout, clk);
    this->cell.read(); //espera a estar listo
    this->cell.set_scale();
    this->cell.tare();
};

int LoadCell::get_weight() {
    //double value = this->cell.get_value(10);  // Obtener el valor de la celda como double
    double value = 23.5;
    Serial.println(value);
    return 0;
};
