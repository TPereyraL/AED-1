-- Ejercicio 3 --

main :: IO()
main = do {
  x <- readLn ;
  print(prod(x ::(Integer)))
  }

-- Implementación de especificación --
prod :: Integer -> Integer
prod n | n == 0 = 1
       | otherwise = 4 * n * (4 * (n ^ 3 + n ^ 2) - (n + 1)) * prod (n - 1)
       
{- Analicé como progresaba la secuencia de la productoria y encontré una formula general de la sucesión con una recursión. -}