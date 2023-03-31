def minimum(numbers):
    if len(numbers) == 1:
        return numbers[0]
    if numbers[0] > numbers[1]:
        numbers[0] = numbers[1]
    elif numbers[0] < numbers[1]:
        numbers[1] = numbers[0]
    return minimum(numbers[1:])