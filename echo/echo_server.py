"""
echo server, usage:

 python echo_server.py <port>

Port is optional, default: 50000
"""

import socket 
import sys

host = '' 
port = 50000 

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

print 'echo_server listening on port', port
s.listen(backlog) 

while True: 
    client, address = s.accept()
    data = client.recv(size) 
    if data: 
        client.send('uw-student: %s' % data) 
    print 'from %s: %s' % (address, data)
    client.close()
