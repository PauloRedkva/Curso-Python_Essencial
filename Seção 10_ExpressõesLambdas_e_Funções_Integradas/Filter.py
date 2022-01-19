"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

***************************************************************

# Biblioteca para trabalhar com dados estatísticos

import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: Assim como a função map(), a filter() recebe dois parametros. Sendo uma função e um iterável

res = filter(lambda x: x > media, dados)
print(list(res))

# Obs: Assim como na função map() após serem utilizados os dados de filter() eles são excluídos da memória.
print(f'Novamente: {list(res)}')

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))
#Outras formas...

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)

print(list(res))

# A diferença entre map() e filter() é:
# Na map() -> recebe dois parametros, uma função e um iterável e retorna um objeto mapeando a função para cada
#elemento do iterável.

# filter() -> Recebe dois parametros, uma função e umiterável e retorna um objeto filtrando apenas os elementos de
# acordo com a função

# Exemplo mais complexo
usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu agora pizzas"]},
    {"username": "jeff", "tweets": ["Eu amo meu gato"]},
    {"username": "carla", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]
print(usuarios)
# Filtrar os usuários que está inativo no Twitter

# Forma 1
#inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

*****************************************************************************************************

"""

# Combinar filter() e map()

nome = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nome)))

print(lista)
