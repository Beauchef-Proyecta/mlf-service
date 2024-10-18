#include "HX711.h"

// Pines HX711
const int LOADCELL_DOUT_PIN = 2;  // Pin DT del HX711
const int LOADCELL_SCK_PIN = 3;   // Pin SCK del HX711

HX711 scale;

void setup() {
  Serial.begin(9600);   // Iniciar comunicación serial
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN); // Inicializar el HX711

  // Esperar a que la celda de carga esté lista
  if (scale.wait_ready_retry(10)) {
    Serial.println("Celda de carga lista.");
  } else {
    Serial.println("Error: Celda de carga no conectada.");
  }

  // Calibrar el factor de escala (ajusta según tu configuración)
  scale.set_scale(1922.f);  // El valor de escala debe ser calibrado con la celda de carga
  scale.tare();  // Restar la tara, es decir, poner la balanza a 0
}

void loop() {
  if (scale.is_ready()) {
    // Leer peso
    float weight = scale.get_units(10);  // Obtener el promedio de 10 lecturas

    // Enviar peso por puerto serial
    Serial.println(weight);
  } else {
    Serial.println("Error: no se puede leer la celda de carga.");
  }

  delay(500);  // Esperar medio segundo antes de la siguiente lectura
}
