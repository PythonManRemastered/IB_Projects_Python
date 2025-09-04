import bubble_sort
def binary_search(unsorted):
    unsorted = bubble_sort.bubble_sort(unsorted)
    find = int(input("Enter the number you wish to find: "))
    low = 0
    top = len(unsorted)-1

    while low <= top:
        mid = (low + top) // 2 
        if unsorted[mid] == find:
            print(f"Found at index {mid}")
            return 1
        elif find > unsorted[mid]:
            low = mid + 1
        else:
            top = mid - 1

    print("Not Found")
    return 0

unsorted = [1, 5, 3, 5, 7, 8, 24, 82, 482, 13, 18]
binary_search(unsorted)
