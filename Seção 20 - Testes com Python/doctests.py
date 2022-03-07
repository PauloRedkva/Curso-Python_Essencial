"""
Doctests

Doctests são testes que colocamos na docstring das funções/métodos Python

Para rodar um test do doctest:

python -m docstest -v nome_do_arquivo.py


"""

def soma(a, b):
    """
    soma os números a e b

    >>> soma(1, 2)
    3
    """
    return a + b

