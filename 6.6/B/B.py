n, k = map(int, input().split())
lst = list(map(int, input().split()))
k = lst[k-1]
lst.remove(k)
count_r=count_l=0

for i in range(n - 1):
    if lst[i] > k:
        count_r += 1
    else:
        count_l += 1
def sumix(left, right):
    #print(left, right)
    if left==0:
        return 0
    if (left+right)%2==0:
        if left%2==0 and right%2==0:
            left -= left//2
            right -= right//2
            return 1 + sumix(left, right)
        else:
            left = left - (left+1)//2
            right = right - right//2
            return 1 + sumix(left, right)
    else:
        if left%2==0 :
            left = left - (left)//2 - 1
            right =  right - right//2
            return 1 + sumix(left, right)
        else:
            left = left - (left+1)//2
            right = right - right//2
            return 1 + sumix(left, right)
            
            
print(sumix(count_l, count_r))
