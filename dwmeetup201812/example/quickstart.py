import json
import network
import time
import math
import umqtt.simple as simple

sta_if = network.WLAN(network.STA_IF)

orgID = "quickstart"
deviceType = "badge2018"
deviceID = ''.join('{:02X}'.format(c) for c in sta_if.config('mac'))

clientID = "d:" + orgID + ":" + deviceType + ":" + deviceID
broker = orgID + ".messaging.internetofthings.ibmcloud.com"
statusTopic = b"iot-2/evt/status/fmt/json"

def sineVal(minValue, maxValue, duration, count):
    sineValue = math.sin(2.0 * math.pi * count / duration) * (maxValue - minValue) / 2.0
    return "{:.2f}".format(sineValue)

def main():
    c = simple.MQTTClient(clientID, broker)
    c.connect()
    print("https://quickstart.internetofthings.ibmcloud.com/#/device/{}/sensor/".format(deviceID))
    status = {'d': {'sine':{}}}
    count = 0
    try:
        while True:
            status['d']['sine'] = sineVal(-1.0, 1.0, 16, count)
            count += 1
            c.publish(statusTopic, json.dumps(status))
            time.sleep_ms(1000)
    finally:
        c.disconnect()
        print("Disonnected")
