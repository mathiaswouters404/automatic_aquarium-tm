#Aquarium Code

import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
step_sleep = 0.002
 
step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°
 
direction = False # True for clockwise, False for counter-clockwise
 
# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]
  
# initializing
GPIO.output( 17, GPIO.LOW )
GPIO.output( 18, GPIO.LOW )
GPIO.output( 27, GPIO.LOW )
GPIO.output( 22, GPIO.LOW )
 
 
motor_pins = [17,18,27,22]
motor_step_counter = 0 ;
 
 
def cleanup():
    GPIO.output( 17, GPIO.LOW )
    GPIO.output( 18, GPIO.LOW )
    GPIO.output( 27, GPIO.LOW )
    GPIO.output( 22, GPIO.LOW )
    GPIO.cleanup()
 
 
# the meat
try:
    i = 0
    for i in range(step_count):
        for pin in range(0, len(motor_pins)):
            GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
        if direction==True:
            motor_step_counter = (motor_step_counter - 1) % 8
        elif direction==False:
            motor_step_counter = (motor_step_counter + 1) % 8
        else: # defensive programming
            print( "uh oh... direction should *always* be either True or False" )
            cleanup()
            exit( 1 )
        time.sleep( step_sleep )
 
except KeyboardInterrupt:
    cleanup()
    exit( 1 )
 
cleanup()
exit( 0 )