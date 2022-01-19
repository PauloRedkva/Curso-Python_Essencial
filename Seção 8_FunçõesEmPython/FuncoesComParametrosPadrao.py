"""

Funçoes com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parametro seja opcional

#Exemplo de Função onde a passagem de parametro seja opcional
print('Geek University')

print()

***************
Exemplo de Função em que a passagem de parametro é obrigatório
def quadrado(numero):
    return numero ** 2
print(quadrado(3))
print(quadrado()) - TypeError:

def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2, 3))
print(exponencial(3, 2))

print(exponencial(3)) #por padrão eleva ao quadrado
print(exponencial(3, 5)) # Eleva a potencia informada pelo usuario

# OBS
# se o usuario passar somente um argumento, este será atribuido ao parametro numero, e calculado o quadrado deste numero;
# Se o usuario passar 2 argumentos, o primeiro será atribuido ao parametro numero e o segundo ao parametro potencia
#será calculada a esta potencia.

print(exponencial())


#Obs: Em funções python, os parametros com valores default (padrão) DEVEM sempre estar ao final da declaração

# Erro
def teste(num=2, potencia):
    return num ** 2
print(teste(6))


def exponencial(numero=4, potencia=2):
    return numero ** potencia

def soma(num1, num2):
    return num1 + num2

print(soma(4, 3))
print(soma(4)) #typeError
print(soma()) #typeError

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

#Por quê usar parametros com valor default?

- Nos permite ser mais flexivel nas funções
- Evita erros com parametros incorretos
- Nos permite trabalhar com exemplos mais legíveis de código;

# Quais tipos de dados podemos utilizar como parametros default para parametros?
- Qualquer tipo de dado
    - Numeros, strings, floats, listas, tuplas, dicionarios, funcoes e etc

*********************************

# Exemplos

def soma(num1, num2):
    return num1 + num2

def mat(num1, num2, fun=soma):
    return fun(num1, num2)

def subtracao(num1, num2):
    return num1 - num2

print(mat(2, 3))
print(mat(2, 2, subtracao))

****************************************************
# Escopo - Evitar problemas e confusões...

# Variáveis Globais
# Variáveis Locais

instrutor = 'Geek' #Variável Global

def diz_oi():
    instrutor = 'Python' # Variável local
    return f'Oi {instrutor}'

print(diz_oi())

#Se tivermos uma variável local com o mesmo nome de uma variável local, a local terá preferencia e será utilizada.
def diz_oi():
    prof = 'Geek'  # variavel local
    return f'Olá {prof}'

print(diz_oi())

print(prof)  # NameError

# Atenção com variaveis globais - Se puder evitar - EVITE!


total = 0

def incrementa():
    total = total + 1 #UnboundLocalError: local variable 'total' referenced before assignment (variavel local esta sendo
    #usada para processamento sem ter sido inicializada
    return total

print(incrementa())

total = 0

def incrementa():
    global total #avisando que queremos utilizar a variavel global

    total = total + 1
    return total

print(incrementa())
**************************************************
"""

# Podemos ter funcoes que são declaradas dentro de funcoes e tambem tem uma forma especial de escopo de variavel

def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())
print(fora())
print(fora())
print(fora())


