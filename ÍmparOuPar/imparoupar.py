# IMPORTAÇÕES DE MÓDULOS
from random import randint

# APRESENTAÇÃO DO JOGO
print('\033[1;35m=' * 60)
print('{:^60}'.format('ÍMPAR OU PAR!'))
print('=' * 60)

# ENTRADA DE DADOS DO JOGADOR E DO COMPUTADOR
cont = 0
while True:
    computador = randint(0, 10)
    while True:
        print('''\033[1;34m
[ 1 ] ÍMPAR
\033[1;36m[ 2 ] PAR\033[m''')
        escolhaplay = int(input('\n\033[34mÍMPAR\033[30m OU \033[36mPAR? \033[30m(Escolha de acordo com o menu) '))

    # CONDIÇÃO PARA CASO O JOGADOR NÃO ENTRE COM UM DADO VÁLIDO
        if escolhaplay != 1 and escolhaplay != 2:
            print('\033[1;31mOPÇÃO INVÁLIDA! Tente novamente.')
        else:
            break

    # COMPARAÇÃO DOS DADOS ACONTECENDO
    print(f'\033[30mVocê escolheu {escolhaplay}')
    player = int(input('\n\033[30mDigite um número para jogar com o do computador: '))
    if (computador + player) % 2 == 0:
        win = 2
    else:
        win = 1

    # CONDIÇÃO PARA CASO O JOGADOR GANHE
    if escolhaplay == win:
        print('\n\033[1;32mVOCÊ GANHOU! Parabéns.')
        print(f'\033[30mO computador jogou {computador} e soma dos dois números ficou {(player + computador)}')
        cont += 1

    # CONDIÇÃO PARA CASO O COMPUTADOR GANHE
    else:
        print(f'\n\033[1;31mVOCÊ PERDEU!')
        print(f'\033[30mO computador jogou {computador} e soma dos dois números ficou {(player + computador)}')

    # CONDIÇÃO PARA CONTINUAR COM O LOOP OU NÃO
    stop = input('\n\033[1;35mVocê deseja parar de jogar? [S/N] ').upper().strip()[0]
    if stop == 'S':
        break
    else:
        continue

# RESULTADOS FINAIS
print(f'\n\033[1;32mJOGO FINALIZADO!\033[m \033[30mVocê ganhou um total de {cont} jogos')
