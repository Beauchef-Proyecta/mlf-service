#include <Servo.h>
#include "HX711.h"
#include "Arduino.h"

class Joint {
   private:
    Servo servo;
    int position;

   public:
    Joint();
    Joint(int pin, int position);

    int set_position(int position);
};

class Relay {
  private:
    int status;
    int pin;

  public:
    Relay();
    Relay(int pin, int status);
    
    void begin();
    int set_status(int status);
};

class LoadCell {
  private:
    HX711 cell;
    int dout;
    int clk;

  public:
    LoadCell();
    LoadCell(int dout, int clk);

    int get_weight();

};
