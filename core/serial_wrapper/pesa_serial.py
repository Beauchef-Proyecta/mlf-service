import serial
import time

class WeightSensor:
    def __init__(self, port, baud_rate=9600, timeout=1):
        self.serial = serial.Serial(port, baud_rate, timeout=timeout)
        time.sleep(2)  # Wait for the serial connection to initialize

    def get_weight(self):
        self.serial.reset_input_buffer()  # Clear the serial buffer
        while self.serial.in_waiting == 0:
            time.sleep(0.01)  # Wait for new data to arrive

        distance = self.serial.readline().decode('utf-8').strip()
        try:
            return float(distance)
        except ValueError:
            return None

    def close(self):
        self.serial.flushInput()
        self.serial.flushOutput()
        self.serial.close()

# Usage
if __name__ == "__main__":
    sensor = WeightSensor('COM4')  # Update with your port
    try:
        while True:
            distance = sensor.get_weight()
            if distance is not None:
                print(f"Peso: {distance} gramos")
            else:
                print("No se pudo obtener el peso")
    except KeyboardInterrupt:
        print("Exiting program")
    finally:
        sensor.close()