def find_longest_increasing_subarray(arr):
    max_length = 1
    current_length = 1

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length



array = [1, 2, 4, 3, 5, 7, 8, 6, 9]
result = find_longest_increasing_subarray(array)

print(result)