-- Ejercicio 5 --

main :: IO()
main = do {
  x <- readLn ;
  print(combinacionesMenoresOIguales(x ::(Integer)))
  }

-- Implementación de especificación --
combinacionesMenoresOIguales :: Integer -> Integer
combinacionesMenoresOIguales n = sumaExterna 1
  where
    sumaExterna i | i > n     = 0
               | otherwise = sumaInterna i 1 + sumaExterna (i + 1)

    sumaInterna i j | i * j <= n = 1 + sumaInterna i (j + 1)
                 | otherwise  = 0

{- Utilicé una recursión ascendente que se detiene con el caso que el indice de la suma externa alcanza el valor tope;
utilizo where en lugar de funciones diferentes ya que debo volver al valor n original en cada una de las etapas del programa;
recorre todos los productos para i valor fijo recorriendo cada j y termina en el ultimo j maximo que cumple la condición;
luego le suma un valor al i y repite el paso anterior.
-}