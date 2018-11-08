import serial
from Phidget22 .Devices.GPS import *

def gps(ch):
	coo = ch.getLatitude()
	coo += " , "
	coo += ch.getLongitude()
	return coo

def main():
	ch = GPS()
	ch.setDeviceSerialNumber(286949)
	ch.setHubPort(-1)
	ch.setIsHubPortDevice(0)
	ch.setChannel(0)
	ch.openWaitForAttachment(5000)
	connection_serial_int = serial.Serial("COM8", 9600)
	input("start")
	connection_serial_out = serial.Serial("COM9", 9600)
	while (1):
		char = connection_serial_int.read()
		connection_serial_out.write(char)
		print(connection_serial_out.read().decode("utf-8"))
		connection_serial_out.write(gps(ch).encode("ascii"))
		print(connection_serial_out.read().decode("utf-8"))

main()