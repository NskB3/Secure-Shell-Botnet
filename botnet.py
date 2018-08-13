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
		print("Output From ",Bot.host)
		print(output)
def add_bot(host, username, password):
	bot = Bot(host, username, password)
	botnet.append(bot)
botnet = []
add_bot('192.168.1.3', 'root', 'toor')
while True:
	inputtedcommand = raw_input("$ ")
	botnet_command(inputtedcommand)
