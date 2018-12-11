# IBM developerWorks meetup 201812 행사 정보

## IoT 뱃지 만져보기 (마이크로 파이썬 프로그래밍 GPIO & SPI (LCD, 버튼, LED))

### 환경 구성

* IoT Badge USB Driver 설치
* IoT Badge 연결 터미널 S/W 설치
* Network 연결
* Web REPL download 및 연결

## 센서 연결하기 (I2C, PWM & ADC (피에조 부저, 조도 센서, 자이로 센서))

### 피에조 부저 동작 맛보기

> [example/buzzer.py](example/buzzer.py)

## Node-RED + IoT (Watson IoT 서비스 연동하기!)

### IBM IoT Platform 구성

1. IBM Cloud의 서비스 카탈로그에서 스타터 킷 중 `Internet of things platform starter`로 선택

 * 바로가기 : https://console.bluemix.net/catalog/starters/internet-of-things-platform-starter

2. Cloud Foundry App 생성

 * IoT Platform Starter는 다음과 같이 구성
    * `Node.js Runtime` 및 `Node-RED` IoT 서버 애플리케이션
    * Node Flow 데이터 저장을 위한 `Cloudant NoSQL Database`
    * IoT 플랫폼인 `Internet of Things Platform`
 * 애플리케이션 이름을 영문으로 입력
 * 애플리케이션 이름에 따라 자동으로 hostname이 제시되지만 고유한 이름이 되도록 `iot201812-{userid}`로 변경한다. (예, `iot2018-hongjs`)
   참고. 만약 중복되어도 애플리케이션은 생성되지만 생성한 앱으로 라우팅이 되지 않음

### Node-RED 실행

1. IoT 서버 애플리케이션 (Node-RED) 접속

  `iot2018-hongjs` 인 경우 Application URL은 다음과 같음

  > https://iot2018-hongjs.mybluemix.net/red

  * 최초 접속 시 관리자 id 및 비밀번호 생성
  * 이후 Node-RED에 접속 시 앞서 생성한 관리자 id 및 비밀번호 입력으로 로그인

2. Node-RED 기본 사용

  * `input` - `function` - `output` 노드
  * `inject`와 `debug` 노드
  * `IoT Quick Start` 노드
  * `IBM IoT` 노드

### IoT Foundation Quickstart 용 예제

1. 마이크로파이썬 mqtt library 설치

> Firmware에 기본으로 탑재되어 있으나 참고용으로 작성

``` python
import upip
upip.install("micropython-umqtt.simple")
```

2. IoT Foundation Quickstart 용 예제

> [example/quickstart.py](example/quickstart.py)

### Watson IoT Platform Quick start 웹페이지 접속

 * https://quickstart.internetofthings.ibmcloud.com/


### Watson IoT Platform 소개

 * IoT Server
 * Application 
 * Gateway
 * Device

### MQTT Client 인증 정보

* Application 인증 정보

> https://console.bluemix.net/docs/services/IoT/reference/security/connect_devices_apps_gw.html#mqtt_authentication

| 항목 | 값 |
|---|---|
| server | *<organization_id>*`.messaging.internetofthings.ibmcloud.com` | 
| port | 1883, 8883 (encrypted), 443 (websockets) |
| username | *API Key* (eg. a-<org_id>-a84ps90Ajs) |
| password | *Authentication token* |
| client id | `a:`*<org_id>*`:`*<app_id>* |

* Application API Key 발급

> https://console.bluemix.net/docs/services/IoT/platform_authorization.html#api-key


* IoTF Device 인증 정보

| 항목 | 값 |
|---|---|
| server | *<organization_id>*`.messaging.internetofthings.ibmcloud.com` | 
| port | 1883, 8883 (encrypted), 443 (websockets) |
| username | `use-token-auth` |
| password | *Authentication token* |
| client id | `d:`*<org_id>*`:`*<device_type>*`:`*<device_id>* |

> https://console.bluemix.net/docs/services/IoT/iotplatform_task.html#iotplatform_subtask2

