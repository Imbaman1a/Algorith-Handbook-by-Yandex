n, m = map(int, input().split())

A = [[0]*m] * n
B = [[0]*m] * n
for i in range(n):
    A[i] = list(map(int, input().split()))
for i in range(n):
    B[i] = list(map(int, input().split()))

C = [[0]*m] * n

for i in range(n):
    for j in range(m):
        C[i][j] = A[i][j] + B[i][j]

for i in range(n):
    for j in range(m):
        print(A[i][j] + B[i][j], end = ' ')
    print()
