import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def importServerList(serverNames):
	server_list = []
	with open(serverNames) as serverListFile:
		server_list = serverListFile.read()
	return server_list

def ping(server): #ping an individual server and return in list form
	output = []
	command = ['ping', '-n', '1', server]
	output = subprocess.run(command, encoding='utf-8', stdout=subprocess.PIPE)
	output = output.stdout.splitlines()
	print(output)


def stringSplit(list):
	list_string = 0
	count = 0
	word = 0
	for list_string in list:
		list_string = list_string.rstrip(',')
		count = count + 1
	print('This is word number {}: {}'.format(2, list[2]))
#This print line was used to determine the correct line of text I needed



#importServerList('ServerList.txt')
#Main function to run it all
def main(): #Main function to put everything together
	server_count = 0
	#server_file = input('Specify your server list here: ') 
		#Manual input of list
	server_file = ('ServerList.txt') #Quick testing input
	#ping(importServerList(server_file))


main()