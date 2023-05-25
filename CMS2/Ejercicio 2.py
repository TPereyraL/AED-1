import sys

def n_fibonaccis(n: int) -> list:
    fibonacci2: int = 1
    fibonacci1: int = 0
    fibonaccis: list = [0,1]
    for i in range(n - 2):
        fibonacci = fibonacci1 + fibonacci2
        fibonacci1 = fibonacci2
        fibonacci2 = fibonacci
        fibonaccis.append(fibonacci)

    return fibonaccis

print('Los primeros 10 fibonaccis son:', n_fibonaccis(10))
print('La longitud de la lista es:', len(n_fibonaccis(10)))

def fibonacciNoRecursivo(n: int) -> int:
    fibonaccis = n_fibonaccis(n + 1)
    res = fibonaccis[n]
    return res


print('El primer fibonacci es', fibonacciNoRecursivo(1))