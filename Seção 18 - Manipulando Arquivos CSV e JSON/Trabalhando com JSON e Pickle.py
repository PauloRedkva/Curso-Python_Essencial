"""
Trabalhando com JSON e Pickle

JSON -> JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por
empresas (Twitter, Facebook, YT) e terceiros (Nós desenvolvedores)

--//--
import json

ret = json.dumps(["produto", {"PlayStation 4": ("2Tb", "Novo", "220V", 2340)}])

print(type(ret))

print(ret)


--//--

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__raca

felix = Gato("Felix", "Vira-lata")

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)

---///---
Integrando o Json com o Pickle.

pip install jsonpickle

import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__raca

felix = Gato("Felix", "Vira-lata")

ret = jsonpickle.encode(felix)

print(ret)

----////----

#escrevendo o arquivo json/pickle
import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__raca

felix = Gato("Felix", "Vira-lata")

with open("felix.json", "w") as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

---////---

"""

# Lendo o arquivo json/pickle
import jsonpickle

class Gato:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    @property
    def nome(self):
        return self.__nome
    @property
    def raca(self):
        return self.__raca

felix = Gato("Felix", "Vira-lata")

with open("felix.json", "r") as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)
