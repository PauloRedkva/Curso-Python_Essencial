"""
Decoradores com diferentes assinaturas


# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return "Olá, eu sou o/a {}".format(nome)

@gritar
def ordenar(principal, acompanhamento):
    return "Olá, eu gostaria de {}, acompanhado de {}, por favor.".format(principal, acompanhamento)

#Testando

#print(saudacao("Angelina"))
print(ordenar("picanha", "batata Frita"))

TypeError: aumentar() takes 1 positional argument but 2 were given:

Para resolver utilizamos um padrão de projeto chamado Decoretor Pattern

Assinatura de uma função é representada pelo seu retorno e parâmetros de entrada.

--//--

# Refatorando com a Decorator Pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return "Olá, eu sou o/a {}".format(nome)

@gritar
def ordenar(principal, acompanhamento):
    return "Olá, eu gostaria de {}, acompanhado de {}, por favor.".format(principal, acompanhamento)

#Testando

#print(saudacao("Angelina"))
print(ordenar("picanha", "batata Frita"))

# Obs: Vale lembrar que podemos utilizar parâmetros nomeados


print(ordenar(acompanhamento="Picanha", principal="Batata Frita"))

"""

# Decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return "Valor incorreto! Primeiro argumento precisa ser o {}".format(valor)
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento("pizza")
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

#print(soma_dez(10, 12))  #22

#print(soma_dez(1, 21)) #22

print(comida_favorita("pizza", "churrasco"))