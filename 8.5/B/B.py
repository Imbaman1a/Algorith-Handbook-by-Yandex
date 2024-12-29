n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
k = int(input())
arr3 = list(map(int, input().split()))


table = [[[0] * (k+1) for _ in range(m+1)] for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        for z in range(1, k+1):
            #print(i,j,z)
            table[i][j][z] = max(table[i-1][j][z], table[i][j-1][z], table[i][j][z-1])
            match = table[i-1][j-1][z-1] + 1
            #mismatch = table[i-1][j-1] + 1
            if arr1[i-1] == arr2[j-1] == arr3[z-1]:
                table[i][j][z] =  max(table[i][j][z], match)
            


print(table[n][m][k])
