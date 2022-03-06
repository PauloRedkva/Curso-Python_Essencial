"""
POO - MRO - Method Resolution Order

É a ordem de execução dos Métodos. Ou seja, quem será executado primeiro?


Em Python podemos conferir a ordem de Execução dos Métodos de 3 formas:

    - Via propriedade da classe __mro__
    - Via método mro()
    - via help


"""
class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f"Eu sou {self.__nome}"

class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f"{self._Animal__nome} está nadando."

    def cumprimentar(self):
        return  f"Eu sou {self._Animal__nome} do mar!"

class Terrestre(Animal):

    def __init__(self, nome):

        super().__init__(nome)

    def andar(self):
        return f"{self._Animal__nome} está andando."

    def cumprimentar(self):
        return f"Eu sou {self._Animal__nome} da terra!"

class Pinguin(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

tux = Pinguin("Tux")

print(tux.cumprimentar())

"""
Pinguin(Aquatico, Terrestre)
Eu sou Tux do mar!

class Pinguin(Terrestre, Aquatico)
Eu sou Tux da terra!

"""