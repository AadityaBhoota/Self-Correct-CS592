def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int):
    def is_fibonacci(num):
        a, b = 0, 1
        while a < num:
            a, b = b, a + b
        return a == num

    count = 0
    num = 2
    while count < n:
        if is_fibonacci(num) and is_prime(num):
            count += 1
        num += 1
    return num - 1

# Test cases








METADATA = {}


def check(candidate):
    assert candidate(1) == 2
    assert candidate(2) == 3
    assert candidate(3) == 5
    assert candidate(4) == 13
    assert candidate(5) == 89
    assert candidate(6) == 233
    assert candidate(7) == 1597
    assert candidate(8) == 28657
    assert candidate(9) == 514229
    assert candidate(10) == 433494437


check(prime_fib)