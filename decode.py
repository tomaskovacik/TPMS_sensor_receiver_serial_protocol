#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import serial
import string
import time
import datetime

global ser 
ser = None 

def connect():
	while(1):
		try:
			print("connecting")
			global ser
			ser = serial.Serial('/dev/ttyUSB0', 19200)
			ser.timeout = 5
			return
		except:
			time.sleep(2) #wait before retrying

try:
	
	connect()

	# read cmds from the radio and act like a cd changer
	while(1):
		try:
			a = ser.read()
			if a == chr(0x55):
				current_time=str(datetime.datetime.now())
				b = ser.read()
	                        cmd = ser.read()
	                        tireID = ser.read()
               		        pressure = ser.read()
	                        temperature = ser.read()
               		        state = ord(ser.read())
               		        if ord(ser.read()) == ord(a)^ord(b)^ord(cmd)^ord(tireID)^ord(pressure)^ord(temperature)^state:
					if b == chr(0xAA):
						if cmd == chr(0x08):
							#print ("sensor information")
							if tireID == chr(0x00):
								tire = "front left"
								#print ("front left")
							elif tireID == chr(0x01):
								tire = "Front right"
								#print ("Front right tire")
							elif tireID == chr(0x10):
								tire = "left back"
								#print ("left back tire")
							elif tireID == chr(0x11):
								tire = "Rear right"
								#print ("Rear Right tire")
							elif tireID == chr(0x05):
								tire = "spare"
								#print ("spare tire")
							if (state & 0b00100000) != 0:
								print (current_time+" Lost signal of "+tire+" tire!")
							elif (state & 0b00001000) != 0:
								print (current_time+" "+tire+" tire leaking! "+str(float(ord(pressure) * 3.44))+"kPa / "+str(ord(temperature) - 50)+"°C")
							elif (state & 0b00010000) != 0:
								print (current_time+" Low battery at "+tire+"! "+str(float(ord(pressure) * 3.44))+"kPa / "+str(ord(temperature) - 50)+"°C")
							else:
								print(current_time+" "+tire+" tire: "+str(float(ord(pressure) * 3.44))+"kPa / "+str(ord(temperature) - 50)+"°C")

		except (serial.SerialException, serial.SerialTimeoutException):
			print "serial port unavailable, reconnecting..."
			ser.close()
			connect()
		except:
			raise

except (KeyboardInterrupt):
	if ser is not None:
		ser.close()
		print "port closed!"
	print "KeyboardInterrupt detected, exiting..."
