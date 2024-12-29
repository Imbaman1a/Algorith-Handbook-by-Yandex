class Node():
    def __init__(self, val, ptr=None):
        self.val = val
        self.ptr = ptr


first_time = True
counter = 0
q = int(input())

while(q):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        x = arr[1]
        y = arr[2]
        y  = Node(y)
        counter += 1
        if x == 0:
            if first_time:
                first_time = False
                head = y
            else:
                y.ptr = head
                head = y
        else:
            target = head
            for i in range(x-1):
                target = target.ptr
            temp = target.ptr 
            target.ptr = y
            y.ptr = temp
            #head = y

    elif arr[0] == 2:
        x = arr[1]
        force = head
        for i in range(x-1):
            force = force.ptr
        
        if counter < x:
            print('FUCK')
            
        else:
            print(force.val)
            
    
    elif arr[0] == 3:
        counter -= 1
        x = arr[1]
        if x !=1:
            target = head
            prev = target
            for i in range(x-1):
                prev = target
                target = target.ptr
            prev.ptr = target.ptr
            if counter == 0 :
                first_time = True
        else:
            head = head.ptr

    q -= 1
