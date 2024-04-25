def unique_product(list_data):
    unique_numbers = set()
    
    for num in list_data:
        if num not in unique_numbers:
            unique_numbers.add(num)
    
    product = 1
    for unique_num in unique_numbers:
        product *= unique_num
    
    return product

def check(candidate):
    assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
    assert unique_product([1, 2, 3, 1,]) == 6
    assert unique_product([7, 8, 9, 0, 1, 1]) == 0

check(unique_product)