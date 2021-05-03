d = {'marcos': 28, 'joao':30, 'maria': 25}
d2 = {'jose':18, 'carlos': 25, 'joao':19}
print("Chaves em comum entre {} e {}".format(d, d2))
print(d.keys() & d2.keys())
print("Chaves que tem em em {} e não tem em {}".format(d, d2))
print(d.keys() - d2.keys())