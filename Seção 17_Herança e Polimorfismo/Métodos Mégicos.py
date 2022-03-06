"""
POO - Métodos Mágicos

São todos os métodos que utilizam dunder. Dunder > Double Underscore

dunder init -> __init__

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

--//--

Dunder  __repr__ -> Faz a representação do Objeto.

    def __repr__(self):
        return self.titulo

--//--

dir(__builtins__)
"""

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __len__(self):
        return self.paginas

    #def __del__(self):
    #    print("um objeto do tipo Livro foi deletado da memória")

    def __add__(self, other):
        return f"{self} - {other}"

    def __mul__(self, other):
        if isinstance(other, int):
            msg = " "
            for n in range(other):
                msg += " " + str(self)
            return msg
        return "Não posso multiplicar"


livro1 = Livro("Python Rocks!", "Geek University", 400)

livro2 = Livro("Inteligencia Artificial com Python", "Geek University", 350)

print(livro1)
print(livro2)
print(len(livro1))
print(livro1 + livro2)
print(livro1 * 3)
