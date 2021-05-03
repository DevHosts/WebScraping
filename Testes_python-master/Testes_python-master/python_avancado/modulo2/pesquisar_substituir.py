import re

texto = 'A data do meu aniversaio  é da 21/04/2000'
padrao = re.compile(r'\d+/\d+/\d+$')

encontrados = padrao.findall(texto)
print(encontrados[0])

print(texto.replace(encontrados[0], '20/03/200'))
print("Alterado")
#print(re.sub(padrao, r'\2-\3-\1', texto))
