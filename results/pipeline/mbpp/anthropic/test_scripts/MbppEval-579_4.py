def find_dissimilar(test_tup1, test_tup2):
    dissimilar_set = set()
    
    for element in test_tup1:
        if element not in test_tup2:
            dissimilar_set.add(element)
    
    for element in test_tup2:
        if element not in test_tup1:
            dissimilar_set.add(element)
    
    return tuple(dissimilar_set)

def check(candidate):
    assert find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)) == (3, 6, 7, 10)
    assert find_dissimilar((1, 2, 3, 4), (7, 2, 3, 9)) == (1, 4, 7, 9)
    assert find_dissimilar((21, 11, 25, 26), (26, 34, 21, 36)) == (34, 36, 11, 25)

check(find_dissimilar)