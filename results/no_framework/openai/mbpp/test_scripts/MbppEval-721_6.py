def maxAverageOfPath(cost):
    n = len(cost)
    
    dp = [[0.0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = cost[0][0]
    
    # Fill in the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + cost[0][j]
    
    # Fill in the first column
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + cost[i][0]
    
    # Fill in the rest of the dp table
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i][j]
    
    return dp[n-1][n-1] / (2 * n - 1)

# Test cases




def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)