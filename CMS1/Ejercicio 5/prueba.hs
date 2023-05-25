combinations :: Int -> Int
combinations n = outerSum 1
  where
    outerSum i
      | i > n     = 0
      | otherwise = innerSum i 1 + outerSum (i + 1)

    innerSum i j
      | i * j <= n = 1 + innerSum i (j + 1)
      | otherwise  = 0
