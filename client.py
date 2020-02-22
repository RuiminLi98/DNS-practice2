import threading
import time
import random
import sys
import socket


def server(msg , port_curr):
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', port_curr)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.
    #print(msg)
    #msg="welcome"
    csockid.send(msg.encode('utf-8'))    #this place must have problem
    #print(msg)
    # Close the server socket
    ss.close()
    exit()


def client(port_curr):
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port_curr)
    cs.connect(server_binding)

    # Receive data from the server
    data_from_server = cs.recv(100)

    # close the client socket
    cs.close()
    exit()
    return format(data_from_server.decode('utf-8'))

if __name__ == "__main__":
    rsHostName = sys.argv[1]
    rsListenPort = int(sys.argv[2])
    tsListenPort = int(sys.argv[3])
    path_name = "PROJI-HNS.txt"
    file = open(path_name)
    file2 = open('RESOLVED.txt','w')
    while 1:
        lines = file.readlines()
        #print(lines[2])
        if not lines:
            break
        #print(lines[2])
        for line in lines:
            #print(line)
            server(line,rsListenPort)   
            #print(line)
            str=client(rsListenPort+150)
            #print(line)
            x = str[-2:]
            #print(line)
            #print(x)
            if x == 'NS':
                #print(x[1])
                server(str,tsListenPort)
                str=client(tsListenPort)
                file2.write(str)
            else:
                #print("!")
                file2.write(str)