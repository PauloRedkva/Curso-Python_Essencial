"""
zip()

zip() -> Cria um iteravel (Zip object) que agrega elemento de casa um dos iteraveis passados como entrada em pares.

# Exemplos
lista1 = [1, 2, 3]

lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip))
# sempre podemos gerar uma lista, tupla ou dicionario

print(list(zip1))

print(tuple(zip1))

print(dict(zip1))

print(set(zip1))

***************************************************
# Podemos utilizar diferentes iteraveis com zip

tupla = 1, 2, 3, 4, 5
lista =[6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zt = zip(tupla, lista, dicionario.values())

print(list(zt))

# Lista de tuplas

dados = [(0,1), (1,2), (2,3), (3,4), (4,5)]

print(list(zip(*dados)))
"""

# Exemplos mais complexos
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)

# podemos utilizar o map()
final1 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final1))
