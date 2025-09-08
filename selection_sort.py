def selection_sort(array, size):
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
    return array
arr = [1,2,4,3,7,9, 8, 3, 7.6, 5]
size = len(arr)
print(selection_sort(arr, size))