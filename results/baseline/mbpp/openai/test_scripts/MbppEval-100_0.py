def next_smallest_palindrome(num):
    num += 1
    while str(num) != str(num)[::-1]:
        num += 1
    return num

# Test cases




def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)