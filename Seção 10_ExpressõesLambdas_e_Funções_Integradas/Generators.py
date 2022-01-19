"""
Generator Expression

Em aulas anteriores nós estudamos:
- List Comprehension
- Dictionary Comprehension
- Set Comprehension

Não vimos:
Tutle Comprehension...Por que se chamam Generators

nomes = ['Carlos', 'Camila, 'Carla', 'Cassioano', 'Cristina", 'Vanessa']

print(any[nome[0] == 'c' for nome in nomes])

**************************************************************************************************
nomes = ['Carlos', 'Camila', 'Carla', 'Cassioano', 'Cristina', 'Vanessa']

# Poderiamos ter feito utilizando GENERATORS
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension

res = [nome[0] == 'C' for nome in nomes]

print(type(res))
print(res)

# Generator

res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

********************************************************************
# Qual é a utilizade de Getsizeof()? Retorna a quantidade de bytes em memoria do elemento passado como parametro

from sys import getsizeof

#mostra quantos bytes a string Geek está ocupando em memoria. Quanto maior a string, mais espaço ocupa.
print(getsizeof('Geek'))

print(getsizeof('Univertity'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(931651618916115195619816))

print(getsizeof(True))

*********************************************************************************
from sys import getsizeof

#Gerando uma lista de numeros com uma list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

#Gerando uma lista de numeros com uma Set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

#Gerando uma lista de numeros com uma dictionary comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

#Gerando uma lista de numeros com uma Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memoria: ')
print(f' List Comprehension: {list_comp} bytes')
print(f' Set Comprehension: {set_comp} bytes')
print(f' Dictionary Comprehension: {dict_comp} bytes')
print(f' Generator: {gen} bytes')

"""

# Eu posso iterar no generator expressor? SIM!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print (num)
