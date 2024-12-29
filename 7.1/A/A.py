n = int(input())
lst = list(map(int, input().split()))
q = int(input())

minInd = 0
maxInd = n-1

while maxInd >=minInd:
    midInd = (maxInd+minInd)//2
    if lst[midInd] ==q:
        print(midInd)
        break
    elif lst[midInd] > q:
        maxInd = midInd - 1
    else:
        minInd = midInd + 1
if lst[midInd]!=q: 
    print(-1)
