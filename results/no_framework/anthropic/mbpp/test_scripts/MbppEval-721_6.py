def maxAverageOfPath(cost):
    n = len(cost)
    dp = [[0] * n for _ in range(n)]

    # Initialize the first row and column
    dp[0][0] = cost[0][0]
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + cost[0][i]
        dp[i][0] = dp[i-1][0] + cost[i][0]

    # Calculate the maximum average cost for each cell
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + cost[i][j]

    # Calculate the maximum average cost for the entire path
    total_cost = dp[n-1][n-1]
    path_length = 2 * n - 1
    return total_cost / path_length

def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)