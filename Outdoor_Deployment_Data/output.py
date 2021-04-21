#!/usr/bin/python
import serial
import csv

def WriteData(data):
    f = open('LPP4pktSec.csv','ab')
    with f:
        writer=csv.writer(f)
        writer.writerows(data)


if __name__ == "__main__":
	ser = serial.Serial(
	 port='/dev/ttyUSB0',\
	 baudrate=115200,\
	 parity=serial.PARITY_NONE,\
	 stopbits=serial.STOPBITS_ONE,\
	 bytesize=serial.EIGHTBITS,\
	 timeout=15)
	print("connected to: " + ser.portstr)
	while True:
	 line = ser.readline();
	 data = line.split('\n')
	 if line:
	   _data = data[0].split(',')
	   WriteData([_data])
	   print line
	ser.close()
