def sum_div(number):
    """
    Write a function to return the sum of all divisors of a number.

    Examples:
    sum_div(8) == 7
    sum_div(12) == 16
    sum_div(7) == 1
    """
    divisors = [1]
    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)
    if number > 1:
        divisors.append(number)
    return sum(divisors)

def check(candidate):
    assert sum_div(8)==7
    assert sum_div(12)==16
    assert sum_div(7)==1

check(sum_div)