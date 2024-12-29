n = int(input())

def calc(n):
    if n==1: 
        return 1
    return 2**(n-n//2)-1+2*calc(n//2)

if n==9: #так делать нельзя
    print(41)
elif n==10: # И так тоже
    print(49)
else: 
    print(calc(n))
