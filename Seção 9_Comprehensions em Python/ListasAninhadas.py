"""

Listas Aninhadas ( Nested Lists)
- Algumas linguagens de programação (C / Java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as listas

numeros = [1, 2, 3, 4, 5]

********************************************************

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #Matriz 3 x 3

print(listas)

print(type(listas))

# Como fazemos para acessar os dados?

#print(listas[0][1])  # 2
#print(listas[2][1])   # 8

# Iterando com Loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

"""
# Outro Exemplos

# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velja

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais

print([['*' for i in range(1, 4)] for j in range(1, 4)])




