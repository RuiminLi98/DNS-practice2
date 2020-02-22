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
    csockid.send(msg.encode('utf-8'))

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
    return format(data_from_server.decode('utf-8'))
    # close the client
    cs.close()
    exit()


if __name__ == "__main__":
    rsListenPort = int(sys.argv[1])
    str = client(rsListenPort)
    print(str)