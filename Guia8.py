# Ejercicio 1
print ('Ejercicio 1')

# 1.
def pertenece (s: list,e: int) -> bool:
    res = False
    for i in s:
        if e == i:
            res = True
    
    return res

s : list = [2,5,3,8,0,6]

print ('\n 1.')
print ('Si s es:',s)
print ('El', 3, 'perteneces a s?', pertenece (s,3))
print ('El', 4, 'perteneces a s?', pertenece (s,4))


# 2.
def divideATodos (s: list, e: int) -> bool:
    res = True
    for i in s:
        if i % e != 0:
            res = False

    return res

s : list = [2,4,6,10]

print ('\n 2.')
print ('Si s es:',s)
print ('El', 3, 'divide a todos los numeros de s?', divideATodos (s,3))
print ('El', 2, 'divide a todos los numeros de s?', divideATodos (s,2))


# 3.
def sumaTotal (s: list) -> int:
    suma = 0
    for i in s:
        suma += i

    return suma

s : list = [1,4,5,6,2,3]

print ('\n 3.')
print ('Si s es:',s)
print ('La suma de todos los elementos de s es:', sumaTotal(s) )


# 4.
def ordenados (s : list) -> bool:
    res = True
    for i in range(len(s) - 1):
        if s[i] >= s[i+1]:
            res = False
    
    return res

print ('\n 4.')

s : list = [1,3,5,6]
print ('Si s es:',s)
print ('Esta ordenada s?', ordenados (s))

s : list = [1,3,5,6,2]
print ('Si s es:',s)
print ('Esta ordenada s?', ordenados (s))


# 5.
def longitud_mayor_a_7 (s : list) -> bool:
    res = False
    for i in s:
        if len(i) > 7:
            res = True
    
    return res

print ('\n 5.')
s : list = ['Hola', 'Estacion', 'Pala']
print ('Si s es:',s)
print ('s tiene una palabra de mas de 7 letras?', longitud_mayor_a_7(s))

s : list = ['Hola', 'Palabra', 'Pala']
print ('Si s es:',s)
print ('s tiene una palabra de mas de 7 letras?', longitud_mayor_a_7(s))


# 6.
def es_palindroma (f : str) -> bool:
    if f == f[::-1]:
        res = True
    
    else:
        res = False
    
    return res


print ('\n 6.')
f : str = 'neuquen ama neuquen'
print ('Si la frase es:',f)
print ('Es palindromo?',es_palindroma (f))

f : str = 'esta lloviendo'
print ('Si la frase es:',f)
print ('Es palindromo?',es_palindroma (f))


# 7.
def valid_password (password : str) -> str:
    if len (password) > 8:
        if not password.islower():
            if not password.isupper():
                if not password.isalpha():
                    return 'VERDE'
    
    elif len (password) < 5:
        return 'ROJA'

    return 'AMARILLA'


print ('\n 7.')
password : str = 'Zapatilla01'
print ('Si la contraseña es:',password)
print (valid_password (password))

password : str = 'Zap2'
print ('Si la contraseña es:',password)
print (valid_password (password))

password : str = 'zapato3'
print ('Si la contraseña es:',password)
print (valid_password (password))


# 8.
def saldo (mov : list) -> float:
    saldo = 0
    for i in mov:
        if i[0] == 'C':
            saldo += i[1]

        else:
            saldo -= i[1]

    return saldo

print ('\n 8.')
mov = [('C',1200),('C',1800),('D',850),('C',400),('D',1370)]
print ('Si los movimientos fueron:',mov)
print ('El saldo en cuenta sera de:',saldo (mov))


# 9.
def vocales_dif (p : str) -> bool:
    vocales: list = ['A','E','I','O','U']
    palabra: str = p.upper()
    
    for i in range(len(palabra)):
        if palabra[i] in vocales:
            if len(vocales) > 3:
                vocales.remove(palabra[i])

    if len(vocales) <= 3:
        res = True

    else:
        res = False

    return res


print ('\n 9.')
p = 'Palabras'
print ('Si la palabra es:', p)
print ('Entonces la palabra tiene mas de tres vocales:', vocales_dif(p))

p = 'Maravilloso'
print ('Si la palabra es:', p)
print ('Entonces la palabra tiene mas de tres vocales:', vocales_dif(p))


#Ejercicio 2
print ('\nEjercicio 2')

