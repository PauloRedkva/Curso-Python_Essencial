"""
Trabalhando com Delta de Data e Hora

data_inicial = dd/mm/yyyy 15:55:34.9939239

data_final = dd/mm/yyyy 13:36:34.9939239

deta = data_final - data_inicial

# Temos a data de hoje
data_hoje = datetime.datetime.now()

# Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2022, 11, 10, 0)

# calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))

print(repr(tempo_para_evento))

print(tempo_para_evento)

print(f" Faltam {tempo_para_evento.days} dias para seu aniversário")

--//--


"""

import datetime

# Data da compra
data_da_compra = datetime.datetime.now()

print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto

print(vencimento_boleto)
