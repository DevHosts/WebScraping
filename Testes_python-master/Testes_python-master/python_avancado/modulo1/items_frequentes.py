from collections import Counter

palavras = ['marcos', 'jose', 'michel', 'maria','lara', 'jose', 'michel']
palavras_count = Counter(palavras)
print("As duas palavras mais comuns - ", palavras_count.most_common(2))