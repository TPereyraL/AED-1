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

    else:
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
        if i[0] == 'I':
            saldo += i[1]

        else:
            saldo -= i[1]

    return saldo

print ('\n 8.')
mov = [('I',1200),('I',1800),('R',850),('I',400),('',1370)]
print ('Si los movimientos fueron:',mov)
print ('El slado en cuenta sera de:',saldo (mov))


# 9.
def tres_vocales_distintas (p : str) -> bool:
    if 