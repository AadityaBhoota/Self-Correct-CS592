def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than the given number) and decimals
    (the leftover part, which is always smaller than 1).

    Return the decimal part of the number.
    
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3.5) == 0.5
    assert abs(candidate(1.33) - 0.33) < 1e-6
    assert abs(candidate(123.456) - 0.456) < 1e-6

check(truncate_number)