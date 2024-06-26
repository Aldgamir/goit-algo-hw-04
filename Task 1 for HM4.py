import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Створюємо генератор випадкових значень
random_data = [random.randint(0, 1000) for _ in range(1000)]

# Час сортування злиттям
merge_sort_time = timeit.timeit('merge_sort(random_data.copy())', globals=globals(), number=100)
print("Час сортування злиттям:", merge_sort_time)

# Час сортуванням вставками
insertion_sort_time = timeit.timeit('insertion_sort(random_data.copy())', globals=globals(), number=100)
print("Час сортування вставками:", insertion_sort_time)

# Час Timsort (вбудований алгоритм сортування Python)
timsort_time = timeit.timeit('sorted(random_data.copy())', globals=globals(), number=100)
print("Timsort час:", timsort_time)

if merge_sort_time < insertion_sort_time and merge_sort_time < timsort_time:
    print("Сортування злиттям є найшвидшим алгоритмом сортування")
elif insertion_sort_time < merge_sort_time and insertion_sort_time < timsort_time:
    print("Сортування вставками є найшвидшим алгоритмом сортування")
else:
    print("Timsort — найшвидший алгоритм сортування")
