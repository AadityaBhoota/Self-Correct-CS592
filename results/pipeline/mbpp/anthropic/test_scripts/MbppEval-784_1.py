def find_first_even_odd(list1):
    first_even = None
    first_odd = None
    for num in list1:
        if num % 2 == 0 and first_even is None:
            first_even = num
        elif num % 2 != 0 and first_odd is None:
            first_odd = num
        if first_even is not None and first_odd is not None:
            break
    return first_even, first_odd

def multiply_first_even_odd(even_num, odd_num):
    if even_num is None or odd_num is None:
        raise ValueError("Both even and odd numbers must be provided.")
    return even_num * odd_num

def mul_even_odd(list1):
    first_even, first_odd = find_first_even_odd(list1)
    return multiply_first_even_odd(first_even, first_odd)

def check(candidate):
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert mul_even_odd([1,5,7,9,10])==10

check(mul_even_odd)