"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lampadas da sua casa.

--//--
idade = 32

preco = 2340.45

nome = "Felicity Jones"

print(type(idade))
print(type(preco))
print(type(nome))

--//--
class Lampada:
    pass

lamp = Lampada()
print(type(lamp))

# <class '__main__.Lampada'>

Classes podem conter:
    - Atributos -> Representam as características do objeto. Ou seja, pelos atribuitos
    conseguimos representar computacionalmente os estados de um objeto. No caso da Lampada, possivelmente
    iríamos querer saber se a lampada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual a
    luminosidade dela etc.

    - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no
    seu sistema. No caso da lampada, um comportamento que provavelmente iriamos querer representar no nosso sistema
    é o de ligar e desligar a lampada.

Em Python para definir uma classe, utilizamos a palavra reservada 'class'.

OBS: Utilizamos a palavra 'pass' em Python quando temos um Bloco de código que ainda não está implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em Maiúsculo. Se o nome for
composto, utilizamos as iniciais de ambas as palavras em maiúsculo, todas juntas.

Dica Geek: Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares
para nomes de classes, atributos, métodos, arquivos, diretórios e etc.

Obs: Quando estamos planejando um software e definimos quais classes que teremos no sistema, chamamos estes objetos que
serão mapeados para classes de entidade.

"""

class Lampada:
    pass

class ContaCorrente:
    pass

class Produto:
    pass

class Usuario:
    pass

lamp = Lampada()
print(type(lamp))


valor = int("42") # operação de cast

print(help(int))
