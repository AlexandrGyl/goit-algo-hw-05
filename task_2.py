


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iteration = 0
    upper_limit = None
 
    while low <= high:
        iteration += 1 
        mid = (high + low) // 2
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_limit = arr[mid]
            high = mid - 1
 
        # інакше x присутній на позиції і повертаємо його
        else:
            upper_limit = arr[mid]
            break
 
    # якщо елемент не знайдений, встановлюємо верхню межу
    if upper_limit is None:
        if low < len(arr):
            upper_limit = arr[low]
        else:
            upper_limit = None  # якщо x більше за всі елементи в масиві

    return (iteration, upper_limit)


sorted_array = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
target_value = 10
result = binary_search(sorted_array, target_value)
print(result)  