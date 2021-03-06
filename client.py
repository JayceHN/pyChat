#!/usr/bin/env python3
#       HOST(ip)    PORT(1-65535)
import socket
import threading
import sys

#ADDR = "localhost",8888
HELP = """Usage: ./client.py serverAddr portToConnect""",



class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def __init__(self,addr, port): #pseudo
        self.sock.connect((addr,int(port)))

        cliThread = threading.Thread(target=self.sendMsg)
        cliThread.daemon = True
        cliThread.start()

        while True:
            data = self.sock.recv(1024).decode()

            if not data:
                break

            print('>',data)
        self.sock.close()

    def sendMsg(self):
        while True:
            self.sock.send(input("").encode())
            print("\033[A                             \033[A")


        #send bytes (b'smthg')
    #    sock.sendall(b'Hello world !')
    #    data = sock.recv(1024)
    #bytes(or obj) to printable thing
    #print('Received:',repr(data))


try: 
    if(len(sys.argv) < 3):
        print(HELP[0])
    else:
        client = Client(sys.argv[1], sys.argv[2])
except KeyboardInterrupt: 
    print('')
    sys.exit(0)
