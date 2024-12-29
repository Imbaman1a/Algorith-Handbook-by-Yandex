def count_inv(lst):
    if len(lst)<=1:
        return 0
    #lst.sort()
    left_lst = lst[:len(lst)//2]
    right_lst = lst[len(lst)//2:]
    left_inv = count_inv(left_lst)
    right_inv = count_inv(right_lst)
    #print(left_lst, right_lst, left_inv, right_inv)
    split_inv = merge(left_lst, right_lst)
    return left_inv + right_inv + split_inv
def merge(left_lst, right_lst):
    left_lst.sort()
    right_lst.sort()
    #sorted_l = []
    inv = 0
    l, r = 0, 0
    leng_l = len(left_lst)
    leng_r = len(right_lst)
    while l < leng_l and r < leng_r:
        l_el = left_lst[l]
        r_el = right_lst[r]
        if l_el <= r_el:
            #sorted_l.append(l_el)
            l += 1
        else:
            #sorted_l.append(r_el)
            inv += leng_l - l
            r += 1
    #if l < len(left_lst):
        #sorted_l.extend(left_lst[l:])
    #if r < len(right_lst):
        #sorted_l.extend(right_lst[r:])
    
    return inv
n = int(input())
lst = list(map(int, input().split()))
sorted_lst = sorted(lst)
dicty = {}
for idx, num in enumerate(sorted_lst):
    dicty[num] = idx
indexes = []
for i in range(n):
    indexes.append(dicty[lst[i]])

dicty = {}
for idx, num in enumerate(lst):
    dicty[num] = idx    
    
T1 = count_inv(indexes)
minimum = T1
for i in range(n, 1, -1):
    T = T1 + 2 * dicty[i] - n + 1
    minimum = min(minimum, T)
    #print(minimum)
    T1 = T
print(minimum)
