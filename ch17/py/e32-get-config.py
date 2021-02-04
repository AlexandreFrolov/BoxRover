#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import serial
import time
import sys
from time import sleep

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

M0 = 22
M1 = 27

GPIO.setup(M0,GPIO.OUT)
GPIO.setup(M1,GPIO.OUT)

#GPIO.output(M0,GPIO.LOW)
#GPIO.output(M1,GPIO.LOW)

GPIO.output(M0,GPIO.HIGH)
GPIO.output(M1,GPIO.HIGH)
time.sleep(1)

#ser = serial.Serial("/dev/ttyS0",9600)
ser = serial.Serial("/dev/serial0", 9600)
ser.flushInput()

try :
    if ser.isOpen() :
        ser.write(b'\xC1\xC1\xC1')

except :
    if ser.isOpen() :
        ser.close()
	GPIO.cleanup()

received_data = ser.read(6)
sleep(0.03)
print('E32 module config:')
print('{}'.format(received_data.encode('hex')))
GPIO.cleanup()
