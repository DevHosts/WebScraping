import re
import subprocess

ifc = subprocess.check_output('ipconfig ', shell=True)
print(ifc)
ipss = 'seu ip 192.168.1.1'
padrao = re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")

print(padrao.findall(str(ifc)))