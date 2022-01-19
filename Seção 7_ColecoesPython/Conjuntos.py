"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a teoria dos Conjuntos da Matemática.

- Aqui no python os conjuntos são chamados de sets.

Dito isto, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles - Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferenças entre conjuntos (Set) e mapas (Dicionário) em Python?

    - Um dicionário tem chave/valor
    - Um conjunto tem apenas valor;


**************************

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) #repara que temos valores repetidos;

print(s)
print(type(s))

# Obs: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerrar erro e não
#fará parte do conjunto;

#Forma 2 - mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# podemos verificar se determinado elemento está contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')
********************************************

# importante lembrar que além de não termos valores duplicados, não temos ordem.

#Listas aceitam valores duplicados - 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

#Tuplas aceitam valores duplicados - 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'tupla: {tupla} com {len(tupla)} elementos')

#Dicionario não aceitam chaves duplicados - 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

#Conjunto não aceitam valores duplicados - 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

****************************************


# assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente

for valor in s:
    print(valor)

    ****************************************

# Usos interessantes com Sets

# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museus.
# E os visitantes informam manualmente a cidade de onde vieram.
# Nós adicionamos cada cidade em uma LISTA python, já que a lista podemos adicionar novos elementos e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

#agora precisamos saber quantas cidades distintas temos. O que você faria?
# Faria um loop na lista?
# Podemos utilizar o Set para isso;

print(len(set(cidades)))

*******************
# Adicionando elementos em um conjunto

s = {1 ,2 ,3}

s.add(4)
s.add(4) # Duplicidade de informação, não dá erro, simplesmente não adiciona
print(s)

***************************************************
# Removendo elementos em um conjunto
s = {1 ,2 ,3}
print(s)
# Forma 1

ret = s.remove(3) #não é indice. Informamos o valor a ser removido
print(s)
print(ret)

# Obs - Caso o valor não seja encontrado será gerado o erro KeyError | Nenhum valor é retornado.

# Forma 2

s.discard(2)
print(s)
# Obs - Se io valor não for encontrado - Nenhum erro é gerado.

********************
# Copiando um conjunto para outro

# Forma 1 de cópia - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)


# Copiando um conjunto para outro

#Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

*********************************************

# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do Curso Pyhton e um do Curso Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java

# precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)
print(len(unicos1))

# Forma 2 - Utilizando o caractere pipe |

unicos2 = estudantes_python | estudantes_java
print(unicos2)

***************************


# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando Intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#Forma 2 - utilizando &

ambos2 = estudantes_python &  estudantes_java
print(ambos2)

**********************************************

# Gerar um conjunto de estudantes de um curso que não estao no outro

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


# Soma*, valor máximo *, valor mínimo *, tamanho
# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

"""



