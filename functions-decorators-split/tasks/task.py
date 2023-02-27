from typing import List

def split(data: str, sep=None, maxsplit=-1) -> List[str]:
    """
    :param data: str
    :param sep: None
    :param maxsplit: -1
    :return: str.split == List[str]
    """
    if sep is None:
        sep = " "
    if maxsplit == 0:
            return [data]
    if maxsplit < 0:
            maxsplit = len(data)
    res = []
    pos_from = 0
    while pos_from < len(data):
        if maxsplit > 0 and len(res) >= maxsplit:
            res.append(data[pos_from:])
            break
        sep_pos = data.find(sep, pos_from)
        if data[pos_from] == data[sep_pos] and data[sep_pos] == " ":
            pos_from = sep_pos + len(sep)
        else:
            if sep_pos == -1:
                res.append(data[pos_from:])
                break
            res.append(data[pos_from:sep_pos])
            pos_from = sep_pos + len(sep)
    return res