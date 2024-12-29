W, n = map(int, input().split())
lst = list(map(int, input().split()))

pack = [[0] * (n+1) for _ in range(W+1)]
pack[0][0] = 1
for i in range(1, n+1):
    for j in range(0, W+1):
        if lst[i-1] > j:
            pack[j][i] = pack[j][i-1]
        else:
            pack[j][i] = ((pack[j][i-1]) or (pack[j-lst[i-1]][i-1]))

#print(pack[W][n])

def printer(pack):
    for j in range(W,-1,-1):
        if pack[j][n]:
            return j
    return 0

print(printer(pack))

