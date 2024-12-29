n = int(input())
clicks = list(map(int, input().split()))
checks = list(map(int, input().split()))
clicks.sort()
checks.sort()
sumix = 0
for i in range(n):
    sumix += clicks[i] * checks[i]
print(sumix)
