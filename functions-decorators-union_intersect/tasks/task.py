def union(*args) -> set:
    a = []
    for arg in args:
        for elem in arg:
            a.append(elem)
    return set(a)


def intersect(*args) -> set:
    arguments = [elem for elem in args]
    for i in range(len(arguments)-1):
        b = set(arguments[i]).intersection(set(arguments[i+1]))
    return set(b)