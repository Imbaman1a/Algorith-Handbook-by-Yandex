def start_pos(_map, k, s):
    #k - ot 1 do k, s - razmer s x s
    R = len(_map)
    C = len(_map[0])
    s = s - 1
    dicty = {num: [] for num in range(1, k + 1)}
    for num in range(1, k+1):
        find = False
        if not find:
            for i in range(len(_map)):
                for j in range(len(_map[0])):
                    if _map[i][j] == str(num):
                        if i+s < R and j+s < C and _map[i+s][j+s] == str(num):
                            dicty[num].append((i, j))
                            find = True
                            break
                        
                        else:
                            
                            #можно проходить от -s до +s от текущей позиции по высоте и ширине
                            i_min = dicty_min_max[num][0]
                            i_max = dicty_min_max[num][1]
                            j_min = dicty_min_max[num][2]
                            j_max = dicty_min_max[num][3]
                            
                            
                            top = max(0, i_max - s)
                            left = max(0, j_max - s)
                            bot = min(R, i_min + s)
                            right = min(C, j_min + s)
                            
                            #bottom = min(R, i+s)
                            #right = min(C, j+s)
                            for r in range(top, bot - s + 1):
                                for c in range(left, right - s + 1):
                                    #print(r,c, end=' ')
                                    if not any("." in row[c:c+s+1] for row in _map[r:r+s+1]) and any(str(num) in row[c:c+s+1] for row in _map[r:r+s+1])and c+s < C and r+s < R :
                                        dicty[num].append((r, c))
                            find = True
                            break
                
                if find:
                    break
                        
    return dicty


def min_max(_map, k):
    R = len(_map)
    C = len(_map[0])
    dicty = {num: [] for num in range(1, k + 1)}
    for num in range(1, k+1):
        i_min, i_max = 1e7, -1e7
        j_min, j_max = 1e7, -1e7
        dicty[num] = [i_min, i_max, j_min, j_max]
    for i in range(R):
        for j in range(C):
            if _map[i][j].isdigit():
                lst = dicty[int(_map[i][j])]
                i_min = lst[0]
                i_max = lst[1]
                j_min = lst[2]
                j_max = lst[3]

                if i > i_max:
                    dicty[int(_map[i][j])][1] = i
                if i < i_min:
                    dicty[int(_map[i][j])][0] = i
                if j > j_max:
                    dicty[int(_map[i][j])][3] = j
                if j < j_min:
                    dicty[int(_map[i][j])][2] = j
                
    return dicty
            

from itertools import permutations, product

with open(r'input.txt', 'r') as f:
    lst = f.readlines()
t = int(lst[0].strip())
test_cases = []
idx = 1
for _ in range(t):
    n, m, k, s = map(int, lst[idx].strip().split())
    idx += 1 

    desk = []
    for _ in range(n):
        desk.append(lst[idx].strip())
        idx += 1

    test_cases.append((n, m, k, s, desk))

jav = []

for n, m, k, s, _map in test_cases:
    dicty_min_max = min_max(_map, k)
    start_dict = start_pos(_map, k, s)

    keys = list(start_dict.keys())
    key_permutations = permutations(keys)

    # Итоговый список комбинаций
    all_combinations = []

    # Для каждой перестановки ключей генерируем продукты значений
    for perm in key_permutations:
        # Получаем список всех значений для текущей перестановки
        value_combinations = product(*(start_dict[key] for key in perm))
        for combination in value_combinations:
            # Соединяем ключи и соответствующие значения
            result = {perm[i]: combination[i] for i in range(len(perm))}
            all_combinations.append(result)
    K = k
    countix = 0
    
    #Global = set()
    # Вывод всех комбинаций
    for combo in all_combinations:

        visited = set()
        #ans = []
        for k, v in combo.items():
            i = v[0]
            j = v[1]
            temp0 = []
            for row in range(i, i+s):
                for col in range(j, j+s):
                    temp0.append(_map[row][col] == str(k) or _map[row][col] not in visited)
            check = all(temp0)
            
            if check:
                #print(check, k, i , j)
                visited.add(str(k))
                
        if len(visited)==K:
            countix += 1

    jav.append(countix)


with open('output.txt', 'w') as f:
    for item in jav:
        f.write(str(item) + '\n')
