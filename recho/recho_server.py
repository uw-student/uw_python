"""
recho server, usage:

 python recho_server.py <port>

Port is optional, default: 50002
"""

import socket 
import sys

host = '' 
port = 50002 # different default port than echo, both can run on same server

if len(sys.argv) > 1:
    port = int(sys.argv[1])

backlog = 5 
size = 1024 

# server's listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port)) 

print 'recho_server listening on port', port
s.listen(backlog) 

while True: 
    client, address = s.accept()
    print 'accepted connection from ', address
    while True:
        data = client.recv(size) 
        if data:
            client.send('uw-student: %s' % data) 
        else:  # no data, client sent empty message or closed socket
            client.close()
            print 'closed connection'
            break

        
