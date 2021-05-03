import socket
from scapy.all import *
import sys
from scapy.layers.inet import IP, ICMP, Ether,conf
from scapy.layers.l2 import ARP

a = IP(ttl=10)
print(a)
a.dst = '172.217.172.142'
print(a.src, '\n', a.dst)
print(a.ttl)
a.ttl = 128
print(a.ttl)
del a.ttl
print(a.ttl)