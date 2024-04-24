def min_val(listval):
    # Filter out all non-integer elements from the list
    filtered_list = [x for x in listval if isinstance(x, int)]
    
    # Return the minimum value from the filtered list
    return min(filtered_list)

# Test cases




def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)