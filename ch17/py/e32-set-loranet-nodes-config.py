#!/usr/bin/python
# -*- coding: UTF-8 -*-

import RPi.GPIO as GPIO
import serial
import time
import sys
from time import sleep

NODE_CFG = [b'\xC0\x00\x0B\x1A\x0F\xC7',
            b'\xC0\x00\x0C\x1A\x0F\xC7',
            b'\xC0\x00\x0D\x1A\x0F\xC7',
            b'\xC0\x00\x0E\x1A\x0F\xC7']

if len(sys.argv) != 2 or int(sys.argv[1]) < 1 or int(sys.argv[1]) > 4 :
    print("Please enter node id (1, 2, 3, 4)")
    sys.exit(0)

node_id = int(sys.argv[1])
new_cfg = NODE_CFG[node_id-1]

print('Node ' + str(node_id) + ' set new config:')
print('{}'.format(new_cfg.encode('hex')))

confirm = raw_input("Enter 'yes' to confirm: ")
if confirm != 'yes' :
	print("cancelled")
	sys.exit(0)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

M0 = 22
M1 = 27

GPIO.setup(M0,GPIO.OUT)
GPIO.setup(M1,GPIO.OUT)

GPIO.output(M0,GPIO.HIGH)
GPIO.output(M1,GPIO.HIGH)
time.sleep(1)

#ser = serial.Serial("/dev/ttyS0",9600)
ser = serial.Serial("/dev/serial0", 9600)
ser.flushInput()

try :
    if ser.isOpen() :
        ser.write(NODE_CFG[node_id-1])
        time.sleep(1)
except :
    if ser.isOpen() :
        ser.close()
	GPIO.cleanup()

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

print('Node ' + str(node_id) + ' new config:')
print('{}'.format(received_data.encode('hex')))