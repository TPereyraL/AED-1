import sys

def gana(j1: str, j2: str) -> bool:
    if (j1 == 'Piedra' and j2 == 'Tijera') or (j1 == 'Tijera' and j2 == 'Papel') or (j1 == 'Papel' and j2 == 'Piedra'):
       res = True
    else: res = False

    return res

def quienGana(j1: str, j2: str) -> str :
    if gana (j1,j2):
        res = 'Jugador1'
    elif gana(j2,j1):
        res = 'Jugador2'
    else:
        res = 'Empate'

    ganador : str = ''

    return res


print('Piedra, papel o tijera:')
j1 = 'Tijera'
j2 = 'Piedra'
print('Si el Jugador1 juega',j1,'y Jugador2 juega',j2 + ':\nEntonces el ganador es:',quienGana(j1,j2))