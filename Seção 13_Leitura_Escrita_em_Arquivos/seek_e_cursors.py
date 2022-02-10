"""
Seek e Cursors

seek() -> é utilizada para movimentar o cursos pelo arquivo.

************************************************************
Função seek() - Exemplo:
arquivo = open('texto.txt', encoding="utf-8")

print(arquivo.read())

# a função seek() é utilizada para movimentação do cursos pelo arquivo. Ela recebe um parâmetro que indica onde queremos
# colocar o cursor.
# movimentando o Cursor pelo arquivo com a função seek() -> Procurar

arquivo.seek(0)

print(arquivo.read())

arquivo.seek(22)

print(arquivo.read())
**************************************************************
readline
arquivo = open('texto.txt', encoding="utf-8")

# readline -> Funlçai que lê o arquivo linha a linha
ret = arquivo.readline()
print(type(ret))
print(ret)

print(ret.split(' '))
****************************************************************

arquivo = open('texto.txt', encoding="utf-8")
# readlines()

linhas = arquivo.readlines()

print(len(linhas))

*******************************************************************

Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo no disco do computador e
o nosso programa. Esta conexão é chamada de extreaming.
Ao finalizar os trabalhos com o arquivo, devemos fechar esta conexão. Para isto utilizamos a função close()

Passos para se trabalhar com um arquivo

1) Abrir o arquivo;

2) Trabalhar o arquivo;

3) Fechar o arquivo.

# 1 - Abrir o arquivo;
arquivo = open('texto.txt', encoding="utf-8")

# 2 - Trabalhar o arquivo;
print(arquivo.read())

print(arquivo.closed) # verifica se o arquivo está aberto ou fechado | False

# 3 - Fechar o arquivo;
arquivo.close() # True

print(arquivo.closed)

# Obs: Se tentarmos manipular o arquivo após seu fechamento, teremos um ValueError

******************************************************


"""

arquivo = open('texto.txt', encoding="utf-8")

# com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo.
print(arquivo.read(50))
