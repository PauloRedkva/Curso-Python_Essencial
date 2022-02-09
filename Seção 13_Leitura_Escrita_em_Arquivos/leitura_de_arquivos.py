"""
Leitura de Arquivos
Para o conteúdo de um arquivo python, utilizamos a função integrada open(),
que literalmente significa 'abrir'

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro de entradam que neste caso é o caminho
para o arquivo a ser lido. Essa função retorna
um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir, ou entãoteremos o erro
FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>
<class '_io.TextIOWrapper'>

mode r -> Mode de Leitura. r -> read() -> ler

"""

# Exemplo

arquivo = open('texto.txt')

# print(arquivo)

# print(type(arquivo))

print(arquivo.read())

print(arquivo.read())


