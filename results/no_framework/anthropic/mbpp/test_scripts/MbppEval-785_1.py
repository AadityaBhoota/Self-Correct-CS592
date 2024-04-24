def tuple_str_int(test_str):
    """
    Write a function to convert tuple string to integer tuple.

    Examples:
    tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    """
    # Remove the parentheses from the string
    test_str = test_str.strip("()")
    
    # Split the string into individual elements
    elements = test_str.split(", ")
    
    # Convert each element to an integer and return the tuple
    return tuple(int(x) for x in elements)

def check(candidate):
    assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
    assert tuple_str_int("(1, 2, 3)") == (1, 2, 3)
    assert tuple_str_int("(4, 5, 6)") == (4, 5, 6)
    assert tuple_str_int("(7, 81, 19)") == (7, 81, 19)

check(tuple_str_int)