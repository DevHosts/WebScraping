precos = {
    'iphone': 2500,
    'Notbook': 2000,
    'teclado': 90,
    'celular': 990
}

mais_caros = {key:value for key,value in precos.items() if value > 1000}
print(mais_caros)