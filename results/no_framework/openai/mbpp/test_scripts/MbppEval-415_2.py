def max_Product(arr):
    max_num = max(arr)
    arr.remove(max_num)
    
    second_max_num = max(arr)
    product = max_num * second_max_num
    
    return (max_num, second_max_num)

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)