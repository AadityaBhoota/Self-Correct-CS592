def new_tuple(test_list, test_str):
    test_tuple = tuple(test_list)
    test_tuple += (test_str,)
    return test_tuple

# Test cases




def check(candidate):
    assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
    assert new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')
    assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')

check(new_tuple)