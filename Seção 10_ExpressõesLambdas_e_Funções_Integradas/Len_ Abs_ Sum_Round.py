"""
Len() sum() abs(), round():

# Len() -> Retorna o tamanho (ou seja o numero de itens) de um iteravel.

#Só pra revisar

print(len("geek university"))

print(len([1, 2, 3, 4, 5]))

print(len((1, 2, 3, 4, 5)))

print(len({1, 2, 3, 4, 5}))

print(len({'a': 1, 'b': 2, 'c': 3,'d': 4,'e': 5}))

print(len(range(0,10)))

# Por debaixo dos panos, quando utyilizamos a funcao len() o Python faz o seguinte:

# Dunder len
print('Geek University'.__len__())
********************************************
abs()

abs() -> Retorno o valor absoluto de um numero inteiro ou real. De forma básica, seria o seu valor real sem o sinal.
#Exemplos abs()
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))

sum() -> recebe como parametro um iteravel, podendo receber um valor inicial, e retorna a soma total dos elementos, incluindo o valor inicial

OBS: o valor inicial de default é = 0

#Exemplos abs

print(sum([1, 2, 3, 4, 5]))

print(sum([1, 2, 3, 4, 5],5))

round() -> retorna um numero arredondado para n digito de precisao apos a casa decimal.
Se o precisão não for informada o retorna o inteiro mais proximo da entrada.

"""
#Exemplos round()

print(round(10.2))

print(round(10.5))

print(round(10.6))

print(round(1.212121, 2))

print(round(1.2199999999999999999999, 2))
