import argparse
from socket import *



def printBanner(connSock, tgtPort):
    try:
        if (tgtPort == 80):
            connSock.send("GET HTTP/1.1 \r\n")
        else:
            connSock.send('\r\n')

        results = connSock.recv(4096)
        print("[+] Banner: "+ str(results))
    except:
        print("[-] Banner not available\n")

def connScanUdp(tgtHost, tgtPort):
    try:
        connSock = socket(AF_INET, SOCK_DGRAM)
        connSock.connect((tgtHost, tgtPort))
        print("[+] %d open: " % tgtPort)
        printBanner(connSock, tgtPort)
    except:
        print("[+] %d udp closed " % tgtPort)
def connScanTcp(tgtHost, tgtPort):
    try:
        connSocket = socket(AF_INET, SOCK_STREAM)
        connSocket.connect((tgtHost, tgtPort))
        print("[+] %d tcp open " %tgtPort)
        printBanner(connSocket, tgtPort)
    except:
        print("[+] %d tcp closed " % tgtPort)
    finally:
        connSocket.close()


def portScan(tgtHost, tgtPorts, isUdp):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Error: Unknow Host")
        exit(0)
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("[+] Scan result for: "+tgtName[0]+'---')
    except:
        print("[+] --- Scan result for: "+tgtIP+" ---")

    setdefaulttimeout(10)
    for tgtPort in tgtPorts:
        if not isUdp:
            connScanTcp(tgtHost, int(tgtPort))
        else:
            connScanUdp(tgtHost, int(tgtPort))

def main():
    parser = argparse.ArgumentParser('Snart TCP Client Scanner')
    parser.add_argument('-a', '--address', type=str, help='The target IP address')
    parser.add_argument('-p', '--port', type=str, help="The number to connect with")
    parser.add_argument('-u', '--udp', help="include a udp port scan", action="store_true")
    args = parser.parse_args()


    ipadress =  args.address
    portNumbers = args.port.split(',')
    isUdp = args.udp

    portScan(ipadress, portNumbers, isUdp)

if __name__ == '__main__':
    main()