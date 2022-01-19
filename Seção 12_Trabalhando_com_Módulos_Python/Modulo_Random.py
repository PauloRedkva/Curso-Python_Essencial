"""
Trabalhando com Módulo Random - e o que são módulos

- Em Python, módulos nada mais são do que módulos Python.

Módulo Random -> Possui várias funções de numeros pseudo-aleatório.

OBS: Existem duas formas de se utilizar um modulo ou função deste.

# Forma 1 - Importando todo o módulo (não recomendado).

import random

# random() -> Gera um número real pseudo-aleatório entre zero e 01

# Ao realizar o import de todo módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponíveis (Ficarão em Memória). Caso você saiba quais funções você precisa utilizar
# deste módulo, esta não seria a forma ideal de utilização. Nós veremos a forma 2.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função,
# Separados por ponto.
# OBS - Não confunda a função random() com o pacote random. Pode parecer confuso mas a função random() é apenas
# um pacote dentro módulo random.

********************************************************


# Forma 2 - Importando uma função específica do módulo (Fórmula Recomendada)

from random import random

# No importe acima estamos falando: do modulo random, importe a função random.

for i in range(10):
    print(random())

# uniform() -> Gerar um número real pseudo-aleatório entre os valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) # 7 não é incluido.

**********************************************************
# randint() -> Gera valores inteiros pseudoaleatórios entre os valores estabelecidos.

# Gerador de apostas para a Mega-sena

from random import randint

for i in range(6):
    print(randint(1, 61), end=', ')

**********************************************************

# choice() => Mostra um valor aleatório entre o iterável.

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

"""

# shuffle() -> Tem a função de embaralhar dados

from random import shuffle

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

shuffle(cartas)

print(cartas)
