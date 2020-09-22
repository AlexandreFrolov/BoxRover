#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import serial
import time
import sys
from time import sleep

NODE_ADDR_CHAN = [b'\x00\x0B\x0F',
            b'\x00\x0C\x0F',
            b'\x00\x0D\x0F',
            b'\x00\x0E\x0F']

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
M0 = 22
M1 = 27
GPIO.setup(M0,GPIO.OUT)
GPIO.setup(M1,GPIO.OUT)
GPIO.output(M0,GPIO.LOW)
GPIO.output(M1,GPIO.LOW)

time.sleep(1)

#ser = serial.Serial("/dev/ttyS0",9600, timeout=1)
ser = serial.Serial("/dev/serial0", 9600, timeout=1)
ser.flushInput()

try :
    if ser.isOpen() :
        ser.write(NODE_ADDR_CHAN[0])
        ser.write('getData \n'.encode())
except :
    if ser.isOpen() :
        ser.close()
	GPIO.cleanup()
received_data = ser.readline()
sleep(0.03)
data_left = ser.inWaiting()             #check for remaining byte
received_data += ser.read(data_left)
print (received_data.rstrip("\n"))                   #print received data


try :
    if ser.isOpen() :
        ser.write(NODE_ADDR_CHAN[1])
        ser.write('getData \n'.encode())
except :
    if ser.isOpen() :
        ser.close()
	GPIO.cleanup()
received_data = ser.readline()
sleep(0.03)
data_left = ser.inWaiting()             #check for remaining byte
received_data += ser.read(data_left)
print (received_data.rstrip("\n"))                   #print received data
