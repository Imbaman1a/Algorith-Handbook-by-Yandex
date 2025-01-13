X, y = map(int, input().split())

from collections import deque

stack = deque()
visited = set()
visited.add(X)
step = 0
stack.append((X, step))

while stack:

    curr, step = stack.popleft()

    if curr==y:
        break

    for c in range(10):
        next_nums = [curr + c, curr - c, curr * c]

        for num in next_nums:
            
            
            if num not in visited and 0 <= num <= 10**5:
                visited.add(num)
                stack.append((num, step + 1))


print(step)
