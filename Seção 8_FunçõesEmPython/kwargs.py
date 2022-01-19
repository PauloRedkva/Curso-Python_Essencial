"""
**kwargs

**xis

-> Por convenção chamamos de **kwargs

Este é só mais um parametro, mas diferente do *args que coloca os valores extras em uma tupla, o
**kwargs exige que utilizemos parametros nomeados, e transforma esses parametros extras em um dicionario.

# Exemplo

def cores_favoritas(**kwargs):
    print(kwargs)
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

OBS: Os parametros *args e **kwargs não são obrigatorios.

*********************
# Exemplo mais completo

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funções podemos ter (NESTA ORDEM):
# Parametros obrigatórios;
# *args;
# Parametros default (não obrigatórios);
# **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)

minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entenda por que é importante manter a ordem dos parametros na declaração

#Função com a Ordem Correta de Parâmetros:

#def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
#    return [a, b, args, instrutor, kwargs]

# Função com a ordem incorreta de parâmetros:

def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]

a=1
b=2
args=(3,)
instrutor = 'Geek'
kwargs = {'sobrenome':'Univertity' , 'cargo':'Instrutor'}

print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **Kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome':'Jones'}

print(mostra_nomes(**nomes))

"""

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
set = {1, 2, 3}


soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*set)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS - Os nomes da chave em um dicionario devem ser os mesmos dos parametros da função