### IoTF Topic 정보

| Publish topic | 값 | 예시 |
|---|---|---|
| device event | `iot-2/type/`*device_type*`/id/`*device_id*`/evt/`*event_id*`/fmt/`*format_string* | `iot-2/type/`badge2018`/id/`badge001`/evt/`button`/fmt/`json |
| device command | `iot-2/type/`*device_type*`/id/`*device_id*`/cmd/`*command_id*`/fmt/`*format_string* | `iot-2/type/`badge2018`/id/`badge001`/cmd/`led`/fmt/`json |

* Publish 할 때는 모든 정보가 정확해야 함
* Subscribe 할 때는 `+` 문자로 항목 대체 가능

| Subscribe topic | 값 | 예시 |
|---|---|---|
| device status | `iot-2/type/`*device_type*`/id/`*device_id*`/mon` | `iot-2/type/`+`/id/`+`/mon` |
| application status | `iot-2/app/`*app_id*`/mon` | `iot-2/app/`+`/mon` |
| device command | `iot-2/cmd/`*command_id*`/fmt/`*format_string* | `iot-2/cmd/led/fmt/json` |

> https://console.bluemix.net/docs/services/IoT/applications/mqtt.html


### IoT Badge Device Events

- status : sine
- sensor : GYRO, LUMI, IRRECV
- button : A, B, LEFT, RIGHT, UP, DOWN, OK

| 항목 | 값 | 예시 |
|---|---|---|
| 자이로 | gyro | `iot-2/type/`badge2018`/id/`badge001`/evt/`gyro`/fmt/json` |
| 조도센서 | lumi | |
| 버튼 | button | |


### IoT Badge Device Commands

- LCD color
- LED on/off
- IRSEND

| 항목 | 값 | 예시 |
|---|---|---|
| LED | led | `iot-2/type/`badge2018`/id/`badge001`/cmd/`led`/fmt/json` |
| 배경색 | bg | |


### LED 제어 예제

1. 마이크로 파이썬

> [example/led.py](example/led.py)

2. Node-RED

``` json
[{"id":"1e028ecd.947891","type":"ibmiot out","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","outputType":"cmd","deviceId":"240AC423BFF8","deviceType":"badge2018","eventCommandType":"led","format":"json","data":"default","qos":0,"name":"IBM IoT - led","service":"registered","x":590,"y":340,"wires":[]},{"id":"a14bf192.2c085","type":"inject","z":"64c93c11.da56f4","name":"Blue LED Toggle","topic":"","payload":"{\"d\":{\"target\":\"blue\",\"action\":\"toggle\"}}","payloadType":"json","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":160,"y":340,"wires":[["7d02b9fb.439d98"]]},{"id":"1e5b55e7.fb15ea","type":"debug","z":"64c93c11.da56f4","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","x":570,"y":400,"wires":[]},{"id":"f1cb4ee2.43a1e","type":"comment","z":"64c93c11.da56f4","name":"LED Command","info":"","x":140,"y":300,"wires":[]},{"id":"5b683874.1d07f8","type":"inject","z":"64c93c11.da56f4","name":"Blue LED On","topic":"","payload":"{\"d\":{\"target\":\"blue\",\"action\":\"on\"}}","payloadType":"json","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":150,"y":380,"wires":[["7d02b9fb.439d98"]]},{"id":"86d5b821.2b8af8","type":"inject","z":"64c93c11.da56f4","name":"Blue LED Off","topic":"","payload":"{\"d\":{\"target\":\"blue\",\"action\":\"off\"}}","payloadType":"json","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":150,"y":420,"wires":[["7d02b9fb.439d98"]]},{"id":"7d02b9fb.439d98","type":"change","z":"64c93c11.da56f4","name":"nothing","rules":[],"action":"","property":"","from":"","to":"","reg":false,"x":360,"y":340,"wires":[["1e028ecd.947891","1e5b55e7.fb15ea"]]},{"id":"a4331e4b.25022","type":"ibmiot","z":"","name":"ua3ev8","keepalive":"60","serverName":"ua3ev8.messaging.internetofthings.ibmcloud.com","cleansession":true,"appId":"","shared":false}]
```

