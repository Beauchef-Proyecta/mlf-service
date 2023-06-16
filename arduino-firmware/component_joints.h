#include <Servo.h>
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