"""
Módulo Collections:
Ordered Dict

#Em um dicionario a ordem de inserção dos elementos não é garantida para CHAVE e VALOR
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }

for chave, valor in dicionario.items():
    print(f'chave= {chave} : valor = {valor}')

ORDERED DICT -> É um dicionário que garante a ordem de performance dos elementos.

# Fazemos import

from collections import OrderedDict

dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }

for chave, valor in dicionario.items():
    print(f'chave= {chave} : valor = {valor}')

"""

# Entendendo a diferença entre Dict e Ordered Dict

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  #True or False?? True - Já que a ordem dos elementos não importa para o dicionario

#Ordered Dict

from collections import OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) #True or False?? False - Já que a ordem dos elementos IMPORTA para o dicionario