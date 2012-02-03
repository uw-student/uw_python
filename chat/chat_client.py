"""
chat client, usage:

 python chat_client.py <host> <port>

Both host and port are optional, defaults: localhost 50004
host must be present if you want to provide port

Prompt user for each message to send
Repeat sending messages until user enters empty string
"""

import socket 
import sys
import select
import datetime

def prompt():
    sys.stdout.write('> ')
    sys.stdout.flush() # force print of line without \n

host = 'localhost' 
port = 50004 # different default port than echo, both can run on same server
size = 1024 

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

server = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
server.connect((host,port)) 
print 'Connection accepted by (%s,%s)' % (host, port)
prompt()

timeout = 60 # seconds
input = [server, sys.stdin]
running = True
while running:
    inputready,outputready,exceptready = select.select(input,[],[],timeout)

    # timeout
    if not inputready:  
        # could do periodic housekeeping here
        print 'chat client running at %s' % datetime.datetime.now()
        prompt()

    for s in inputready:

        if s == sys.stdin:
            # handle standard input
            msg = sys.stdin.readline().strip('\n')
            if msg:
                server.send(msg) 
            else:          # msg is empty
                server.close() 
                running = False # exit loop

        elif s: # response from server
            data = server.recv(size)
            print data
            prompt()

