def max_Product(arr):
    max_pair = None
    max_product = None
    
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            pair = (arr[i], arr[j])
            product = arr[i] * arr[j]
            if max_product is None or product > max_product:
                max_product = product
                max_pair = pair
            
    return max_pair

def check(candidate):
    assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)
    assert max_Product([0,-1,-2,-4,5,0,-6]) == (-4,-6)
    assert max_Product([1,2,3]) == (2,3)

check(max_Product)