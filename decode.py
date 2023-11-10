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
    while 1:
        try:
            print("connecting")
            global ser
            ser = serial.Serial("/dev/tty.usbserial-210", 9600)
            ser.timeout = 5
            return
        except:
            time.sleep(2)  # wait before retrying
            print("retrying")


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

    eartbeat = bytearray()
    eartbeat.append(0x55)
    eartbeat.append(0xAA)
    eartbeat.append(0x06)
    eartbeat.append(0x19)
    eartbeat.append(0x00)
    eartbeat.append(0xE0)

    # ?? 0x55, 0xAA, 0x06, 0x5B, ??, 0xE0

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
    print("connected")
    try:
        ser.write(querySensorID)
    except (serial.SerialException, serial.SerialTimeoutException):
        print("serial port unavailable, reconnecting...")
        ser.close()
        connect()
    except:
        raise

    # read cmds from the radio and act like a cd changer
    while 1:
        try:
            a = ser.read()
            #print(a)
            if a == chr(0x55):
                current_time = str(datetime.datetime.now())
                print(current_time)
                b = ser.read()
                if b == chr(0xAA):
                    cmd = ser.read()
                    if cmd == chr(0x08):
                        tireID = ord(ser.read())
                        pressure = ord(ser.read())
                        temperature = ord(ser.read())
                        state = ord(ser.read())
                        crc = ord(ser.read())
                        if (
                            crc
                            == ord(a)
                            ^ ord(b)
                            ^ ord(cmd)
                            ^ tireID
                            ^ pressure
                            ^ temperature
                            ^ state
                        ):
                            # print ("sensor information")
                            if tireID == 0:
                                tire = "Front left"
                                # print ("front left")
                            elif tireID == 0x01:
                                tire = "Front right"
                                # print ("Front right tire")
                            elif tireID == 0x10:
                                tire = "Rear left"
                                # print ("left back tire")
                            elif tireID == 0x11:
                                tire = "Rear right"
                                # print ("Rear Right tire")
                            elif tireID == 5:
                                tire = "Spare"
                                # print ("spare tire")
                            if (state & 0b00100000) != 0:
                                print(
                                    current_time + " Lost signal of " + tire + " tire!"
                                )
                            elif (state & 0b00001000) != 0:
                                print(
                                    current_time
                                    + " "
                                    + tire
                                    + " tire leaking! "
                                    + str(float(pressure * 3.44))
                                    + "kPa / "
                                    + str(temperature - 50)
                                    + "°C"
                                )
                            elif (state & 0b00010000) != 0:
                                print(
                                    current_time
                                    + " Low battery at "
                                    + tire
                                    + "! "
                                    + str(float(pressure * 3.44))
                                    + "kPa / "
                                    + str(temperature - 50)
                                    + "°C"
                                )
                            else:
                                print(
                                    current_time
                                    + " "
                                    + tire
                                    + " tire: "
                                    + str(float(pressure * 3.44))
                                    + "kPa / "
                                    + str(temperature - 50)
                                    + "°C"
                                )

                if cmd == chr(0x09):
                    tireID = ord(ser.read())
                    ID0 = ord(ser.read())
                    ID1 = ord(ser.read())
                    ID2 = ord(ser.read())
                    ID3 = ord(ser.read())
                    crc = ord(ser.read())

                    if (
                        crc
                        == ord(a) ^ ord(b) ^ ord(cmd) ^ tireID ^ ID0 ^ ID1 ^ ID2 ^ ID3
                    ):
                        # print tires ids:
                        if tireID == 1:
                            text = "Front left"
                        if tireID == 2:
                            text = "Front right"
                        if tireID == 3:
                            text = "Rear left"
                        if tireID == 4:
                            text = "Rear left"
                        if tireID == 5:
                            text = "Spare"

                        text = text + " id: "

                        if ID0 < 0xF:
                            ID0 = "0" + "%x" % ID0
                        else:
                            ID0 = "%x" % ID0
                        if ID1 < 0xF:
                            ID1 = "0" + "%x" % ID1
                        else:
                            ID1 = "%x" % ID1
                        if ID2 < 0xF:
                            ID2 = "0" + "%x" % ID2
                        else:
                            ID2 = "%x" % ID2
                        if ID3 < 0xF:
                            ID3 = "0" + "%x" % ID3
                        else:
                            ID3 = "%x" % ID3

                        text += ID0 + ID1 + ID2 + ID3
                        print(text)

        except (serial.SerialException, serial.SerialTimeoutException):
            print("serial port unavailable, reconnecting...")
            ser.close()
            connect()
        except:
            raise
except KeyboardInterrupt:
    if ser is not None:
        ser.close()
        print("port closed!")
    print("KeyboardInterrupt detected, exiting...")
