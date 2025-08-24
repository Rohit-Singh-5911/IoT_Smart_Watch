Smart Watch using ESP32
📖 Overview
This project is a Smart Watch built using the ESP32 microcontroller. The smartwatch integrates multiple features such as time display, stopwatch, temperature monitoring, and pressure monitoring. The user interacts with the system via a touch sensor and a button. Data is displayed on an OLED display, while sensors like LM35 (temperature) and BMP180 (pressure) provide real-time readings.
To ensure stable power delivery, a USB power supply is used to power the ESP32 and peripherals. Additionally, a voltage regulator is integrated to provide 3.3V supply to components that cannot handle 5V, thus preventing overheating and damage.

⚙️ Features
⏰ Time Display (HH:MM:SS) – Shown on OLED when the touch sensor is pressed.
⏱ Stopwatch – Activated after toggling via touch sensor:
Start/Stop/Lap functionality controlled by a button.
🌡 Temperature Monitoring – Using LM35 sensor.
🌬 Pressure Monitoring – Using BMP180 sensor.
⚡ Power Management –
USB supply provides 5V for ESP32 and some devices.
A regulator ensures 3.3V for low-voltage components to prevent overheating.

🛠 Components Used
ESP32 (ESP32 board)
OLED Display
Touch Sensor
Push Button
LM35 Temperature Sensor
BMP180 Pressure Sensor
Voltage Regulator (3.3V output)
USB Power Supply
Jumper Wires & Breadboard

📂 Folder Structure
SmartWatch-ESP32/
│── code/          # Source code (Arduino/PlatformIO)
│── images/        # Circuit diagrams, project images
│── README.md      # Documentation file

🚀 Working Principle
Touch Sensor Input
First Touch → Display Time (HH:MM:SS).
Second Touch → Switch to Stopwatch mode.
Third Touch → Show Temperature.
Fourth Touch → Show Pressure.
Then cycle repeats.

Button Function in Stopwatch Mode
First Press → Start Stopwatch.
Second Press → Stop Stopwatch.
Third Press → Record Lap or Restart.

Power Management
USB power (5V) directly powers ESP32 and compatible components.
Voltage regulator steps down to 3.3V for sensors that require it.


🎯 Future Improvements
Add Bluetooth connectivity for mobile sync.
Add step counter / accelerometer for fitness tracking.
Implement battery-powered design instead of USB supply.

