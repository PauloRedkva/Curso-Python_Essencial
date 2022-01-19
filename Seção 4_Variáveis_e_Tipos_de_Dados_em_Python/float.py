"""
Tipo Float

Tipo Real, decimal

Casas decimais
Obs: Separador de casa decimais na programação é ponto e não a vírgula
"""
#Errado do ponto de vista do float - gera uma tupla
valor = 1,44
print(valor)
print(type(valor))

#certo do ponto de vista float
valor = 1.44
print(valor)
print(type(valor))

#é possível fazer dupla atribuição

valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))

#Podemos converter um float para int
"""
OBS: Ao converter valores FLOAT para inteiros - Perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

#podemos trabalhar com números complexos
variavel = 5j