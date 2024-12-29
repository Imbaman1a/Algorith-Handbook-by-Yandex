
def kol(lst, num):
    if num > lst[-1] or num < lst[0]:
        return 0
    l = 0 
    r = len(lst) - 1
    res = 0
    while r >= l:
        mid =  (l+r)//2
        #print(mid)
        if lst[mid] == num:
            j = mid
            while r>=j and lst[j]==num:
                res += 1
                j += 1
            j = mid-1
            while l <= j and lst[j] == num:
                res += 1
                j -= 1
            break
        elif lst[mid] > num:
            r = mid - 1
        else:
            l = mid + 1
    
    return res

    


n = int(input())

k = list(map(int,input().split()))

m = int(input())

q= list(map(int,input().split()))

dicty = {}


for i in range(m):
    if dicty.get(q[i],-1)==-1:
        dicty[q[i]] = kol(k, q[i])
    print(dicty[q[i]], end= ' ')

