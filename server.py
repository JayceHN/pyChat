#!/usr/bin/env python3
#import socket
#       HOST(ip)    PORT(1-65535)
import socket
import threading
import sys

HELP = """Usage: ./server.py listeningAddr portToServ""",



class Server:
    #addr family type (IPv4 here), SOCK_STREAM == TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    #list of connected clients
    conns = []
    #name = ''

    def __init__(self, addr, port):
        #bind socket
        self.sock.bind((addr, int(port)))
        #wait for input (listening socket)
        self.sock.listen()
        #self.name = name 

    def handler(self, conn, addr):
        while True:
            #reads whatever the client send, max size 1024
            data = conn.recv(1024).decode()
            if not data:
                self.conns.remove(conn)
                break
                    
            print('Received:',data)

            for cli in self.conns:
                cli.send(data.encode())

    def run(self):
        while True:
            nuConn, addr = self.sock.accept()
            connThread = threading.Thread(target=self.handler, args=(nuConn,addr))
            connThread.daemon = True
            connThread.start()
            self.conns.append(nuConn) 
            #nuConn.send(('Welcome to %s server' % self.name).encode())
            print('New connection : ', self.conns)


try: 
    if(len(sys.argv) < 3):
        print(HELP[0])
    else:
        server = Server(sys.argv[1], sys.argv[2])
        server.run()
except KeyboardInterrupt:
    print('')
    server.sock.close()
    sys.exit(0)

