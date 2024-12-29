n = int(input())
lst = list(map(int, input().split()))
lst.sort()

if sum(lst)%3!=0:
    print(0)
else:
    V = sum(lst)//3
    split = [[[0] * (V+1) for _ in range(V+1)] for _ in range(n+1)] 
    split[0][0][0] = 1
    for i in range(1, n+1):
        for s1 in range(0, V+1):
            for s2 in range(0, V+1):
                split[i][s1][s2] = split[i-1][s1][s2] 
                if s1 >= lst[i-1]:
                    split[i][s1][s2] = (split[i][s1][s2] or split[i - 1][s1 - lst[i-1]][s2])
                if s2 >= lst[i-1]:
                    split[i][s1][s2] = (split[i][s1][s2] or split[i - 1][s1][s2 - lst[i-1]])

    print(split[n][V][V])
