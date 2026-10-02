# coding: utf-8

""" Un client http très simple. """

import socket

# Tout d'abord une interrogation du serveur DNS, même si on ne s'en sert pas.

print("Interrogation du DNS: " + socket.gethostbyname("www.univ-tln.fr"))

# 1- Construction d'un objet qui représente la socket
#    vers laquelle le client veut se connecter

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2- ouverture de la connexion vers la socket

s.connect(("www.univ-tln.fr", 80))

# 3- construction du message à envoyer, ici une requête http.

request = "GET / HTTP/1.1\r\n"
request += "Host: www.univ-tln.fr\r\n"
request += "Connection: Close\r\n\r\n"

# 4- envoi sur la socket

s.send(request.encode('UTF-8'))

# 5- lecture de 15 octets sur la socket (augmenter pour lire plus...)

data = s.recv(15)

# 6- convertion de la séquence de 15 octets en une chaîne de caractères
#    et l'afficher.

print(data.decode('utf-8'))

# 7- fermeture de la socket
s.close()
