def add_nested_tuples(test_tup1, test_tup2):
    '''
    Write a function to perform index wise addition of tuple elements in the given two nested tuples.

    Examples:
    add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((7, 10), (7, 14), (3, 10), (8, 13))
    add_nested_tuples(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((9, 12), (9, 16), (5, 12), (10, 15))
    add_nested_tuples(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((11, 14), (11, 18), (7, 14), (12, 17))
    '''
    result = []
    for i in range(len(test_tup1)):
        result.append(tuple(sum(x) for x in zip(test_tup1[i], test_tup2[i])))
    return tuple(result)

def check(candidate):
    assert add_nested_tuples(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((7, 10), (7, 14), (3, 10), (8, 13))
    assert add_nested_tuples(((2, 4), (5, 6), (3, 10), (2, 11)), ((7, 8), (4, 10), (2, 2), (8, 4))) == ((9, 12), (9, 16), (5, 12), (10, 15))
    assert add_nested_tuples(((3, 5), (6, 7), (4, 11), (3, 12)), ((8, 9), (5, 11), (3, 3), (9, 5))) == ((11, 14), (11, 18), (7, 14), (12, 17))

check(add_nested_tuples)