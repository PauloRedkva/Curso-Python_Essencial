"""
Escrevendo em arquivos CSV

reader() (leitor), writer() (escritor)

writerow() -> Escreve uma linha

--//--

# writer() -> Gera um objeto para que possamos escrever em um arquivo CSV.
#Utilizamos o método writerow() para escrever cada linha. Este método recebe uma lista.

from csv import writer

with open("filmes.csv", "w", encoding="utf-8") as arquivo:  # Para acrescentar ao invés de "w" - usa "a".
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(["Título", "Gênero", "Duração"])
    while filme != "sair":
        filme = input("Informe o nome do filme: ")
        if filme != "sair":
            genero = input("informe o gênero: ")
            duracao = input("informe a duração (em minutos): ")
            escritor_csv.writerow([filme, genero, duracao])

---///---
"""

# DictWriter
# Obs: As chaves do dicionário devem ser as mesmas utilizadas como cabeçalho.

from csv import DictWriter

with open("filmes2.csv", "w", encoding="utf-8") as arquivo:  # Para acrescentar ao invés de "w" - usa "a".
    cabecalho = ["Título", "Genero", "Duração"]
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != "sair":
        filme = input("Informe o nome do filme: ")
        if filme != "sair":
            genero = input("informe o gênero: ")
            duracao = input("informe a duração (em minutos): ")
            escritor_csv.writerow({"Título": filme, "Genero": genero, "Duração": duracao})
