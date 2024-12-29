n, k, w = map(int, input().split())
costs = [0]*k
weeks = [0]*k
for i in range(k):
    costs[i], weeks[i] = map(int, input().split())

maxWeeks = n * w

combined_list = [[a, b] for a, b in zip(costs, weeks)]

combined_list.sort(reverse=True, key=lambda x: x[0])

profit = 0

for a, b in combined_list:

    if maxWeeks ==0:
        break
    amount = min(maxWeeks, b)
    profit += amount * a
    maxWeeks -= amount

print(profit)
