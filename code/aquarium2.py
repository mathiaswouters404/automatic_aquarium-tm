# https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/
# https://ben.akrin.com/driving-a-28byj-48-stepper-motor-uln2003-driver-with-a-raspberry-pi/
# https://www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/
# https://stackoverflow.com/questions/62243448/raspberry-gpio-time-trigger
# https://www.hackster.io/hardikrathod/push-button-with-raspberry-pi-6b6928

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)


def on(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

def off(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    
i = int(1)
j = int(1)
k = int(1)

try:
    while True:
        button_state1 = GPIO.input(19)
        button_state2 = GPIO.input(26)
        if button_state1 == False:
            while i == 1:
                print('Button 1 Pressed')
                i += 1
            on(17)
            on(18)
            time.sleep(0.01)
            off(17)
            on(27)
            time.sleep(0.01)
            off(18)
            on(22)
            time.sleep(0.01)
            off(27)
            on(17)
            time.sleep(0.01)
            off(22)
            on(18)
            i == 1
            #time.sleep(0.2)
        elif button_state2 == False:
            while j == 1:
                print('Button 2 Pressed')
                j += 1
            on(18)
            off(22)
            time.sleep(0.01)
            on(17)
            off(27)
            time.sleep(0.01)
            on(22)
            off(18)
            time.sleep(0.01)
            on(27)
            off(17)
            time.sleep(0.01)
            on(18)
            on(17)
            j == 1
        else:
            while k == 1:
                print('Button released')
                k += 1
            GPIO.output(17, False)
            GPIO.output(18, False)
            GPIO.output(27, False)
            GPIO.output(22, False)
            k == 1

except KeyboardInterrupt:
    off(17)
    off(18)
    off(22)
    off(27)
    GPIO.cleanup()