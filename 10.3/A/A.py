n, m = map(int, input().split())

games = [ list(map(int, input().split())) for _ in range(m)]

from collections import defaultdict

graph = defaultdict(list)

for u, v, t in games:
    if t==1:
        graph[u].append(v)
    else:
        graph[v].append(u)

visited = [0] * (n + 1)
stack = [0] * (n + 1)
        
def dfs(v, graph, visited, stack):
    visited[v] = 1
    stack[v] = 1
    for u in graph[v]:
        if not visited[u]:
            if dfs(u, graph, visited, stack):
                ans_1[u] = True
                return True
        elif stack[u]:
            ans_1[u] = True
            return True
    stack[v] = 0
    ans_1[v] = False
    return False



def dfs_connected(v):
    countix = 1
    visited_con[v] = 1
    for u in graph[v]:
        if not visited_con[u]:
            countix +=  dfs_connected(u)
    return countix
    

ans_1 = [0] * (n+1)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, graph, visited, stack)
        
ans_2 = [0] * (n+1)
lst = []
stats = False

for i in range(1, n+1):
    visited_con = [0] * (n + 1)
    ans_2[i] = dfs_connected(i)
    if ans_2[i] in ans_2[:i]:
        break

ans_2.sort()

if ans_2 == list(range(n+1)):
    stats = True
    
if any(s for s in ans_1[1:]):
    print('NO')
else:

    if stats:
        print('YES')
    else:
        print('NO')
