# coding utf-8

import socket, struct, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("sinfo2.univ-tln.fr", 37))

s.send("".encode("utf-8"))

reply = time.ctime(socket.ntohl(struct.unpack('I', s.recv(1024))[0]) - 2208988800) 

print(reply)
s.close()

print("EOF")
