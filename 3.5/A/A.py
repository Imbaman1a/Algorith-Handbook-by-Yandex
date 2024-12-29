n = input()
lst = list(map(int, input().split()))

def srt(lst1, lst2):
    lst_t = []
    while len(lst1) and len(lst2):
        if min(lst1) > min(lst2):
            lst_t.append(min(lst2))
            lst2.remove(min(lst2))
        else:
            lst_t.append(min(lst1))
            lst1.remove(min(lst1))
    while lst1:
        lst_t.append(min(lst1))
        lst1.remove(min(lst1))
    while lst2:
        lst_t.append(min(lst2))
        lst2.remove(min(lst2))
    
    return lst_t

def sorting(lst):
    if len(lst)==1:
        return lst
    firsthalf = lst[:len(lst)//2]
    secondhalf = lst[len(lst)//2:]
    sorted_1 = sorting(firsthalf)
    sorted_2 = sorting(secondhalf)
    total_lst = srt(sorted_1, sorted_2)
    return total_lst
lst = sorting(lst)
for i in range(int(n)):
    print(lst[i],end=' ')
