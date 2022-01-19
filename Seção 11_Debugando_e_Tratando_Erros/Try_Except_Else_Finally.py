"""

Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA (**DO USUARIO**) DEVE SER TRATADA!
Obs: A função do usuário é destruir seu sistema

# Else é executado somente se não ocorrer o erro.

num = 0

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Valor incorreto')
else:
   print(f'Você digitou {num}')

# Finally

num = 0

try:
    num = int(input('Informe um numero: '))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f' Você digitou o número {num}')
finally:
    print('Executando o finally')

#Obs: O bloco finally é sempre executado independente se houve excessão ou não.
# O Finally é geralmente utilizado para fechar ou desalocar recursos.


# exemplo mais complexo ERRADO

def dividir(a, b):
    return a / b

num1 = int(input('informe o primeiro numero: '))

try:
    num2 = int(input('informe o segundo numero: '))
except ValueError:
    print("O valor precisa ser numerico")

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor Incorreto')

*************************************************************************

# exemplo mais complexo CORRETO

# Obs:  Você é responsável pelas entradas de suas funções. Então trate-as!

def dividir(a, b):
   try:
       return int(a) / int(b)
   except ValueError:
       return 'Valor incorreto'
   except ZeroDivisionError:
       return 'Não é possível realizar uma divisão por zero'

num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(dividir(num1, num2))

*************************************************************
# exemplo mais complexo - Genérico

# Obs:  Você é responsável pelas entradas de suas funções. Então trate-as!

def dividir(a, b):
   try:
       return int(a) / int(b)
   except:
       return 'Ocorreu um problema'


num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(dividir(num1, num2))

************************************************
# exemplo mais complexo - Semi-Genérico

# Obs:  Você é responsável pelas entradas de suas funções. Então trate-as!

def dividir(a, b):
   try:
       return int(a) / int(b)
   except(ValueError, ZeroDivisionError):
       return 'Ocorreu um problema'


num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(dividir(num1, num2))

"""


# exemplo mais complexo - Semi-Genérico

# Obs:  Você é responsável pelas entradas de suas funções. Então trate-as!

def dividir(a, b):
   try:
       return int(a) / int(b)
   except(ValueError, ZeroDivisionError) as err:
       return f'Ocorreu um problema: {err}'


num1 = input('informe o primeiro numero: ')
num2 = input('informe o segundo numero: ')

print(dividir(num1, num2))
