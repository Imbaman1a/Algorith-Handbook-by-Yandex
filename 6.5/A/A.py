n = int(input())
k = 1
counter = 0
while k*(k+1)/2 <=n:
    k += 1
    counter += 1

print(counter)
