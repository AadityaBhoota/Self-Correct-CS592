def find_even_pair(A, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (A[i] ^ A[j]) % 2 == 0:
                count += 1
    return count

def check(candidate):
    assert find_even_pair([5, 4, 7, 2, 1]) == 4
    assert find_even_pair([7, 2, 8, 1, 0, 5, 11]) == 9
    assert find_even_pair([1, 2, 3]) == 1

check(find_even_pair)