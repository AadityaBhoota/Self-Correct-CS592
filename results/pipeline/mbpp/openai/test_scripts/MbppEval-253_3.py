def count_integer(list1):
    count = 0
    
    for num in list1:
        if isinstance(num, int):
            count += 1
    
    return count

def check(candidate):
    assert count_integer([1,2,'abc',1.2]) == 2
    assert count_integer([1,2,3]) == 3
    assert count_integer([1,1.2,4,5.1]) == 2

check(count_integer)