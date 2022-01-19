"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- São muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela; é bom fazer uma verificação para que
a função seja simplificada.
Já utilizamos várias funções desde que iniciamos o curso:
- print(0
- len()
- max()
- count()
- e muitas outras;

"""

# Exemplo de utilização de funções:

#cores = ['verde', 'amarelo', 'azul', 'branco']

# Utilizando a função integrada (Built-in) do Python print()

#print(cores)

#curso = 'Programação em Python: Essencial'
#print(curso)

#cores.append('roxo')
#print(cores)

#curso.append('mais dados...') # AttributeError: 'str' object has no attribute 'append'
#print(curso)

#cores.clear()
#print(cores)

# print(help(print)
# DRY = Don't Repeat Yourself - Não repita você mesmo / Não repita seu código
# Mas então, como definir funções?

"""
Em Python a forma geral de definir uma função é:

def nome_da_função(parametros_de_entrade):
    bloco_da_função
    
Onde
nome_da_funcao -> Sempre, com letras minúscular, e se for nome composto, separado por underline (snake Case);
parametros_de_entrada -> opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função, ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS:  Veja que para definir uma função, utilizamos uma palavra reservada 'def' informando ao `Python que  
estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos:
utilizado em Python para definir Blocos 

"""

# Definindo a primeira função
# Definição
def diz_oi():
    print('oi!')
"""
OBS: 
1- Veja que dentro das nossas funções podemos utilizar outras funções;
2- Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi;
3- Veja que esta função não recebe nenhum parâmetro de entrada;
4- Veja que esta função não retorna nada; 
"""

# Utilizando funções
#Chamada de execução
#diz_oi()

"""
ATENÇÃO:
Nunca esqueça de utilizar o () ao executar uma função.
#errado!
diz_oi
diz_oi ()
#certo
diz_oi()

"""

# Exemplo 2

def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante!')

cantar_parabens()

#for n in range(5):
#    cantar_parabens()

# Em Python podemos criar variáveis do tipo de uma função e executar esta função através da variável

canta = cantar_parabens

canta()