def bubble_sort(numbers):
    result = list(numbers)  # copy, so the original is not changed
    n = len(result)
    for i in range(n):
        for j in range(n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result