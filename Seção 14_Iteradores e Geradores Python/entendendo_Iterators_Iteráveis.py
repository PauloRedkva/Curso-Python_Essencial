"""
Entendendo Iterators e Iterable:

Iterator
    -> Um objetoc que pode ser iterado.
    -> Um objetivo que retorna um dado, sendo um elementos por vez quando uma função next() é chamada;
    -> String, lista, conjuntos, tupla.
Iterable:
    -> Um objeto que irá retornar um iterator quando a função iter() for chamada.

nome = 'Geek' # É um iterable, mas não é um iterator
numeros = [1, 2, 3, 4, 5, 6] # É um iterable, mas não é um iterator

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1)) # G
print(next(it1)) # e
print(next(it1)) # e
print(next(it1)) # k
print(next(it1)) #StopIteration

"""
nome = "Geek"

for letra in nome:
    print(f'{letra}')





