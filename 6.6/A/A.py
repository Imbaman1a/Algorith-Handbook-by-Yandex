n = int(input())

lst = list(map(int, input().split()))

def check(num1, num2):
    if num2 < 0:
        return True
    if int(str(num1)+str(num2)) > int(str(num2)+str(num1)):
        return True
    else:
        return False
    
def Largest(lst):
    salary = ''
    while lst:
        maxNumber= float('-inf')
        for num in lst:
            if check(num, maxNumber):
                maxNumber = num
        salary = salary + str(maxNumber)
        lst.remove(maxNumber)
    return salary

print(Largest(lst))
