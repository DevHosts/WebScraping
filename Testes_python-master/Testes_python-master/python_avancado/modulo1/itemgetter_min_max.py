from operator import itemgetter

lista  = [{'idade':20}, {'idade':29}, {'idade':19}, {'idade':21}]
print(min(lista, key=itemgetter('idade')))