# IMPORTAÇÃO DE MÓDULOS
from random import randint
from time import sleep

# APRESENTAÇÃO DO JOGO
print('\033[1;30mVAMOS JOGAR PEDRA, PAPEL OU TESOURA!')

# ENTRADA DE DADOS E DECLARAÇÃO DE VARIÁVEIS DO JOGO
contwin = contlost = contdraw = 0
while True:

    # ESCOLHA DA MÁQUINA
    computador = randint(1, 3)

    # ESCOLHA DO JOGADOR
    print('''\033[1;31m
[ 1 ] PEDRA\033[1;34m
[ 2 ] PAPEL\033[1;35m
[ 3 ] TESOURA''')
    player = int(input('\n\033[1;30mEscolha a sua jogada de acordo com o menu:\n'))

    # A COMPARAÇÃO DO JOGO ACONTECENDO E RESULTADOS INICIAIS
    print('\033[1;30mJO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO!!!\033[m\n')

    # CONDIÇÃO PARA CASO O JOGO EMPATE
    if player == computador:
        print('\033[1;30m-=\033[m' * 5)
        print('\033[1;30mEMPATE!\033[m')
        print('\033[1;30m-=\033[m' * 5)
        contdraw += 1

    # CONDIÇÃO PARA CASO O JOGADOR GANHE
    elif (player == 1 and computador == 3) or (player == 3 and computador == 2) or (player == 2 and computador == 1):
        print('\033[1;32m-=\033[m' * 6)
        print('\033[1;32mVOCÊ GANHOU!')
        print('\033[1;32m-=\033[m' * 6)
        contwin += 1

    # CONDIÇÃO PARA CASO O COMPUTADOR GANHE
    elif (player == 2 and computador == 3) or (player == 1 and computador == 2) or (player == 3 and computador == 1):
        print('\033[1;31m-=\033[m' * 10)
        print('\033[1;31mO COMPUTADOR GANHOU\033[m')
        print('\033[1;31m-=\033[m' * 10)
        contlost += 1

    # CONDIÇÃO PARA CASO O JOGADOR NÃO DÊ UMA ENTRADA VÁLIDA
    else:
        print('\033[31mVocê não escolheu pedra, nem papel, nem tesoura, tente novamente.(\033[m')

    # CONDIÇÃO PARA CONTINUAR O LOOP OU NÃO
    stop = input('\n\033[1;33mVocê deseja parar de jogar? [S/N] ').upper().strip()[0]
    if stop == 'S':
        break
    else:
        continue

# RESULTADOS FINAIS
print('\n\033[1;32mJOGO FINALIZADO!\033[m')
print(f'\033[32m\nVocê GANHOU um total de {contwin} jogos!')
print(f'\033[31mVocê PERDEU um total de {contlost} jogos!')
print(f'\033[37mVocê EMPATOU um total de {contdraw} jogos!')
