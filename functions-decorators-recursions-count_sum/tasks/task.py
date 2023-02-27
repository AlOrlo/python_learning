import functools
from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    """
    Add your code here or call it from here   
    """
    if len(sequence) == 0:
        return 0
    elif type(sequence[0]) is list:
        return seq_sum(sequence[0]) + seq_sum(sequence[1:])
    elif type(sequence[0]) is tuple:
        return seq_sum(sequence[0]) + seq_sum(sequence[1:])
    else:
        return sequence[0] + seq_sum(sequence[1:])
