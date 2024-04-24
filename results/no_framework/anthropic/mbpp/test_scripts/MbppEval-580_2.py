def even_ele(test_tuple, even_fnc):
    """
    Write a function to remove uneven elements in the nested mixed tuple.

    Examples:
    even_ele((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    even_ele((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    even_ele((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)
    """
    result = ()
    for item in test_tuple:
        if isinstance(item, tuple):
            result += (even_ele(item, even_fnc),)
        elif even_fnc(item):
            result += (item,)
    return result

# Example usage




def check(candidate):
    assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
    assert extract_even((5, 6, (8, 7, (4, 8)), 7, 9)) == (6, (8, (4, 8)))
    assert extract_even((5, 6, (9, 8, (4, 6)), 8, 10)) == (6, (8, (4, 6)), 8, 10)

check(even_ele)