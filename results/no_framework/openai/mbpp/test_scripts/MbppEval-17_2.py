def square_perimeter(a):
    return 4 * a

# Test the function with the given examples
assert square_perimeter(10) == 40
assert square_perimeter(5) == 20
assert square_perimeter(4) == 16

def check(candidate):
    assert square_perimeter(10)==40
    assert square_perimeter(5)==20
    assert square_perimeter(4)==16

check(square_perimeter)