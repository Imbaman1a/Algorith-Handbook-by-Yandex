n = int(input())


ans = dict()
countix = 1


for tens in range(n // 10 + 1):

    for fives in range((n - 10 * tens) // 5 + 1):

        ones = n - 10 * tens - 5 * fives

        string = '10 ' * tens + '5 ' * fives + '1 ' * ones
        string = string.strip()  

        if string not in ans.values():
            ans[countix] = string
            countix += 1


print(len(ans))


for key, values in ans.items():
    print(len(values.split()), values)

