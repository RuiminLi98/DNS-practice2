import socket
import sys

rsHostName = sys.argv[1]
rsListenPort = int(sys.argv[2])
tsListenPort = int(sys.argv[3])
file = open('PROJI-HNS.txt')
file2 = open('RESOLVED.txt','w')

while 1:
	lines = file.readlines()
	if not lines:
		break
	for line in lines:
		s = socket.socket()
		s.connect((rsHostName, rsListenPort))
		s.send(line.encode())
		str = s.recv(1024).decode()
		str = str.strip()
		tempStr = str[-1:]
		if(tempStr == 'S'):
			temp = str.split(" ") 
			tsHostName = temp[0]
			s2 = socket.socket()
			s2.connect((tsHostName, tsListenPort))
			s2.send(line.encode())	
			str = s2.recv(1024).decode()
			str = str.strip()
		file2.write(str)
		file2.write('\n')
		s.close()