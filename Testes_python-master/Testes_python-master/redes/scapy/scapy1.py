from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP
from scapy.layers.l2 import Ether

a = IP()
print('1--' ,a.show())
a = IP()/TCP()
print('2--', a.show())
a = Ether()/IP()/TCP()
print('3--',a.show())
a = IP()/TCP()/"GET / HTTP/1.1\r\n\r\n"
print('4--',a.show())
a = Ether()/IP()/UDP()
print('5--', a.show())
a = IP(proto=55)/TCP()
print('6--', a.show())

