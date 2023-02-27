def check_str(s: str):
    symbols_del = ' !@#$%^&*(),.?;:-—\'\"'
    for elem in symbols_del:
        s = s.replace(elem, "")
    s_new = s.lower()
    if len(s) % 2 == 1:
        s_fhalf = s_new[:int((len(s_new)/2))]
        s_shalf = s_new[int((len(s_new)/2)+1)::]
        rev_shalf = s_shalf[::-1]
    else:
        s_fhalf = s_new[:int((len(s_new) / 2))]
        s_shalf = s_new[int((len(s_new) / 2))::]
        rev_shalf = s_shalf[::-1]
    if s_fhalf == rev_shalf:
        return True
    else:
        return False