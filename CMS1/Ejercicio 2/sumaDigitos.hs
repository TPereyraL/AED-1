-- Ejercicio 2 --

main :: IO()
main = do {
  x <- readLn ;
  print(sumaDigitos(x ::(Int)))
  }

-- Función principal que devuelve la suma de cada digito del número --
sumaDigitos :: Int -> Int
sumaDigitos n | n == 0 = 0
              | otherwise = mod n 10 + sumaDigitos (div n 10)
