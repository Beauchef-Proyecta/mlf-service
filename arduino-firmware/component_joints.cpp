#include "Arduino.h"
#include "component_joints.h"
#include <string.h>  // Para memcpy

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

uint8_t Relay::set_status(uint8_t status){
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

uint8_t LoadCell::get_weight() {
    double value = this->cell.get_value(10);  // Obtener el valor de la celda como double
    byte b[sizeof(double)];  // Crear un arreglo de bytes del tamaño de un double
    memcpy(b, &value, sizeof(double));  // Copiar el double a un arreglo de bytes

    // Escribir los bytes en el puerto serie
    Serial.write(b, sizeof(double));
    return 0;
};
