"""
Módulos Externos

Utilizamos o gerenciador de Pacotes Python chamado Pip - Python Installer Packege

Pacotes oficiais em: https://pypi.org

colorama -> É utilizado para permitir impressão de textos coloridos no terminal

Instalando um módulo - pip install nome-do-modulo

"""
from colorama import init, Fore

init()

print(Fore.MAGENTA + 'Geek University')
print(Fore.BLUE + 'Geek University')
