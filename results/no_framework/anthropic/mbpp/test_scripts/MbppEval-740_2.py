def tuple_to_dict(test_tup):
    """
    Write a function to convert the given tuple to a key-value dictionary using adjacent elements.
    Examples:
    tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
    tuple_to_dict((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
    tuple_to_dict((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}
    """
    return {test_tup[i]: test_tup[i + 1] for i in range(0, len(test_tup), 2)}

def check(candidate):
    assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
    assert tuple_to_dict((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
    assert tuple_to_dict((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}

check(tuple_to_dict)