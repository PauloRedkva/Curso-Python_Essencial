"""
Escrevendo um iterador customizado

OBS: Funções dentro de uma classe são chamados de métodos.

"""

#for n in range(0, 11):
#    print(n)
import self as self


class Contador:
    def __init__(self, menor, maior):      # Função Especial - Construtor
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


for n in Contador(1, 61):
    print(n)

for n in range(1, 61):
    print(n)

"""
it = iter(con)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
"""
