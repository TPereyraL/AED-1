-- Ejercicio 4 --

main :: IO()
main = do {
  x <- readLn ;
  print(sumaPrimerosNImparesEspecial(x ::(Integer)))
  }

-- Implementación de especificación --
sumaPrimerosNImparesEspecial :: Integer -> Integer
sumaPrimerosNImparesEspecial n | n == 1 = 4
                       | otherwise = (4 * n) + sumaPrimerosNImparesEspecial (n - 1)

{- Analicé como progresaba la secuencia de la sumatoria y encontré que se trataba de;
 4 * n + 4 * (n-1) + ... + 4 * 1; 
 entonces utilice esa recursión con n == 1 -> 4 como caso base. 
 -}