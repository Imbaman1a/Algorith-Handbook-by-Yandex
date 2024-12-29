q = int(input())

dicty = dict()

while q:
    lst = list(map(int, input().split()))
    
    if lst[0] == 1:
        x = lst[1]
        y = lst[2]
        dicty[x] = y 
    else:
        y = lst[1]
        print(dicty.get(y, -1))
    q -= 1
