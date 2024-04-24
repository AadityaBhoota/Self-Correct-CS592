def add_lists(test_list, test_tup):
    concatenated_list = list(test_tup) + test_list
    return tuple(concatenated_list)

def check(candidate):
    assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)
    assert add_lists([6, 7, 8], (10, 11)) == (10, 11, 6, 7, 8)
    assert add_lists([7, 8, 9], (11, 12)) == (11, 12, 7, 8, 9)

check(add_lists)