def binary_search(array, value):
    
    low, high = 0, len(array) - 1

    while low <= high:
        middle = (high + low) // 2

        if array[middle] == value:
            return middle
        elif array[middle] < value:
            low = middle + 1
        else:
            high = middle - 1

    return None


b = [2, 2, 3, 6, 7, 7]

print(binary_search(b, 7))
