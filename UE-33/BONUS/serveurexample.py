# coding: utf-8

import socket, sys, threading

def clientthread(conn):
	conn.send(("Hello from " + HOST + ":" + str(PORT) + "\n").encode("UTF-8"))
	
	while True:
		# Recieving from client
		data = conn.recv(1024).decode("UTF-8")
		reply = "Reçu: " + data
		
		if data.upper().strip() == "FIN" or data.strip() == "":
			break
		
		conn.sendall(reply.encode("UTF-8"))
	
	conn.close()

HOST = "0.0.0.0"
PORT = 2005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print("Bind failed. Error code: " + str(msg.errno) + " Message " + msg.strerror)
	sys.exit()
	
s.listen()

print("Serveur en écoute sur " + HOST + ":" + str(PORT))

while True:
	try:
		conn, addr = s.accept()
		print("Connexion de " + addr[0] + ":" + str(addr[1]))
		
		t = threading.Thread(None, clientthread, None, (conn,), {})
		t.start()
	except KeyboardInterrupt:
		print("Stop.\n")
		break
		
s.close()

print("EOF")




















