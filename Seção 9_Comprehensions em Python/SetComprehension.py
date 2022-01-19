"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

"""
# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)

# outro Exemplo

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# Desafio: Faça uma alteração na estrutura acima para gerar um dicionario ao inves de SET (só colocar x de Chave)

# Para finalizar

letras = {letra for letra in 'Geek University'}
print(letras)
