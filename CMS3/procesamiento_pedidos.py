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

        #si esta en los productos del stock
        else:
            if stock[product] < products[product]:
                status = 'incompleto' 
                #productos y stock es modificado (inout)
                products[product] = stock[product]

                stock[product] = 0

            #si hay stock suficiente
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
        pedidos_precesados.append(procesado_pedido(pedidos.get(),stock_productos,precios_productos))
  
    return pedidos_precesados


if __name__ == '__main__':
  pedidos: Queue = Queue()
  list_pedidos = json.loads(input())
  [pedidos.put(p) for p in list_pedidos]
  stock_productos = json.loads(input())
  precios_productos = json.loads(input())
  print("{} {}".format(procesamiento_pedidos(pedidos, stock_productos, precios_productos), stock_productos))

# Ejemplo input  
# pedidos: [{"id":21,"cliente":"Gabriela", "productos":{"Manzana":2}}, {"id":1,"cliente":"Juan","productos":{"Manzana":2,"Pan":4,"Factura":6}}]
# stock_productos: {"Manzana":10, "Leche":5, "Pan":3, "Factura":0}
# precios_productos: {"Manzana":3.5, "Leche":5.5, "Pan":3.5, "Factura":5}