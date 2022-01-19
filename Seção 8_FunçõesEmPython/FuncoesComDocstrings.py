"""
Documentando funcoes com Docstrings

# Exemplos

def diz_oi():
    Uma função simples que retorna a string 'Oi!' (separado por 03 aspas duplas)
    return 'Oi!'

print(diz_oi())

print(help(diz_oi()))

print(diz_oi.__doc__)
OBS: Podemos ter acesso a documentação de uma função em Python
utilizando o método especial __doc__

Podemos ainda fazer acesso com a funcao Help
"""
def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potencia' informada
    :param numero: Número que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial Padrão é 2
    :return: Retorna o exponencial de 'numero' por 'potencia.
    """
    return numero ** potencia

print(help(exponencial))