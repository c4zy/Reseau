import sys, socket, struct, time

domain = "sinfo2.univ-tln.fr"
port = 37

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((domain, port))

request = ""

s.send(request.encode("UTF-8"))

data = time.ctime((socket.ntohl(struct.unpack('I', s.recv(4))[0])) - 2208988800)

print(data)

