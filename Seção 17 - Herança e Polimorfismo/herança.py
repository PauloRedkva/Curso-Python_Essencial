"""

POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe que
passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionário
    - nome;
    - sobrenome;
    - cpf;
    - matrícula;

Perguntar: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns
a outras entidades?

class Cliente:
    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

class Funcionario:
    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"

cliente1 = Cliente("Angelina", "Jolie", "123.456.789-99", 5000)
funcionario1 = Funcionario("Felicity", "Jones", "987;654.321-11", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

----////----

Obs: Quando uma classe herda de outra classe ela herda todos os atributos e métodos da classe herdada.

Quando uma classe herda de outra classe. A classe herdade é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe genérica;

Quando uma classe herda de outra classe, ele é chamada:
    [Cliente, Funcionário]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica

---//---

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # Forma comum de acessar dados da Super Classe.
        self.__renda = renda

class Funcionario(Pessoa):
    # Funcionário herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Não é uma forma comum de acessar a Super Classe.
        self.__matricula = matricula


cliente1 = Cliente("Angelina", "Jolie", "123.456.789-99", 5000)
funcionario1 = Funcionario("Felicity", "Jones", "987;654.321-11", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())

print(cliente1.__dict__)
print(funcionario1.__dict__)

----////----

# Sobrescrita de Métodos (Overriding)

Sobrescrita de método ocorre quando reescrevemos / reimplementamos o método presente na super Classe em classes filhas.

"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f"{self.__nome} {self.__sobrenome}"


class Cliente(Pessoa):
    """Cliente herda de Pessoa """

    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf) # Forma comum de acessar dados da Super Classe.
        self.__renda = renda

class Funcionario(Pessoa):
    """ Funcionário herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Não é uma forma comum de acessar a Super Classe.
        self.__matricula = matricula

# Sobrescrita de Métodos (Overriding)
    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f"Funcionário: {self.__matricula} Nome: {self._Pessoa__nome}"

cliente1 = Cliente("Angelina", "Jolie", "123.456.789-99", 5000)
funcionario1 = Funcionario("Felicity", "Jones", "987.654.321-11", 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
