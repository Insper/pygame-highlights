import tkinter as tk
from threading import Thread
try:
	from GameServer import Server
except:
	from Servidor_Cliente.GameServer import Server
import time

class Screen():
	def __init__(self):
		print('Screen Started')
		self.server = Server()
		self.ServerOnce = False

		self.window = tk.Tk()
		self.window.geometry('250x300')
		self.window.title('Create')
		self.window.resizable(0, 0)
		for i in range(6):
			self.window.rowconfigure(i, minsize=50)
		self.window.columnconfigure(0, minsize=250)

		self.title = tk.Label(self.window)
		self.title.configure(text='SERVER CONTROL', bg='yellow')
		self.title.configure(font=('pixelmix', 15, 'bold'))
		self.title.grid(row=0, rowspan=2, column=0, sticky='nsew')

		self.infoLabel = tk.Label(self.window)
		self.infoLabel.configure(text='Click "Open Server"\n\nto start the Server'.upper())
		self.infoLabel.configure(font=('pixelmix', 10))
		self.infoLabel.grid(row=2, rowspan=2, column=0, sticky='nsew')

		self.bot_openServer = tk.Button(self.window)
		self.bot_openServer.configure(text='OPEN SERVER', command=self.SecondScreen)
		self.bot_openServer.configure(font=('pixelmix', 11))
		self.bot_openServer.grid(row=4, rowspan=2, column=0, sticky='nsew')

	def ServerRun(self):
		self.server.serverStart()
				
	def SecondScreen(self):
		if not self.ServerOnce:
			self.ServerOnce = True
			serverThread = Thread(target=self.ServerRun)
			serverThread.start()

		self.infoLabel.configure(text='Click "Close Connection" to\n\nstop accepting new players'.upper())
		self.infoLabel.configure(font=('pixelmix', 8))
		self.infoLabel.grid(row=2, rowspan=2, column=0, sticky='nsew')

		self.ip = tk.Label(self.window)
		var = tk.StringVar()
		try:
			var.set('IP: ' + self.server.host)
		except: pass
		self.ip.configure(textvariable=var, bg='black')
		self.ip.configure(font=('pixelmix', 11), fg='white')
		self.ip.grid(row=4, column=0, sticky='nsew')

		self.bot_stopAcpt = tk.Button(self.window)
		self.bot_stopAcpt.configure(text='CLOSE CONNECTION', command=self.stopAcpt)
		self.bot_stopAcpt.configure(font=('pixelmix', 11))
		self.bot_stopAcpt.grid(row=5, column=0, sticky='nsew')

	def stopAcpt(self):
		self.server.stopAccepting()
		self.StartWindow()

	def StartWindow(self):
		self.infoLabel.configure(text='Good Luck'.upper())
		self.infoLabel.configure(font=('pixelmix', 12))
		self.infoLabel.grid(row=2, rowspan=2, column=0, sticky='nsew')

		self.bot_start = tk.Button(self.window)
		self.bot_start.configure(text='START GAME', command=self.CommandStart)
		self.bot_start.configure(font=('pixelmix', 11))
		self.bot_start.grid(row=4, rowspan=2, column=0, sticky='nsew')

	def CommandStart(self):
		self.server.startGame()
		self.window.destroy()

	def start(self):
		self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.window.mainloop()

	def on_closing(self):
		try:
			self.server.Close()
		except: pass
		self.window.destroy()

screen = Screen()
screen.start()