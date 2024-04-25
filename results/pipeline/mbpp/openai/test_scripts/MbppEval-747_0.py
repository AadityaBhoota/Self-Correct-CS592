def lcs_of_three(X, Y, Z):
    dp = [[[0 for _ in range(len(Z) + 1)] for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]

    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            for k in range(1, len(Z) + 1):
                if X[i - 1] == Y[j - 1] == Z[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    
    return dp[len(X)][len(Y)][len(Z)]

def check(candidate):
    assert lcs_of_three('AGGT12', '12TXAYB', '12XBA') == 2
    assert lcs_of_three('Reels', 'Reelsfor', 'ReelsforReels') == 5
    assert lcs_of_three('abcd1e2', 'bc12ea', 'bd1ea') == 3

check(lcs_of_three)