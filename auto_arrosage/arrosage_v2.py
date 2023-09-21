#############################################
###     arrosage.py
#############################################

import RPi.GPIO as GPIO
import time
import datetime

R = [2, 3, 4]
#[M1 = 4
# M2 = 3
# M3 = 2]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for x in R:
    GPIO.setup(x, GPIO.OUT)


############################
#     Summer Hollidays

for x in R:
    GPIO.output(x, 1)

time.sleep(60)

for x in R:
    GPIO.output(x, 0)


############################
#       Test blink
# while 1:

#     for x in R:
#         GPIO.output(x, 1)
#     time.sleep(1)

#     for x in R:
#         GPIO.output(x, 0)
#     time.sleep(1)


#############################################
### palmier_watering.py
#############################################

import RPi.GPIO as GPIO
import time
import datetime

R = 14

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(R, GPIO.OUT)

GPIO.output(R, 1)
time.sleep(4)
GPIO.output(R, 0)

#############################################
### endlessGo.py
#############################################

import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

gpiotoreset = [2, 3, 4]

while 1:
    for x in gpiotoreset:
        GPIO.setup(x, GPIO.OUT)
        GPIO.output(x, 1)
