"""
Estruturas Lógicas: and (e), or (ou), not (não), is (é)

Operadores Unários:
-not

Operadores Binários:
- and, or, is

Regras de Funcionamento:

Para o And, ambos valores precisam ser True
Para o or, um ou outro valor precisa ser True
Para o not, o valor do Booleano é invertido
"""

ativo = True
logado = True
"""
if ativo is logado:
    print("Bem-vindo usuário!")
else:
    print('Você precisa atividas sua conta. Por favor, cheque seu e-mail')
"""
#se não estiver ativo
if not ativo:
    print('Cheque seu e-mail')
else:
    print('Bem-vindo usuário')

print(not False)