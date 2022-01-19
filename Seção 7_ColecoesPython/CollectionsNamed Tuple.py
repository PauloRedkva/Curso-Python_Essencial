"""

Módulo Collection - Named Tuple

#recap tupla
tupla = (1, 2, 3)
print(tupla[1])

# Named Tuple -> São tuplas diferenciadas onde especificamos um nome para a mesma e também parâmetros


"""
from collections import namedtuple

# precisamos definir um nome e parâmetros

# Forma 1 - Declaração da Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração da Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

#Forma 3 - Declaração Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#usando

ray = cachorro(idade =2, raca='chow-chow', nome='Ray')
print(ray)

# Acessando os dados - Forma 1

print(ray[0]) # idade
print(ray[1]) # raca
print(ray[2]) # nome


# Acessando os dados - Forma 2
print(ray.idade)
print(ray.raca)
print(ray.nome)
print(ray.index('chow-chow'))
print(ray.count('chow-chow'))