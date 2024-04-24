def union_elements(test_tup1, test_tup2):
    # Combine the elements of both tuples
    combined = test_tup1 + test_tup2
    
    # Converting the combined tuple to a set to remove duplicates
    unique_elements = set(combined)
    
    # Sorting the unique elements and converting them back to a tuple
    sorted_union = tuple(sorted(unique_elements))
    
    return sorted_union

# Test cases




def check(candidate):
    assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
    assert union_elements((1, 2, 3, 4),(3, 4, 5, 6) ) == (1, 2, 3, 4, 5, 6)
    assert union_elements((11, 12, 13, 14),(13, 15, 16, 17) ) == (11, 12, 13, 14, 15, 16, 17)

check(union_elements)