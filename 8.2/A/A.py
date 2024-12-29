n = int(input())

lst = [float('inf')] * (n+1)

lst[0] = 0

for m in range(1, n+1):
    for c in ([1,3,4]):
        if m-c<0:
            continue
        if c<=m:
            lst[m] = min(lst[m], 1 + lst[m-c])

print(lst[n])
