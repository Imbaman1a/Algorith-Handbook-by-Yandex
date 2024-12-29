def min_total_length(n, k, points):
    if k >= n:
        return 0  # Если отрезков больше или столько же, как точек, длина будет 0 (отрезки нулевой длины)

    points.sort()  # Сортируем точки по возрастанию
    # Находим расстояния между соседними точками
    gaps = [points[i + 1] - points[i] for i in range(n - 1)]
    
    # Сортируем разрывы по убыванию
    gaps.sort(reverse=True)

    # Минимальная длина - сумма всех расстояний минус (k-1) самых больших разрывов
    min_length = sum(gaps) - sum(gaps[:k - 1])

    return min_length

n, k = map(int, input().split())

lst = list(map(int, input().split()))

print(min_total_length(n, k, lst))
