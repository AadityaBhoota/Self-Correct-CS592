def common_in_nested_lists(nestedlist):
    """
    Write a function to find the common elements in given nested lists.

    Examples:
    common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]) == [18, 12]
    common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]) == [5, 23]
    common_in_nested_lists([[2, 3, 4, 1], [4, 5], [6, 4, 8], [4, 5], [6, 8, 4]]) == [4]
    """
    # Create a set of the first list to use as a reference
    reference = set(nestedlist[0])

    # Iterate through the remaining lists
    for lst in nestedlist[1:]:
        # Convert the list to a set and find the intersection with the reference set
        reference = reference.intersection(set(lst))

    # Convert the resulting set back to a sorted list and return it
    return sorted(list(reference))

def check(candidate):
    assert set(common_in_nested_lists([[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]))==set([18, 12])
    assert set(common_in_nested_lists([[12, 5, 23, 25, 45], [7, 11, 5, 23, 28], [1, 5, 8, 18, 23, 16]]))==set([5,23])
    assert set(common_in_nested_lists([[2, 3,4, 1], [4, 5], [6,4, 8],[4, 5], [6, 8,4]]))==set([4])

check(common_in_nested_lists)