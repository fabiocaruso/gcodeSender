import os, socket, json, time, struct

filefolder = "C:/Users/Fabio Caruso/Documents/3D Drucker/"
HOST = '192.168.1.59'
PORT = 49372
sock = False

def connect(sock):
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((HOST, PORT))
			sock.settimeout(1)
			print("Connected successfully")
			return sock
		except socket.error:
			print("Connecting...")
			time.sleep(1)
			pass
			
def disconnect(sock):
	print("Disconnected")
	sock.close()
	return True
		
def send_gcode(sock, gcode_file):
	while True:
		with open(gcode_file + files[0], "r") as fp:
			for line in fp:
				sock.sendall(struct.pack('>I', len(line)) + line.encode())
			sock.sendall(struct.pack('>I', len(";||")) + ";||".encode())
		fp.close()
		break
	os.remove(gcode_file + files[0])

print("Try to connect to: " + HOST + ":" + str(PORT))
sock = connect(sock)
while True:
	files = os.listdir(filefolder)
	if files:
		if os.access(filefolder + files[0], os.R_OK):
			try:
				send_gcode(sock, filefolder)
			except socket.error:
				disconnect(sock)
				time.sleep(2)
				sock = connect(sock)