def bell_Number(n):
    """
    Write a python function to find nth bell number.

    Examples:
    bell_Number(2) == 2
    bell_Number(3) == 5
    bell_Number(4) == 15
    """
    if n == 0:
        return 1
    
    bell_nums = [0] * (n + 1)
    bell_nums[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            bell_nums[i] += bell_nums[j] * bell_nums[i - j - 1]
    
    return bell_nums[n]

def check(candidate):
    assert bell_Number(2) == 2
    assert bell_Number(3) == 5
    assert bell_Number(4) == 15

check(bell_Number)