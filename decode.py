#!/usr/bin/python3
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
    querySensorID = bytearray()
    querySensorID.append(0x55)
    querySensorID.append(0xAA)
    querySensorID.append(0x06)
    querySensorID.append(0x07)
    querySensorID.append(0x00)
    querySensorID.append(0x00)
    querySensorID.append(0x0C)

    eventACK = bytearray()
    eventACK.append(0x55)
    eventACK.append(0xAA)
    eventACK.append(0x06)
    eventACK.append(0x00)
    eventACK.append(0x00)
    eventACK.append(0x00)

    heartbeat = bytearray()
    heartbeat.append(0x55)
    heartbeat.append(0xAA)
    heartbeat.append(0x06)
    heartbeat.append(0x19)
    heartbeat.append(0x00)
    heartbeat.append(0xE0)

	#?? 0x55, 0xAA, 0x06, 0x5B, ??, 0xE0

    pairingSensorLeftBack = bytearray()
    pairingSensorLeftBack.append(0x55)
    pairingSensorLeftBack.append(0xAA)
    pairingSensorLeftBack.append(0x06)
    pairingSensorLeftBack.append(0x01)
    pairingSensorLeftBack.append(0x10)
    pairingSensorLeftBack.append(0x00)

    pairingSensorBackRight = bytearray()
    pairingSensorBackRight.append(0x55)
    pairingSensorBackRight.append(0xAA)
    pairingSensorBackRight.append(0x06)
    pairingSensorBackRight.append(0x01)
    pairingSensorBackRight.append(0x11)
    pairingSensorBackRight.append(0x00)

    pairingSensorFrontLeft = bytearray()
    pairingSensorFrontLeft.append(0x55)
    pairingSensorFrontLeft.append(0xAA)
    pairingSensorFrontLeft.append(0x06)
    pairingSensorFrontLeft.append(0x01)
    pairingSensorFrontLeft.append(0x00)
    pairingSensorFrontLeft.append(0x00)

    pairingSensorFrontRight = bytearray()
    pairingSensorFrontRight.append(0x55)
    pairingSensorFrontRight.append(0xAA)
    pairingSensorFrontRight.append(0x06)
    pairingSensorFrontRight.append(0x01)
    pairingSensorFrontRight.append(0x01)
    pairingSensorFrontRight.append(0x00)

    pairingSensorSpareTire = bytearray()
    pairingSensorSpareTire.append(0x55)
    pairingSensorSpareTire.append(0xAA)
    pairingSensorSpareTire.append(0x06)
    pairingSensorSpareTire.append(0x01)
    pairingSensorSpareTire.append(0x05)
    pairingSensorSpareTire.append(0x00)

    stopPairing = bytearray()
    stopPairing.append(0x55)
    stopPairing.append(0xAA)
    stopPairing.append(0x06)
    stopPairing.append(0x06)
    stopPairing.append(0x00)
    stopPairing.append(0x00)

    wheelsChangeLeftFrontRightFront = bytearray()
    wheelsChangeLeftFrontRightFront.append(0x55)
    wheelsChangeLeftFrontRightFront.append(0xAA)
    wheelsChangeLeftFrontRightFront.append(0x07)
    wheelsChangeLeftFrontRightFront.append(0x03)
    wheelsChangeLeftFrontRightFront.append(0x00)
    wheelsChangeLeftFrontRightFront.append(0x01)
    wheelsChangeLeftFrontRightFront.append(0x00)

    wheelsChangeLeftFrontLeftBack = bytearray()
    wheelsChangeLeftFrontLeftBack.append(0x55)
    wheelsChangeLeftFrontLeftBack.append(0xAA)
    wheelsChangeLeftFrontLeftBack.append(0x07)
    wheelsChangeLeftFrontLeftBack.append(0x03)
    wheelsChangeLeftFrontLeftBack.append(0x00)
    wheelsChangeLeftFrontLeftBack.append(0x10)
    wheelsChangeLeftFrontLeftBack.append(0x00)

    wheelsChangeLeftFrontRightBack = bytearray()
    wheelsChangeLeftFrontRightBack.append(0x55)
    wheelsChangeLeftFrontRightBack.append(0xAA)
    wheelsChangeLeftFrontRightBack.append(0x07)
    wheelsChangeLeftFrontRightBack.append(0x03)
    wheelsChangeLeftFrontRightBack.append(0x00)
    wheelsChangeLeftFrontRightBack.append(0x11)
    wheelsChangeLeftFrontRightBack.append(0x00)

    wheelsChangeRightFrontLeftBack = bytearray()
    wheelsChangeRightFrontLeftBack.append(0x55)
    wheelsChangeRightFrontLeftBack.append(0xAA)
    wheelsChangeRightFrontLeftBack.append(0x07)
    wheelsChangeRightFrontLeftBack.append(0x03)
    wheelsChangeRightFrontLeftBack.append(0x01)
    wheelsChangeRightFrontLeftBack.append(0x10)
    wheelsChangeRightFrontLeftBack.append(0x00)

    wheelsChangeRightFrontRightBack = bytearray()
    wheelsChangeRightFrontRightBack.append(0x55)
    wheelsChangeRightFrontRightBack.append(0xAA)
    wheelsChangeRightFrontRightBack.append(0x07)
    wheelsChangeRightFrontRightBack.append(0x03)
    wheelsChangeRightFrontRightBack.append(0x01)
    wheelsChangeRightFrontRightBack.append(0x11)
    wheelsChangeRightFrontRightBack.append(0x00)

    wheelsChangeLeftBackRightBack = bytearray()
    wheelsChangeLeftBackRightBack.append(0x55)
    wheelsChangeLeftBackRightBack.append(0xAA)
    wheelsChangeLeftBackRightBack.append(0x07)
    wheelsChangeLeftBackRightBack.append(0x03)
    wheelsChangeLeftBackRightBack.append(0x10)
    wheelsChangeLeftBackRightBack.append(0x11)
    wheelsChangeLeftBackRightBack.append(0x00)

    wheelsChangeSpareFrontLeft = bytearray()
    wheelsChangeSpareFrontLeft.append(0x55)
    wheelsChangeSpareFrontLeft.append(0xAA)
    wheelsChangeSpareFrontLeft.append(0x07)
    wheelsChangeSpareFrontLeft.append(0x03)
    wheelsChangeSpareFrontLeft.append(0x00)
    wheelsChangeSpareFrontLeft.append(0x05)
    wheelsChangeSpareFrontLeft.append(0x00)

    wheelsChangeSpareFrontRight = bytearray()
    wheelsChangeSpareFrontRight.append(0x55)
    wheelsChangeSpareFrontRight.append(0xAA)
    wheelsChangeSpareFrontRight.append(0x07)
    wheelsChangeSpareFrontRight.append(0x03)
    wheelsChangeSpareFrontRight.append(0x01)
    wheelsChangeSpareFrontRight.append(0x05)
    wheelsChangeSpareFrontRight.append(0x00)

    wheelsChangeSpareBackLeft = bytearray()
    wheelsChangeSpareBackLeft.append(0x55)
    wheelsChangeSpareBackLeft.append(0xAA)
    wheelsChangeSpareBackLeft.append(0x07)
    wheelsChangeSpareBackLeft.append(0x03)
    wheelsChangeSpareBackLeft.append(0x10)
    wheelsChangeSpareBackLeft.append(0x05)
    wheelsChangeSpareBackLeft.append(0x00)
    
    wheelsChangeSpareBackRight = bytearray()
    wheelsChangeSpareBackRight.append(0x55)
    wheelsChangeSpareBackRight.append(0xAA)
    wheelsChangeSpareBackRight.append(0x07)
    wheelsChangeSpareBackRight.append(0x03)
    wheelsChangeSpareBackRight.append(0x11)
    wheelsChangeSpareBackRight.append(0x05)
    wheelsChangeSpareBackRight.append(0x00)

    reset = bytearray()
    reset.append(0x55)
    reset.append(0xAA)
    reset.append(0x06)
    reset.append(0x58)
    reset.append(0x55)
    reset.append(0xE0)

    connect()
    try:
        ser.write(querySensorID)
    except (serial.SerialException, serial.SerialTimeoutException):
        print ("serial port unavailable, reconnecting...")
        ser.close()
        connect()
    except:
        raise

	# read cmds from the radio and act like a cd changer
    while(1):
        try:
            ser.write(querySensorID)
            a = ser.read()
            if a == (b'\x55'):
                current_time=str(datetime.datetime.now())
                b = ser.read()
                if b == b'\xAA':
                    cmd = ser.read()
                    if cmd == b'\x08':
                        tireID = ord(ser.read())
                        pressure = ord(ser.read())
                        temperature = ord(ser.read())
                        state = ord(ser.read())
                        crc = ord(ser.read())
                        if crc == ord(a)^ord(b)^ord(cmd)^tireID^pressure^temperature^state:
                            if tireID == 0:
                                print ("---------------------------------------------------------------------------------------")
                                tire = "Front left"
                            elif tireID == 0x01:
                                tire = "Front right"
                            elif tireID == 0x10:
                                tire = "Rear left"
                            elif tireID == 0x11:
                                tire = "Rear right"
                            elif tireID == 5:
                                tire = "Spare"
                            if (state & 0b00100000) != 0:
                                print (current_time+" Lost signal of "+tire+" tire!")
                            elif (state & 0b00001000) != 0:
                                print (current_time+" "+tire+" tire leaking! "+str(float(pressure * 3.44))+"kPa / "+str(temperature - 50)+"°C")
                            elif (state & 0b00010000) != 0:
                                print (current_time+" Low battery at "+tire+"! "+str(float(pressure * 3.44))+"kPa / "+str(temperature - 50)+"°C")
                            elif (state & 0b00000010) != 0:
                                print (current_time+" High battery voltage?? at "+tire+"! "+str(float(pressure * 3.44))+"kPa / "+str(temperature - 50)+"°C")
                            elif (state & 0b00000100) != 0:
                                print (current_time+" High temperature at "+tire+"! "+str(float(pressure * 3.44))+"kPa / "+str(temperature - 50)+"°C")
                            else:
                                print(current_time+" "+tire+" tire: "+str(float(pressure * 3.44))+"kPa / "+str(temperature - 50)+"°C")
                            ser.write(eventACK)
                    elif cmd == b'\x09':
                        tireID = ord(ser.read())
                        ID0 = ord(ser.read())
                        ID1 = ord(ser.read())
                        ID2 = ord(ser.read())
                        ID3 = ord(ser.read())
                        crc = ord(ser.read())
                        if crc == ord(a)^ord(b)^ord(cmd)^tireID^ID0^ID1^ID2^ID3:
                            #print tires ids:
                            if tireID == 1:
                                text = "Front left"
                            if tireID == 2:
                                text = "Front right"
                            if tireID == 3:
                                text = "Rear left"
                            if tireID == 4:
                                text = "Rear right"
                            if tireID == 5:
                                text = "Spare"
                            text = text+" id: "
                            if ID0 < 0xF:
                                ID0 = '0' + '%x' % ID0
                            else:
                                ID0 = '%x' % ID0
                            if ID1 < 0xF:
                                ID1 = '0' + '%x' % ID1
                            else:
                                ID1 = '%x' % ID1
                            if ID2 < 0xF:
                                ID2 = '0' + '%x' % ID2
                            else:
                                ID2 = '%x' % ID2
                            if ID3 < 0xF:
                                ID3 = '0' +'%x' % ID3
                            else:
                                ID3 = '%x' % ID3
                            text += ID0 + ID1 + ID2 + ID3
                            print (text)
                            ser.write(eventACK)
                    elif cmd == b'\x06':
                        subcmd=ser.read()
                        if (subcmd == 0):
                                ssubcmd=ser.read()
                                print(ord(ssubcmd))
                                if (ssubcmd == -120): #handshake?
                                    ser.write(heartbeat)
                        elif (ord(subcmd) == 24): #pairing
                            tireID=ord(ser.read())
                            if tireID == 0:
                                tire = "Front left"
                            elif tireID == 0x01:
                                tire = "Front right"
                            elif tireID == 0x10:
                                tire = "Rear left"
                            elif tireID == 0x11:
                                tire = "Rear right"
                            elif tireID == 5:
                                tire = "Spare"
                            text += " sensor pairing successfull"
                            print(text)
                            ser.write(eventACK)
                        elif (ord(subcmd) == -75):
                            #ack with time ?
                            print(ord(ser.read())) ##changing in time
                    elif cmd == b'\x07':
                        subcmd=ser.read()
                        if (ord(subcmd) == 48): #tire swap
                            tireID1=ser.read()
                            tireID2=ser.read()
                            if tireID1 == 0:
                                tire1 = "Front left"
                            elif tireID1 == 0x01:
                                tire1 = "Front right"
                            elif tireID1 == 0x10:
                                tire1 = "Rear left"
                            elif tireID1 == 0x11:
                                tire1 = "Rear right"
                            elif tireID1 == 5:
                                tire1 = "Spare"
                            if tireID2 == 0:
                                tire2 = "Front left"
                            elif tireID2 == 0x01:
                                tire2 = "Front right"
                            elif tireID2 == 0x10:
                                tire2 = "Rear left"
                            elif tireID2 == 0x11:
                                tire2 = "Rear right"
                            elif tireID2 == 5:
                                tire2 = "Spare"
                            print ("exchange: ",tire1," for ",tire2)
                    else:
                        print("cmd: ",ord(cmd))
                        packet_bytes=int.from_bytes(cmd,"big")
                        packet_bytes=packet_bytes-3
                        while packet_bytes>0:
                            print(" "+ str(ser.read()))
                            packet_bytes=packet_bytes-1
        except (serial.SerialException, serial.SerialTimeoutException):
            print ("serial port unavailable, reconnecting...")
            ser.close()
            connect()
        except:
            raise
except (KeyboardInterrupt):
    if ser is not None:
        ser.close()
        print ("port closed!")
    print ("KeyboardInterrupt detected, exiting...")
