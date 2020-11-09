tabela = ['_', '_', '_', '_', '_', '_', '_', '_', '_']


def desenho(vetor):
    jogodavelha = ''
    for i in range(len(vetor)):
        if i == 2 or i == 5 or i == 8:
            jogodavelha += ' ' + vetor[i] + ' \n'
        else:
            jogodavelha += ' ' + vetor[i] + ' |'
    return jogodavelha
    

def verificador(vetor, posicao):
    resultado = False
    if vetor[posicao] == '_':
        resultado = True
    return resultado


def verificavitoria(vetor, simbolo):
    resultado = False
    # HORIZONTAL
    if vetor[0] == simbolo and vetor[1] == simbolo and vetor[2] == simbolo:
        resultado = True
    elif vetor[3] == simbolo and vetor[4] == simbolo and vetor[5] == simbolo:
        resultado = True
    elif vetor[6] == simbolo and vetor[7] == simbolo and vetor[8] == simbolo:
        resultado = True
    # VERTICAL
    elif vetor[0] == simbolo and vetor[3] == simbolo and vetor[6] == simbolo:
        resultado = True
    elif vetor[1] == simbolo and vetor[4] == simbolo and vetor[7] == simbolo:
        resultado = True
    elif vetor[2] == simbolo and vetor[5] == simbolo and vetor[8] == simbolo:
        resultado = True
    # DIAGONAL
    elif vetor[0] == simbolo and vetor[4] == simbolo and vetor[8] == simbolo:
        resultado = True
    elif vetor[6] == simbolo and vetor[4] == simbolo and vetor[2] == simbolo:
        resultado = True
    return resultado


def verificaempate(vetor):
    resultado = True
    for i in vetor:
        if i == '_':
            resultado = False
    return resultado


jogador = 1
jogadornum1 = 0
jogandornum2 = 0

while True:
    if jogador == 1:
        jogadornum1 = input('Digite uma posição de 1 a 9: ')
        if verificador(tabela, int(jogadornum1) - 1):
            tabela[int(jogadornum1) - 1] = 'X'
            jogador = 2
            print(desenho(tabela))
        else:
            print(desenho(tabela))
            print('POSIÇÃO JÁ OCUPADA!')
    if verificavitoria(tabela, 'X'):
        print('JOGADOR NÚMERO 1 GANHOU!')
        break
    if verificaempate(tabela):
        print('VELHA!')
        break

    if jogador == 2:
        jogadornum2 = input('Digite uma posição de 1 a 9: ')
        if verificador(tabela, int(jogadornum2) - 1):
            tabela[int(jogadornum2) - 1] = 'O'
            jogador = 1
            print(desenho(tabela))
        else:
            print(desenho(tabela))
            print('POSIÇÃO JÁ OCUPADA!')

    if verificavitoria(tabela, 'O'):
        print('JOGADOR NÚMERO 2 GANHOU!')
        break
    if verificaempate(tabela):
        print('VELHA!')
        break

