-- Ejercicio 1 --

main :: IO ()
main = do
  x <- readLn
  print (sumaMenosQueMax (x :: (Integer, Integer, Integer)))

-- Función principal que devuelve el Booleano de la inecuación --
sumaMenosQueMax :: (Integer, Integer, Integer) -> Bool
sumaMenosQueMax (t0, t1, t2) = maximo (t0, t1, t2) > minimo (t0, t1, t2) + medio (t0, t1, t2)


-- Función que devuelve el valor más alto de la tupla --
maximo :: (Integer, Integer, Integer) -> Integer
maximo (a, b, c) | (a > b) && (a > c) = a
                 | (b > a) && (b > c) = b
                 | otherwise = c

-- Función que devuelve el valor más bajo de la tupla --
minimo :: (Integer, Integer, Integer) -> Integer
minimo (a, b, c) | (a < b) && (a < c) = a
              | (b < a) && (b < c) = b
              | otherwise = c

-- Función que devuelve el valor medio de la tupla --
medio :: (Integer, Integer, Integer) -> Integer
medio (a, b, c) | ((b <= a) && (a <= c)) || ((c <= a) && (a <= b)) = a
                | ((a <= b) && (b <= c)) || ((c <= b) && (b <= a)) = b
                | otherwise = c

