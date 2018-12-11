# Hardware

## ESP32
* https://en.wikipedia.org/wiki/ESP32
* 듀얼코어 32bit, WiFi, BLE, GPIO, PWM, ADC, DAC, SPI, UART, Touch, etc..
* [Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32_datasheet_en.pdf)

### ESP32-WROOM-32D
* ESP32 Dual core
* 4MB Flash
* KC 인증
* 개당 $3.5
* [Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf)

### ESP32 DevKitC
* CP2102N 으로 PC 전원 공급 및 시리얼 UART 연결
* 적색 LED는 상시 전원
* 연결 불량시 C15 제거
* EN 버튼으로 재부팅
* esptool 로 firmware 기록시 자동으로 부트로더모드 진입
	* 동작하지 않을 경우 BOOT 누른 상태에서 EN 으로 재부팅


# Firmware 업데이트
* 아직 OTA 미지원

## USB Serial 연결
* [드라이버 다운로드](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)
	* CP2102N 최신 칩셋 사용이라 최신 드라이버로 업데이트 하지 않으면 롬 플래시때 오작동
* Serial 터미널 연결
	* Windows 에서는 Putty 로 `COM` 포트 지정 후 `115200` 속도 연결
	* Mac 이나 Linux 에서는 `screen` 이용
		* screen 은 `CTRL-A`, `CTRL-K` 후 `y` 로 종료
	* Mac
		* `brew install screen` 으로 설치
		* `screen /dev/tty.SLAB_USBtoUART 115200`
	* Linux
		* 드라이버 기본 지원
		* `screen /dev/ttyUSB0`

## Flash Download Tool (Windows)
* https://www.espressif.com/en/products/hardware/esp32/resources
* `Tools` > `Flash Download Tools (ESP8266 & ESP32)`

## esptool

### 설치방법
* Python 설치 (Windows)
* pip 설치
* `pip install esptool`

### Firmware 업데이트
```
esptool.py erase_flash
esptool.py -b 921600 write_flash 0x1000 firmware.bin
```
* erase_flash 진행시 FATFS 까지 삭제됨
* MicroPython firmware 만 업데이트시는 FATFS 유지
* Badge firmware 중 일부는 둘 다 업데이트

## LCD - ILI9341 2.4" TFT
* 320x240
* 회전가능
* RGB565 16bit color
* VSPI 연결

## LED
* GPIO17 노란색
* GPIO16 파란색
* J10 GPIO16 연동 IR 전용
	* 0.8A 정도 전류 인가되기 때문에, IR LED 연결시 상시 구동 금지!!

## Input
* 5 way tactile switch
* Tactile switch * 2 (A, B)
	* A (왼쪽) 은 선택용
	* B (오른쪽) 은 취소용

## GPIO
* J4, J5, J6: ADC 주용도
* J7, J8: I2C 등 센서 연결
* J9: HSPI 혹은 일반 센서 연결
	* 스위치와 신호 간섭 가능
* J11: Sharp GP2Y1014AU0F 미세먼지 센서 전용
	* 미세먼지 센서 사용시 J14에 220uF 연결

# MicroPython
## Firmware
* MicroPython 1.9.4 기반
* ESP8266 과 비슷
	* 기본 튜토리얼 공유 가능
	* 몇가지 차이점 있음
* uGFX 지원 추가
* 0x1000 부터 firmware
* 현재 2MB (한글폰트 포함)
* 0x200000 부터 FATFS
* 메모리 관리 주의

## Platform
* OTA 지원
	* boot.py
	* main.py
		* RTC 를 이용하여 deepsleep(1) 후 프로그램 로딩
	* util.py
	* version.txt
## apps
* home
* netconfig
* ...

## REPL / WebREPL
* https://github.com/micropython/webrepl
* 8266 포트에서 websocket 연결
	* 웹에서 이용시 `https` 아닌 `http` 로 접속해야함
* 한번에 한 연결만 접속 가능
* Windows 에서는 `SHIFT-INSERT` 로 붙여넣기
* `CTRL-E` 로 다중 붙이기 모드 사용 가능
	* `CTRL-D` 로 종료, `CTRL-C` 로 취소
* `TAB` 자동완성 가능

# uGFX
* https://ugfx.io/
* TiLDA, SHA2017 포팅 기반
* IBM Plex, Naver 나눔스퀘어 폰트 포함

## 기본 명령어
### ugfx.init()
* 출력 초기화
* `boot.py` 에서 이미 실행

### ugfx.clear(COLOR)
`ugfx.clear(ugfx.BLACK)`

### ugfx.HTML2COLOR(HEXCOLOR)
```python
light_blue = ugfx.HTML2COLOR(0x01d7dd)
ugfx.clear(light_blue)
```

### ugfx.RGB2COLOR(RED, GREEN, BLACK)
```
green20 = ugfx.RGB2COLOR(87, 215, 133)
ugfx.clear(green20)
```


### ugfx.orientation()
### ugfx.orientation(DEGREE)

### ugfx.width()

### ugfx.height()

### ugfx.set_default_font(FONT_NAME)

### ugfx.set_default_style(STYLE_OBJ)

### ugfx.fonts_list()

### ugfx.get_char_width(CHAR, FONT_NAME)
```
ugfx.get_char_width(ord('i'), 'IBMPlexSans_Regular26')
ugfx.get_char_width(ord('O'), 'IBMPlexSans_Regular26')
```

### ugfx.get_string_width(STRING, FONT_NAME)
`ugfx.get_string_width('IBM', 'IBMPlexSans_Regular26')`


### ugfx.char(X, Y, CHAR, FONT_NAME, COLOR)
```
ugfx.char(10, 10, ord('A'), 'IBMPlexMono_Bold48', ugfx.BLUE)
```

### ugfx.text(X, Y, STRING, COLOR)

### ugfx.string(X, Y, STRING, FONT_NAME, COLOR)

### ugfx.string_box(X, Y, W, H, STRING, FONT, COLOR, JUSTIFY)


