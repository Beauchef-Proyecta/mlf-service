#include <Servo.h>
#include "HX711.h"
#include "Arduino.h"

class Joint {
   private:
    Servo servo;
    uint8_t position;

   public:
    Joint();
    Joint(int pin, uint8_t position);

    uint8_t set_position(uint8_t position);
};

class Relay {
  private:
    int status;
    int pin;

  public:
    Relay();
    Relay(int pin, int status);
    
    void begin();
    uint8_t set_status(uint8_t status);
};

class LoadCell {
  private:
    HX711 cell;
    int dout;
    int clk;

  public:
    LoadCell();
    LoadCell(int dout, int clk);

    uint8_t get_weight();

};


class DistanceSensor {
  private:
    int trigger_pin;
    int echo_pin;

  public:
    DistanceSensor();
    DistanceSensor(int trigger_pin, int echo_pin);

    uint8_t get_distance();

};