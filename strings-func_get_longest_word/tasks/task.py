def get_longest_word(s: str) -> str:
    y = 0
    word = None
    for i in s.split():
        if len(i) > y:
            y = len(i)
            word = i
    return word
