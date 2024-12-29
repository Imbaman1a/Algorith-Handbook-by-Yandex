def MaximumLoot(W, weight_l, cost_l):
    n = len(weight_l)
    value = 0.0
    # Вычисляем ценность за единицу веса
    cost_per_weight = [(cost_l[i] / weight_l[i], weight_l[i], cost_l[i]) for i in range(n)]
    
    # Сортируем по убыванию ценности за единицу веса
    cost_per_weight.sort(reverse=True, key=lambda x: x[0])
    
    for cost_per, weight, cost in cost_per_weight:
        if W == 0:
            break  # Если рюкзак заполнен
        # Берём максимальный возможный вес
        amount = min(weight, W)
        value += cost_per * amount
        W -= amount
    
    return value

# Чтение входных данных
n, W = map(int, input().split())
cost_l = [0] * n
weight_l = [0] * n

for i in range(n):
    cost_l[i], weight_l[i] = map(int, input().split())

# Вычисляем максимальную ценность
result = MaximumLoot(W, weight_l, cost_l)

# Выводим результат с округлением до 4 знаков после запятой
print(f"{result:.4f}")

