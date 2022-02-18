"""

Funções de maior Grandeza - Higher Order Functions - HOF

O que isto significa?

- Quando uma linguagem de Programação suporta HOF, indica que podemos ter funções que retornam outras funções como
 resultado ou até mesmo que podemos passar funções como argumentos para outras funções , e até mesmo criar variáveis do
 tipo de funções nos nossos programas.

 OBS: Na seção de funções, nós estudamos isto.

 Em Python, as funções são cidadãos de Primeira Classe (First Class Citizen)

 # Exemplos - Definindo as funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# testando as funções

print(calcular(4,3, somar))

print(calcular(4,3, diminuir))

print(calcular(4,3, multiplicar))

print(calcular(4,3, dividir))

# Nested Functions - Funções Aninhadas

 #Em Python podemos ter funções dentro de Funções, que são conhecidas por Nested Functions ou também Inner Functions
 # (funções internas).

# Exemplo:

from random import choice
def cumprimento(pessoa):
    def humor():
        return choice(("E aí ", "Suma daqui ", "Gosto muito de você "))
    return humor() + pessoa

# testando
print(cumprimento("Angelina"))
print(cumprimento("Felicity"))


# Retornando Funções de Outras Funçãoes

from random import choice

def faz_me_rir():
    def rir():
        return choice(("hahahahahaha ", "kkkkkkk ", "rsrs "))
    return rir

# Testando

rindo = faz_me_rir()
print(rindo())

"""

# Inner functions (Funções Internas / Nested Functions) podem acessar o escopo de funções mais externas.

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(("hahahahaha ", "lolololololo ", "kkkkkkkkkk "))
        return f'{risada} {pessoa}'
    return dando_risada

#Testando
rindo = faz_me_rir_novamente("Fernanda")

print(rindo())
print(rindo())
print(rindo())








