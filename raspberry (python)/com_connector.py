import serial
import subprocess

def main():
	if (input("Do you kwon the serial port ? (Y/n)") == 'n'):
		find_com()
	com_input = input("Serial port arduino ?")
	com_output = input("Serial port output ?")
	print_here = 0
	if (input("Do you want to print here ? (Y/n)") == 'y'):
		print_here = 1
	connection_serial_int = serial.Serial(com_input, 9600)
	connection_serial_out = serial.Serial(com_output, 9600)
	line = ""
	while (1):
		char = connection_serial1.read()
		connection_serial2.write(char)
		if (print_here) :
			char = tmp.decode('utf_8')
			if (tmp == '\n'):
				print(ch)
				ch = ""
			else :
				ch += tmp

def find_com():
	if os.name == 'posix'
		print(subprocess.check_output(["wmic", "path", "Win32_SerialPort", "get", "DeviceId"]))
	else :
		print(subprocess.check_output(["ls", "/dev", "|", "grep", "tty"]))

main()
