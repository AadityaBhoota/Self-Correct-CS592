def mul_even_odd(list1):
    even_found = False
    odd_found = False
    even_product = 1
    odd_product = 1
    
    for num in list1:
        if num % 2 == 0 and not even_found:
            even_product *= num
            even_found = True
        elif num % 2 != 0 and not odd_found:
            odd_product *= num
            odd_found = True
        
        if even_found and odd_found:
            break
    
    return even_product * odd_product

def check(candidate):
    assert mul_even_odd([1,3,5,7,4,1,6,8])==4
    assert mul_even_odd([1,2,3,4,5,6,7,8,9,10])==2
    assert mul_even_odd([1,5,7,9,10])==10

check(mul_even_odd)