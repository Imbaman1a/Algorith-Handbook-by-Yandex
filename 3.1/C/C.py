a = list(map(int, input().split()))
def fact(x):
    if x<=1: return 1
    return x* fact(x-1)

print(int(fact(a[0]+a[1]-1)/(fact(a[1]) * fact(a[0]-1))))
