"""
Lendo arquivos CSV:

CVS - Comma Separeted Values - Valores Separados por Vírgula

# Separador por vírgula
1, 2, 3, 4, 5, 6

"geek", "university", "Python", "Ciência

# Separador por ponto e vírgula

1; 2; 3; 4; 5; 6

"geek"; "university",; "Python"; "Ciência

# separador por Espaço

1 2 3 4 5 6

"geek" "university" "Python" "Ciência

Para conseguir dados e treinar:
http://dados.gov.br/dataset

--//--

# Possível de se trabalhar, mas não é o ideal. (Trabalhoso)
with open("lutadores.csv", encoding="utf8") as arquivo:
    dados = arquivo.read()
    #print(type(dados))
    dados = dados.split(",")[2:]
    print(dados)

--//--

A Linguagem Python possui duas formas diferentes para ler dados em Arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como Listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como OrderedDicts;

--//--

# Reader

from csv import reader

with open("lutadores.csv", encoding="utf-8") as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        #Cada linha é uma lista
        print(f"{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centímetros")

--//--

# DictReader

from csv import DictReader

with open("lutadores.csv", encoding="utf-8") as arquivo:
    leitor_csv = DictReader(arquivo)

    for linha in leitor_csv:
        #Cada linha é uma lista
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} centímetros")

--//--
Por padrão o método dict

"""

# DictReader com outro separador

from csv import DictReader

with open("lutadores.csv", encoding="utf-8") as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=",") # delimiter o padrão é , mas pode ser outro: ";" "=" " "

    for linha in leitor_csv:
        #Cada linha é uma lista
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']} centímetros")


