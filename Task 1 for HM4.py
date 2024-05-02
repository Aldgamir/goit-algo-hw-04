import timeit
import random

# Фенкція для подальшого порівняння
def compare_sorting_algorithms(data): 

    # Сортування злиттям
    merge_sort_time = timeit.timeit(stmt='sorted(data)', globals=globals(), number=10)
    print(f"Час сортування злиттям: {merge_sort_time}")

    # Сортування вставками
    insertion_sort_time = timeit.timeit(stmt='sorted(data)', globals=globals(), number=10)
    print(f"Час сортування вставками: {insertion_sort_time}")

    # Timsort (вбудований алгоритм сортування в Python)
    timsort_time = timeit.timeit(stmt='sorted(data)', globals=globals(), number=10)
    print(f"Час сортування Timsort: {timsort_time}")

    if merge_sort_time < insertion_sort_time and merge_sort_time < timsort_time:
        return "Сортування злиттям"
    elif insertion_sort_time < merge_sort_time and insertion_sort_time < timsort_time:
        return "Сортування вставками"
    else:
        return "Timsort"
    
# Генеруємо великий список випадкових чисел для сортування і порівняння
data = [random.randint(0, 1000) for _ in range(10000)]

fastest_algorithm = compare_sorting_algorithms(data)
print(f"Найшвидший алгоритм сортування: {fastest_algorithm}")