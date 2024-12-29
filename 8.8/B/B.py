lst = input()
stack = []
ans = []
wrong = False
n = len(lst)
temp = ''
i = 0
while i < n:
    if lst[i]==' ':
        i += 1
        continue
    if lst[i].isdigit():
        while i < n and lst[i].isdigit():
            temp += lst[i]
            i += 1
        ans.append(temp)
        i -= 1
        temp = ''
    elif lst[i].isalpha():
        wrong = True
        break
    else:
        if lst[i] != ')':
            if lst[i]=='*':
                while stack and stack[-1] == '*' and stack[-1] != '(':
                    ans.append(stack.pop())
                stack.append(lst[i])
            elif lst[i]=='+' or lst[i]=='-':
                while stack and stack[-1] != '(':
                    ans.append(stack.pop())
                stack.append(lst[i])
            else:
                stack.append(lst[i])
        else:
            while stack and stack[-1] !='(':
                ans.append(stack.pop())
            if not stack:
                wrong = True
            else:
                stack.pop()
    i += 1
            
while stack:
    ans.append(stack.pop())

stack = []
if not wrong:
    for item in ans:
        if item.isdigit():
            stack.append(int(item))
        else:
            if len(stack)>=2:
                dig_2 = stack.pop()
                dig_1 = stack.pop()
            else:
                stack.extend([1,2,3])
                break
            if item == '+':
                stack.append(dig_1 + dig_2)
            if item == '-':
                stack.append(dig_1 - dig_2)
            if item == '*':
                stack.append(dig_1 * dig_2)
        #print(stack[-1])

    if (len(stack)>1):
        print('WRONG')
    else:
        print(stack[0])
else:
    print('WRONG')
