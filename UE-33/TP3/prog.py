# coding utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.56.103", 21))

reply = s.recv(2048).decode("utf-8")
state = int(reply.split(" ")[0])
print(reply)

while True:
	if state == 220:
		s.send("USER user\r\n".encode("utf-8"))
	elif state == 331:
		s.send("PASS user\r\n".encode("utf-8"))
	elif state == 230:
		s.send("SYST\r\n".encode("utf-8"))
	elif state == 215:
		break
		
	reply = s.recv(1024).decode("utf-8")
	print(reply)
	state = int(reply.split(" ")[0])
	
s.close()

print("EOF")
