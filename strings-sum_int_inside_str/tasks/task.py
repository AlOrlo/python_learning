def get_fractions(a_b: str, c_b: str) -> str:
    a_slice = slice(0, a_b.find("/"))
    c_slice = slice(0, c_b.find("/"))
    b_slice = slice(a_b.find('/'), len(a_b))
    sum = str(str(int(a_b[a_slice]) + int(c_b[c_slice])) + a_b[b_slice])
    res = "{} + {} = {}".format(a_b, c_b, sum)
    return res
