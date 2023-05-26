from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
    repeticiones : int = 1
    masRepeticiones: int = 1
    for i in range(len(l) - 1):
        if l[i] == l[i + 1]:
            repeticiones += 1
            
        else:
            if repeticiones > masRepeticiones:
                masRepeticiones = repeticiones

            repeticiones = 1
    if repeticiones > masRepeticiones:
        masRepeticiones = repeticiones

    if l == []:
        masRepeticiones = 0

    return masRepeticiones

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))