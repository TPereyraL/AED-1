from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def filaAnteriorMasN (matriz: List[List[int]],fila: int, n: int) -> bool:
    res: bool = True
    for col in range(len(matriz[0])):
        if matriz[fila - 1][col] - n != matriz[fila][col]:
            res = False
    
    return res

def filasParecidasAanterior (matriz: List[List[int]], n: int):
    res: bool = True
    for fil in range(1,len(matriz)):
        if not filaAnteriorMasN (matriz, fil, n):
            res = False

    return res

def posibleN (matriz: List[List[int]]) -> int:
    return matriz[0][0] - matriz[1][0]

def filasParecidas(matriz: List[List[int]]) -> bool :
    n = posibleN (matriz)
    res = filasParecidasAanterior (matriz, n)
    return res


if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))