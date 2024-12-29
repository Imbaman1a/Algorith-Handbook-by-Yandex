lst = list(map(int, input().split()))
n = lst[0]
m = lst[1]
if n==m:
    print('Lose')
elif abs(n-m)%3==0:
    print('Lose') 
else:
    print('Win')
