"""
Manipulando Data e Hora em Python.

Python tem um módulo Built-in (integrado) para se trabalhar com data e hora
chamado datetime

--//--
import datetime

#print(dir(datetime))

print(datetime.MAXYEAR)

print(datetime.MINYEAR)

# Retorna a data e hora corrente
print(datetime.datetime.now())  # 2022-03-06 11:25:46.175663  | BR->06/03/2022

# datetime.datetime(year, month, day, minute, second, microsecond)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()

print(inicio)

#alterar o horário para x horas, x minutos, x segundos, x microsegundo
inicio = inicio.replace(hour=11, minute=0, second=0, microsecond=0)
print(inicio)

--//--
# Recebendo dados do usuário e convertendo para data


evento = datetime.datetime(2023, 1, 1, 0)

print(type(evento))

print(type("31/12/2018"))

print(evento)

nascimento = input("Informe sua data de nascimento (dd/mm/yyyy): ")

nascimento = nascimento.split("/")

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

print(type(nascimento))

--//--



"""
import datetime

evento = datetime.datetime.now()

# Acesso individual dos elementos de data e hora.

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)

print(dir(evento))
