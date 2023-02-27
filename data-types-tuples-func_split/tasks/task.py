from typing import Tuple

def get_tuple(num: int) -> Tuple[int]:
    num = str(num)
    y = []
    for elem in num:
        y.append(int(elem))
    return tuple(y)