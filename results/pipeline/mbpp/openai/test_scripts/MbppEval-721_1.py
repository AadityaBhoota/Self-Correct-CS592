def maxAverageOfPath(cost):
    def isValid(row, col, size):
        return 0 <= row < size and 0 <= col < size

    N = len(cost)

    dp = [[0] * N for _ in range(N)]

    dp[0][0] = cost[0][0]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            if isValid(i - 1, j, N):
                from_above = dp[i - 1][j]
            else:
                from_above = float('-inf')
                
            if isValid(i, j - 1, N):
                from_left = dp[i][j - 1]
            else:
                from_left = float('-inf')
                
            dp[i][j] = max(from_above, from_left) + cost[i][j]

    return dp[N-1][N-1] / (2*N-1)

def check(candidate):
    assert maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]) == 5.2
    assert maxAverageOfPath([[2, 3, 4], [7, 6, 5], [8, 4, 10]]) == 6.2
    assert maxAverageOfPath([[3, 4, 5], [8, 7, 6], [9, 5, 11]]) == 7.2
    assert maxAverageOfPath([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 5.8

check(maxAverageOfPath)