def round_and_sum(list1):
    rounded_sum = 0
    for num in list1:
        rounded_num = round(num)
        rounded_sum += rounded_num
    
    total = rounded_sum * len(list1)
    
    return total

def check(candidate):
    assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50])==243
    assert round_and_sum([5,2,9,24.3,29])==345
    assert round_and_sum([25.0,56.7,89.2])==513

check(round_and_sum)