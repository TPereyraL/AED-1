-- Ejercicio 1 --

-- 1
longitud :: [t] -> Integer
longitud [] = 0
longitud (x : xs) = 1 + longitud xs


-- 2
ultimo :: [t] -> t
ultimo (x : []) = x
ultimo (x : xs) = ultimo xs


-- 3
principio :: [t] -> [t]
principio [a] = []
principio (x : xs) = x : principio xs


--4
reverso:: [t] -> [t]
reverso [] = []
reverso (x : xs) = reverso xs ++ [x]


-- Ejercicio 2 --

-- 1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece x (y : ys) | x == y = True
                     | otherwise = pertenece x ys


-- 2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [a] = True
todosIguales (x : xs) | x /= head xs = False
                      | otherwise = todosIguales xs


-- 3 
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [a] = True
todosDistintos (x : xs) | pertenece x xs = False
                        | otherwise = todosDistintos xs


-- 4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos x = not (todosDistintos x)


-- 5 
quitar :: (Eq t) => t -> [t] -> [t]
quitar x (y : ys) | not (pertenece x (y : ys)) = (y : ys)
                  | x == y = ys
                  | otherwise = y : quitar x ys


-- 6
quitarTodos :: (Eq t) => t -> [t] -> [t]
quitarTodos _ [] = []
quitarTodos x y | quitar x y == y = y
                | otherwise = quitarTodos x (quitar x y)


-- 7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x : xs) = x : eliminarRepetidos (quitarTodos x xs)


-- 8
mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] _ = True
mismosElementos (x :xs) y | not (pertenece x y) = False
                          | otherwise = mismosElementos xs y


-- 9 
capicua :: (Eq t) => [t] -> Bool
capicua (x : xs) | longitud (x : xs) < 2 = True
                 | x /= ultimo xs = False
                 | otherwise = capicua (principio xs) 



-- Ejercicio 3 --

-- 1
sumatoria :: [Integer] -> Integer
sumatoria [] = 0
sumatoria (x :xs) = x + sumatoria xs


-- 2
productoria :: [Integer] -> Integer
productoria [] = 1
productoria (x : xs) = x * productoria xs 


-- 3
maximo :: [Integer] -> Integer
maximo (x : xs) | xs == [] = x
                | x >= (head xs) = maximo (x : (tail xs))
                | x < (head xs) = maximo xs


-- 4
sumarN :: Integer -> [Integer] -> [Integer]
sumarN n (x : xs) | (x : xs) == [] =[]
                  | otherwise = (x + n) : sumarN n xs


-- 9
ordenar :: [Integer] -> [Integer]
ordenar x | x == [] = []
          | otherwise (quitar (maximo x)) ++ [maximo x]
            

-- Ejercicio 4 --

-- 4
palabras :: [Char] -> [[Char]]
palabras [] = []
palabras x = primeraPalabra x : palabras (quitarPrimeraPalabra x)

primeraPalabra :: [Char] -> [Char]
primeraPalabra [] = []
primeraPalabra (x : xs) | x /= '' = x : primeraPalabra xs
                        | otherwise = []

quitarPrimeraPalabra :: [Char] -> [Char]
quitarPrimeraPalabra [] = []
quitarPrimeraPalabra (x : xs) | x /= '' = quitarPrimeraPalabra xs
                              | otherwise = xs


-- 5
aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x : xs) = x ++ aplanar xs


-- Ejercicio 5 --