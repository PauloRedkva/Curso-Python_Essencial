"""
Entendendo o *args

- O *args é um paremetro, como outro qualquer. Isso significa que você poderá chamar de qualquer coisa, desde que
comece com *(asterisco)
Exemplo:
*xis
Mas por convenção, utilizamos *args para definí-los

Mas o que é o *args?

O parametro *args utilizando em uma função, coloca os valores extras informados como entrada em uma tupla.
Então desde já lembre-se que tuplas são imutáveis.

****************************************
#Exemplos

def soma_todos_numeros(num1, num2, num3):
    return  num1 + num2 + num3

print(soma_todos_numeros(4, 6, 9))

#print(soma_todos_numeros(4, 6)) #TypeError

#print(soma_todos_numeros(4, 6, 9, 5)) #TypeError

# Entendendo o args

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))

*** Melhorando o código com função SUM

def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))
********************************************************

# Entendendo o args

def soma_todos_numeros(nome, email, *args):
    return sum(args)


print(soma_todos_numeros('Angelina', 'jolie@angelina.com'))
print(soma_todos_numeros('Angelina', 'jolie@angelina.com', 1))
print(soma_todos_numeros('Angelina', 'jolie@angelina.com', 2, 3))
print(soma_todos_numeros('Angelina', 'jolie@angelina.com', 2, 3, 4))
print(soma_todos_numeros('Angelina', 'jolie@angelina.com', 3, 4, 5, 6))

print(soma_todos_numeros('Angelina', 'jolie@angelina.com', 24.65, 12.5))

******************************
# Outro exemplo de utilização do args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza quem é você...'

print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
"""

def soma_todos_numeros(*args):
    print(args)
    return sum(args)

#print(soma_todos_numeros())
#print(soma_todos_numeros(3, 4, 5, 6))

numeros = {1, 2, 3, 4, 5, 6, 7}

# Desempacotador

print(soma_todos_numeros(*numeros))

# o * asterisco serve para que informemos ao python que estamos passando uma coleção de dados.
#desta forma ele saberá que precisa desempacotar os dados.