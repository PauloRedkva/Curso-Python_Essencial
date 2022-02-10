"""
Escrevendo em arquivos

# Obs: Ao abrir um arquivo para Leitura, não podemos realizar a escrita nele. Apenas ler
Da mesma forma, se abrirmos um arquivo para escrita, não podemos lê-lo, somente escrever nele.

# Ao abrir um arquivo para escrita, o arquivo é criado no sistema operacional

Obs: Para escrevermos dados em um arquivo, após abrir o arquivo utilizamos a função write().
Esta função recebe uma string como parâmetro, caso contrário teremos um TypeError.

Abrindo um arquivo para escrita com o modo 'w', se o arquivo não existir será criado.
Caso ele já exista, um anterior será apagado e um novo será criado. Desta forma, qualquer
o conteúdo no arquivo anterior será perdido.


# Forma tradicional de escrita em arquivo (não Paytonica)

# Exemplo de escrita

arquivo = open('mais.txt', 'w')

arquivo.write('Um texto qualquer\n')
arquivo.write('Mais um texto\n')

arquivo.close()


EXEMPLO:
Forma Paytonica:

with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha.')

***************************************************************
with open('geek.txt', 'w') as arquivo:
    arquivo.write('Geek\n' * 1000)

**************************************************************

"""
with open('frutas.txt', 'w') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta)
            arquivo.write('\n')
        else:
            break
