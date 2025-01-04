n, m = map(int, input().split())
_map = [['.'] * m for _ in range(n) ]
for i in range(n):
    s = input()
    for j in range(m):
        if s[j]=='#':
            _map[i][j] = '#'

r, c = map(int, input().split())
q = int(input())
moves = input()

status_dict = {'upL':'left',
                'upR':'right',
                'leftL':'down',
                'leftR':'up',
                'downL':'right',
                'downR':'left',
                'rightL':'up',
                'rightR':'down'}

moves_dict = {
    'up' : [-1, 0],
    'left': [0,-1],
    'right': [0, 1],
    'down': [1, 0]
            }

status = 'up'
visited = set()
countix = 1
r, c = r-1, c-1

visited.add((r,c))

for xod in moves:
    if xod=='M':
        step = moves_dict[status]
        r_new = r + step[0]
        c_new = c + step[1]
        
        if r_new >=0 and r_new < n and c_new >=0 and c_new < m and _map[r_new][c_new]!='#':
            r, c = r_new, c_new
            if (r, c) not in visited:
                countix += 1
                visited.add((r,c))                
        
    else:
        status = status_dict[status+xod]
    #print(xod, status, countix)    
print(countix)

