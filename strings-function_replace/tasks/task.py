def replacer(s: str) -> str:
    new_s = ''
    for i in s:
        if i == '\"':
            new_s += '\''
        elif i == '\'':
            new_s += '\"'
        else:
            new_s += i
    return new_s