def find_sum(arr):
    unique_elements = set()
    sum_non_repeated = 0
    
    for num in arr:
        if arr.count(num) == 1:
            unique_elements.add(num)
    
    sum_non_repeated = sum(unique_elements)
    
    return sum_non_repeated

# Test cases




def check(candidate):
    assert find_sum([1,2,3,1,1,4,5,6]) == 21
    assert find_sum([1,10,9,4,2,10,10,45,4]) == 71
    assert find_sum([12,10,9,45,2,10,10,45,10]) == 78

check(find_sum)