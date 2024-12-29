n = int(input())

def xanoi(n, one, two):
    if n==1:
        print(one, two)
        return
    three = 6 - one - two
    xanoi(n-1, one, three)
    print(one, two)
    xanoi(n-1, three, two)
print(2**n-1)
xanoi(n, 1, 3)
