def multiply_num(numbers):
    """
    Write a function to multiply all the numbers in a list and divide with the length of the list.

    Examples:
    multiply_num((8, 2, 3, -1, 7)) == -67.2
    multiply_num((-10,-20,-30)) == -2000.0
    multiply_num((19,15,18)) == 1710.0
    """
    if len(numbers) == 0:
        return 0
    
    product = 1
    for num in numbers:
        product *= num
    
    return product / len(numbers)

def check(candidate):
    assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
    assert math.isclose(multiply_num((-10,-20,-30)), -2000.0, rel_tol=0.001)
    assert math.isclose(multiply_num((19,15,18)), 1710.0, rel_tol=0.001)

check(multiply_num)