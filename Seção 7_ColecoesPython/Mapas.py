"""
Mapas -> Conhecidos em Python como dicionários

Dicionários em Python são representados por chaves {}

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em janeiro {chave} recebi R$ {receita[chave]}')

***************************
Acessando as chaves:
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

*******************
#Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)

******************
#Desempacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

**********************
#Soma*, Valor máximo*, Valor mínimo*, tamnho
# * Se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

"""
receita = {'janeiro': 100, 'fev': 250, 'mar': 400}
print(receita)


