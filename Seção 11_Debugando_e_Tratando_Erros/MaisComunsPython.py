"""
Erros mais comuns em Python:

É importante prestar a atenção e aprender a ler as saídas de erros geradas pela execução do nosso código.

Os erros mais comuns:

SyntaxError -> Ocorre quando o python encontra um erro de sintaxe. Ou seja, você escreveu algo que o python não
reconhece como parte da linguagem

Exemplos syntaxerror:

a) def funcao:    #falta ()
    print('geek university')

b) def = 1
    None = 1

c)

return

2 - nameError -> Ocorre quando uma variavel ou funcao não foi definida

Exemplos: NameError
a) print(geek)

b) geek()

c)
a = 18

if a < 10:
    msg = 'É menor que 10'

print(msg)

3º TypeError -> ocorre quando uma função/operação/ação é aplicada a um tipo errado.
a)
print(len(5))

b)
print('Geek' + [])

4º IndexError -> Ocorre quando tentamos acessar um elementos em uma lista ou outro tipo de dado indexado utilizando
um indice inválido.

a) lista = ['Geek']

print(lista[2])

b) lista = ['Geek']

print(lista[0][10])

5º -> valueError -> ocorre quando uma funcao ou operacao built-in (integrada)
recebe um argumento com tipo correto mas valor inapropriado
a)
print(int('geek')) - Se fosse um '42' ele conseguiria converter

6º keyerror -> Ocorre quando tentamos acessar um dicionario com uma chave que não existe

a)
dic = {}
print(dic['Geek'])

7ª AttributeError -> Ocorre quando uma variavel não tem um atributo/funcao
Exemplos de attributeError

a)
tupla = (11, 2, 31, 4)

print(tupla.sort())  - Sort é para listas, não consegue ser aplicado em TUPLA!


8- IndentantionError -> Ocorre quando nao respeitamos a identacao do python que é de 4 espaços.
"""

tupla = (11, 2, 31, 4)

print(tupla.sort())