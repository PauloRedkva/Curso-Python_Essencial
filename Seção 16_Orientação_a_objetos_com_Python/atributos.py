"""
POO - Atributos

Atributos -> Representam as características do Objeto. Ou seja, pelos atributos, nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmicos;

# Atributos de Instância: São atributos declarados dentro do Método Contrutor.

Obs: Método construtor é um método especial utilizado para a construção do objeto.

# Em java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
    public int getVoltagem(){
        return this.voltagem
    }
}

Em Python, por convenção, ficou estabelecido que, tod(o) atributo de uma classe é publico.
Ou seja, pode ser acessado em tod o projeto
Caso queiramos demonstrar que um determinado atributo deve ser privado, ou seja,
que deve ser acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se __ duplo underscore
no início de seu nome.

Isso é conhecido também como Name Mangling.

--//--
# Obs: Lembre-se que isso é apenas uma convenção, ou seja, a Linguagem Python não vai impedir que façamos
# acesso aos atributos sinalizados como privados fora da classe.

# Exemplo:
user = Acesso("user@gmail.com", "123456")

print(user.email)
#print(user.__senha) # AttributeError

print(dir(user))

print(user.mostra_senha())  # Temos acesso. Mas não deveríamos ter este acesso. (name Mangling)

user.mostra_senha()
user.mostra_email()

---//---

# O que significa atributos de Instância?
# Significa que ao criarmos instancias/objetos de uma classe, todas as instancias terão estes atributos.

user1 = Acesso("user1@gmail.com", "123456")
user2 = Acesso("user2@gmail.com", "654321")

user1.mostra_email()
user2.mostra_email()

---///---
# Atributos de Classe

# Atributos de classe, são atributos, claro, que são declarados diretamente na classe, ou seja, fora do construtor
# Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instancias da classe.
# Ou seja, ao invés de cada instancia da classe ter seus próprios valores, como é o caso dos atributos de instancia,
# com atributos de classe todas as instancias terão o mesmo valor para este atributo.

p1 = Produto("PS4", "Video Game", 2300)
p2 = Produto("Xbox", "Video Game", 4500)

print(p1.valor) # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor) # Acesso possível, mas incorreto de um atributo de classe

# Obs: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto) # Acesso correto de um atributo de classe

print(p1.id)
print(p2.id)

# Obs: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
# são chamados de atributos estáticos;

---///---




"""
# Classes com atributo de instancias púlicas
class Lampada:
    def __int__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

# Atributos Públicos e Atributos Privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)

# Refatorar a classe Produto

class Produto:
    #Atributo de Classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

# Atributos Dinâmicos -> Um atributo de instancia que pode ser criado em tempo de execução

# Obs: O atributo dinâmico será exclusivo da instancia que o criou.

p1 = Produto("PS4", "Video Game", 2300)
p2 = Produto("Arroz", "Mercearia", 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = "5 kg" # Note que na classe Produto não existe o atributo peso

print(f"Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}")

# print(f"Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}")

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)

#print(Produto.__dict__)

del p2.peso

print(p1.__dict__)
print(p2.__dict__)
