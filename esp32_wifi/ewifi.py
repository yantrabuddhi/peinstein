#!/usr/bin/env python
import serial
import sys
import time

if (len(sys.argv))<4:
	print("usage: ewifi.py <serial device> <ssid> <password>")
print("\ndevice: "+sys.argv[1])
print("\ninit_wifi(\""+sys.argv[2]+"\",\""+sys.argv[3]+"\")\n")
ser = serial.Serial(port=sys.argv[1], baudrate=115200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False)
time.sleep(1)
ser.write("\ninit_wifi(\""+sys.argv[2]+"\",\""+sys.argv[3]+"\")\n")
ser.close()
