"""

Módulo Collections - Counter (contador)

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo collection counter que é parecido com um dicionário
contendo como chave o elemento da lista passada como parâmetro e como valor a quantidade de ocorrências desse elemento

# Utilizando o Counter | Realizando o import

from collections import Counter

#podemos utilizar qualquer iterável - aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

#utilizando o Counter
res = Counter(lista)

print(res)

print(type(res))

# Counter({1: 5, 3: 5, 2: 3, 5: 3, 4: 2, 45: 2, 66: 2, 43: 1, 34: 1})
# <class 'collections.Counter'>

# veja que para cada elemento da lista o Counter criou uma Chave e colocou o valor de ocorrencias.

Exemplo 2:

print(Counter('Geek University'))

# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})


"""

from collections import Counter

# Exemplo 3

texto = """ O Akagi foi um porta-aviões operado pela Marinha Imperial Japonesa.
Inicialmente projetado como o segundo cruzador de batalha da Classe Amagi, 
teve seu batimento de quilha em dezembro de 1920, 
no Arsenal Naval de Kure. 
Porém, a fim de cumprir os termos do Tratado Naval de Washington, 
foi convertido em um porta-aviões ainda durante sua construção. 
Foi lançado ao mar em abril de 1925 e comissionado na frota japonesa em março de 1927.
Era capaz de transportar mais de oitenta aeronaves e 
contava com uma bateria antiaérea composta por vários canhões de 203, 120 e 25 milímetros. 
Seu deslocamento carregado era de 42 mil toneladas e velocidade máxima de 31 nós."""

palavras = texto.split()
#print(palavras)

res = Counter(palavras)
print(res)

print(res.most_common(5))