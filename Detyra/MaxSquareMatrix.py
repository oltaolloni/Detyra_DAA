# Ju jepet një matricë e vlerave boolean MxN që përfaqëson një tabelë fushash
# të lira (True) ose të zëna (False).
# Gjeni madhësinë e katrorit më të madh të fushave të lira.
def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0  # Nëse matrica është 0, nuk ka katror të lirë

    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for _ in range(M)]  # Matrica DP
    max_side = 0  # Mbajmë madhësinë e katrorit më të madh

    for i in range(M):
        for j in range(N):
            if matrix[i][j]:  # Vetëm nëse qeliza është e lirë (True)
                if i == 0 or j == 0:
                    dp[i][j] = 1  # Rreshti ose kolona e parë mund të kenë maksimum një qelizë
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])  # Përditësojmë madhësinë maksimale

    return max_side ** 2  # Kthejmë sipërfaqen e katrorit më të madh

matrix = [
    [True, True, False, True],
    [True, True, False, True],
    [False, True, True, True],
    [False, True, True, True],
    [False, True, True, True]
]

print(maximalSquare(matrix))