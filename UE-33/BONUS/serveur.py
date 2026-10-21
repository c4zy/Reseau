# coding utf-8

import socket, sys, threading

def headX(L, x):
	res = ""
	i = 0
	while i < x:
		res += str(L[i]) + " "
		i += 1
	return res
	
def tailX(L, x):
	res = ""
	i = x+1
	while i < len(L):
		res += str(L[i]) + " "
		i += 1
	return res

def clientthread(conn):
	conn.send(("Hello from " + HOST + ":" + str(PORT) + "\n").encode('UTF-8'))
	values = []
	
	while True:
		data = conn.recv(1024).decode("UTF-8")
		reply = "> "
		request = data.upper().strip()
		
		if request == "DATA":
			instr = conn.recv(1024).decode("UTF-8")
			while instr.strip() != "":
				values += [int(instr)]
				instr = conn.recv(1024).decode("UTF-8")
		
		elif request == "MIN":
			conn.send((reply + str(min(values)) + "\n").encode("UTF-8"))
			
		elif request == "MAX":
			conn.send((reply + str(max(values)) + "\n").encode("UTF-8"))
			
		elif request == "SUM":
			conn.send((reply + str(sum(values)) + "\n").encode("UTF-8"))
			
		elif request.split()[0] == "HEAD":
			conn.send((reply + str(headX(values, int(request.split()[1]))) + "\n").encode("UTF-8"))
			
		elif request.split()[0] == "TAIL":
			conn.send((reply + str(tailX(values, int(request.split()[1]))) + "\n").encode("UTF-8"))
			
		elif request == "FIN":
			break
			
	conn.close()

HOST = "0.0.0.0"
PORT = 2007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
	s.bind((HOST, PORT))
	
except socket.error:
	print("Bind error!")
	sys.exit()
	
s.listen()

print("En attente sur " + HOST + ":" + str(PORT))

while True:
	try:
		conn, addr = s.accept()
		print("Connected at " + addr[0] + ":" + str(addr[1]))
		
		t = threading.Thread(None, clientthread, None, (conn,), {})
		t.start()

	except KeyboardInterrupt:
		print("Stop.\n")
		break
	
s.close()
print("EOF")
