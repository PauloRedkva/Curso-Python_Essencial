"""
Assertions (Afirmações / Checagens / Questionamentos)

Em Python utilizamos a palavra reservada "assert" para realizar simples afirmações utilizadas nos testes.

Utilizamos o "assert" em uma expressão que queremos checar se é válida ou não.

Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError.

# Obs: Podemos especificar opcionalmente um segundo argumento ou mesmo uma mensagem de erro personalizada.
# Obs: A palavra "assert" pode ser utilizada em qualquer função ou código nosso... não precisa ser exclusivamente nos testes.

--//--

# ALERTA: Cuidado ao usar "assert"

Se um programa Python for executado com o parâmetro -O, nenhum assertion será validado. Ou seja, todas as duas validações
já eram!



"""
# ALERTA: Cuidado ao usar "assert"
def soma_numero_positivos(a, b):
    assert a > 0 and b > 0, "Ambos números precisam ser positivos"
    return a + b

ret = soma_numero_positivos(2, 4) # 6
ret = soma_numero_positivos(-2, 4) # AssertionError
print(ret)

def comer_fastfood(comida):
    assert comida in [
        "pizza",
        "sorvete",
        "doces",
        "batata frita",
        "Cachorro quente",
    ], "A comida precisa ser fast food"
    return f"Eu estou comendo {comida}"

comida = input("Informe a comida ")

print(comer_fastfood(comida))

