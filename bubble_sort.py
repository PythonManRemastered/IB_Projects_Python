def bubble_sort(unsorted):
    for i in range(0, len(unsorted)):
        for j in range(0, len(unsorted)-i-1):
            if unsorted[j] > unsorted[j+1]:
                unsorted[j+1], unsorted[j] = unsorted[j], unsorted[j+1]
    print(unsorted)
    return(unsorted)