# 1.
def pares_por_ceros (lista : list):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista[i] = 0
        
print ("\n 1.")

lista: list = [1,2,3,4,5,6]
print ("Si la lista es:", lista)
pares_por_ceros (lista)
print ("La lista pares por ceros sera:", lista)


# 2.
def pares_por_ceros_out (lista : list) -> list:
    lista_new: list = lista.copy()
    for i in range(len(lista)):
        if lista_new[i] % 2 == 0:
            lista_new[i] = 0
    
    return lista_new

print ("\n 2.")

lista: list = [1,2,3,4,5,6]
print ("Si la lista es:", lista)
print ("La lista pares por ceros sera:", pares_por_ceros (lista))


# 3.
def sin_vocales (p : str) -> str:
    p_mayus : str = p.upper()
    res : str = ""
    vocales : list = ['A','E','I','O','U']
    for i in range(len(p)):
        if not (p_mayus[i] in vocales):
            res = res + (p[i])
        
    return res

print ("\n 3.")

p : str = "Salamin"
print ("Si la cadena es:", p)
print ("La cadena sin vocales sera:", sin_vocales(p))


# 4.
def reemplazaVocales (p : str) -> str:
    p_mayus : str = p.upper()
    res : str = ""
    vocales : list = ['A','E','I','O','U']
    for i in range(len(p)):
        if not (p_mayus[i] in vocales):
            res = res + (p[i])
        else:
            res = res + "_"
    
    return res

print ("\n .")

p : str = "Reemplazar"
print ("Si la cadena es:", p)
print ("La cadena sin vocales sera:", reemplazaVocales(p))


# 5.
def daVueltaStr (p : str) -> str:
    res : str = ""
    for i in range(1,len(p) + 1):
        res = res + p[len(p) - i]

    return res


print ('\n 5.')
f : str = 'neuquen ama neuquen'
print ('Si la frase es:',f)
print ('Dada vuelta:',daVueltaStr (f))

f : str = 'esta lloviendo'
print ('Si la frase es:',f)
print ('Dada vuelta:',daVueltaStr (f))


#Ejercicio 3
print ('\nEjercicio 3')

# 1.
def lista_estudiantes () -> list:
    lista : list = []
    nombre: str = input('Ingrese el nombre del alumno ("listo" para terminar):')

    while nombre != 'listo':
        lista.append(nombre.capitalize())
        nombre = input('Ingrese el nombre del alumno ("listo" para terminar):')

    return lista


print ('\n 1.')
lista : list = lista_estudiantes ()
print ('Los estudiantes son:', lista)


# 2.
def movimientos () -> list:
    movimientos : list = []
    movimiento : str = input('Ingrese la operacion (“C” = Cargar, “D” = Descontar, “X” = Finalizar): ').upper()
    monto : float = 0

    while movimiento != 'X':
        if movimiento == 'C':
            monto = float(input('Ingrese el monto que desea cargar: '))
            movimientos.append(('C',monto))

        else:
            monto = float(input('Inrese el monto a descontar: '))
            movimientos.append(('D',monto))
        
        movimiento = input('Ingrese la operacion (“C” = Cargar, “D” = Descontar, “X” = Finalizar): ').upper()
    return movimientos

print ('\n 2.')
mov = movimientos()
print ('Si los movimientos fueron:', mov)
print ('El saldo en cuenta sera de:',saldo (mov))


import random
# 3.
def siete_y_medio ():
    cartas : list = []
    decide : str = input('Desea comenzar sacando o plantarse sin jugar (s/p): ').upper()
    
    while decide != 'P':
        carta = random.randint(1,12)
        while carta == 8 or carta == 9:
            carta = random.randint(1,12)

        if carta < 10:
            cartas.append(carta)
        else:
            cartas.append(0.5)
        
        print ('La carta es:',carta)
        
        decide : str = input('Desea seguir sacando o plantarse (s/p): ').upper()
    
    carta = random.randint(1,12)
    while carta == 8 or carta == 9:
        carta = random.randint(1,12)

    if carta < 10:
            cartas.append(carta)
    else:
        cartas.append(0.5)
    
    print ('La última carta es:',carta)

    if sumaTotal(cartas) <= 7.5:
        print('Felicitaciones, ganaste.')

    else:
        print('Perdiste huevon.')

print ('\n 3.')
print ('Juguemos al siete y medio!')
siete_y_medio()

