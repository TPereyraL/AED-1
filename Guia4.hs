


-- Ejercicio 1

fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci (n - 1) + fibonacci (n - 2)


-- Ejercicio 2

parteEntera :: Float -> Integer
parteEntera x | x > -1 && x < 1 = 0
              | x > 0 = parteEntera (x - 1) + 1
              | otherwise = parteEntera (x + 1) - 1


-- Ejercicio 3

esDivisible :: Integer -> Integer ->Bool
esDivisible a b | a == 0 = True
                | a < b = False
                | otherwise = esDivisible (a - b) b


-- Ejercicio 4

sumaImpares :: Integer -> Integer
sumaImpares n | n == 0 = 0
              | otherwise = sumaImpares(n - 1) + (n * 2 - 1)


-- Ejercicio 5

medioFact :: Integer -> Integer
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = medioFact (n - 2) * n

-- Ejercicio 6

sumaDigitos :: Integer -> Integer
sumaDigitos n | n == 0 = 0
              | otherwise = mod n 10 + sumaDigitos (div n 10)


-- Ejercicio 7

todosDigitosIguales :: Integer -> Bool
todosDigitosIguales n | sacarUltimoDigi n == 0 = True
                      | mod (sacarUltimoDigi n) 10 /= mod n 10 = False
                      | otherwise = todosDigitosIguales (sacarUltimoDigi n)
                      where sacarUltimoDigi n = div n 10
                

-- Ejercicio 8

cantDigitos :: Integer -> Integer
cantDigitos n | n < 10 = 1
              | otherwise = 1 + cantDigitos (div n 10)

ultimoDigito :: Integer -> Integer
ultimoDigito n = mod n 10

sacarUltimo :: Integer -> Integer
sacarUltimo n = div n 10

iesimoDigito :: Integer -> Integer -> Integer
iesimoDigito n i | cantDigitos n == i = ultimoDigito n
                 | otherwise = iesimoDigito (sacarUltimo n) i


-- Ejercicio 9

sacarPrimer :: Integer -> Integer
sacarPrimer n = n - ((iesimoDigito n 1) * 10 ^ (cantDigitos n))

esCapicua :: Integer -> Bool
esCapicua n | cantDigitos n < 2 = True
            | iesimoDigito n 1 == ultimoDigito n = esCapicua (sacarUltimo(sacarPrimer n))
            | otherwise = False


-- Ejercicio 10
 
-- a --
f1 :: Integer -> Integer
f1 n | n == 0 = 1
     | otherwise = 2 ^ n + f1 (n - 1)

-- b --
f2 :: Integer -> Float -> Float
f2 n q | n == 1 = q
       | otherwise = q ^ n + f2 (n - 1) q

-- c --
f3 :: Integer -> Float -> Float
f3 n q | n == 0 = 0
       | otherwise = q ^ (2 * n) + q ^ (2 * n - 1) + f3 (n - 1) q

-- d --
f4 :: Integer -> Float -> Float
f4 n q | n == 0 = 1
       | otherwise = q ^ (2 * n) + q ^ (2 * n -1) - q ^ (n - 1) + f4 (n - 1) q


-- Ejercicio 11

factorial :: Integer -> Integer
factorial n | n == 0 = 1
            | otherwise = n * factorial (n - 1)

eAprox :: Integer -> Float
eAprox n | n == 0 = 1
         | otherwise = (1 / (fromIntegral (factorial n) :: Float)) + eAprox (n - 1)


-- Ejercicio 12

recursion :: Integer -> Float
recursion n | n == 1 = 2
            | otherwise = 2 + (1 / (recursion (n - 1)))

raizDe2Aprox :: Integer ->Float
raizDe2Aprox n | n == 1 = 1
               | otherwise = (recursion n) - 1
       

-- Ejercicio 13

f13 :: Integer -> Integer -> Integer
f13 n m | n == 0 = 0
        | otherwise = sumaInternaF13 n m + f13 (n - 1) m

sumaInternaF13 :: Integer -> Integer -> Integer
sumaInternaF13 n m | m == 1 = n
                   | otherwise = n ^ m + sumaInternaF13 n (m - 1)

-- Ejercicio 14

{-
-- Version uno; sumatorias separadas

sumatoria :: Integer -> Integer -> Integer
sumatoria _ 0 = 0
sumatoria q n = q ^ n + sumatoria q (n - 1)


sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m = sumatoria q n * sumatoria q m
-}


-- Version dos; sumatorias juntas

sumaPotencias :: Integer -> Integer -> Integer -> Integer
sumaPotencias q n m | n == 0 = 0				   						
                    | otherwise = sumaInterna14 q n m + sumaPotencias q (n - 1) m

sumaInterna14 :: Integer -> Integer -> Integer -> Integer
sumaInterna14 q n m | m == 0 = 0
                  | otherwise = q ^ (n + m) + sumaInterna14 q n (m - 1)


-- Ejercicio 15

sumaRacionales :: Integer -> Integer -> Float
sumaRacionales n m | n == 0 = 0
                   | otherwise = sumaInternaQ n m + sumaRacionales (n - 1) m

sumaInternaQ :: Integer -> Integer -> Float
sumaInternaQ n m | m == 1 = (fromIntegral n :: Float)
                 | otherwise = ((fromIntegral n :: Float) / (fromIntegral m :: Float)) + sumaInternaQ n (m - 1)


-- Ejercicio 16 

-- a --

menorDivisor :: Integer -> Integer
menorDivisor n = minDivAux n 2

minDivAux :: Integer -> Integer -> Integer
minDivAux n i | mod n i == 0 = i
              | otherwise = minDivAux n (i + 1)

-- b --

esPrimo :: Integer -> Bool
esPrimo n = menorDivisor n == n

-- c --

sonCoprimos :: Integer -> Integer -> Bool
sonCoprimos n m = minComunDenom n m == 1

minComunDenom :: Integer -> Integer -> Integer
minComunDenom n m | m == 0 = n
                  | otherwise = minComunDenom m (mod n m)
{- Este último algoritmo calcula hasta que los restos den 0;
si te queda m mayor que n lo rota en la siguiente recursión-}

-- d --

nEsimoPrimo :: Integer -> Integer
nEsimoPrimo 1 = 2
nEsimoPrimo n = siguientePrimo (nEsimoPrimo (n - 1))

siguientePrimo :: Integer -> Integer
siguientePrimo n | esPrimo (n + 1) = n + 1
                 | otherwise = siguientePrimo (n + 1)

{-
nEsimoPrimo :: Integer -> Integer
nEsimoPrimo n = nEsimoPrimoAux 1 2
  where nEsimoPrimoAux i p | i == n = p
                           | esPrimo (p + 1) = nEsimoPrimoAux (i + 1) (p + 1)
                           | otherwise = nEsimoPrimoAux i (p + 1)
{- Este último es cortesía de chatGPT -}
-}

-- Ejercicio 17

esFibonacci :: Integer -> Bool
esFibonacci n | n == 1 = True
              | 