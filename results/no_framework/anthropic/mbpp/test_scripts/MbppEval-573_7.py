def unique_product(list_data):
    """
    Write a python function to calculate the product of the unique numbers in a given list.

    Examples:
    unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000
    unique_product([1, 2, 3, 1,]) == 6
    unique_product([7, 8, 9, 0, 1, 1]) == 0
    """
    unique_numbers = set(list_data)
    product = 1
    for num in unique_numbers:
        product *= num
    return product

def check(candidate):
    assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
    assert unique_product([1, 2, 3, 1,]) == 6
    assert unique_product([7, 8, 9, 0, 1, 1]) == 0

check(unique_product)