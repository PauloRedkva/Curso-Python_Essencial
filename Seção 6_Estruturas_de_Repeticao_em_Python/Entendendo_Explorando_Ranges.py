"""
Ranges
-Precisamos entender o loop for para usar os ranges.
-Precisamos conhecer o range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatória, mas sim de maneira específica.

Formas gerais:
#Exemplo Forma 1
range(valor_de_parada)

for num in range(11):
    print(num)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

#forma 2

Range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (início especificado pelo usuario, e passo de 1 em 1)

#Forma 3

range(valor_de_inicio, valor_de_parada, passo

BS: valor_de_parada não inclusive (início especificado pelo usuario, e passo especificado pelo usuario)

for num in range(1, 10, 2):
    print(num)

Exemplo 4:
for num in range(10, -1, -1):
    print(num)


"""

for num in range(10, -1, -1):
    print(num)
