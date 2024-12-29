n = int(input())
lst = list(map(int, input().split()))

def solve(lst):
    ans = 0
    lst.sort()
    l, r = 0, 0
    while l < len(lst):
        while r < len(lst) and lst[r]==lst[l]:
            r += 1
        if r-l > len(lst)/4:
            ans += 1
        if ans >=3:
            return 1
        l = r
        
    return 0

print(solve(lst))
        
