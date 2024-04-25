def find_Odd_Pair(A, N):
    count = 0
    for i in range(N):
        for j in range(i + 1, N):  # Start from i+1 to avoid repeated pairs
            xor_val = A[i] ^ A[j]
            for k in range(j + 1, N):
                if (xor_val ^ A[k]) % 2 != 0:
                    count += 1
    return count

def check(candidate):
    assert find_Odd_Pair([5,4,7,2,1],5) == 6
    assert find_Odd_Pair([7,2,8,1,0,5,11],7) == 12
    assert find_Odd_Pair([1,2,3],3) == 2

check(find_Odd_Pair)