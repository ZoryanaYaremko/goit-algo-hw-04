import timeit
import random
from tabulate import tabulate

# Функція сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Функція сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Функція Timsort (використовує вбудовану функцію sorted)
def tim_sort(arr):
    return sorted(arr)

# Генерація випадкових даних
def generate_data(size):
    random_data = [random.randint(1, 1000) for _ in range(size)]
    sorted_data = sorted(random_data)
    reverse_sorted_data = sorted_data[::-1]
    half_sorted_data = sorted_data[:size//2] + random_data[size//2:]
    return random_data, sorted_data, reverse_sorted_data, half_sorted_data

# Порівняння часу виконання
def compare_sorts(sizes):
    results = []
    for size in sizes:
        random_data, sorted_data, reverse_sorted_data, half_sorted_data = generate_data(size)
        
        result_row = [size]

        # Випадкові дані
        result_row.append(timeit.timeit(lambda: insertion_sort(random_data.copy()), number=1))
        result_row.append(timeit.timeit(lambda: merge_sort(random_data.copy()), number=1))
        result_row.append(timeit.timeit(lambda: tim_sort(random_data.copy()), number=1))

        # Відсортовані дані
        result_row.append(timeit.timeit(lambda: insertion_sort(sorted_data.copy()), number=1))
        result_row.append(timeit.timeit(lambda: merge_sort(sorted_data.copy()), number=1))
        result_row.append(timeit.timeit(lambda: tim_sort(sorted_data.copy()), number=1))

        # Зворотно відсортовані дані
        result_row.append(timeit.timeit(lambda: insertion_sort(reverse_sorted_data.copy()), number=1))
        result_row.append(timeit.timeit(lambda: merge_sort(reverse_sorted_data.copy()), number=1))
        result_row.append(timeit.timeit(lambda: tim_sort(reverse_sorted_data.copy()), number=1))

        # Наполовину відсортовані дані
        result_row.append(timeit.timeit(lambda: insertion_sort(half_sorted_data.copy()), number=1))
        result_row.append(timeit.timeit(lambda: merge_sort(half_sorted_data.copy()), number=1))
        result_row.append(timeit.timeit(lambda: tim_sort(half_sorted_data.copy()), number=1))

        results.append(result_row)

    headers = ["Size", "IS (Rand)", "MS (Rand)", "TS (Rand)", "IS (Sorted)", "MS (Sorted)", "TS (Sorted)", "IS (Rev)", "MS (Rev)", "TS (Rev)", "IS (Half)", "MS (Half)", "TS (Half)"]
    print(tabulate(results, headers=headers, floatfmt=".6f", tablefmt="github"))

# Вказуємо розміри масивів для тестування
sizes = [10, 100, 1000, 10000]
compare_sorts(sizes)


