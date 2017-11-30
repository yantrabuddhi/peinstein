#!/usr/bin/env python
import serial
import sys

if (len(sys.argv))<4:
	print("usage: ewifi.py <serial device> <ssid> <password>")
print("\ndevice: "+sys.argv[1])
print("\ninit_wifi(\""+sys.argv[2]+"\",\""+sys.argv[3]+"\")\n")
ser = serial.Serial(sys.argv[1],115200)
ser.write("\ninit_wifi(\""+sys.argv[2]+"\",\""+sys.argv[3]+"\")\n")
