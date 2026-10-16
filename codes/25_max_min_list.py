def find_max_min(numbers):
    if len(numbers) == 0:
        raise ValueError("List is empty")
    maximum = numbers[0]
    minimum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n
    return (maximum, minimum)