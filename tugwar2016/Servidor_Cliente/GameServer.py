import socket, time
from threading import Thread #threads geram "microservers" que computam a pontuação de cada usuário
from random import randint

#O programa segue uma ordem "cronológica", na qual a função anterior chama a próxima. Nas divisões, são momentos em que a anterior não chamou a seguinte

class Server():
	def __init__(self):
		self.closeAll = False
		try:
			self.host = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][1] #arrumar para todos pcs try except
		except:
			self.host = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][0]  #pega o IP da máquina
		self.port = 80 #a porta da conexão é a porta 80 web (sempre aberta, não precisa)

	def ServerIP(self):
		return self.host

	def serverStart(self):	#a função inicia o servidor
		print("Servidor Iniciado") #Todos os prints são para demosntrar visualmente o que está acontecendo
		print('Server IP:', self.host, '\n')
		self.clients_connected = list()
		self.Restarting = False
		self.START = False #variável setada logo no início que será usada pra iniciar o jogo

		self.servertcp = socket.socket() #A conexão estabelecida é TCP
		self.servertcp.bind((self.host, self.port)) 

		self.servertcp.listen(1)
		self.servertcp.setblocking(0) #diz que está aberto a receber múltiplas conexões
		self.stop_acpt = False

		while not self.closeAll: #escuta os clientes
			if self.verifyAcpt():
				break
			try:
				c, addr = self.servertcp.accept()
				if not (c, addr) in self.clients_connected:
					self.clients_connected.append((c, addr))
					print(addr)	
					c.send('connected'.encode()) #Se conectou, confirma ao usuário
			except: pass
		print(self.clients_connected)
		print("Open connection ended")

		for client in self.clients_connected:
			client[0].send('connection closed'.encode())

		self.ReceiveThreadsDone = 0
		self.team_blue = list()
		self.team_red = list()
		self.BlueNames = list()
		self.RedNames = list()
		self.blueDict = dict()
		self.redDict = dict()
		self.generalDict = dict()
		self.NameDict = dict()

		self.pointsRED = 0
		self.pointsBLUE = 0
		self.doneThreads = 0

		self.winner = str()

		self.CloseThis = False

		#PARA CADA USUÁRIO ABRE-SE UMA THREAD, QUE COMPUTARÁ INDIVIDUALMENTE A PONTUÇÃO, ADICIONANDO-A A UMA VARIÁVEL QUE TODAS AS THREADS TEM ACESSO
		for client in self.clients_connected:
			self.generalDict[client] = Thread(target=self.serverForClient, args=(client,))
			self.generalDict[client].start()
		self.EndOfGame()

	def verifyAcpt(self):
		return self.stop_acpt

	def stopAccepting(self):
		self.stop_acpt = True

	def serverForClient(self, client): #código que é rodado para cada cliente
		self.myteam = str()
		mypoints = 0
		print("Server Working")
		while not self.closeAll:
			try:
				data = client[0].recv(1024)

				if data == 'sending my name'.encode(): ##################### Código para enviar o nome
					print("Receiving Name\n")
					while not self.closeAll:
						try:
							name = client[0].recv(1024)
							name2 = str(name).split("'")
							self.NameDict[client] = [str(name2[1])] #armazena o nome enviado em um dicionário
							print('Name Received')
							print(str(name2[1]), 'playing')
							break
						except: pass

				elif data == "sending my team".encode(): ##################### Código para enviar o time
					print("Receiving Team\n")
					while not self.closeAll:
						try:
							team = client[0].recv(1024)
							team2 = str(team).split("'")
							if team == 'blue'.encode():
								self.team_blue.append(client)
								self.BlueNames.append(str(name2[1]))
								self.blueDict[str(name2[1])] = 0
							elif team == 'red'.encode():
								team2 = str(team).split("'")
								self.team_red.append(client)
								self.BlueNames.append(str(name2[1]))
								self.redDict[str(name2[1])] = 0
							client[0].send(str(team2[1]).encode())	
							self.myteam = team2[1]
							print("Team Received")
							print(str(name2[1]), str(self.myteam))
							break
						except: pass

			except: pass		

			if self.START: ##################### Código para começar o jogo
				print('''\n################################################
GAME STARTED
################################################\n''')
				initial_time = time.clock()
				print('Receiving...\n')
				while not self.closeAll:
					if 0 <= (time.clock()-initial_time)%.1 <= .005:
						msg = self.totalPoints()
						print('Sending:', msg)
						if msg <= -100: #O servidor é responsável por computar se houve um ganhador. -100 equivale a azul ganhou, 0 no meio, e 100 vermelho.
							msg = "blue"
							self.winner = 'blue'
							self.CloseThis = True
							break
						elif msg >= 100:
							msg = "red"
							self.winner = 'red'
							self.CloseThis = True
							break
						client[0].send(str(msg).encode())

					try:
						pack = client[0].recv(1024)
						print(pack)
						pack2 = str(pack).split("'")
						print(name2[1], pack2[1])
						if int(pack2[1]) >= 3:
							if int(pack2[1]) <= 30:
								self.addPack(self.myteam, pack2[1])
							else:
								print('Recv Ignored')	
						else:
							print('Recv Ignored')

					except: pass

			if self.CloseThis:
				break

		self.doneThreads += 1

	def startGame(self):
		self.START = True
		self.startGameforClients()

	def startGameforClients(self):
		for player in self.clients_connected:
			player[0].send('start'.encode())
			print('Sent to {0}'.format(player[1]))

	def addPack(self, team, pack):
		if team == 'blue':
			self.pointsBLUE += int(pack)
			print('blue:', self.pointsBLUE)
		elif team == 'red':
			self.pointsRED += int(pack)
			print('red:', self.pointsRED)

	def totalPoints(self):
		return self.pointsRED-self.pointsBLUE

	def EndOfGame(self):
		while not self.closeAll:
			if self.doneThreads == len(self.clients_connected):
				break
		print('All threads done')
		for client in self.clients_connected:
			client[0].send(str(self.winner).encode())
		time.sleep(1)
		self.Close()

	def Close(self):
		self.closeAll = True
		self.servertcp.close()
		print('Server Closed')