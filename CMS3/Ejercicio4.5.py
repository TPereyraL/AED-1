from queue import Queue
from typing import Dict

def open(caja, minuto) -> bool:
  res: bool = True
  if caja == 'Caja1' and minuto < 1:
    res = False
  elif caja == 'Caja3' and minuto < 2:
    res = False
  elif caja == 'Caja2' and minuto < 3:
    res = False
  
  return res


def asignacion_caja (cajas: Dict[str, Dict[str, int]],fila: Queue, minuto: int):
  keys = cajas.keys()
  for caja in keys:
    caja_abierta: bool = open(caja, minuto)
    caja_disponible: bool = cajas[caja]['cliente'] == 0
    hay_fila: bool = not fila.empty()

    if caja_abierta and caja_disponible and hay_fila:
        cajas[caja]['cliente'] = fila.get()

def tiempos_atencion(cajas):
  keys = cajas.keys()
  for caja in keys:
    caja_ocupada: bool = cajas[caja]['cliente'] != 0
    if caja_ocupada:
      cajas[caja]['tiempo'] += 1


def continua_atencion(cajas, fila):
  keys = cajas.keys()
  for caja in keys:
    tiempo_atendido: int = cajas[caja]['tiempo']
    if caja == 'Caja1' and tiempo_atendido == 10:
      cajas[caja]['cliente'] = 0
      cajas[caja]['tiempo'] = 0

    elif caja == 'Caja2' and tiempo_atendido == 4:
      cajas[caja]['cliente'] = 0
      cajas[caja]['tiempo'] = 0
    
    elif caja == 'Caja3' and tiempo_atendido == 4:
      fila.put(cajas[caja]['cliente'])
      cajas[caja]['cliente'] = 0
      cajas[caja]['tiempo'] = 0

# El tipo de fila debería ser Queue[int], pero la versión de python del CMS no lo soporta. Usaremos en su lugar simplemente "Queue"
def avanzarFila(fila: Queue, min: int):
  minuto: int = 0
  cajas: Dict[str, Dict[str, int]] = {'Caja1': 
                                        {'cliente': 0, 'tiempo': 0},
                                     'Caja2': 
                                        {'cliente': 0, 'tiempo': 0},
                                     'Caja3': 
                                        {'cliente': 0, 'tiempo': 0}}
  ultimo_fila: int = fila.qsize()
  
  while minuto <= min:
    if minuto % 4 == 0:
      ultimo_fila += 1
      # print(ultimo_fila)
      # print(list(fila.queue))
      fila.put(ultimo_fila)
      # print(list(fila.queue))
      
      
    
    asignacion_caja(cajas, fila, minuto)
    tiempos_atencion(cajas)
    continua_atencion(cajas, fila)

    minuto += 1


# fila = Queue()


# print('Fila al iniciar:\n[]')


# min = 4 
# avanzarFila(fila,min)

# print('Fila a los', min, 'minutos:')
# fila_list: list = list(fila.queue)
# print(fila_list)