### Background Color 제어 예제

1. 마이크로 파이썬

> [example/color.py](example/color.py)

2. Node-RED

``` json
[{"id":"667d4dee.b38e44","type":"ibmiot out","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","outputType":"cmd","deviceId":"240AC423BFF8","deviceType":"badge2018","eventCommandType":"anything","format":"json","data":"default","qos":0,"name":"IBM IoT - anything","service":"registered","x":610,"y":520,"wires":[]},{"id":"fa57f80.01c4408","type":"inject","z":"64c93c11.da56f4","name":"RED","topic":"","payload":"{\"d\":{\"color\":\"red\"}}","payloadType":"json","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":130,"y":520,"wires":[["8a2ffc0c.3b365"]]},{"id":"86fb5e08.6766c","type":"comment","z":"64c93c11.da56f4","name":"Color Command","info":"","x":140,"y":480,"wires":[]},{"id":"d23d9a8a.3448a8","type":"inject","z":"64c93c11.da56f4","name":"GREEN","topic":"","payload":"{\"d\":{\"color\":\"green\"}}","payloadType":"json","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":130,"y":560,"wires":[["8a2ffc0c.3b365"]]},{"id":"70524771.c4ff38","type":"inject","z":"64c93c11.da56f4","name":"BLUE","topic":"","payload":"{\"d\":{\"color\":\"blue\"}}","payloadType":"json","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":130,"y":600,"wires":[["8a2ffc0c.3b365"]]},{"id":"8a2ffc0c.3b365","type":"change","z":"64c93c11.da56f4","name":"color command type","rules":[{"t":"set","p":"eventOrCommandType","pt":"msg","to":"color","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":380,"y":520,"wires":[["667d4dee.b38e44","32bf0de1.8c9fa2"]]},{"id":"32bf0de1.8c9fa2","type":"debug","z":"64c93c11.da56f4","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"true","x":570,"y":580,"wires":[]},{"id":"c93c9c66.cad3","type":"inject","z":"64c93c11.da56f4","name":"0xffe0","topic":"","payload":"{\"d\":{\"color\":\"0xffe0\"}}","payloadType":"json","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":130,"y":640,"wires":[["8a2ffc0c.3b365"]]},{"id":"8971f881.27c878","type":"inject","z":"64c93c11.da56f4","name":"asdf","topic":"","payload":"{\"d\":{\"color\":\"asdf\"}}","payloadType":"json","repeat":"","crontab":"","once":false,"onceDelay":0.1,"x":130,"y":680,"wires":[["8a2ffc0c.3b365"]]},{"id":"a4331e4b.25022","type":"ibmiot","z":"","name":"ua3ev8","keepalive":"60","serverName":"ua3ev8.messaging.internetofthings.ibmcloud.com","cleansession":true,"appId":"","shared":false}]
``` 

### 버튼 이벤트 예제

1. 마이크로 파이썬

> [example/button.py](example/button.py)

2. Node-RED

``` json
[{"id":"332834d9.b8fa5c","type":"comment","z":"64c93c11.da56f4","name":"Button Event","info":"","x":130,"y":740,"wires":[]},{"id":"8866da01.e8ee08","type":"ibmiot in","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","inputType":"evt","logicalInterface":"","ruleId":"","deviceId":"240AC423BFF8","applicationId":"","deviceType":"badge2018","eventType":"button","commandType":"","format":"json","name":"IBM IoT - button","service":"registered","allDevices":true,"allApplications":"","allDeviceTypes":false,"allLogicalInterfaces":"","allEvents":false,"allCommands":"","allFormats":"","qos":0,"x":140,"y":780,"wires":[["956314a5.80d4c8"]]},{"id":"2d2c6cb.ba64994","type":"debug","z":"64c93c11.da56f4","name":"","active":true,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":610,"y":780,"wires":[]},{"id":"f211620c.86c0d","type":"change","z":"64c93c11.da56f4","name":"button","rules":[{"t":"set","p":"payload","pt":"msg","to":"payload.d.char","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":450,"y":780,"wires":[["2d2c6cb.ba64994"]]},{"id":"956314a5.80d4c8","type":"switch","z":"64c93c11.da56f4","name":"","property":"payload.d.type","propertyType":"jsonata","rules":[{"t":"eq","v":"keydown","vt":"str"}],"checkall":"true","repair":false,"outputs":1,"x":310,"y":780,"wires":[["f211620c.86c0d"]]},{"id":"a4331e4b.25022","type":"ibmiot","z":"","name":"ua3ev8","keepalive":"60","serverName":"ua3ev8.messaging.internetofthings.ibmcloud.com","cleansession":true,"appId":"","shared":false}]
``` 

