n = int(input())
lst = list(map(int, input().split()))

def solve(lst):
    lst.sort()
    l, r = 0, 0
    while l < len(lst):
        while r < len(lst) and lst[r]==lst[l]:
            r += 1
        if r-l > len(lst)/2:
            return 1
        if l > len(lst)/2:
            return 0
        l = r
    return 0

print(solve(lst))
        
