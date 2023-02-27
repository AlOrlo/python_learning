from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    # TODO: Add your code here
    s = s.lower()
    y = set(s)
    key_s = []
    value_s = []
    for i in y:
        count = s.count(i)
        key_s.append(i)
        value_s.append(count)
    return dict(zip(key_s, value_s))