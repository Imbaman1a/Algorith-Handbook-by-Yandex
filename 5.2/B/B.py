def GCD(a,b):
    if a==0 or b==0:
        return max(a,b)
    return GCD(b, a%b)

a, b = map(int, input().split())

print(a*b//GCD(a,b))
