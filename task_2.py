# Реалізувати двійковий пошук для відсортованого масиву з дробовими числами. Написана функція для двійкового пошуку
# повинна повертати кортеж, де першим елементом є кількість ітерацій, потрібних для знаходження елемента.
# Другим елементом має бути "верхня межа" — це найменший елемент, який є більшим або рівним заданому значенню.

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        # Знаходимо серединний елемент та порівнюємо його з цільовим значенням
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return iterations, arr[mid]

    # Якщо елемент не знайдено, повертаємо кількість ітерацій та верхню межу
    # Верхня межа - це останній елемент, який є меншим за цільове значення
    if right >= 0:
        upper_bound = arr[right]
    else:
        upper_bound = None

    return iterations, upper_bound


# Приклад використання
arr = [0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3, 1.5, 1.7, 1.9]

# існуючий елемент
target = 1.3
iterations, upper_bound = binary_search(arr, target)
print("Кількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)

# не існуючий елемент
target = 1.2
iterations, upper_bound = binary_search(arr, target)
print("\nКількість ітерацій:", iterations)
print("Верхня межа:", upper_bound)
