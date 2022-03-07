"""
Por que testar nosso código?

Testes automatizados!

          Aplicação Web
-------------------------------
/      frontend e backend     /
------------------------------
/     testes automatizados   /
------------------------------

Por que testar nosso código?
    - Reduzir bugs (problemas) no código existente;
    - Testes garantem que novos recursos de sua aplicação não quebrem (alterem) recurso antigo
    - Testes garantem que bugs (problemas) que foram corrigidos anteriormente continuam corrigidos
    - Testes garantem que a refatoração que costumamos fazer não tragam novos bugs.

--//--
TDD - Test Driven Development ( Desenvolvimento guiado por testes)

Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro
    - Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso)
    - Então você refatora o código, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red
    - Green
    - Refactor


"""
class Gato:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        print(f"{self.__nome} está miando...")

felix = Gato("Felix")

felix.miar()

print(felix.nome)
