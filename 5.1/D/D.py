n = int(input())
if n>1:
    n = n + 2
    n = n%60
    if n==0:
        print(9)
    else:

        lst = [0] * (n+1)
        lst[1] = 1
        for i in range(2,n+1):
            lst[i] = lst[i-1] + lst[i-2]
        print((lst[-1]-1)%10)
else:
    print(n)

