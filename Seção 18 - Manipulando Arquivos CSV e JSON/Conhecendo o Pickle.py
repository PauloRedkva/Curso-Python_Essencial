"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização

Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

#Obs: O módulo Pickle não é seguro contra dados maliciosos e desta forma não é recomendado trabalhar
com arquivos Pickle vindos de outras pessoas que você não conheça ou de fontes desconhecidas.

--//--
# fazendo a escrita em pickle

felix = Gato("Felix")
pluto = Cachorro("Pluto")

with open("animais.pickle", "wb") as arquivo:  # b é de binário
    pickle.dump((felix, pluto), arquivo)                         # dump recebe dois parâmetros

--//--


"""
import pickle

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f"{self.nome} está comendo ...")

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f"{self.nome} está miando...")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f"{self.nome} está latindo")

# Fazer a leitura de arquivos de Dados em arquivos pickle

with open("animais.pickle", "rb") as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f"O gato chama-se {gato.nome}")
    gato.mia()
    print(f"O tipo do gato é {type(gato)}")

    print(f"O cachorro chama-se {cachorro.nome}")
    cachorro.late()
    print(f"O tipo do gato é {type(cachorro)}")
