# import du module de gestion des sockets  
import socket 

# import du module de gestion du temps
import time

# import du module de threading 
from _thread import *
import threading 
		
class NetworkElement:
		
	def __init__(self, idLocal, idDistant, ipLocal, ipDistant):
	
		port = 5000
		self.idLocal = idLocal
		self.idDistant = idDistant
		self.ipLocal = ipLocal
		self.ipDistant = ipDistant
		self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		print("[+] "+str(ipLocal)+":"+str(port+idLocal))
		
		# Initialisation de l'envoi
		port = port + self.idLocal
		s = self.serverSocket 
		s.bind((ipLocal, port)) 
		l = threading.Lock()
		l.acquire()
		print('[ Machine ',idLocal,'|',ipLocal ,':',(port),']\n')  
		l.release()
		
		background_thread = threading.Thread(target=self.listening)
		background_thread.start()
		
	def listening(self):
		# Mise sur écoute de la socket
		while True:
			s = self.serverSocket
			s.listen(5)
 
			# Connexion avec le client
			c, addr = s.accept()
			print('[ Machine ',self.idLocal,'|',self.ipLocal ,':',(5000+self.idLocal),' ]  Message recu de :', addr[0],':',addr[1])
		
	def send(self, message):
		print('\n[ Machine ',self.idLocal,'|',self.ipLocal ,':',(5000+self.idLocal),' ]')
		
		# Etablissement de la connexion avec le receveur
		port = 5000 + self.idDistant
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((self.ipDistant, port))
		
		# Fonctions d'envoi