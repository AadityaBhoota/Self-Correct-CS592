def count_integer(list1):
    count = 0
    for item in list1:
        if type(item) == int:
            count += 1
    return count

# Testing the function with the provided examples




# Additional test cases


def check(candidate):
    assert count_integer([1,2,'abc',1.2]) == 2
    assert count_integer([1,2,3]) == 3
    assert count_integer([1,1.2,4,5.1]) == 2

check(count_integer)