def tuple_intersection(test_list1, test_list2):
    """
    Find the tuple intersection of elements in the given tuple list irrespective of their order.

    Examples:
    tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)], [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
    tuple_intersection([(4, 1), (7, 4), (11, 13), (17, 14)], [(1, 4), (7, 4), (16, 12), (10, 13)]) == {(4, 7), (1, 4)}
    tuple_intersection([(2, 1), (3, 2), (1, 3), (1, 4)], [(11, 2), (2, 3), (6, 2), (1, 3)]) == {(1, 3), (2, 3)}
    """
    intersection = set()
    for t1 in test_list1:
        for t2 in test_list2:
            if (t1[0], t1[1]) == (t2[1], t2[0]) or (t1[0], t1[1]) == (t2[0], t2[1]):
                intersection.add(tuple(sorted(t1)))
    return intersection

def check(candidate):
    assert tuple_intersection([(3, 4), (5, 6), (9, 10), (4, 5)] , [(5, 4), (3, 4), (6, 5), (9, 11)]) == {(4, 5), (3, 4), (5, 6)}
    assert tuple_intersection([(4, 1), (7, 4), (11, 13), (17, 14)] , [(1, 4), (7, 4), (16, 12), (10, 13)]) == {(4, 7), (1, 4)}
    assert tuple_intersection([(2, 1), (3, 2), (1, 3), (1, 4)] , [(11, 2), (2, 3), (6, 2), (1, 3)]) == {(1, 3), (2, 3)}

check(tuple_intersection)