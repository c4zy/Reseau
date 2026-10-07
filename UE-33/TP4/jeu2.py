import socket, random, sys

HOST = "127.0.0.1"
PORT = 6764

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.bind((HOST, PORT))
except socket.error:
	print("Bind error!")
	sys.exit()
	
s.listen()
print("Listening:")

while True:
	cx, addr = s.accept()
	cx.send("Game\n".encode("UTF-8"))
	
	while True:
		cx.send("Max: ".encode("UTF-8"))
		maxi = int(cx.recv(1024).decode("UTF-8"))
		
		nb = random.randrange(0, maxi+1)
		print(nb)
		lim1, lim2 = 0, maxi
		
		guess = random.randrange(0, maxi+1)
		
		while guess != nb:
			if guess > nb:
				cx.send(("Less " + str(guess) + "\n").encode("UTF-8"))
				lim2 = guess
				
			else:
				cx.send(("More " + str(guess) + "\n").encode("UTF-8"))
				lim1 = guess
				
			guess = random.randrange(lim1, lim2+1)
			
		cx.close()
		
		print(guess)
		break
	break
