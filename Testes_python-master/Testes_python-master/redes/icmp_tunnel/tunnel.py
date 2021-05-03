from scapy.all import *
from scapy.layers.inet import ICMP, IP


def main():
    while True:
        command = input("# Enter command: ")
        pinger = IP(dst='localhost')/ICMP(id=0x0001, seq=0x1)/command
        send(pinger)

        rx = sniff(count=1, timeout=2)
        print(rx[0][Raw].load.decode('utf-8'))


if __name__ == '__main__':
    main()

