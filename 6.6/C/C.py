import math
r, c = map(int, input().split())
ans = r*c - (math.ceil(r/3)*math.ceil(c/3))
print(ans)
