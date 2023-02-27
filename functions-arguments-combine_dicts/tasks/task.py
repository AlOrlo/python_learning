from typing import List, Dict

def combine_dicts(*args:List[Dict[str, int]]) -> Dict[str, int]:
    dict_res = [elem for elem in args]
    res2 = {keys: sum(elem[keys] for elem in dict_res if keys in elem) for
            keys in set(keys for elem in dict_res for keys in elem)}
    return res2