### 조도 센서 이벤트 예제

1. 마이크로 파이썬

> [example/luminance.py](example/luminance.py)

2. Node-RED

``` json
[{"id":"cd5ca1ba.9f4c8","type":"comment","z":"64c93c11.da56f4","name":"Luminance Event","info":"","x":140,"y":860,"wires":[]},{"id":"bf3e35a3.69df48","type":"ibmiot in","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","inputType":"evt","logicalInterface":"","ruleId":"","deviceId":"240AC423BFF8","applicationId":"","deviceType":"badge2018","eventType":"luminance","commandType":"","format":"json","name":"IBM IoT - luminance","service":"registered","allDevices":true,"allApplications":"","allDeviceTypes":false,"allLogicalInterfaces":"","allEvents":false,"allCommands":"","allFormats":"","qos":0,"x":150,"y":900,"wires":[["f50ddfec.e2947"]]},{"id":"cf17863f.5c0388","type":"debug","z":"64c93c11.da56f4","name":"","active":false,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":610,"y":900,"wires":[]},{"id":"f50ddfec.e2947","type":"change","z":"64c93c11.da56f4","name":"Luminance","rules":[{"t":"set","p":"payload","pt":"msg","to":"payload.d.luminance","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":370,"y":900,"wires":[["cf17863f.5c0388"]]},{"id":"a4331e4b.25022","type":"ibmiot","z":"","name":"ua3ev8","keepalive":"60","serverName":"ua3ev8.messaging.internetofthings.ibmcloud.com","cleansession":true,"appId":"","shared":false}]
``` 

3. Node-RED v2

