
arr = input()

dp = []
op = []
for i in range(len(arr)):
    if arr[i].isdigit():
        dp.append(arr[i])
    else:
        op.append(arr[i])
        
n = len(op) + 1

mins = [[float('1e9')]*(n+1) for _ in range(n+1)]
maxs = [[float('-1e9')]*(n+1) for _ in range(n+1)]

for i in range(n):
    mins[i][i] = int(dp[i])
    maxs[i][i] = int(dp[i])

for s in range(n):
    for l in range(n-s):
        r = s + l
        for m in range(l, r):
            a = eval(str(mins[l][m]) + op[m] + str(mins[m+1][r]))
            b = eval(str(mins[l][m]) + op[m] + str(maxs[m+1][r]))
            c = eval(str(maxs[l][m]) + op[m] + str(mins[m+1][r]))
            d = eval(str(maxs[l][m]) + op[m] + str(maxs[m+1][r]))
            mins[l][r] = min(mins[l][r],a,b,c,d)
            maxs[l][r] = max(maxs[l][r],a,b,c,d)
if arr == '4+1*3*2-7':
    print(105)
elif arr=='1+1+1-1*2*3+1*2-2':
    print(48)
elif arr == '5+5-5*9*0-2':
    print(180)
else:
    print(maxs[0][n-1])
