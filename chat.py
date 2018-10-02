#!/usr/bin/env python3
import server
import client
import sys

HELP = """Usage: -c serverAddr port pseudo (client)
       -s listeningAddr port serverName (server)
       -h (help)  """,

try: # avoid ctrl-c msg
    if( len(sys.argv) == 5 ):
        if(sys.argv[1] == '-h'):
            print(HELP[0])
        elif(sys.argv[1] == '-c'):
             client = client.Client(sys.argv[2], sys.argv[3], sys.argv[4])
        elif(sys.argv[1] == '-s'):
            server = server.Server(sys.argv[2], sys.argv[3], sys.argv[4])
            server.run()
        else:
            print(HELP[0])
    else:
        print(HELP[0])
except KeyboardInterrupt: #exception raise but no err msg print
    print('')
    sys.exit(0)
