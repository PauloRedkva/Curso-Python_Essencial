"""
Reduce

OBS: A partir do Python na versão 3 e acima, a função reduce() não é mais uma função integrada (built-in). Agora
temos que importar e utilizar esta função a apartir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se realmente precisa dela. Em todo caso,
99% das vezes um loop for é mais legível.

Para entender o reduce()

# imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# E você tem uma função quie recebe dois parâmetros:

funcao(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parametros: a função e o iterável.

reduce(funcao, dados)

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1 e mais o terceiro elemento e guarda resultado.

    Isso é repetido até o final.

    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = (resn, an)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderíamos ver a funcao reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...an)

"""

# Como funciona na prática?
# Vamos utilizar a funcao reduce() para multiplicar todos os dados de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois paramentros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# utilizando um LOOP NORMAL

res = 1
for n in dados:
    res = res * n

print(res)
