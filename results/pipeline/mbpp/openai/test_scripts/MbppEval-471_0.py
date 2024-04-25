def find_remainder(arr, n): 
    product = 1
    
    for num in arr:
        product *= num
        product %= n
    
    return product % n

def check(candidate):
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
    assert find_remainder([1,1,1],1) == 0
    assert find_remainder([1,2,1],2) == 0

check(find_remainder)