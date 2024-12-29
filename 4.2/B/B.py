def sumix(lst1, lst2, n1, n2):
    n_max = max(n1, n2)
    lst_c = [0]*(n_max+1)

    idx_1 = -1
    idx_2 = -1
    idx_c = -1

    while idx_1 >= -1 * (min(n1, n2) +1) and idx_2 >= -1 * (min(n1, n2) + 1):
        lst_c[idx_c] = lst1[idx_1] + lst2[idx_2]
        idx_c -= 1
        idx_1 -= 1
        idx_2 -= 1

    while idx_1 >= -1 * (n1 + 1):
        lst_c[idx_c] = lst1[idx_1]
        idx_c -= 1
        idx_1 -= 1
    while idx_2 >= -1 * (n2 +1 ):
        lst_c[idx_c] = lst2[idx_2]
        idx_c -= 1
        idx_2 -= 1

    return lst_c 


n_a = int(input())
A = list(map(int, input().split()))

n_b = int(input())
B = list(map(int, input().split()))

print(max(n_a,n_b))

res = sumix(A, B, n_a, n_b)

for i in range(len(res)):
    print(res[i], end=' ')
