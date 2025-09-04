def name_func():
    x = [1,3,5,7,9]
    y = []
    for i in range(len(x)-1, -1,-1):
        y.append(x[i])
    print(y)

def array_list():
    x = int(input("Enter array size: "))
    hold_arr = []
    even_sum = 0
    odd_count = 0
    sum = 0
    for i in range(x):
        y = int(input("Enter a number: "))
        hold_arr.append(y)
        if y%2 == 0:
            even_sum += y
        else:
            odd_count += 1
        sum += y
    
    print("The sum is " + str(sum))
    print("The average is " + str(sum/x))
    print("The odd count is " + str(odd_count))
    print("The array was " + str(hold_arr))

def sum_of_elements():
    size_array = int(input("Enter size of array: "))
    sum = 0
    el_array = []
    for i in range(size_array):
        check = int(input("Enter array element: "))
        el_array.append(check)
        sum += check
    print("The sum of the entered elements is " + str(sum))

def largest_smallest():
    arr_check = [1,4,2,54,29,-29]
    max = arr_check[0]
    min = arr_check[0]
    for i in arr_check:
        if i > max:
            max = i
        elif i < min: 
            min = i
    print("The largest element in the array is " + str(max))
    print("The smallest element in the array is " + str(min))

def reverse_in_place():
    array_check = [1,2,3,4,5]
    i = 0
    while i <= len(array_check)-i-1:
        array_check[i], array_check[len(array_check)-i-1] = array_check[len(array_check)-i-1], array_check[i]
        i+= 1
    print(array_check) # check why return(array_check) doesn't work

def find_name():
    array_names = ["John", "Jimmy", "Jaquarius", "Demarcus"]
    array_phone_numbers = [1111111111,2222222222,3333333333,4444444444]
    name = input("Enter name: ")
    check = 0 
    for i in range(0, len(array_names)):
        if array_names[i] == name:
            check = i
    print("The corresponding phone number: ", array_phone_numbers[check])