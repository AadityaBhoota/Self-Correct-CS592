from collections import defaultdict

def count_Substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count

def check(candidate):
    assert count_Substrings('112112') == 6
    assert count_Substrings('111') == 6
    assert count_Substrings('1101112') == 12

check(count_Substrings)