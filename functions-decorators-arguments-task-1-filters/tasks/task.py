import copy
from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters
    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    selected_array = selector
    f_copy_for_filters = copy.deepcopy(data)  # create a copy, i'll delete non-selected keys
    filtered = {k: v for elem in filters for k, v in elem.items()}  #union all filters in one dictionary
    for i in range(len(data)):  #delete unnecessary items, not represented in selector
        for key in data[i].keys():
            if key in selected_array:
                continue
            else:
                del f_copy_for_filters[i][key]
    result = copy.deepcopy(f_copy_for_filters)
    for elem in f_copy_for_filters:
        for key, values in filtered.items():
            if elem[key] not in values and elem in result:
                result.remove(elem)
    fin_res = [dict(sorted(item.items())) for item in result] #sorting the result by keys
    return fin_res

def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    return [x for x in columns]



def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    return {column: [j for j in values]}


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'Volleyball'))),
        field_filter(*('gender', *('male',))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value


if __name__ == "__main__":
    test_query()