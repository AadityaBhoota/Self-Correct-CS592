def divisible_by_digits(startnum, endnum):
    result = []
    for i in range(startnum, endnum + 1):
        if all(i % int(digit) == 0 for digit in str(i) if digit != '0'):
            result.append(i)
    return result

# Test cases




def check(candidate):
    assert divisible_by_digits(1,22)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
    assert divisible_by_digits(1,15)==[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15]
    assert divisible_by_digits(20,25)==[22, 24]

check(divisible_by_digits)