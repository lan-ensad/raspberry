import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relai = 2
file = open('log.txt', 'a')
GPIO.setup(relai, GPIO.OUT)

line = "\n=============== \nON\t" + str(datetime.datetime.now())
print(line)
file.write(line)
GPIO.output(relai, 1)

time.sleep(60)

line = "\nOFF\t "+str(datetime.datetime.now())
print(line)
file.write(line)
GPIO.output(relai, 0)

file.close()