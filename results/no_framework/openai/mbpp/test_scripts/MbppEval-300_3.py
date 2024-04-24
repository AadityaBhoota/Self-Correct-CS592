def count_binary_seq(n):
    if n == 0:
        return 1.0

    dp = [0] * (2*n + 1)
    dp[0] = 1.0

    for i in range(1, 2*n+1):
        dp[i] = 0
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]

    return dp[2*n]

# Test cases




def check(candidate):
    assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(2), 6.0, rel_tol=0.001)
    assert math.isclose(count_binary_seq(3), 20.0, rel_tol=0.001)

check(count_binary_seq)