from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,int]]) -> Dict[str,List[str]]:
  from typing import List
from typing import Dict
import json

def unir_diccionarios(a_unir: List[Dict[str,int]]) -> Dict[str,List[str]]:
    res: Dict[str,List[str]] = {}
    for dict in a_unir:
        keys: List[str] = dict.keys()
        for key in keys:
            if key in res:
                res[key].append(dict[key])
            else:
                res[key] = [dict[key]]

    return res


if __name__ == '__main__':
  x = json.loads(input()) # Ejemplo de input: [{"a":2},{"b":3,"a":1}]
  print(unir_diccionarios(x))