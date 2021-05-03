from scapy.all import *
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.layers.l2 import Ether

sr1(IP(dst='172.217.30.110')/ICMP(dport=80, flags='S'))
