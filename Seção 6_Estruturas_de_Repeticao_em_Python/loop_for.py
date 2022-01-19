"""
Loop for

Loop -> Estrutura de Repetição

For -> Uma destas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    // execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteráveis

Exemplos de Iteráveis:
- String
    Nome = 'Geek University'
- Lista
    Lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1,10)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1,10) #Temos que transformar em uma lista
#exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)


#exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

#exemplo de for 3 (iterando sobre um range) - Range (valor inicial, valor final)
#obs: O valor final não é "inclusive"
for numero in range(1,10):
    print(numero)

Enumerate:
for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

tabela de emoji - Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
#Original: U+1F602
#modificado: U0001F602
"""
"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)
"""

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F602' * num)