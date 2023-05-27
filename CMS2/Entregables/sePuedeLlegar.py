from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def vuelo_origen (origen: str, vuelos: List[Tuple[str, str]]) -> Tuple[bool, Tuple[str, str]]:
    res: bool = False
    vueloDeOrigen: Tuple[str, str] = ('0','0')
    for vuelo in vuelos:
        if vuelo[0] == origen:
            vueloDeOrigen = vuelo
            res = True
    return (res, vueloDeOrigen)


def ruta (origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> List[Tuple[str, str]]:
    ruta: List[Tuple[str, str]] = []
    while vuelo_origen(origen, vuelos)[0]:
        ruta.append(vuelo_origen(origen, vuelos)[1])
        if ruta[len(ruta) - 1][1] != destino:
            origen = vuelo_origen(origen, vuelos)[1][1]
        
        else:
            origen = 'none'

    if ruta[len(ruta) - 1][1] != destino:
        ruta = []
    return ruta

   


def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :
    if len(ruta(origen, destino, vuelos)) == 0:
        res = -1
    else:
        res = len(ruta(origen, destino, vuelos))
    return res

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))