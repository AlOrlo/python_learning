from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
        self.res = []
    # TODO: add your code here

    def __add__(self, other):
        self.other = other
        for i in self.values:
            self.res.append(f'{i} {self.other}')
        return self.res

