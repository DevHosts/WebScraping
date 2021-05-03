import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('10.230.80.121', 80))
msg ='GET / HTTP/1.1\n\n'
s.send(msg.encode())
print(s.recv(1024))
s.close()