n = int(input())

lst = [float('inf')] * (n+1)
lst[0] = 0

for i in range(1, n+1):
    lst[i] = 1 + lst[i-1]
    if (i)%2==0:
        lst[i] = min(lst[i], 1 + lst[(i)//2])
    if (i)%3==0:
        lst[i] = min(lst[i], 1 + lst[(i)//3])
        
operations = []

while n > 1:
    operations.append(n)
    if lst[n] == 1 + lst[n-1]:
        n -= 1
    elif n%2==0 and lst[n] == 1 + lst[n//2]:
        n = n //2
    elif n%3==0 and lst[n] == 1 + lst[n//3]:
        n = n // 3
operations.append(1)
print(len(operations) - 1)
print(*operations[::-1])
