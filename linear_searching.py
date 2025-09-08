def linear_search(target, array):
    solution_arr = []
    for i in range(0, len(array)):
        if target == array[i]:
            solution_arr.append(i)
    if len(solution_arr) == 0:
        return("Not Found")
    return("Found at the following index values ", solution_arr)
array_checker = [1,2,3,6,2,5]
target = 5
print(linear_search(target, array_checker))
