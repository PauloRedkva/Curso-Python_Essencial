"""
O que são Decoradores? (Decorators)

- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;

/---------------------------------------------\
/           Function Decorator                 \
------------------------------------------------


----------------------------------------------------
/ /---------------------------------------------\  \
/ /  Function ("comum") -> Função decorada       \  \
/ ------------------------------------------------  \
/------------------------------------------------------

- Decorators também são exemplos de Higher Order Functions;
- Decorators tem uma sintaxe própria, usando @ (Syntact Sugar)

# Testando 1
#saudacao()
teste = seja_educado(saudacao)
teste()

# Testando 2
def seja_educado(funcao):
    def sendo():
        print("Foi um prazer conhecer você! ")
        funcao()
        print("Tenha um ótimo dia! ")
    return sendo

def saudacao():
    print("Seja bem-vindo(a) à Geek University")

def raiva():
    print("EU TE ODEIO! ")

raiva_educada = seja_educado(raiva)
raiva_educada()

------//-------

# Decorators como função (com Sintaxe recomendada / "com açucar sintático")

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("Foi um prazer conhecer você")
        funcao()
        print("Tenha um excelente dia!")
    return sendo_mesmo

@seja_educado_mesmo
def apresentando():
    print("Meu nome é Pedro")

apresentando()

@seja_educado_mesmo
def dormir():
    print("Quero dormir...")

dormir()

---//---

# OBS: Não confunda Decorator com Decorator Function

"""

