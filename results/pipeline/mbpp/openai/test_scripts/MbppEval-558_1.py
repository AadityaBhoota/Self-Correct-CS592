def digit_distance_nums(n1, n2):
    str_n1 = str(n1)
    str_n2 = str(n2)

    if len(str_n1) < len(str_n2):
        str_n1 = str_n1.zfill(len(str_n2))
    elif len(str_n2) < len(str_n1):
        str_n2 = str_n2.zfill(len(str_n1))

    total_distance = 0
    for digit1, digit2 in zip(str_n1, str_n2):
        total_distance += abs(int(digit1) - int(digit2))

    return total_distance

# Testing with examples




def check(candidate):
    assert digit_distance_nums(1,2) == 1
    assert digit_distance_nums(23,56) == 6
    assert digit_distance_nums(123,256) == 7

check(digit_distance_nums)