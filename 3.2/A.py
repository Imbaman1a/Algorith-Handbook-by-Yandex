n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))
countix = 0
while lst:
    minimum_idx = 0
    minimum_val = lst[minimum_idx][1]
    
    for i in range(1,len(lst)):
        if lst[i][1]<minimum_val:
            minimum_val = lst[i][1]
            minimum_idx = i
        
    lst.pop(minimum_idx)
    lst_temp = []
    for i in range(len(lst)):

        if lst[i][0]<=minimum_val:
            pass
        else:
            lst_temp.append(lst[i])
    lst = lst_temp.copy()        
  
    countix += 1    
print(countix)
