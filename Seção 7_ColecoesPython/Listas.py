"""
Listas

Listas em Python funcionam como vetores ou matrizes (arrays) em outras linguagens, com a diferença de serem DINAMICOS e
também de podermos colocar QUALQUER tipo de dado.

Linguagem C/Java:
    - possuem tamanho e tipo de dado fixo;
    - OU seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será sempre
    do tipo inteiro e poderá ter sempre no máximo 5 vetores.
Já em Python:
- Dinâmico: não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo; ou seja , podemos colocar qualquer tipo de dado,
As listas em python são representadas por colchetes []

********************************************************
type([])

lista1 = [1, 99, 4, 27, 15, 22, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek Univertisty')

#Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

#podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

#podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas


Para adicional elementos ou valores em listas utilizamos a função append
Obs: Com append, nós só conseguimos adicionar um elementos por vez.
lista1.append(12, 34, 56) #erro

print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1])
print(lista1)

if [8, 3 , 1] in lista1:
    print('encontrei a lista')
else:
    print('não encontrei a lista')

lista1.extend([123, 44, 67])
print(lista1)

#podemos inserir um novo elemento na lista informando a posiçao do indice
#obs: Isto não substitui o valor inicial. Será deslocado para a direita na lista
lista1.insert(2, 'novo valor')
print(lista1)

# podemos facilmente juntar duas listas

lista6 = lista1 + lista2
print(lista6)

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]
print(lista6)
print(type(lista6))

#Iterando sobre listas
#Exemplo 1 utilizando for

for elemento in lista4:
    print(elemento)

#exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

"""
lista1 = [1, 99, 4, 27, 15, 22, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek Univertisty')

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45345345345]



