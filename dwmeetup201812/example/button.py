import json
import network
import time
import math
import umqtt.simple as simple
from machine import Pin
import ugfx

sta_if = network.WLAN(network.STA_IF)

orgID = "ua3ev8" # <<< org_id 
deviceType = "badge2018"
deviceID = ''.join('{:02X}'.format(c) for c in sta_if.config('mac'))
user = "use-token-auth"
authToken = 'helloiot' # <<< auth_token

clientID = "d:" + orgID + ":" + deviceType + ":" + deviceID
broker = orgID + ".messaging.internetofthings.ibmcloud.com"
buttonTopic = b"iot-2/evt/button/fmt/json"
statusTopic = b"iot-2/evt/status/fmt/json"
colorCommandTopic = b"iot-2/cmd/color/fmt/json"
ledCommandTopic = b"iot-2/cmd/led/fmt/json"

# LED
led_red = Pin(17, Pin.OUT, value=0)
led_blue = Pin(16, Pin.OUT, value=0)

# ugfx
ugfx.init()
ugfx.input_init()
ugfx.clear(ugfx.BLACK)

# Button 

def btn_cb(c, key, pressed):
  event = {'d': {'char': key, 'type': 'keydown' if pressed else 'keyup' }}
  print((buttonTopic, key, event))
  c.publish(buttonTopic, json.dumps(event))

def sub_cb(topic, msg):
    obj = json.loads(msg)
    print((topic, msg, obj))
    if topic == ledCommandTopic:
        led_cb(obj)
    elif topic == colorCommandTopic:
        color_cb(obj)

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

prev_color = ""
def color_cb(obj):
  global prev_color
  if obj['d']['color'] == "red":
      color = ugfx.RED
  elif obj['d']['color'] == "green":
      color = ugfx.GREEN
  elif obj['d']['color'] == "blue":
      color = ugfx.BLUE
  elif obj['d']['color'] == "gray":
      color = ugfx.GRAY
  elif obj['d']['color'] == "yellow":
      color = ugfx.YELLOW
  elif obj['d']['color'] == "orange":
      color = ugfx.ORANGE
  elif obj['d']['color'] == "purple":
      color = ugfx.PURPLE
  elif obj['d']['color'] == "black":
      color = ugfx.BLACK
  elif obj['d']['color'] == "white":
      color = ugfx.WHITE
  else:
      try:
        color = int(obj['d']['color'])
      except:
        print('Unknown color')
        return
  if prev_color != color:
      ugfx.clear(color)
      prev_color = color

def sineVal(minValue, maxValue, duration, count):
    sineValue = math.sin(2.0 * math.pi * count / duration) * (maxValue - minValue) / 2.0
    return "{:.2f}".format(sineValue)

def main():
    c = simple.MQTTClient(clientID, broker, user=user, password=authToken, ssl=True)
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(colorCommandTopic)
    c.subscribe(ledCommandTopic)
    # init input button 
    ugfx.input_attach(ugfx.JOY_UP, lambda pressed: btn_cb(c, 'U', pressed))
    ugfx.input_attach(ugfx.JOY_DOWN, lambda pressed: btn_cb(c, 'D', pressed))
    ugfx.input_attach(ugfx.JOY_LEFT, lambda pressed: btn_cb(c, 'L', pressed))
    ugfx.input_attach(ugfx.JOY_RIGHT, lambda pressed: btn_cb(c, 'R', pressed))
    ugfx.input_attach(ugfx.BTN_MID, lambda pressed: btn_cb(c, 'M', pressed))
    ugfx.input_attach(ugfx.BTN_A, lambda pressed: btn_cb(c, 'A', pressed))
    ugfx.input_attach(ugfx.BTN_B, lambda pressed: btn_cb(c, 'B', pressed))
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
        ugfx.input_init()
        print("Disonnected")
