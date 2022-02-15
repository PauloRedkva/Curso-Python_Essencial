"""

Sistema de arquivos - Manipulação com

Módulo os

# Arquivo
print(os.path.exists("arquivo.txt"))
print(os.path.exists("frutas.txt"))

#Descobrindo se um arquivo ou diretório existe.


# Diretório
print(os.path.exists("nome"))


# criando arquivos
# Forma 1

open("arquivo-teste.txt", "w").close()
# Forma 2

open("arquivo-teste2.txt", "a").close()

#Forma 3
with open('arquivo-test3.txt', "w") as arquivo:
    pass

Usando Módulo os -> os.mknod('arquivo-teste4.txt')

***************************************************

#Criando arquivos
os.mknod('arquivo-teste4.txt')

# Criar diretório
os.mkdir('nome_do_diretório')

********************************************
#Criando multi-diretírios (árvore de diretórios)
os.makedirs("templates/geek/university")

*******************************************
#Removendo arquivos.
os.remove('nome_do_arquivo')
***************************************
# Removendo diretórios vazios

os.rmdir('templates)
***************************************
# Removendo uma árvore de diretórios
for arquivo in os.scandir("geek2"):
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file():
        os.rmdir(arquivo.path)


https://docs.python.org/3/library/os.html?highlight=os#modulo-os

"""



