from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def input_a_tupla(vuelos: str) -> List[Tuple[str, str]]:
    return [tuple(vuelo.split(',')) for vuelo in vuelos.split()]

def vuelo_del_origen(origen: str,vuelos: List[Tuple[str, str]]) -> Tuple[str,str]:
    res = ('no', 'no')
    for i in vuelos:
        if origen == i[0]:
            res = i

    return res



def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
    res: int = -1
    nro_vuelos: int = 0
    vuelo = vuelo_del_origen(origen,vuelos)
    while nro_vuelos <= len(vuelos) and vuelo[1] != destino:
        if vuelo[1] != destino:
            vuelo = vuelo_del_origen(vuelo[1],vuelos)
            nro_vuelos += 1
        
        else:
            res = nro_vuelos + 1

    return res

origen = input('Ingrese el origen: ')
destino = input('Ingrese el destino: ')
vuelos = input_a_tupla(input('Ingrese los vuelos: '))
print ('La cantidad de vuelos sera:',sePuedeLlegar(origen,destino,vuelos))