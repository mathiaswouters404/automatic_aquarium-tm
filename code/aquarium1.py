# https://tutorials-raspberrypi.com/how-to-control-a-stepper-motor-with-raspberry-pi-and-l293d-uln2003a/
# https://ben.akrin.com/driving-a-28byj-48-stepper-motor-uln2003-driver-with-a-raspberry-pi/
# https://www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/
# https://stackoverflow.com/questions/62243448/raspberry-gpio-time-trigger

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


def on(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)

def off(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

try:
    while True:
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

except KeyboardInterrupt:
    off(17)
    off(18)
    off(22)
    off(27)
    GPIO.cleanup()