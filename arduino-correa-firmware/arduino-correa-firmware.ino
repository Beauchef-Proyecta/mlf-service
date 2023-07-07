#include <Wire.h>

#define ENCODER   4
#define PUENTEH_1 11
#define PUENTEH_2 7

const int MY_ADDRESS = 2;
const int ROBOT_ARDUINO_ADDRESS = 1;
bool encoder;

void setup() {
  setup_components();
  setup_communications();
}

void loop() {
  Wire.beginTransmission(ROBOT_ARDUINO_ADDRESS);
  encoder = readEncoder();
  Wire.write(encoder);
  Wire.endTransmission();
}

void setup_communications() {
  Wire.begin(MY_ADDRESS);
  Serial.begin(115200);
  Wire.onReceive(moveBelt);
}

void setup_components() {
  pinMode(ENCODER, INPUT);
  pinMode(PUENTEH_1, OUTPUT);
  pinMode(PUENTEH_2, OUTPUT);

  digitalWrite(PUENTEH_1, LOW);
  digitalWrite(PUENTEH_2, LOW);
}

void moveBelt(int byteCount) {
  while (Wire.available()){
    byte receivedData = Wire.read(); // lee lo que llega
  }
}

