from typing import List, Tuple

def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    str_list = list(str_list)
    str_list.sort()
    str_list_result = []
    for i in range(len(str_list)):
        str_list_result.append(str_list[i]) if str_list[i] != str_list[i-1] else None
    return str_list_result