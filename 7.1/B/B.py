def search(lst, num):
    if num > lst[-1] or num < lst[0]:
        return -1
    l = 0
    r = len(lst)
    mid = (l+r)//2
    while l <= r:
        if lst[mid] == num:
            return mid
        if lst[mid] > num:
            r = mid - 1
            mid = (l+r)//2
        else:
            l = mid + 1
            mid = (l+r)//2
    
    if lst[l]==num:
        return l
    else:
        return -1



k = int(input())
q = list(map(int, input().split()))
n = int(input())
k = list(map(int, input().split()))

for i in range(n):
    print(search(q, k[i]))


