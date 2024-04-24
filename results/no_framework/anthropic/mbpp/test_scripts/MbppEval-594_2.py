def diff_even_odd(list1):
    """
    Write a function to find the difference of the first even and first odd number of a given list.

    Examples:
    diff_even_odd([1,3,5,7,4,1,6,8]) == 3
    diff_even_odd([1,2,3,4,5,6,7,8,9,10]) == 1
    diff_even_odd([1,5,7,9,10]) == 9
    """
    even_num = None
    odd_num = None

    for num in list1:
        if num % 2 == 0 and even_num is None:
            even_num = num
        elif num % 2 != 0 and odd_num is None:
            odd_num = num
        if even_num is not None and odd_num is not None:
            break

    if even_num is None:
        even_num = 0
    if odd_num is None:
        odd_num = 0

    return abs(even_num - odd_num)

def check(candidate):
    assert diff_even_odd([1,3,5,7,4,1,6,8])==3
    assert diff_even_odd([1,2,3,4,5,6,7,8,9,10])==1
    assert diff_even_odd([1,5,7,9,10])==9

check(diff_even_odd)