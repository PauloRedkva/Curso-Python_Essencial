"""
Modulo Collections - Deque

-> Podemos dizer que o Deque é uma lista de alta performance


"""

from collections import deque

# criando deques

deq = deque('geek')
print(deq)

# Adicionando elementos no deque

deq.append('y') # adiciona no final
print(deq)

deq.appendleft('k') #adiciona no começo
print(deq)

#remove elementos
print(deq.pop())
print(deq) # remove e retorna o último elemento

print(deq.popleft()) #remove e retorna o primeiro elemento
print(deq)