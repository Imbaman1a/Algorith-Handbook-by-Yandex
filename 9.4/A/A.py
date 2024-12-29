q = int(input())

stack = []

while(q):

    lst = list(map(int, input().split()))

    if lst[0] == 1:
        stack.append(lst[1])
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.pop()
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)


    q -= 1
