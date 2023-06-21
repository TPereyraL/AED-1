from queue import Queue
from typing import Dict


def tiempos_atencion(cajas: Dict[str, Dict[str,int]], caja) -> bool:
  res: bool = False
  if caja == 'Caja1':
    if cajas[caja]['tiempo'] == 9:
      res = True
      cajas[caja]['tiempo'] = 0
    
    else:
      cajas[caja]['tiempo'] += 1
  
  elif caja == 'Caja2' or caja == 'Caja3':
    if cajas[caja]['tiempo'] == 3:
      res = True
      cajas[caja]['tiempo'] = 0
    
    else:
      cajas[caja]['tiempo'] += 1

  return res
    
    


def cajas_update(cajas: Dict[str, Dict[str,int]], min: int, fila: Queue):

  keys = cajas.keys()
  for caja in keys:
    caja_libre: bool = cajas[caja]['cliente'] == 0

    if not caja_libre:
      tiempo_cumplido: bool = tiempos_atencion(cajas, caja)
      if tiempo_cumplido:
        if caja == 'Caja3':
          fila.put(cajas[caja]['cliente'])
        cajas[caja]['cliente'] = 0
    



# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
  cajas: Dict[str, Dict[str, int]] = {'Caja1': 
                                        {'cliente': 0, 'tiempo': 0},
                                     'Caja2': 
                                        {'cliente': 0, 'tiempo': 0},
                                     'Caja3': 
                                        {'cliente': 0, 'tiempo': 0}}

  for i in range(min + 1):

    clientes: int = fila.qsize()
    for cliente in range(clientes):
      
      if cajas['Caja1']['cliente'] == 0:
        cajas['Caja1']['cliente'] = fila.get()

      if cajas['Caja2']['cliente'] == 0 and i > 2:
        cajas['Caja2']['cliente'] = fila.get()

      if cajas['Caja3']['cliente'] == 0 and i > 1:
        cajas['Caja3']['cliente'] = fila.get()
    
    cajas_update(cajas, i, fila)
    

cajas: Dict[str, Dict[str,int]] = {'Caja1': 
                                        {'cliente': 0, 'tiempo': 0},
                                     'Caja2': 
                                        {'cliente': 0, 'tiempo': 0},
                                     'Caja3': 
                                        {'cliente': 0, 'tiempo': 0}}

fila = Queue()

print('Fila al iniciar:\n[1,2,3,4]')
fila.put(1)
fila.put(2)
fila.put(3)
fila.put(4)

min = 10
avanzarFila(fila,min)

print('Fila a los', min, 'minutos:')
for i in range(fila.qsize()):
  print(fila.get())