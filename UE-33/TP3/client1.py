# coding: utf-8

""" Un client http très simple. """

import socket, struct, time

domain = "sinfo2.univ-tln.fr"
port = 37

print("Interrogation du DNS: " + socket.gethostbyname(domain))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((domain, port))

data = s.recv(4)

data = struct.unpack('I', data)[0]

print(time.ctime(socket.ntohl(data) - 2208988800))

s.close()
