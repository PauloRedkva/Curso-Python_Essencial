"""
Módulo Collections:

-> Default Dict

#Recap Dicionários

dicionario = {'curso': 'programação em Python: Essencial'}
print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # ??? KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Este valor será utulizado sempre que não houver um valor definido. Caso tentemos
acessar a chave que não existe, essa chave será criada e o valor default será atribuido.

Lambda - Funções sem nome que podem ou não receber paarâmetros de entrada e retornar valores.

"""

#fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro']) #Keyerror no dicionario comum, ,mas aqui não

print(dicionario)