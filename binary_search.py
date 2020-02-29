def binary_search(list, item):
    # В переменных low и high хранятся границы той части списка, в которой выполняется поиск
    low = 0
    high = len(list) - 1

    # Пока эта часть не скоратится до одного элемента...
    while low <= high:
        # ... проверяем средний элемент
        mid = (low + high) // 2
        guess = list[mid]
        # Значение найдено
        if guess == item:
            return mid
        # Много
        if guess > item:
            high = mid - 1
        # Мало
        else:
            low = mid + 1
    # Значение не существует
    return None


my_list = [1, 2, 3, 7, 8, 10]

binary_search(my_list, 3)
