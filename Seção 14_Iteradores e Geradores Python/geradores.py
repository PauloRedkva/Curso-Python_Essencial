"""

Geradores (Generators)

- São iterators (iteradores);

OBS: O contrário não é verdadeiro. Ou seja, nem t@do iterator é um generator.

Outras informações:
- Geradores podem ser criados com funções geradoras;
- Funções geradoras utilizam a palavra reservada yield;
- Generators pode ser criados com Expressões Geradoras;

Diferenças entre Funções e Generator Fuctions (Funções Geradoras)

----------------------------------------------------------------------------------------
/ Funções                                 /      Generator Functions                  /
---------------------------------------------------------------------------------------
/ utizam return                          /         utilizam yield                     /
---------------------------------------------------------------------------------------
/ retorna uma vez                       /   podem utilizar yield multiplas vezes      /
---------------------------------------------------------------------------------------
/ quando executada, retorna um valor    /   quando executada, retorna um generator    /
---------------------------------------------------------------------------------------

# Exemplo de Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# Obs: Uma generator function não é um Gerador. Ela gera um generator.

gen = conta_ate(5)

# print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

***************************************************
# Exemplo de Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = conta_ate(10)

for num in gen:
    print(num)
*********************************************
gen = conta_ate(10)

print(next(gen)) # 1

print('Geek')
print("\n")

for num in gen:
    print(num)
**********************************************

"""

# Exemplo de Função Geradora (Generator Function)

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

gen = list(conta_ate(10))
print(gen)

