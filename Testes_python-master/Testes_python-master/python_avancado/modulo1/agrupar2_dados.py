from itertools import groupby
from operator import itemgetter

alunos = [
    {'nome': 'Luana', 'saida': '01/06/2019'},
    {'nome': 'Carlos', 'saida': '01/07/2018'},
    {'nome': 'Debora', 'saida': '01/06/2019'},
    {'nome': 'Michel', 'saida': '05/01/2019'}
]

alunos.sort(key=itemgetter('saida'))
print(alunos)

for dado, item in groupby(alunos, key=itemgetter('saida')):
    print(dado)
    for i in item:
        print(' ', i)