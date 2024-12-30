from collections import deque

deq = deque()
q = int(input())

while q:

    lst = list(map(int, input().split()))

    if lst[0]==1:
        deq.append(lst[1])
        print(deq[0])

    else:
        deq.popleft()

        if deq:
            print(deq[0])
        else:
            print(-1)




    q -= 1

