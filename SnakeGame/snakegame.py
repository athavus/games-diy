# IMPORTAÇÃO DE MÓDULOS
from freegames import square, vector
from random import randrange
from turtle import *

# DEFINIÇÃO DA MIRA DA COBRA
mira = vector(0, -10)


def ponto1(x, y):
    mira.y = y
    mira.x = x


# DEFINIÇÃO DO TAMANHO DA COBRA E DA TELA
cobra = [vector(10, 0)]


def ponto2(head):
    return -800 < head.x < 400 and -800 < head.y < 400


# DEFINIÇÃO DA FORMA E TAMANHO DA COMIDA, RANDOMIZAÇÃO DO SPAWN TAMBÉM
comida = vector(0, 0)


def ponto3():
    head = cobra[-1].copy()
    head.move(mira)

    if not ponto2(head) or head in cobra:
        square(head.x, head.y, 9, 'red')
        update()
        return

    cobra.append(head)

# DEFINIÇÃO DE QUANDO A COBRA COMER ALGUMA COMIDA
    if head == comida:
        print('Snake:', len(cobra))
        comida.x = randrange(-15, 15) * 10
        comida.y = randrange(-15, 15) * 10
    else:
        cobra.pop(0)

    clear()
# DEFINIÇÃO DAS CORES E DA MORTE DA COBRA
    for body in cobra:
        square(body.x, body.y, 9, 'green')

    square(comida.x, comida.y, 9, 'red')
    update()
    ontimer(ponto3, 100)


# DEFINIÇÃO DAS TECLAS PRA MOVIMENTAÇÃO DA COBRA
hideturtle()
tracer(False)
listen()
onkey(lambda: ponto1(0, 10), 'Up')
onkey(lambda: ponto1(0, -10), 'Down')
onkey(lambda: ponto1(-10, 0), 'Left')
onkey(lambda: ponto1(10, 0), 'Right')
ponto3()
done()
