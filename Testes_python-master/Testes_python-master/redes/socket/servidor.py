import socket

host = '127.0.0.1'
port = 444
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(4)
    conn, addr = s.accept()
    with conn:
        print("Connected by ", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)