``` json
[{"id":"f5a9a0d3.fa727","type":"comment","z":"64c93c11.da56f4","name":"Luminance Event V2","info":"","x":150,"y":960,"wires":[]},{"id":"ff138051.70bba","type":"ibmiot in","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","inputType":"evt","logicalInterface":"","ruleId":"","deviceId":"240AC423BFF8","applicationId":"","deviceType":"badge2018","eventType":"luminance","commandType":"","format":"json","name":"IBM IoT - luminance","service":"registered","allDevices":true,"allApplications":"","allDeviceTypes":false,"allLogicalInterfaces":"","allEvents":false,"allCommands":"","allFormats":"","qos":0,"x":150,"y":1000,"wires":[["8afe494d.9b7098"]]},{"id":"50f4ad0e.023794","type":"debug","z":"64c93c11.da56f4","name":"","active":false,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":650,"y":1000,"wires":[]},{"id":"8afe494d.9b7098","type":"change","z":"64c93c11.da56f4","name":"Luminance","rules":[{"t":"set","p":"payload","pt":"msg","to":"payload.d.luminance","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":370,"y":1000,"wires":[["88e19341.e98f8"]]},{"id":"ddbedb2d.dd54b8","type":"change","z":"64c93c11.da56f4","name":"WHITE","rules":[{"t":"set","p":"payload","pt":"msg","to":"white","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":490,"y":1060,"wires":[["841b8c1f.6b75a"]]},{"id":"71d0eae6.400634","type":"ibmiot out","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","outputType":"cmd","deviceId":"240AC423BFF8","deviceType":"badge2018","eventCommandType":"color","format":"json","data":"default","qos":0,"name":"IBM IoT - anything","service":"registered","x":750,"y":1180,"wires":[]},{"id":"841b8c1f.6b75a","type":"change","z":"64c93c11.da56f4","name":"color payload","rules":[{"t":"set","p":"payload","pt":"msg","to":"{\"d\":{\"color\":payload}}","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":700,"y":1060,"wires":[["50f4ad0e.023794","71d0eae6.400634"]]},{"id":"a5bd03ef.02f9","type":"change","z":"64c93c11.da56f4","name":"RED","rules":[{"t":"set","p":"payload","pt":"msg","to":"red","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":490,"y":1100,"wires":[["841b8c1f.6b75a"]]},{"id":"702540a8.31f3d","type":"change","z":"64c93c11.da56f4","name":"BLUE","rules":[{"t":"set","p":"payload","pt":"msg","to":"blue","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":490,"y":1140,"wires":[["841b8c1f.6b75a"]]},{"id":"6ff56a3c.9b4764","type":"change","z":"64c93c11.da56f4","name":"BLACK","rules":[{"t":"set","p":"payload","pt":"msg","to":"black","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":500,"y":1180,"wires":[["841b8c1f.6b75a"]]},{"id":"88e19341.e98f8","type":"function","z":"64c93c11.da56f4","name":"switch","func":"if (msg.payload < 100) return [msg, null, null, null]\nelse if (msg.payload < 300) return [null, msg, null, null]\nelse if (msg.payload < 500) return [null, null, msg, null]\nreturn [null, null, null, msg]","outputs":4,"noerr":0,"x":350,"y":1120,"wires":[["ddbedb2d.dd54b8"],["a5bd03ef.02f9"],["702540a8.31f3d"],["6ff56a3c.9b4764"]]},{"id":"a4331e4b.25022","type":"ibmiot","z":"","name":"ua3ev8","keepalive":"60","serverName":"ua3ev8.messaging.internetofthings.ibmcloud.com","cleansession":true,"appId":"","shared":false}]
``` 

### 자이로/가속도 센서 이벤트 예제

1. 마이크로 파이썬

> [example/accel.py](example/accel.py)

2. Node-RED

``` json
[{"id":"319bb39.402ba4c","type":"comment","z":"64c93c11.da56f4","name":"Accelerometer Event","info":"","x":150,"y":1240,"wires":[]},{"id":"4383d2a0.77cb2c","type":"ibmiot in","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","inputType":"evt","logicalInterface":"","ruleId":"","deviceId":"240AC423BFF8","applicationId":"","deviceType":"badge2018","eventType":"accel","commandType":"","format":"json","name":"IBM IoT - accel","service":"registered","allDevices":true,"allApplications":"","allDeviceTypes":false,"allLogicalInterfaces":"","allEvents":false,"allCommands":"","allFormats":"","qos":0,"x":140,"y":1280,"wires":[["5b338fd6.0f7a"]]},{"id":"5b338fd6.0f7a","type":"change","z":"64c93c11.da56f4","name":"Acceleration x-axis","rules":[{"t":"set","p":"payload","pt":"msg","to":"payload.d.acceleration_y","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":350,"y":1280,"wires":[["a7b01a5.416a7e8"]]},{"id":"a7b01a5.416a7e8","type":"debug","z":"64c93c11.da56f4","name":"","active":false,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":610,"y":1280,"wires":[]},{"id":"a4331e4b.25022","type":"ibmiot","z":"","name":"ua3ev8","keepalive":"60","serverName":"ua3ev8.messaging.internetofthings.ibmcloud.com","cleansession":true,"appId":"","shared":false}]
``` 

3. Node-RED V2

