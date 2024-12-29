import random

n = int(input())
lst = list(map(int, input().split()))

def quicksort(lst):
    if len(lst)==1:
        return lst
    if len(lst)==0:
        return []
    c = random.choice(lst)
    left = []
    mid = []
    right = []
    for item in lst:
        if item < c:
            left.append(item)
        if item == c:
            mid.append(item)
        if item > c:
            right.append(item)
    left_s = quicksort(left)
    right_s = quicksort(right)
    return left_s + mid + right_s
ans = quicksort(lst)
print(*ans)

