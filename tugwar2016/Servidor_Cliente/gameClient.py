import time, socket
from threading import Thread
from random import randint  

#O programa segue uma ordem "cronológica", na qual a função anterior chama a próxima. Nas divisões, são momentos em que a anterior não chamou a seguinte 

class Client():
	def __init__(self):
		self.closeAll = False
		self.port = 80
		self.connection_status = 'none'
		self.percentage = .5
		self.valuerecv = 0

	def showMyHost(self): 
		try:
			IP = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][1] #ultrabooks tem um endereço de IP a menos
		except:
			IP = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0] #a estrutura try e except é usada pra contornar isso
		return IP

	def setHost(self, serverIP): #Insere o host do servidor
		self.hostServer = serverIP

	def setName(self, name): #Insere o nome do jogador
		self.Name = name

	def clientStart(self): #o client envia antes da informação, qual o tipo de dado que ele está enviando (time?, nome?)
		self.connectionDone = self.sendInfos = self.retryConnection = self.stopReceiving = False
		self.Wait = True
		self.lastValue = 0

		while not self.closeAll: #closeAll é usado para evitar que o cliente fica aberto
			if not self.connectionDone and not self.retryConnection:
				print('Client Starting...')
				self.clientTCP = socket.socket()
				try:
					self.clientTCP.connect((self.hostServer, self.port))
				except: pass

				self.clientTCP.setblocking(0)
				timeout0 = time.clock()

				data = str()

				self.checkStatus('Trying to connect...')

				while not self.closeAll:
						if time.clock()-timeout0 >= 20:
							timeout = True
							break
						else:
							timeout = False
							try:
								data = self.clientTCP.recv(1024)
								if data:
									if data == 'connected as principal'.encode():
										self.checkStatus('Connected as principal')
										break
									elif data == 'connected'.encode():
										self.checkStatus('Connected')
										break
							except:
								pass

				if timeout:
					self.checkStatus('Timeout')
					return 'timeout'
				else:
					self.connectionDone = True
					print('Connection Done')

				print('Waiting to send')
				while not self.closeAll:
					try:
						data = self.clientTCP.recv(1024)
						if data == 'connection closed'.encode():
							break
					except: pass	

			if self.connectionDone and self.sendInfos:
				print('Sending name...')
				self.clientTCP.send('sending my name'.encode())
				time.sleep(1)
				self.clientTCP.send(str(self.setName).encode())
				print('Name sent')
				time.sleep(1)

				print('Sending my team...')
				self.clientTCP.send('sending my team'.encode())
				time.sleep(1)
				self.clientTCP.send(str(self.myteam).encode())
				print('Team sent')

				self.Wait = True

				print('Waiting start...')

				while not self.closeAll:
					try:
						data = self.clientTCP.recv(1024)
						if data == 'start'.encode():
							break
					except: pass

				print('started')
				self.Wait = False
				break
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def SendInfos(self):
		print("Preparing to send Infos...")
		self.sendInfos = True
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def checkStatus(self, value):
		self.connection_status = value
		print(value)

	def Status(self):
		return self.connection_status
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def closeConnection(self):
		self.clientTCP.send('close'.encode())
#----------------------------------------------------------------------------------------------------------------------------------------------------------------		
	def setTeam(self, team):
		if team == 'random':
			number = randint(0, 1)
			if number == 0:
				team = 'blue'
			else:
				team = 'red'
		self.myteam = team
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def displayTeams(self):
		self.clientTCP.send('update players'.encode())
		with self.setblocking(1):
			update = self.clientTCP.recv(1024)
		update2 = str(update).split("'")
		update3 = str(update).split("][")
		redUp = (str(update3).split("["))[1].split(",")
		blueUp = (str(update3).split("]"))[2].split(",")
		print(redUp, blueUp)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def StartGame(self):
		print('Sending start...')
		self.clientTCP.send('start game'.encode())
		print('Start sent')
		self.waitStart()

	def waitStart(self):	
		return self.Wait
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def sendPackages(self, value):
		self.totalclicks(int(value))
		print('Sent', value)
		self.clientTCP.send((str(value)).encode())
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def totalclicks(self, value):
		self.myclicks = value
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def receivePoints(self):
		while not self.closeAll:
			if self.stopReceiving:
				print('Stopped Receiving')
				break
			try:
				value = self.clientTCP.recv(1024)
				print('recv:', value)
				self.valuerecv = str(value).split("'")[1]
			except: pass
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
	def getValue(self):
		if self.valuerecv == 'blue' or self.valuerecv == 'red':
			self.stopReceiving = True
			return str(self.valuerecv)

		elif int(self.valuerecv) >= 0:
			if len(str(self.valuerecv)) < 3:
				return int(self.valuerecv)
			else:
				print('Recv Ignored')
		else:
			if len(str(self.valuerecv)) < 4:
				return int(self.valuerecv)
			else:
				print('Recv Ignored')

	def Close(self): #fecha a conexão do cliente
		self.closeAll = True
		print('Client Closed')
		self.clientTCP.close()

	def Reset(self): #reseta todas as variáveis pra quando o jogo reinicia
		self.closeAll = False
		self.port = 80
		self.connection_status = 'none'
		self.percentage = .5
		self.valuerecv = 0