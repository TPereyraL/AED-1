from queue import Queue
from typing import List
from typing import Dict
from typing import Union
import json



def stock_check (products: Dict [str,int], stock: Dict[str, int]) -> str:
    status: str =  'completo'
    
    shop_list: list[str] = list(products.keys())
    product_stock: list[str] = list(stock.keys())
    
    for product in shop_list: 
        
        if not (product in product_stock):
            status =  'incompleto'
            #products es modificado (inout)
            products[product] = 0

        else:
            if stock[product] < products[product]:
                status = 'incompleto' 
                #productos y stock es modificado (inout)
                products[product] = stock[product]

                stock[product] = 0


            else:
                #stock es modificado (inout)
                left: int = stock[product] - products[product]
                stock[product] = left


        
    return status

def budget(products: Dict[str, int], prices: Dict[str, float]) -> float:
    total: float = 0
    shop_list: list[str] = list(products.keys())

    for product in shop_list:
        if products[product] != 0:
            total = total + (float(products[product]) * prices[product])

    return total

def procesado_pedido(pedido: Dict,
                     stock: Dict[str, int],
                     precios: Dict[str, float]) -> Dict:
    pedido_procesado: Dict = pedido
    estados = stock_check(pedido_procesado['productos'], stock)
    pedido_procesado['precio_total'] = budget(pedido_procesado['productos'], precios)
    pedido_procesado['estado'] = estados


    return pedido_procesado


# ACLARACIÓN: El tipo de "pedidos" debería ser: pedidos: Queue[Dict[str, Union[int, str, Dict[str, int]]]]
# Por no ser soportado por la versión de CMS, usamos simplemente "pedidos: Queue"
def procesamiento_pedidos(pedidos: Queue,
                          stock_productos: Dict[str, int],
                          precios_productos: Dict[str, float]) -> List[Dict[str, Union[int, str, float, Dict[str, int]]]]:
    pedidos_precesados: List[Dict[str, Union[int, str, float, Dict[str, int]]]] = []
    
    while not pedidos.empty():
        pedido = pedidos.get()
        print('Pedido sin procesar:\n',pedido)
        pedidos_precesados.append(procesado_pedido(pedido,stock_productos,precios_productos))
        print('Pedido procesado:\n',pedido)
        print('Stock Despues:\n', stock_productos)
  
    return pedidos_precesados


#Testing
pedidos = Queue()

pedido1 = {
    'id': 21,
    'cliente': 'Gabriela',
    'productos': {'Manzana': 2}
}
print('Pedido 1:')
print(pedido1)
pedidos.put(pedido1)

pedido2 = {
    'id': 1,
    'cliente': 'Juan',
    'productos': {'Manzana': 2, 'Pan': 4, 'Factura': 6}
}
print('Pedido 2:')
print(pedido2)
pedidos.put(pedido2)

pedido3 = {
    'id': 3,
    'cliente': 'Pedro',
    'productos': {'Naranja': 3, 'Leche': 1}
}
print('Pedido 3:')
print(pedido3)
pedidos.put(pedido3)

pedido4 = {
    'id': 4,
    'cliente': 'María',
    'productos': {'Manzana': 1, 'Banana': 5, 'Yogur': 2}
}
print('Pedido 4:')
print(pedido4)
pedidos.put(pedido4)

pedido5 = {
    'id': 5,
    'cliente': 'Laura',
    'productos': {'Pan': 3, 'Lechuga': 2, 'Tomate': 4, 'Sandia': 1}
}
print('Pedido 5:')
print(pedido5)
pedidos.put(pedido5)


stock_productos = {
    'Manzana': 8,
    'Pan': 10,
    'Factura': 5,
    'Naranja': 6,
    'Leche': 3,
    'Banana': 7,
    'Yogur': 4,
    'Lechuga': 2,
    'Tomate': 9
}

precios_productos = {
    'Manzana': 2.5,
    'Pan': 1.5,
    'Factura': 2.0,
    'Naranja': 1.0,
    'Leche': 3.0,
    'Banana': 0.5,
    'Yogur': 1.8,
    'Lechuga': 0.75,
    'Tomate': 0.9
}


print('Stock Antes:\n', stock_productos)
procesamiento_pedidos(pedidos, stock_productos, precios_productos)
