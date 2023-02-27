from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    keys = []
    values = []
    if num == 0:
        return dict(zip(keys, values))
    else:
        for i in range(1, num + 1):
            keys.append(i)
            values.append(i * i)
    return dict(zip(keys, values))