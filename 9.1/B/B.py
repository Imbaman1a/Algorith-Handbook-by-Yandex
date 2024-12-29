n = int(input())

lst = list(map(int, input().split()))

lst_prefix_max = [0] * n

lst_prefix_min = [0] * n

lst_sufix_max = [0] * (n-1)

lst_sufix_min = [0] * (n-1)

min_val = 1e7
max_val = -1e7
for i in range(n):
    if lst[i] > max_val:
        max_val = lst[i]
        idx = i
    lst_prefix_max[i] = idx
    
for i in range(n):
    if lst[i] < min_val:
        min_val = lst[i]
        idx = i
    lst_prefix_min[i] = idx
    
min_val = 1e7
max_val = -1e7

for i in range(n-1, 0, -1):
    if lst[i] > max_val:
        max_val = lst[i]
        idx = i
    lst_sufix_max[i-1] = idx
    
for i in range(n-1, 0, -1):
    if lst[i] < min_val:
        min_val = lst[i]
        idx = i
    lst_sufix_min[i-1] = idx
    
min_val = 1e7
max_val = -1e7

min_ans = []
max_ans = []

for i in range(n-1):
    max_delta = lst[lst_prefix_max[i]] - lst[lst_sufix_min[i]]
    min_delta = lst[lst_prefix_min[i]] - lst[lst_sufix_max[i]]
    if min_delta < min_val:
        min_val = min_delta
        min_l = lst_prefix_min[i]
        min_r = lst_sufix_max[i]

    if max_delta > max_val:
        max_val = max_delta
        max_l = lst_prefix_max[i]
        max_r = lst_sufix_min[i]

for i in range(n-1):
    max_delta = lst[lst_prefix_max[i]] - lst[lst_sufix_min[i]]
    min_delta = lst[lst_prefix_min[i]] - lst[lst_sufix_max[i]]
    
    if min_delta == min_val:
        min_ans.append([lst_prefix_min[i], lst_sufix_max[i]])
    if max_delta == max_val:
        max_ans.append([lst_prefix_max[i], lst_sufix_min[i]])

        
seen = set()
unique_data_mins = []
for item in min_ans:
    t = tuple(item)
    if t not in seen:
        unique_data_mins.append(item)
        seen.add(t)

seen = set()
unique_data_maxs = []
for item in max_ans:
    t = tuple(item)
    if t not in seen:
        unique_data_maxs.append(item)
        seen.add(t)        
        
min_ans.sort(key=lambda x: (x[0], x[1]))
max_ans.sort(key=lambda x: (x[0], x[1]))

min_l = min_ans[0][0]

for i in range(min_l + 1, n):
    if lst[min_l] - lst[i]==min_val:
        min_r = i
        #print(min_r)
        break
max_l = max_ans[0][0]
for i in range(max_l + 1, n):
    if lst[max_l] - lst[i]==max_val:
        max_r = i
        #print(max_r)
        break

print(min_l + 1, min_r +1)
print(max_l + 1, max_r +1)
