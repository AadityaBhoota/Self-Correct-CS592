def unique_sublists(list1):
    counts = {}
    for sublist in list1:
        tuple_sublist = tuple(sublist)
        if tuple_sublist in counts:
            counts[tuple_sublist] += 1
        else:
            counts[tuple_sublist] = 1
    return counts

# Test cases




def check(candidate):
    assert unique_sublists([[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]])=={(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
    assert unique_sublists([['green', 'orange'], ['black'], ['green', 'orange'], ['white']])=={('green', 'orange'): 2, ('black',): 1, ('white',): 1}
    assert unique_sublists([[1, 2], [3, 4], [4, 5], [6, 7]])=={(1, 2): 1, (3, 4): 1, (4, 5): 1, (6, 7): 1}

check(unique_sublists)