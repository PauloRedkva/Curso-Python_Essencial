"""
Any e All

All() -> Retorna True se todos os elementos do iterável ou ainda se o iterável esta vazio.

#Exemplo all()

print(all[0, 1, 2, 3, 4])) # Todos os números são verdadeiros? False
print(all[1, 2, 3, 4])) # Todos os números são verdadeiros? True
print(all[])) # Todos os números são verdadeiros? True

print(all(1, 2, 3, 4))) # Todos os números são verdadeiros? True
print(all{1, 2, 3, 4})) # Todos os números são verdadeiros? True

print(all('1', '2', '3', '4'))) # Todos os números são verdadeiros? True
print(all('Geek')) # Todos os números são verdadeiros? True


nomes = ['Carlo', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(all(nome[0] == 'C' for nome in nomes))

#
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 1]))

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

print(any([0, 1, 2, 3, 4])) # True

print(any([0, False, {}, ()])) # False

