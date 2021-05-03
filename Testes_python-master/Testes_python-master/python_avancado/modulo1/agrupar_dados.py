import itertools
from operator import itemgetter
from itertools import groupby
linhas = [
    {'nome': 'Marcos', 'data': '27/1/1987'},
    {'nome': 'João', 'data': '18/11/1967'},
    {'nome': 'Maria', 'data': '27/1/1987'},
    {'nome': 'pedro', 'data': '18/11/1967'},
    {'nome': 'Julia', 'data': '18/11/1967'},
]


linhas.sort(key=itemgetter('data'))

for data, items in groupby(linhas, key=itemgetter('data')):
    print(data)
    for i in items:
        print(" ", i)


linhas2 = [
    {'idade': 20, 'data': '20/05/2000'},
    {'idade': 23, 'data': '20/05/2001'},
    {'idade': 22, 'data': '20/05/2002'},
    {'idade': 20, 'data': '20/05/2000'},
    {'idade': 21, 'data': '20/05/2001'},
]

linhas.sort(key=itemgetter('data'))
print("Linha 2: ")
linhas2.sort(key=itemgetter('idade'))
print(linhas2)

for dados, item  in groupby(linhas2,key=itemgetter('idade')):
    print(dados)
    for i in item:
        print(' ', i)
