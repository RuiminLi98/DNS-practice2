import socket
import sys

s = socket.socket()
rsListenPort = int(sys.argv[1])
s.bind(('', rsListenPort))
s.listen(5)
entry_table = {}
path_name2 = "PROJI-DNSRS.txt"
file2 = open(path_name2)
while 1:
    lines = file2.readlines()
    if not lines:
        break
    for line in lines:
		line = line.strip()
		x = line[-1:]
		if x == 'S':
			temp=line
		else:
			x=line.split(" ")
			entry_table[x[0].lower()] = line
while True:
	c, addr = s.accept()
	str = c.recv(1024).decode().strip().lower()
	if(str in entry_table):
		c.send(entry_table[str].encode())
	else:
		c.send((temp).encode())
	c.close()
	