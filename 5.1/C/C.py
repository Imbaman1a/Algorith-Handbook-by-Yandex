def PisanoPeriod(m):
    current = 0
    nex = 1
    period = 0
    while True:
        oldNext = nex
        nex = (current + nex) % m
        current = oldNext
        period = period + 1
        if current == 0 and nex == 1:
            return period

n, m = map(int, input().split())
n = n % PisanoPeriod(m)
if n>1:
    lst = [0] * (n+1)
    lst[1] = 1
    for i in range(2,n+1):
        lst[i] = lst[i-1] + lst[i-2]
    print(lst[-1]%m)
else:
    print(n)

