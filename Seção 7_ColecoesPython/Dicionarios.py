"""
Dicionários

Obs: Em algumas linguagens de programação os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}

print(type({})) => <class 'dict'>

****************
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

Obs: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

**********************
# criação de dicionários

#Forma 1 - Forma mais comum

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

#Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

**********************************
# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma que lista e tupla
print(paises['br'])
print(paises['py'])
# Caso tentamos fazer o acesso a uma chave que não existe, teremos o erro KeyError
# Forma 2 -  Acessando via get -    ***RECOMENDADA ***

print(paises.get('br'))
print(paises.get('ru'))

*****************
pais = paises.get('ru')

#caso o get não encontre o objeto com a chave informada, será informada o valor None e não será gerado KeyError

if pais:
    print(f'Encontrei o País {pais}')
else:
    print(f'Não encontrei o País {pais}')

Obs: Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('py', 'Não encontrado')
print(f'Encontrei o país {pais}')

*****************************
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']
***************************************
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário, como chaves
#de dicionarios

# Tuplas são bastante interessantes de serem utilizadas como chaves de dicionários, pois são imutáveis
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}
print(localidades)
print(type(localidades))

*************************************************
# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

#forma 1
receita['abr'] = 350
print(receita)

#forma 2

novo_dado = {'maio': 500}
receita.update(novo_dado)

print(receita)

# Atualizando dados em um dicionário
# Forma 1
receita['maio'] = 550

print(receita)
# Forma 2
receita.update({'maio': 600})
print(receita)

# Conclusao 1 - A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# Conclusao 2 - Em um dicionário NÃO podemos ter chaves repetidas.

************************
# COMO REMOVER dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

#Forma 1
ret = receita.pop('mar')
print(ret)
print(receita)
# Obs: precisamos sempre informar a chave e caso não encontre o elemento, um KeyError é retornado.
# Obs 2: Ao remover um objeto, o valor deste objeto é retornado

#Forma 2

del receita['fev']

print(receita)
# se a chave não existir será gerado um KeyError
# OBS: neste caso o valor removido não é retornado

"""
# imagine que você tem um comércio eletrônico, onde temos um carrinho de compra na qual adicionamos produtos.
"""
Carrinho de compras:
    Produto 1:
        -nome;
        -quantidade;
        -preço;
    Produto 2:
        -nome;
        -quantidade;
        -preço;
        
*********************************************
# Poderiamos utilizar uma lista para isto? Sim

carrinho = []
produto1 = ['playstation 4', 1, 2300.00]
produto2 = ['God od War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto.

# Poderíamos utilizar uma tupla para isto? Sim!

produto1 = ('playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto.

# 3 - Poderíamos utilizar um dicionário para isto? SIM!!!

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
#podemos ter a certeza sobre cada informação

# Métodos de Dicionários:

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

d.clear()
print(d)

********************************
#Forma 1
novo = d.copy() #deep copy no python
print(novo)

novo['d'] = 4

print(d)
print(novo)

#copiando um dicionário para outro

#Forma 2 # Shallow Copy

novo = d

print(novo)

novo['d'] = 4

print(d)
print(novo)

# Métodos de Dicionários:

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

#Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um interável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 10), 'novo')
print(veja)

"""


