"""
Sorted
OBS: Não confunda apesar do nome com a função sort() que já estudamos em listas. O sort() só funciona em lista

Podemos usar o sorted() com qualquer iteravel.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: o sorted() sempre retorna uma lista com os elementos do iteravel ordenados

# exemplo
numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))

print(numeros)

***********************************
# Adicionando parametros ao sorted()

numeros = [6, 1, 8, 2]
print(numeros)
print(sorted(numeros))
# Adicionando parametros ao sorted()
print(sorted(numeros, reverse=True)) #Ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu agora pizzas"]},
    {"username": "jeff", "tweets": ["Eu amo meu gato"]},
    {"username": "carla", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock" }
]
print(usuarios)

# Ordenando pelo username
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

******************************************************************************************************************

"""

# Ultimo exemplo

musicas = [
    {"título": "Thnderstruck", "tocou": 3},
    {"título": "Dead Skin Mask", "tocou": 2},
    {"título": "Back in Black", "tocou": 4},
    {"título": "too old to rock'in' roll, too young to die", "tocou": 32},
]
#Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica["tocou"]))

#Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica["tocou"], reverse=True))
