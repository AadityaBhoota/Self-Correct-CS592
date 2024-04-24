def sum_of_digits(nums):
    total_sum = 0

    for num in nums:
        if isinstance(num, int):
            digits = [int(digit) for digit in str(abs(num)) if digit.isdigit()]
            total_sum += sum(digits)

    return total_sum

# Test cases



def check(candidate):
    assert sum_of_digits([10,2,56])==14
    assert sum_of_digits([[10,20,4,5,'b',70,'a']])==19
    assert sum_of_digits([10,20,-4,5,-70])==19

check(sum_of_digits)