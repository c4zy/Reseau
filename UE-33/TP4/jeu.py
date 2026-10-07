import socket, sys, random

HOST = '127.0.0.1'
PORT = 2005
MAX_DATA_LEN = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((HOST, PORT))
except socket.error:
	print("Bind error!")
	sys.exit()
	

s.listen()
print("Listening:")
	
while True:
	cs, addr = s.accept()
	print("New connection at {} port {}".format(addr[0], addr[1]))
	
	cs.send("GAME START\n".encode("UTF-8"))
	
	cs.send("Choose a maximum: ".encode("UTF-8"))
	maxi = int(cs.recv(MAX_DATA_LEN).decode("UTF-8"))
	nb = random.randrange(0, maxi+1)
	
	while True:
		cs.send("Guess: ".encode("UTF-8"))
		query = int(cs.recv(MAX_DATA_LEN).decode("UTF-8"))
		
		if query == nb:
			cs.close()
			break
		elif query > nb:
			cs.send("Less\n".encode("UTF-8"))
		else:
			cs.send("More\n".encode("UTF-8"))
			
	break
