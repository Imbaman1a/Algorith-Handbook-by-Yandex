def MaximumLoot(S, cost_l):
    
    cost_l.sort()
    value = 0
    if S < cost_l[value]: return 0
    
    while S - cost_l[value]>=0:
        S -= cost_l[value]
        value += 1    
    
    return value

n, S = map(int, input().split())
cost_l = [0] * n

for i in range(n):
    cost_l[i] = int(input())

print(MaximumLoot(S, cost_l))
