def prog(n, A, B):
    C = ['']*n
    for i in range(n):
        C[i] = A[i]+B[i]
    
    return C


n = int(input())
A = input()
B = input()
C = prog(n, A, B)
for i in range(n):
    print(C[i], end='')
