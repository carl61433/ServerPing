import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os

def importServerList():
	serverList = []
	with open('ServerList.txt') as serverListFile:
		serverList = serverListFile.read()
	print(serverList)
	return serverList
	"""for serverList in line:
		serverList = serverList.rstrip('\n')
		ping(serverList)
	"""
	###Need to move the for loop to another function###

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
"""
def main(): #Main function to put everything together
	server_file = input('Specify your server list here: ')
	importServerList(server_file)
"""


"""
Import list of servers
Separate into a list, and grab the oldschoolXX portion, where XX is the 
	server number
"OldschoolXX" needs to be associated with ping (time=XXXms)
"""

##########Just realized at 11:31PM I should##########
##########probably utilize return and have one#########
##########parent function put everything together###########