import RPi.GPIO as GPIO
import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

file = open('log.txt', 'a')

i = 2
GPIO.setup(i, GPIO.OUT)
GPIO.output(i, 0)

line = "\n=============== \nREBOOT :\t" + str(datetime.datetime.now()+'\n')
file.write(line)
file.close()