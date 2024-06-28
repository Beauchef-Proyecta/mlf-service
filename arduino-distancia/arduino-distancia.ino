
#define TRIGGER 13
#define ECHO 12

void setup() {
  Serial.begin(9600); 
  pinMode(TRIGGER, OUTPUT);
  pinMode(ECHO, INPUT);
}

void loop() {
  long duration, distance;
  
  digitalWrite(TRIGGER, LOW); 
  delayMicroseconds(2); 
  
  digitalWrite(TRIGGER, HIGH);
  delayMicroseconds(10); 
  
  digitalWrite(TRIGGER, LOW);
  
  duration = pulseIn(ECHO, HIGH);
  distance = (duration / 2) / 29.1; 

  Serial.println(distance);
  delay(1000);
}