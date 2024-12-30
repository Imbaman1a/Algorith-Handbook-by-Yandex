n = int(input())
k = int(input())
lst = list(map(int, input().split()))

from collections import deque

ans_fast = deque()
L = 0
R = 0
ans = 0

while R < n:
    while ans_fast and lst[ans_fast[-1]] > lst[R]:
        ans_fast.pop()
    

    ans_fast.append(R)
    
    if (R + 1) >= k:
        ans+= (lst[ans_fast[0]])
        L += 1
    
    if L > ans_fast[0]:
        ans_fast.popleft()
    
    R += 1
        
print(ans)
    
