# IMPORTAÇÃO DE MÓDULOS
from random import randint

# APRESENTAÇÃO DO JOGO
print('\033[1;35m-=\033[m' * 30)
print('{:^60}'.format('\033[1;35mJOGO DO ADIVINHA'))
print('\033[1;35m-=\033[m' * 30)

# ENTRADA DOS NOMES DOS DOIS JOGADORES
nome1 = input('\033[1;37mQual é o nome do primeiro jogador? ')
nome2 = input('Qual é o nome do segundo jogador? ')
nome = nome1

# ENTRADA DO INTERVALO QUE O COMPUTADOR IRÁ GERAR UM NÚMERO ALEATÓRIO
n1 = int(input('Qual será o inicio do intervalo? '))
n2 = int(input('Qual será o fim do intervalo?\033[m '))

# COMEÇO DO JOGO
cont = 0

# ÍNICIO DO LOOP
for c in range(0, 2):
    a = randint(n1, n2)
    while True:
        # VARIÁVEL PARA CONTAR QUANTAS TENTATIVAS O PRIMEIRO JOGADOR PRECISOU PARA ACERTAR O NÚMERO QUE O COMPUTADOR PENSOU
        cont = cont+1
        if nome == nome1:
            cont1 = cont
        elif nome == nome2:
            cont2 = cont
        # ENTRADA DAS TENTATIVAS DO PRIMEIRO JOGADOR
        b = int(input('\033[1;37m\nTente adivinhar o número que o computador pensou: '))

        # CONDIÇÃO PARA CASO O JOGADOR ACERTE O NÚMERO QUE O COMPUTADOR PENSOU
        if a == b:
            print('\033[1;32m\nParabéns! \033[1;37mVocê adivinhou o número que o computador pensou!\b')
            if nome == nome1:
                print(f'\033[37m{nome} conseguiu acertar o número que a máquina pensou em {cont1} tentativas, vez do jogador 2!\n ')
            elif nome == nome2:
                print(f'\033[37m{nome} conseguiu acertar o número que a máquina pensou em {cont2} tentativas\n ')
            cont = 0
            break
        # CONDIÇÃO PARA CASO O JOGADOR ERRE O NÚMERO QUE O COMPUTADOR PENSOU
        else:
            print('\033[1;31m\nVocê não acertou o número que o computador pensou')

            # CONDIÇÃO PARA CASO O NÚMERO QUE O COMPUTADOR PENSOU FOR MAIOR QUE O NÚMERO QUE O JOGADOR COLOCOU
            if a > b:
                print('\n\033[1;37mO número do computador é \033[1;32mMAIOR\033[1;37m, você está perto! Tente novamente')

            # CONDIÇÃO PARA CASO O NÚMERO QUE O COMPUTADOR PENSOU FOR MENOR QUE O NÚMERO QUE O JOGADOR COLOCOU
            elif a < b:
                print('\n\033[1;37mO número do computador é \033[1;31mMENOR\033[1;37m, você está perto! Tente novamente')
    nome = nome2
# RESULTADOS FINAIS
# CONDIÇÃO PARA CASO OS DOIS JOGADORES EMPATEM
if cont1 == cont2:
    print(f'\033[1;37m{nome1} e {nome2} EMPATARAM!')
else:

    # CONDIÇÃO PARA CASO O PRIMEIRO JOGADOR GANHE
    if cont1 < cont2:
        print(f'\033[1;32m{nome1} GANHOU!')
        print(f'\033[1;31m{nome2} PERDEU!')

    # CONDIÇÃO PARA CASO O SEGUNDO JOGADOR GANHE
    else:
        print(f'\033[1;32m{nome2} GANHOU!')
        print(f'\033[1;31m{nome1} PERDEU!')
