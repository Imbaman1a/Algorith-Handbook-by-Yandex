n = int(input())

cords = []
for i in range(n):
    cords.append(list(map(int, input().split())))

cords.sort(key=lambda x: x[1])


sumix = 1
r_m = cords[0][1]
ans = []
ans.append(r_m)

for l, r in cords:

    if l <= r_m :
        pass
    else:
        r_m = r
        sumix += 1
        ans.append(r_m)
print(sumix)

print(' '.join([str(x) for x in ans]))
