n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))


table = [[0] * (m+1) for _ in range(n+1)]



for i in range(1, n+1):
    for j in range(1, m+1):
        insertion = table[i][j-1]
        deletion = table[i-1][j]
        match = table[i-1][j-1] + 1
        #mismatch = table[i-1][j-1] + 1
        if arr1[i-1] == arr2[j-1]:
            table[i][j] =  max(insertion, deletion, match)
        else:
            table[i][j] = max(insertion, deletion)
print(table[n][m])
