def common_in_nested_lists(nestedlist):
    # Initialize the common set with the first list
    common_elements = set(nestedlist[0])

    # Find the common elements between all lists
    for lst in nestedlist[1:]:
        common_elements.intersection_update(lst)

    return list(common_elements)

# Test the function with examples




def check(candidate):
    assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
    assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]))==set([5,23])
    assert set(common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]))==set([4])

check(common_in_nested_lists)