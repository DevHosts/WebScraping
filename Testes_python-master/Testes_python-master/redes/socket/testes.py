import socket
import time


def main():
    op = input("Welcome!!\n"
               "Only host(1)\n"
               "Range IP(2)\n:")
    if op == '1':
        hostname = input("host: ")
        iphost = socket.gethostbyname(hostname)
        portScan(iphost)
    elif op == '2':
        iphost = input("host: ")
        host = str(iphost[:-4])
        for i in range(1, 255):
            portScan('%s.%s' % (host, i))
    print("Exinting Scan!")
    print("Thanks.")


def portScan(ip):
    ports = [x for x in range(20,1024)]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for p in ports:
        try:
            print(p)
            s.connect((ip, p))
            resp = s.recv(1024)
            print("[+]Port ", p, " open")
            if resp:
                print("[+]Banner ", resp)
        except:
            pass






#main()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname('www.pg.df.gov.br')
s.connect((ip, 21))
r = s.recv(4096)
time.sleep(1)
print(r)
s.send(b'USER anonymous\r\n')
r = s.recv(4096)
print(r)
s.send(b'PASS\r\n')
r = s.recv(4096)
print(r)
s.close()

