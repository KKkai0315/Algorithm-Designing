n, w = map(int, input().split())
a = []
M = [[0] * (w + 1) for _ in range(n + 1)]
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(1, n + 1):
    for j in range(1, w + 1):
        if a[i - 1][0] > j:
            M[i][j] = M[i - 1][j]
        else:
            M[i][j] = max(M[i - 1][j], a[i - 1][1] + M[i - 1][j - a[i - 1][0]])
print(M[n][w])
