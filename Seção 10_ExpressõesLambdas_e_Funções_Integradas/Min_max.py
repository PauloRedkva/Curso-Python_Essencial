"""
Min and Max

max() -> Retorna o maior valor de um iteravel ou o maior de dois ou mais elementos.

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))

min() -> Retorna o menor valor de um iteravel ou de dois ou mais elementos.
"""
musicas = [
    {"título": "Thnderstruck", "tocou": 3},
    {"título": "Dead Skin Mask", "tocou": 2},
    {"título": "Back in Black", "tocou": 4},
    {"título": "too old to rock'in' roll, too young to die", "tocou": 32},
]
#Ordena da mais tocada para a mais tocada
print(max(musicas, key=lambda musica: musica["tocou"])['título'])

#Ordena da menos tocada para a menos tocada
print(min(musicas, key=lambda musica: musica["tocou"])['título'])

max = 0

for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
       print(musica['título'])

min = 9999

for musica in musicas:
    if musica['tocou'] < min:
       min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['título'])