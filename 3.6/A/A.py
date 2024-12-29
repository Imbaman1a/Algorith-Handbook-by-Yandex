def partition(A):
    num = A[0]
    j= 0
    for i in range(1, len(A)):
        if A[i]<num:
            j += 1
            A[j], A[i] = A[i], A[j]
    A[0], A[j] = A[j], A[0]

    return A





n = int(input())
lst = list(map(int, input().split()))

lst = partition(lst)
for i in range(len(lst)):
    print(lst[i], end=' ')
