import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def importServerList():
	serverList = 0
	serverListFile = open('ServerList.txt')
	line = serverListFile.read().split()
	for serverList in line:
		serverList = serverList.rstrip('\n')
		ping(serverList)

def ping(host):
	output = []
	command = ['ping', '-n', '1', host]
	output = subprocess.run(command, encoding='utf-8', stdout=subprocess.PIPE)
	output = output.stdout.splitlines()
	stringSplit(output)


def stringSplit(list):
	list_string = 0
	count = 0
	word = 0
	for list_string in list:
		list_string = list_string.rstrip(',')
		count = count + 1
	print('This is word number {}: {}'.format(2, list[2]))
#This print line was used to determine the correct line of text I needed



importServerList()
#ping('google.com')


"""
Import list of servers
Separate into a list, and grab the oldschoolXX portion, where XX is the 
	server number
Send each line separately to 
"""