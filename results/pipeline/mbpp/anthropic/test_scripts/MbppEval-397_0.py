def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return float(numbers[1])

def check(candidate):
    assert median_numbers(25,55,65)==55.0
    assert median_numbers(20,10,30)==20.0
    assert median_numbers(15,45,75)==45.0

check(median_numbers)