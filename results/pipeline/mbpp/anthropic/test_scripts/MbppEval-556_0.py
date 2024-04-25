def find_Odd_Pair(A, N):
    odd_count = 0
    for num in A:
        if num % 2 == 1:
            odd_count += 1
    return odd_count * (N - odd_count)

def check(candidate):
    assert find_Odd_Pair([5,4,7,2,1],5) == 6
    assert find_Odd_Pair([7,2,8,1,0,5,11],7) == 12
    assert find_Odd_Pair([1,2,3],3) == 2

check(find_Odd_Pair)