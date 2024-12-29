n = int(input())
lst = list(map(int, input().split()))
lst.sort()

print(max(lst[0]*lst[1]*lst[-1], lst[-1]*lst[-2]*lst[-3]))
