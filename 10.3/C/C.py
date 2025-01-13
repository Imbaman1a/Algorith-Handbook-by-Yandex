n, m = map(int, input().split())
_map = [['.'] * m for _ in range(n)]

moves = {

    'U': [-1, 0],
    'D': [1, 0],
    'R': [0, 1],
    'L': [0, -1]
}

from collections import deque

stack = deque()

visited = set()
countix = 0
for i in range(n):
    s = input()
    for j in range(m):
        if s[j]=='#':
            _map[i][j] = '#'
        else:
            countix += 1
        if s[j] == 'S':
            start_r = i
            start_c = j
        if s[j] == 'F':
            fin_r = i
            fin_c = j

visited.add((start_r, start_c))
string = ''
stack.append((start_r, start_c, string))
stats = False
while stack:
    pos_r, pos_c, string = stack.popleft()

    if pos_r == fin_r and pos_c == fin_c:
        break
    if len(visited)==countix:
        string = -1
        stats = True
        break
    for k, v in moves.items():
        new_r = pos_r + v[0]
        new_c = pos_c + v[1]
        new_string = string + k
        if (new_r, new_c) not in visited and 0<=new_r<n and 0<=new_c<m and _map[new_r][new_c] != '#':
            visited.add((new_r, new_c))
            stack.append((new_r, new_c, new_string))


if stats:
    print(string)
else:
    print(len(string))
    print(string)
