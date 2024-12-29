n, L = map(int, input().split())

lst = list(map(int, input().split()))

lst.sort()

countix = 0
sum_len = 0
left_pointer = 0
right_pointer = 0

visited = set()
visited.add(left_pointer)

while(left_pointer < n and right_pointer + 1 < n):
    
    visited.add(right_pointer)
    sum_len = lst[right_pointer + 1] - lst[left_pointer]
    
    if sum_len < L:

        right_pointer += 1

    elif sum_len == L:
        countix += 1
        visited.add(right_pointer + 1)
        left_pointer = right_pointer + 2
        right_pointer = left_pointer

    else:
        countix += 1
        left_pointer = right_pointer + 1
        right_pointer = left_pointer
            
if (n-1) not in visited:
    countix += 1
        
print(countix)
