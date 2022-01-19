"""
Trabalhando com Módulos Built-In (Módulos integrados, que já vem instalados no python)

---------------------------
| Python| Módulos built-in |
--------------------------

#  Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

*************************

# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())

*************************
# Importando todo o módulo
import random

print(random.random())
]
*************************
# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi

print(rdi(5, 89))

****************************
# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))

print(rdm())

**************************************
# Costumamos a utilizar tuple para colocar multiplos importes de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice)

print(random())

print(randint(5, 90))

lista = ['geek', 'University', 'Python']
shuffle(lista)
print(lista)
print(choice('University'))

https://docs.python.org/3/py-modindex.html

"""
# Costumamos a utilizar tuple para colocar multiplos importes de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice)

print(random())

print(randint(5, 90))

lista = ['geek', 'University', 'Python']
shuffle(lista)
print(lista)
print(choice('University'))
