def min_val(listval):
    """
    Write a function to find the minimum value in a given heterogeneous list.

    Examples:
    min_val(['Python', 3, 2, 4, 5, 'version']) == 2
    min_val(['Python', 15, 20, 25]) == 15
    min_val(['Python', 30, 20, 40, 50, 'version']) == 20
    """
    # Initialize the minimum value to the first numeric value in the list
    min_value = next((x for x in listval if isinstance(x, (int, float))), None)

    # Iterate through the list and update the minimum value if a smaller value is found
    for item in listval:
        if isinstance(item, (int, float)) and (min_value is None or item < min_value):
            min_value = item

    # If no numeric values were found, return None
    return min_value

def check(candidate):
    assert min_val(['Python', 3, 2, 4, 5, 'version'])==2
    assert min_val(['Python', 15, 20, 25])==15
    assert min_val(['Python', 30, 20, 40, 50, 'version'])==20

check(min_val)