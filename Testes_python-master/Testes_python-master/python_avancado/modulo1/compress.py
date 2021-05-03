from itertools import compress

nomes = ['marcos', 'joao', 'maria']


cont = [10, 5, 6, 2]

mais5 = [i > 5 for i in cont]

print(mais5)
print(list(compress(nomes, mais5)))
