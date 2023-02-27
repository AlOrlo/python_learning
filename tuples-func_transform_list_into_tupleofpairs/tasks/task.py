from typing import Any, Tuple, List

def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    res = []
    if len(lst) != 1:
        for i in range(len(lst) - 1):
            r1 = []
            for j in range(2):
                r1.append(lst[i + j])
            res.append(tuple(r1))
    else:
        None
    return res