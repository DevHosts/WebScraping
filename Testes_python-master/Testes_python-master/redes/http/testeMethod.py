import socket



method = ['PUT ', 'GET', 'HEAD', 'POST']

# for i in method:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('200.130.64.4', 80))
#     s.send(str.encode(i+' /XSS.html HTTP/1.1\r\n'))
#     resp = s.recv(2048)
#     print(i+"- > ", resp)
# s.close()


s.send(str.encode("OPTIONS HTTP/1.1\r\n"))
r = s.recv(2048)
print(r)