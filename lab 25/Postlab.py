import serial
import time

arduino = serial.Serial(port='COM16', baudrate=115200, timeout=0.1)
time.sleep(2)  

while True:
    message = input("Enter a message to send: ")
    arduino.write((message + '\n').encode())   
    time.sleep(0.05)
    response = arduino.readline().decode().strip()
    print(response)
