import socket
import struct
from ctypes import *





def initTcpSocket():
    sniffer_tcp = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

    sniffer_tcp.bind(('0.0.0.0', 0))
    sniffer_tcp.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL,1)
    return sniffer_tcp

def startSniffing():
    sniffer_tcp = initTcpSocket()

    print("sniffer is listening for incoming connections")

    try:
        while True:
            raw_buffer_tcp = sniffer_tcp.recvfrom(65535)[0]
            ip_head_tcp = IPHeader(raw_buffer_tcp[0:20])

            if(ip_head_tcp =='TCP'):
                print('Protocol: %s %s -> %s ' % (ip_head_tcp.protocol, ip_head_tcp.source_address, ip_head_tcp.destination))

def main():
    startSniffing()

