import socket
import sys, getopt
import requests

hostname = 'http://siabi.ifb.edu.br/'
port = 443
headers = ''

def usage():
    print('Program designed to explore and find vunerability in WebSites:\n\n'
          '-h, --help       \n'
          '-u, --url        url, path of site \n'
          '-p, --port       port open of service\n'
          '-f, --file       word-list to search directories\n'
          '--header         set headers\n'
          '--sqlInjection[auto]   will test flags slq in url\n')

def argsOptions():
    args = sys.argv[1:]
    print(args)

def bruteForceUrl(host, dict):
    if headers:
        req = requests.get(host, headers)
        arq = open(str(dict), 'r')
        f1 = arq.readlines()
        for url in f1:
            try:
                new_req = requests.get(str(req.url) + str(url), headers)
                if new_req.status_code == 200:
                    print("[Found][+] {}".format(new_req))

            except:
                pass
        print("[+]Teminate brute-force url.")
        return ''

    else:
        try:
            req = requests.get(host)
        except:
            print("URl inválida")
            print("\nVerifique!")
            return ''


        arq = open(str(dict), 'r')
        f1 = arq.readlines()
        for url in f1:
            try:
                new_req = requests.get((str(req.url)+str(url))[:-3])
                print(new_req.status_code)
                if new_req.status_code == 200:
                    print("[Found][+] {}".format(new_req.url[:-3]))
            except:
                pass
        print("[+]Teminate brute-force url.")

bruteForceUrl(hostname, 'dicionario.txt')
