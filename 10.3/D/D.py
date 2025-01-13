n, m = map(int, input().split())
_map = [['.'] * m for _ in range(n)]

moves = {

    'U': [-1, 0],
    'D': [1, 0],
    'R': [0, 1],
    'L': [0, -1]
}

from collections import deque

for i in range(n):
    s = input()
    for j in range(m):
        if s[j]=='#':
            _map[i][j] = '#'

        if s[j] == 'S':
            start_r = i
            start_c = j
        if s[j] == 'F':
            fin_r = i
            fin_c = j
        if s[j] == 'D':
            door_r = i
            door_c = j
            _map[i][j]='D'
        if s[j] == 'K':
            key_r = i
            key_c = j

def seek(_map, start_r, start_c, fin_r, fin_c):
    
    stack = deque()
    visited = set()
    visited.add((start_r, start_c))
    string = ''
    stack.append((start_r, start_c, string))
    
    while stack:
        pos_r, pos_c, string = stack.popleft()
    
        if pos_r == fin_r and pos_c == fin_c:
            break
    
        for k, v in moves.items():
            new_r = pos_r + v[0]
            new_c = pos_c + v[1]
            new_string = string + k
            if (new_r, new_c) not in visited and 0<=new_r<n and 0<=new_c<m and _map[new_r][new_c] != '#':
                visited.add((new_r, new_c))
                stack.append((new_r, new_c, new_string))

    if pos_r == fin_r and pos_c == fin_c:
        return string
    else:
        return '-1'

    
_map_copy = [row[:] for row in _map] 
_map_copy[door_r][door_c] = '#'
ans_F_without_K = seek(_map_copy, start_r, start_c, fin_r, fin_c)
ans_K = seek(_map_copy, start_r, start_c, key_r, key_c)
_map_copy[door_r][door_c] = 'D'
ans_K_D = seek(_map_copy, key_r, key_c, door_r, door_c)
ans_K_D_F = seek(_map_copy, door_r, door_c, fin_r, fin_c)

Total = ans_K + 'P' + ans_K_D + ans_K_D_F

if '-1' in ans_F_without_K and '-1' in Total:
    print(-1)

elif ans_F_without_K =='-1':
    print(len(Total))
    print(Total)

else:
    print(len(ans_F_without_K))
    print(ans_F_without_K)


