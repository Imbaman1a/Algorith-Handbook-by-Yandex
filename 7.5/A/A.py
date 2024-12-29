import math
n = int(input())

lst = [0] * n

for i in range(n):
    x, y = map(int, input().split())
    lst[i] = (x, y)

def dist(ptr1, ptr2):
    return round( ((ptr1[0]-ptr2[0])**2 + (ptr1[1]-ptr2[1])**2)**0.5, 6)


def solve(arr):

    arr.sort(key = lambda x: x[0])


    def func(lst):
        if len(lst)<=3:
            ll = len(lst)
            ans = float('inf')
            for i in range(ll):
                for j in range(i+1, ll):
                    ans = min(ans, dist(lst[i], lst[j]))
            #print(lst, ans)
            return ans
        else:
            ll = len(lst)
            left = lst[:ll//2]
            right = lst[ll//2:]
            mins_d = min(func(left), func(right))
            #print(mins_d)
            #lst = list(filter(lambda x: abs(x[0] - lst[ll//2][0]) < mins_d , lst))
                        
            sli = []
            mid = ll//2
            sli.append(lst[mid])
            idx = mid - 1

            while idx >= 0 and abs(lst[idx][0] - lst[mid][0]) < mins_d and abs(idx - mid) < 7:
                sli.append(lst[idx])
                idx -= 1

            idx = mid + 1

            while idx < ll and abs(lst[idx][0] - lst[mid][0])  < mins_d and abs(idx - mid) < 7:
                sli.append(lst[idx])
                idx += 1

            
            lst = sli
            lst.sort(key=lambda x: x[1]*x[0])
            
            for i in range(1, len(lst)):

                if dist(lst[i], lst[i-1])  < mins_d:

                    mins_d = dist(lst[i], lst[i-1])
                    

            #print(mins_d)
            return mins_d
    
    return func(arr)

print(solve(lst))
