def list_tuple(listx):
    return tuple(listx)

def check(candidate):
    assert list_tuple([5, 10, 7, 4, 15, 3])==(5, 10, 7, 4, 15, 3)
    assert list_tuple([2, 4, 5, 6, 2, 3, 4, 4, 7])==(2, 4, 5, 6, 2, 3, 4, 4, 7)
    assert list_tuple([58,44,56])==(58,44,56)

check(list_tuple)