Setix = set()

q = int(input())

while (q):

    lst = list(map(int, input().split()))

    if lst[0]==1:
        Setix.add(lst[1])
        
    else:
        print(1 if lst[1] in Setix else 0)

    q -= 1

