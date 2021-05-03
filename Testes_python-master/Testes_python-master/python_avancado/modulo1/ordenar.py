from operator import itemgetter

linhas = [{'idade':19, 'nome':'michel'}, {'idade': 19, 'nome': 'aline'}, {'idade': 20, 'nome': 'erica'}]
linha_pelo_nome = sorted(linhas, key=itemgetter('nome'))
linha_pela_idade = sorted(linhas, key=itemgetter('idade'))
print(linhas)
print("pelo nome: ")
print(linha_pelo_nome)
print("pela idade: ")
print(linha_pela_idade)