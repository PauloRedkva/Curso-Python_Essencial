"""
O Bloco Try/Except

Utilizamos o Bloco try/except para tratar erros que podem ocorrer em nosso codigo. Previnindo
assim que o programa pare de funcionar e o usuario receba mensagens de erro inesperadas.

A forma geral mais simples é:
try:
    //execução problemática
except:
    // o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro genérico

try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a funcao Geek(), caso encontre erros, imprima a mensagem de erro.

try:
    len(5)
except:
    print('Deu algum problema')

# Tente executar a funcao Geek(), caso encontre erros, imprima a mensagem de erro.


OBS: Tratar erro de forma genérica, não é a melhor forma de tratamento de erros. O ideal é sempre tratar de forma específica

# Exemplo 3 - Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

try:
    len(5)
except TypeError:
    print('Você está utilizando uma função inexistente')

# Exemplo 5 - Tratando um erro específico com detalhes do erro!

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')


try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
except NameError as erra:
    print(f' Deu NameError: {erra}')

"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": "Geek"}
print(pega_valor(dic, "game"))







