apariciones :: Integer -> [Integer] -> Integer
apariciones _ [] = 0
apariciones e (x:xs) | x == e = 1 + apariciones e xs
                     | otherwise = apariciones e xs

repeticiones :: [Integer] -> [Integer] -> [(Integer, Integer)]
repeticiones [] _ = []
repeticiones (x:xs) s = (x,(apariciones x s) - 1) : repeticiones xs s

contarRepetidos :: [Integer] -> [(Integer, Integer)]
contarRepetidos s = repeticiones (eliminarRepetidos s) s

eliminarRepetidos :: [Integer] -> [Integer]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos((quitarTodos x xs))

quitarTodos :: Integer -> [Integer] -> [Integer]
quitarTodos _ [] = []
quitarTodos e (x:xs) | e == x = quitarTodos e xs
                     | otherwise = x : (quitarTodos e xs)

eliminarYContarRepetidos :: [Integer] -> ([Integer],[(Integer, Integer)])
eliminarYContarRepetidos s = (eliminarRepetidos s, contarRepetidos s)