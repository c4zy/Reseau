import socket, sys

domain = "192.168.56.103"
port = 21  # FTP
state = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((domain, port))

while True:
	data = (s.recv(1024)).decode("UTF-8")
	print(data)
	
	if state == 0 and data.startswith("220"):
		s.send("USER user\r\n".encode("UTF-8"))
		state = 1
	elif state == 1 and data.startswith("331"):
		s.send("PASS user\r\n".encode("UTF-8"))
		state = 2
	elif state == 2 and data.startswith("230"):
		s.send("SYST\r\n".encode("UTF-8"))
		state = 3
	else:
		break

s.close()
