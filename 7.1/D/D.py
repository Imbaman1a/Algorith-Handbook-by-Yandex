def cover_lst(lst, num, k):
    seg = 1
    lst_cover = lst[0]
    
    for i in range(1,n):
        if lst[i] > lst_cover + num:
            seg += 1
            lst_cover = lst[i]
        
        if seg > k:
            return False
    return True
        
    
    


n, k = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

l, r = 0, lst[-1] - lst[0]

while l < r:
    mid = (l+r)//2
    
    if cover_lst(lst, mid, k):
        r =  mid
    else:
        l = mid + 1
        
        
print(l)
        

