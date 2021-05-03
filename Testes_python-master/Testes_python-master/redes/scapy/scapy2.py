from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.l2 import Ether

print(raw(IP()))
#print(IP().show())
a = Ether()/IP(dst='www.pg.df.gov.br')/TCP()/"GET / HTTP/1.1 \n\n"
print(hexdump(a))
b = raw(a)
c = raw(Ether(b))
print(ls(a))