"""
Introdução ao Módulo Unittest

Unittest -> Testes Unitários.

O que são testes Unitários?

teste unitário é a forma de se testar unidades individuais de código FONTE.

Unidades individuais podem ser: funções, métodos, classes, módulos, etc.

OBS: Teste unitário não é específico da Linguagem Python.

Para criar nossos testes, criamos classes que herdam de unittest.TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()


TestCase -> Casos de teste para sua unidade.

# Conhecendo as assertions

--//--

Documentação: https://docs.python.org/3/library/unittest.html

Interessante verificar TestCase (Tabela)

Por convenção, todos os testes em um test devem ter seu nome
iniciado com test_
--//--

Para executar os testes com unittest

python nome_do_modulo.py

# Para executar no modo verbose
python nome_do_modulo -v

--///--
# Docstrings nos testes

Podemos acrescentar e é recomendado o uso de docstrings nos nossos testes.
"""

# Prática - Utilizando a abordagem TDD

