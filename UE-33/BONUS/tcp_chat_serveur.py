# coding utf-8

import socket, sys, select

def broadcastToClients(socket, msg):
	for sock in CONNECTION_LIST:
		if sock != server_socket and sock != socket:
			sock.send(msg.encode("UTF-8"))

CONNECTION_LIST = []
CONNECTION_NICKS = dict()
HOST = "0.0.0.0"
PORT = 5000
RECV_BUFFER = 4096


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	server_socket.bind((HOST, PORT))
except socket.error:
	print("Bind failed!")
	sys.exit()
	
server_socket.listen(10)
CONNECTION_LIST.append(server_socket)
print("Server listening at " + HOST + ":" + str(PORT))

while True:
	try:
		read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])
		
		for sock in read_sockets:
			if sock == server_socket:
				sockfd, addr = server_socket.accept()
				CONNECTION_LIST.append(sockfd)
				print("Client connected at " + addr[0] + ":" + str(addr[1]))
				broadcastToClients(sockfd, "[" + addr[0] + ":" + str(addr[1]) + "] entered the room!\n")
				
			else:
				try:
					data = sock.recv(RECV_BUFFER).decode("UTF-8")
					
					if data:
						request = (data.split()[0]).upper().strip()
						entry = (data.split()[1]).strip()
						
						if request == "NICKNAME":
							if entry:
								CONNECTION_NICKS[sock] = entry
					
						else:
							if sock not in CONNECTION_NICKS:
								broadcastToClients(sock, "<" + str(sock.getpeername()) + "> " + data + "\n")
							else:
								broadcastToClients(sock, "<" + entry + "> " + data + "\n")
							print(data)
						
				except:
					print("Unexpected error: " + sys.exc_info()[0])
					sock.close()
					CONNECTION_LIST.remove(sock)
					continue
		
	except KeyboardInterrupt:
		break

server_socket.close()

print("EOF")
