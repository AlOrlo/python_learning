from typing import Any, Dict, List, Set

def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    d = set()
    for i in lst:
        for val in i.values():
            d.add(val)
    return d