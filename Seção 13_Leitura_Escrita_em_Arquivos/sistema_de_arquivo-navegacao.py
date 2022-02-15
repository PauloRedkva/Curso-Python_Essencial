"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar e fazer o uso do módulo os.

os -> Operating System - Sistema Operacional.

*************************

# Fazer import
import os

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())

# para mudar de diretório, podemos utilizar o chdir()

#os.chdir("..")


***********************

# Obs: Para usuarios Windows
print(os.path.isabs('C:\\Users\\paulo'))


**************************


# Podemos identificar o sistema operacional com módulo os

# print(os.name)

# podemos ter mais detalhes no sistema operacional

#print(os.uname())

#print(sys.platform)
os.path.join(os.getcwd(), "geek") # acessa o diretorio objetivo


# Podemos listar os diretórios com o listdir()

print(os.listdir())
"""
# Fazer import
import os
import sys

# Podemos listar os diretórios com mais detalhes com scandir()

print(os.scandi())