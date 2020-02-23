import socket
import sys

s = socket.socket()
tsListenPort = int(sys.argv[1])
s.bind(('', tsListenPort))
s.listen(5)
entry_table = {}
path_name2 = "PROJI-DNSTS.txt"
file3 = open(path_name2)
entry_table = {}
while 1:
    lines = file3.readlines()
    if not lines:
        break
    for line in lines:
        line = line.strip()
        x = line.split(" ")
        entry_table[x[0].lower()] = line
print "Listening"
while True:
    c, addr = s.accept()
    str = c.recv(1024).decode().strip().lower()
    if(str in entry_table):
        c.send(entry_table[str].encode())
    else:
        c.send((str + " - Error:HOST NOT FOUND").encode())
    c.close()
	