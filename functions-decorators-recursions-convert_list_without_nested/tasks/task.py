from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    l = len(sequence)
    if l == 0:
        return sequence
    elif l == 1:
        elem = sequence[0]
        try:
            return linear_seq(list(elem))
        except TypeError:
            return [elem]
    else:
        x = l // 2
        return linear_seq(sequence[:x]) + linear_seq(sequence[x:])