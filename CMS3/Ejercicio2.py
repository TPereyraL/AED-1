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

d = [{'a':'3','b':'2'}, {'b':'3','c':'4'},{'a':'5'}]
print(unir_diccionarios(d))