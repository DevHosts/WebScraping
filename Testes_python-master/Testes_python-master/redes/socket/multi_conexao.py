import selectors
import socket
import types

ip = '127.0.0.1'
port = 440
sel = selectors.DefaultSelector()
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.bind((ip, port))
lsock.listen(4)
print("Listening on ", (ip, port))
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)


messages = [b'Message 1 from client.', b'Message 2 from client.']


def start_connections(host, port, num_conns):
    server_addr = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print('starting connection', connid, 'to', server_addr)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(False)
        sock.connect_ex(server_addr)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(connid=connid,
                                     msg_total=sum(len(m) for m in messages),
                                     recv_total=0,
                                     messages=list(messages),
                                     outb=b'')
        sel.register(sock, events, data=data)

def accept_wrapper(sock):
    con, addr = sock.accept()
    print("Accpeted connetion from, ", addr)
    con.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(con, eventts, data=data)

def service_connetion(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb +=recv_data
        else:
            print("Closeing connection to ", data.addr)
            sel.unregister((sock))
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print("Echoing ", repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]


while True:
    eventts = sel.select(timeout=None)
    for key, mask in eventts:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connetion(key, mask)



