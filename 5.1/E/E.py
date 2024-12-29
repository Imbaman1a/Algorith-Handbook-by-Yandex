m, n = map(int, input().split())

def res(n):
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
            return ((lst[-1]-1)%10)
    else:
        return (n)
if m ==0:
    m += 1
tot = (res(n) - res(m-1))
if tot < 0:
    print(tot+10)
else:
    print(tot)
