# Two dimensional array - Programming assignment
# 1 Construct code that creates a two-dimensional array or list with three rows and three columns. Fill it with values read from the keyboard. Calculate the sum of all values and their average,
#  and display the results. 
 
# 2 Construct a program that creates a two-dimensional array or list with three rows and three columns. Display the sum of all elements per column. Display the average of all elements per row. 
 
# 3 Construct code that creates a two-dimensional array or list with three rows and three columns that stores random numbers. 
# Display the array and output the sum of all the elements on the principal diagonal. Calculate the sum of the elements on the secondary diagonal and display this value as well.
import random
import numpy as np 

def q1():
    x = int(input("Enter columns: "))
    y = int(input("Enter rows: "))
    arr1 = [[0 for i in range(x)] for j in range(y)]
    print(arr1)
    count = 0
    sum = 0
    for i in range(0, 3):
        x = arr1[i]
        for j in range(0, 3):
            num = int(input("Enter element: "))
            x[j] = num
            sum += num
            count +=1 
    print(arr1)
    print(sum)
    print(sum/count)

def q2():
    arr1 = [[1,2,3], [2,3,4], [5,9,10]]
    col_sum = 0 
    col_sum_arr = []
    row_avg = 0
    row_avg_arr = []
    for i in range(0,3):
        for j in range(0,3):
            s = arr1[j]
            col_sum += s[i]
        col_sum_arr.append(col_sum)
        col_sum = 0
    for i in range(0,3):
        x = arr1[i]
        for j in range(0,3):
            row_avg += x[j]
        row_avg_arr.append(row_avg/3)
        row_avg = 0
    print(arr1, col_sum_arr, row_avg_arr)

def q3():
    arr1 = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(0, 3):
        arr2 = arr1[i]
        for j in range(0,3):
            arr2[j] = random.random()

    i = 0
    j = 0
    p_diag_sum = 0 
    s_diag_sum = 0
    while i <= 2 and j <= 2:
        arr3 = arr1[i]
        p_diag_sum += arr3[j]
        i += 1
        j += 1

    i = 0
    j = 2

    while i <= 2 and j >= 0:
        arr4 = arr1[i]
        s_diag_sum += arr4[j]
        i += 1
        j -= 1        

    print("This is the original array", arr1)   
    print("This is the principal diagonal sum", np.round(p_diag_sum, 2))
    print("This is the secondary diagonal sum", np.round(s_diag_sum, 2))
