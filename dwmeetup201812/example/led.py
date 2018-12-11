import json
import network
import time
import math
import umqtt.simple as simple
from machine import Pin

sta_if = network.WLAN(network.STA_IF)

orgID = "ua3ev8" # <<< org_id 
deviceType = "badge2018"
deviceID = ''.join('{:02X}'.format(c) for c in sta_if.config('mac'))
user = "use-token-auth"
authToken = 'helloiot' # <<< auth_token

clientID = "d:" + orgID + ":" + deviceType + ":" + deviceID
broker = orgID + ".messaging.internetofthings.ibmcloud.com"
statusTopic = b"iot-2/evt/status/fmt/json"
ledCommandTopic = b"iot-2/cmd/led/fmt/json"

# LED
led_red = Pin(17, Pin.OUT, value=0)
led_blue = Pin(16, Pin.OUT, value=0)

def sub_cb(topic, msg):
    obj = json.loads(msg)
    print((topic, msg, obj))
    if topic == ledCommandTopic:
        led_cb(obj)

def led_cb(obj):
  if obj['d']['target'] == "red":
      led = led_red
  elif obj['d']['target'] == "blue":
      led = led_blue
  else:
      print('Unknown target')
      return
  if obj['d']['action'] == "on":
      led.value(1)
  elif obj['d']['action'] == "off":
      led.value(0)
  elif obj['d']['action'] == "toggle":
      led.value(1 if led.value() == 0 else 0)
  else:
      print('Unknown action')
      return

def sineVal(minValue, maxValue, duration, count):
    sineValue = math.sin(2.0 * math.pi * count / duration) * (maxValue - minValue) / 2.0
    return "{:.2f}".format(sineValue)

def main():
    c = simple.MQTTClient(clientID, broker, user=user, password=authToken, ssl=True)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(ledCommandTopic)
    print("Connected, waiting for event")

    status = {'d': {'sine':{}}}
    count = 0
    try:
        while True:
            status['d']['sine'] = sineVal(-1.0, 1.0, 16, count)
            count += 1
            c.publish(statusTopic, json.dumps(status))
            time.sleep_ms(1000)
            #c.wait_msg()
            c.check_msg()
    finally:
        c.disconnect()
        print("Disonnected")
