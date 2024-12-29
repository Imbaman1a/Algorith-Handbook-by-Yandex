arr1 = input()
arr2 = input()

n = len(arr1)
m = len(arr2)

table = [[0] * (m+1) for _ in range(n+1)]


for j in range(m+1):
    table[0][j] = j
for i in range(n+1):
    table[i][0] = i
for i in range(1, n+1):
    for j in range(1, m+1):
        insertion = table[i][j-1] + 1
        deletion = table[i-1][j] + 1
        match = table[i-1][j-1]
        mismatch = table[i-1][j-1] + 1
        if arr1[i-1] == arr2[j-1]:
            table[i][j] =  min(insertion, deletion, match)
        else:
            table[i][j] = min(insertion, deletion, mismatch)
print(table[n][m])