``` json
[{"id":"3bc317e9.054bf8","type":"comment","z":"64c93c11.da56f4","name":"Accelerometer Event V2","info":"","x":160,"y":1340,"wires":[]},{"id":"2263db9b.20bc04","type":"ibmiot in","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","inputType":"evt","logicalInterface":"","ruleId":"","deviceId":"240AC423BFF8","applicationId":"","deviceType":"badge2018","eventType":"accel","commandType":"","format":"json","name":"IBM IoT - accel","service":"registered","allDevices":true,"allApplications":"","allDeviceTypes":false,"allLogicalInterfaces":"","allEvents":false,"allCommands":"","allFormats":"","qos":0,"x":140,"y":1380,"wires":[["99064023.0e444"]]},{"id":"99064023.0e444","type":"change","z":"64c93c11.da56f4","name":"Acceleration","rules":[{"t":"set","p":"payload","pt":"msg","to":"payload.d","tot":"msg"}],"action":"","property":"","from":"","to":"","reg":false,"x":330,"y":1380,"wires":[["217f9bfb.ec5c24"]]},{"id":"daa2a33d.a79ef","type":"debug","z":"64c93c11.da56f4","name":"","active":false,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload.roll","x":720,"y":1380,"wires":[]},{"id":"c8774551.b35038","type":"change","z":"64c93c11.da56f4","name":"BLACK","rules":[{"t":"set","p":"payload","pt":"msg","to":"black","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":460,"y":1500,"wires":[["5fc6afb2.e41ab"]]},{"id":"ff6626f1.970df8","type":"ibmiot out","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","outputType":"cmd","deviceId":"240AC423BFF8","deviceType":"badge2018","eventCommandType":"color","format":"json","data":"default","qos":0,"name":"IBM IoT - color","service":"registered","x":740,"y":1560,"wires":[]},{"id":"5fc6afb2.e41ab","type":"change","z":"64c93c11.da56f4","name":"color payload","rules":[{"t":"set","p":"payload","pt":"msg","to":"{\"d\":{\"color\":payload}}","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":660,"y":1500,"wires":[["ff6626f1.970df8"]]},{"id":"df55dd06.c1ee4","type":"change","z":"64c93c11.da56f4","name":"RED","rules":[{"t":"set","p":"payload","pt":"msg","to":"red","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":450,"y":1540,"wires":[["5fc6afb2.e41ab"]]},{"id":"61d8ddca.c94404","type":"switch","z":"64c93c11.da56f4","name":"Pitch","property":"payload.pitch","propertyType":"msg","rules":[{"t":"btwn","v":"-10.0","vt":"num","v2":"10.0","v2t":"num"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":310,"y":1520,"wires":[["c8774551.b35038"],["df55dd06.c1ee4"]]},{"id":"217f9bfb.ec5c24","type":"function","z":"64c93c11.da56f4","name":"roll & pitch","func":"let X = msg.payload.acceleration_x\nlet Y = msg.payload.acceleration_y\nlet Z = msg.payload.acceleration_z\n\nmsg.payload.roll = Math.atan2(Y, Z) * 180/Math.PI;\nmsg.payload.pitch = Math.atan2(X, Math.sqrt(Y*Y + Z*Z)) * 180/Math.PI;\n\nreturn msg;","outputs":1,"noerr":0,"x":330,"y":1440,"wires":[["daa2a33d.a79ef","f34f48e9.4db618","61d8ddca.c94404"]]},{"id":"c7d8b911.c91578","type":"change","z":"64c93c11.da56f4","name":"ON","rules":[{"t":"set","p":"payload","pt":"msg","to":"on","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":450,"y":1640,"wires":[["a2ae3543.970d78"]]},{"id":"e5492fd4.0c91a","type":"ibmiot out","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","outputType":"cmd","deviceId":"240AC423BFF8","deviceType":"badge2018","eventCommandType":"led","format":"json","data":"default","qos":0,"name":"IBM IoT - led","service":"registered","x":730,"y":1700,"wires":[]},{"id":"a2ae3543.970d78","type":"change","z":"64c93c11.da56f4","name":"blue led payload","rules":[{"t":"set","p":"payload","pt":"msg","to":"{\"d\":{\"target\":\"blue\",\"action\":payload}}","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":660,"y":1640,"wires":[["e5492fd4.0c91a"]]},{"id":"cc0aba61.493bd8","type":"change","z":"64c93c11.da56f4","name":"OFF","rules":[{"t":"set","p":"payload","pt":"msg","to":"off","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":450,"y":1680,"wires":[["a2ae3543.970d78"]]},{"id":"f34f48e9.4db618","type":"function","z":"64c93c11.da56f4","name":"Roll","func":"let prop = Number(msg.payload.roll)\nif (prop < -10.0 || 10.0 < prop) return [msg, null]\nreturn [null, msg]","outputs":2,"noerr":0,"x":310,"y":1660,"wires":[["c7d8b911.c91578"],["cc0aba61.493bd8"]]},{"id":"a4331e4b.25022","type":"ibmiot","z":"","name":"ua3ev8","keepalive":"60","serverName":"ua3ev8.messaging.internetofthings.ibmcloud.com","cleansession":true,"appId":"","shared":false}]
``` 

