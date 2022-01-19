"""
Tuplas (tuple)

- São bastante parecidas com listas
- Existem basicamente 2 diferenças
1 Tuplas são representadas por ()
2 Tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda operação em uma tupla gera uma nova
tupla

DEFINIÇÃO - DEFINE PELA VÍRGULA!!!
# Cuidado 1 - AS tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# Cuidade 2: Tuplas com 1 elemento

tupla3 = (4) #isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) #isso é uma tupla
print(tupla4)
print(type(tupla4))

#conclusão: Podemos concluir que Tuplas são definidas pela vírgula e não pelo uso do parenteses

*************

#podemos gerar uma tupla dinamicamente com range (início, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

#Desempacotamente do tupla
tupla = 'Geek University', 'Programação em Python: Essencial'
escola, curso = tupla
print(escola)
print(type(curso))

Obs: Gera erro (valueError) se colocarmos um numero diferente de elementos que queremos desempacotar.

# Métodos para: adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis

#soma*, Valor Máximo*, Valor mínimo* e tamanho

# * Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))
****************************************
# Concatenação de Tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

********************************
# verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)

*****************************
tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

*******************************

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))
# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

**************************

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro')


# O acesso de elementos de uma tupla é semelhante a de uma lista

print(meses[5])

#interar com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual índice um elemento está na tupla
print(meses.index('Junho'))

#Obs: Caso o elemento não exista será gerado Erro - ValueError

#slicing

#tupla[inicio:fim:passo]

print(meses[5:9])

*******************************
# Por que utilizar tuplas?
# - Tuplas são mais rápidas do que listas
# - Tuplas deixam seu código mais seguro*
#* Isso porque trabalhar com elementos imutaveis traz segurança para o código.

# copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla #na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tupla)
"""
# Dicas de Utilização de tuplas

# devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção
# Exemplo 1:
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro','Dezembro')

