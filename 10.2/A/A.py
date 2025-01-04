n, m = map(int, input().split())

lst = []
dicty = dict()

for i in range(1, n+1):
    dicty[i] = set()

for _ in range(m):
    temp = list(map(int, input().split()))
    
    for i in range(2, len(temp)):
        (dicty[temp[i-1]]).add(temp[i])
        (dicty[temp[i]]).add(temp[i-1])
            
    lst.append(set(temp[1:]))

ans_1 = [[0] * n for _ in range(n)]
ans_2 = [[0] * n for _ in range(n)]

for k, v in dicty.items():
    for item in v:
        ans_1[k-1][item-1] = 1
        
from itertools import combinations
            
for s in lst:
    
    combs = list(combinations(s,2))
    
    for i,j in combs:
        ans_2[i-1][j-1] = 1
        ans_2[j-1][i-1] = 1
    
            
            
for i in range(n):
    print(*ans_1[i])
    
for i in range(n):
    print(*ans_2[i])
