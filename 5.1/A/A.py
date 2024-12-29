n = int(input())
if n>1:
    lst = [0] * (n+1)
    lst[1] = 1
    for i in range(2,n+1):
        lst[i] = lst[i-1] + lst[i-2]
    print(lst[-1])
elif n==1:
    print(1)
else:
    print(0)
