n = int(input())
lst = list(map(int, input().split()))
stack = []
ans = [0] * n

for i in range(n):
    while stack and stack[-1][0] < lst[i]:
        _ , idx = stack.pop()
        ans[i] += ans[idx] + 1
    stack.append((lst[i], i))

print(*ans)
        
        
    
