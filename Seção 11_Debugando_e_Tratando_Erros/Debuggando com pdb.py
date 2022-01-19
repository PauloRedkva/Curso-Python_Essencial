"""
Debuggando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto

# Obs: Utilizar print para debuggar codigo é uma prática ruim!
def dividir(a, b):
    print(a, b)
    try:
       return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
       return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

**********************************************

# Exemplo com Pycharm:

def dividir(a, b):
    try:
       return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
       return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

# Obs: Utilizar formas mais profissionais de se fazer o 'debug', utilizando o 'debbuger'
# Em Python podemos fazer isto em diferentes IDE, como Pycharm ou utilizando
# o PDB - Python Debugger

# Exemplo com PDB: Python Debugger - exemplo 1

# Para utilizar o Python Debbugger, precisamos importar a biblioteca pdb e então utilizar a funcao set_trace()
# comandos básicos do PDB:
# l (Lista onde estamos no código)
# n (próxima linha)
# p ( imprime variável)
# c (continua execução

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()  # Forma manual de debugger
nome_completo = nome + ' '+ sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso' + curso
print(final)
# Exemplo com PDB: Python Debugger - exemplo 2

# Para utilizar o Python Debbugger, precisamos importar a biblioteca pdb e então utilizar a funcao set_trace()
# comandos básicos do PDB:
# l (Lista onde estamos no código)
# n (próxima linha)
# p ( imprime variável)
# c (continua execução

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()  # Forma manual de debugger
nome_completo = nome + ' '+ sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso' + curso
print(final)

# Por que utilizar este formato?

# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os importes de bibliotecas no início
# do arquivo. Por isso, ao invés de colocarmos o import do pdb no inicio do arquivo,
# nós colocamos somente onde vamos debuggar, depois apagamos a linha.


"""

# Obs: Utilizar formas mais profissionais de se fazer o 'debug', utilizando o 'debbuger'
# Em Python podemos fazer isto em diferentes IDE, como Pycharm ou utilizando
# o PDB - Python Debugger

# Exemplo com PDB: Python Debugger - exemplo 3

# Para utilizar o Python Debbugger, precisamos importar a biblioteca pdb e então utilizar a funcao set_trace()
# comandos básicos do PDB:
# l (Lista onde estamos no código)
# n (próxima linha)
# p ( imprime variável)
# c (continua execução

# * No python 3.7 ou superior, não é mais necessário importar a biblioteca PDB pois o comando debug foi
# incorporado como função (built-in) chamada breakpoint()

#OBs: Cuidados com conflitos entre nomes de variáveis e os comandos do pdb

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()  # Forma manual de debugger
nome_completo = nome + ' '+ sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz curso' + curso
print(final)

# Por que utilizar este formato?

# O debug é utilizado durante o desenvolvimento. Costumamos realizar todos os importes de bibliotecas no início
# do arquivo. Por isso, ao invés de colocarmos o import do pdb no inicio do arquivo,
# nós colocamos somente onde vamos debuggar, depois apagamos a linha.



