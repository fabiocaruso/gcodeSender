import socket, json, struct, os, time
from printrun.printcore import printcore
from printrun import gcoder

HOST = '0.0.0.0'
PORT = 49372
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
data = []
while conn:
	raw = conn.recv(4)
	if raw:
		len = struct.unpack('>I', raw)[0]
		line = conn.recv(len).decode()
		if line == ";||":
			if data:
				while True:
					if os.access("/dev/ttyUSB0", os.W_OK):
						p = printcore('/dev/ttyUSB0',115200)
						gcode = gcoder.LightGCode(data)
						if p.startprint(gcode):
							print("Printing...")
						data = ""
						break
					else:
						print("Can't Connect to the 3D Printer. Is it attached?")
						time.sleep(10)
		elif line:
			data.append(line)