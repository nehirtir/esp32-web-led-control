import random
import time

def read_temperature():
    return round(random.uniform(20.0, 30.0), 2)

def read_humidity():
    return round(random.uniform(40.0, 70.0), 2)

print("Starting sensor simulation...")

while True:
    temp = read_temperature()
    hum = read_humidity()

    print(f"Temperature: {temp} °C | Humidity: {hum} %")

    with open("sensor_log.txt", "a") as file:
        file.write(f"Temp: {temp} °C, Humidity: {hum} %\n")

    time.sleep(2)
