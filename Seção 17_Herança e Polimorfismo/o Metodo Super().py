"""
POO - O método Super():

O método Super() se refere a super classe.

Com super() eu consigo fazer acesso a qualquer elemento da classe pai.

"""

class Animal:
    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f"O {self.__nome} fala {som}")

class Gato(Animal):
    def __init__(self, nome, especie, raca):
        #Animal.__init__(self, nome, especie)  # É possível, mas não recomendado
        super().__init__(nome, especie)        # Recomendando. Se passo o super() não precisa passar self.
        self.__raca = raca

felix = Gato("Felix", "Felino", "Angorá")

felix.faz_som("miau")