4. Node-RED v3

``` json
[{"id":"ac925d31.51e3a","type":"comment","z":"64c93c11.da56f4","name":"Accelerometer Event V3","info":"","x":160,"y":1840,"wires":[]},{"id":"7c68edf.ec1e514","type":"ibmiot in","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","inputType":"evt","logicalInterface":"","ruleId":"","deviceId":"240AC423BFF8","applicationId":"","deviceType":"badge2018","eventType":"accel","commandType":"","format":"json","name":"IBM IoT - accel","service":"registered","allDevices":true,"allApplications":"","allDeviceTypes":false,"allLogicalInterfaces":"","allEvents":false,"allCommands":"","allFormats":"","qos":0,"x":140,"y":1880,"wires":[["8f931173.7a976"]]},{"id":"8f931173.7a976","type":"change","z":"64c93c11.da56f4","name":"Acceleration","rules":[{"t":"set","p":"payload","pt":"msg","to":"payload.d","tot":"msg"}],"action":"","property":"","from":"","to":"","reg":false,"x":330,"y":1880,"wires":[["5e84d78.0bf3528"]]},{"id":"2c2048a9.d0a228","type":"debug","z":"64c93c11.da56f4","name":"","active":false,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload.roll","x":720,"y":1880,"wires":[]},{"id":"a04233f7.6b611","type":"change","z":"64c93c11.da56f4","name":"BLACK","rules":[{"t":"set","p":"payload","pt":"msg","to":"black","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":460,"y":2000,"wires":[["7baf35ef.72ee1c","81d654fd.e372c8"]]},{"id":"fd450ef1.e4219","type":"ibmiot out","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","outputType":"cmd","deviceId":"240AC423BFF8","deviceType":"badge2018","eventCommandType":"color","format":"json","data":"default","qos":0,"name":"IBM IoT - color","service":"registered","x":740,"y":2060,"wires":[]},{"id":"4328bc4f.60b654","type":"change","z":"64c93c11.da56f4","name":"color payload","rules":[{"t":"set","p":"payload","pt":"msg","to":"{\"d\":{\"color\":payload}}","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":920,"y":2000,"wires":[["fd450ef1.e4219"]]},{"id":"88860678.965308","type":"change","z":"64c93c11.da56f4","name":"RED","rules":[{"t":"set","p":"payload","pt":"msg","to":"red","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":450,"y":2040,"wires":[["7baf35ef.72ee1c","81d654fd.e372c8"]]},{"id":"cedafecc.57ee9","type":"switch","z":"64c93c11.da56f4","name":"Pitch","property":"payload.pitch","propertyType":"msg","rules":[{"t":"btwn","v":"-10.0","vt":"num","v2":"10.0","v2t":"num"},{"t":"else"}],"checkall":"true","repair":false,"outputs":2,"x":310,"y":2020,"wires":[["a04233f7.6b611"],["88860678.965308"]]},{"id":"5e84d78.0bf3528","type":"function","z":"64c93c11.da56f4","name":"roll & pitch","func":"let X = msg.payload.acceleration_x\nlet Y = msg.payload.acceleration_y\nlet Z = msg.payload.acceleration_z\n\nmsg.payload.roll = Math.atan2(Y, Z) * 180/Math.PI;\nmsg.payload.pitch = Math.atan2(X, Math.sqrt(Y*Y + Z*Z)) * 180/Math.PI;\n\nreturn msg;","outputs":1,"noerr":0,"x":330,"y":1940,"wires":[["2c2048a9.d0a228","d2da0b6d.8ff4f8","cedafecc.57ee9"]]},{"id":"e5a21ede.ec7c7","type":"change","z":"64c93c11.da56f4","name":"ON","rules":[{"t":"set","p":"payload","pt":"msg","to":"on","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":450,"y":2140,"wires":[["3439e0f7.cfe67","6c7743dc.87dd3c"]]},{"id":"f86e267.c71b2d8","type":"ibmiot out","z":"64c93c11.da56f4","authentication":"apiKey","apiKey":"a4331e4b.25022","outputType":"cmd","deviceId":"240AC423BFF8","deviceType":"badge2018","eventCommandType":"led","format":"json","data":"default","qos":0,"name":"IBM IoT - led","service":"registered","x":730,"y":2200,"wires":[]},{"id":"7cc1774d.4b8708","type":"change","z":"64c93c11.da56f4","name":"blue led payload","rules":[{"t":"set","p":"payload","pt":"msg","to":"{\"d\":{\"target\":\"blue\",\"action\":payload}}","tot":"jsonata"}],"action":"","property":"","from":"","to":"","reg":false,"x":920,"y":2140,"wires":[["f86e267.c71b2d8"]]},{"id":"ac8ee3.8d06a12","type":"change","z":"64c93c11.da56f4","name":"OFF","rules":[{"t":"set","p":"payload","pt":"msg","to":"off","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":450,"y":2180,"wires":[["3439e0f7.cfe67","6c7743dc.87dd3c"]]},{"id":"d2da0b6d.8ff4f8","type":"function","z":"64c93c11.da56f4","name":"Roll","func":"let prop = msg.payload.roll\nif (prop < -10.0 || 10.0 < prop) return [msg, null]\nreturn [null, msg]","outputs":2,"noerr":0,"x":310,"y":2160,"wires":[["e5a21ede.ec7c7"],["ac8ee3.8d06a12"]]},{"id":"3439e0f7.cfe67","type":"debug","z":"64c93c11.da56f4","name":"","active":false,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":570,"y":2280,"wires":[]},{"id":"7baf35ef.72ee1c","type":"debug","z":"64c93c11.da56f4","name":"","active":false,"tosidebar":true,"console":false,"tostatus":false,"complete":"payload","x":610,"y":1940,"wires":[]},{"id":"81d654fd.e372c8","type":"function","z":"64c93c11.da56f4","name":"check previous color","func":"let key = `status-${msg.deviceId}`\nvar status = flow.get(key)\nif (status) {\n    if (status.color === msg.payload) {\n        return\n    }\n    status['color'] = msg.payload\n} else {\n    status = {\n        'color': msg.payload\n    }\n}\nflow.set(key, status)\n\nreturn msg;","outputs":1,"noerr":0,"x":680,"y":2000,"wires":[["4328bc4f.60b654"]]},{"id":"6c7743dc.87dd3c","type":"function","z":"64c93c11.da56f4","name":"check previous blue led","func":"let key = `status-${msg.deviceId}`\nvar status = flow.get(key)\nif (status) {\n    if (status.blue === msg.payload) {\n        return\n    }\n    status['blue'] = msg.payload\n} else {\n    status = {\n        'blue': msg.payload\n    }\n}\nflow.set(key, status)\n\nreturn msg;","outputs":1,"noerr":0,"x":690,"y":2140,"wires":[["7cc1774d.4b8708"]]},{"id":"a4331e4b.25022","type":"ibmiot","z":"","name":"ua3ev8","keepalive":"60","serverName":"ua3ev8.messaging.internetofthings.ibmcloud.com","cleansession":true,"appId":"","shared":false}]
```

