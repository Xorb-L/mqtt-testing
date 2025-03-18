import network
import time
from umqtt.simple import MQTTClient

# WiFi-inställningar
SSID = "SSID_HERE!" # gonna try to do an env file for this 
PASSWORD = "PASSWORD_HERE!" # same for the password

# MQTT-inställningar
MQTT_BROKER = "IP_TO_BROKER_SERV_HERE"  # Change to for example your pi zero 2w's IP
MQTT_TOPIC = "sensor/temperature"

# Anslut till Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Ansluter till Wi-Fi...")  # translation: connecting to wifi
    time.sleep(1)

print("Wi-Fi anslutet!") # wifi connected

# Anslut till MQTT-broker
client = MQTTClient("pico_sensor", MQTT_BROKER)
client.connect()
print("Ansluten till MQTT!")

# Publicera sensorvärden
while True:
    temperature = 22.5  # Simulerad temperatur
    client.publish(MQTT_TOPIC, str(temperature))
    print(f"Publicerade: {temperature} °C")
    time.sleep(5)
