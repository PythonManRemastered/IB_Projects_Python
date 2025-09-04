# Q1
def find_first(c, array):
    check = []
    min = len(array)
    for i in range(0, len(array)):
        if c == array[i]:
            check.append(i)
    for k in check:
        if k < min:
            min = k
    return min

##############################

# Q4

# a(i) => The program will throw an error, likely list index outside range
# a(ii) => Use a try-except statement, where any list index lesser than 0 or greater than 5 is given an error message requiring the user to enter a different number

def avg(numbers):
    sum = 0
    for k in numbers:
        sum += k
    return sum/len(numbers)

# c(i) => [78.43, 43.20,12.45, 3.12, 13.50,43.67]
# c(ii) => Swap the largest and smallest numbes in the array

def max_pos(numbers):
    max = numbers[0]
    max_index = 0
    for i in range(0, len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
            max_index = i
    return max_index

##############################

# Q5

# a => 16.30
# b => Find the sum of all values in the array 'Unit_Price', and divide this sum by the number of the elements in the array

def find_product(product_ID, unit_Price):
    index = input("Enter the product ID: ")
    st_index = -1
    for i in range(0, len(product_ID)):
        if product_ID[i] == index:
            st_index = i
    if st_index == -1:
        return "Product ID not found"
    else: 
        return unit_Price[st_index]

# d(i) => Maximum units that can be in array 'Three' is 10

def common(one, two, three):
    for i in range(0, len(one)):
        for j in range(0, len(two)):
            if one[i] == two[j]:
                three.append(one[i])
    return three

##############################

# Q8

def costperkm(age):
    if age<5:
        return 0
    if age >= 5 and age <= 15:
        return 0.2*0.5
    elif age > 65:
        return (0.2 -(0.2*0.3))
    
# 8b => 1.3 km
# 8c => 2.2km
# 8d => Find the sum of all distances with index between the indexes of the location names inclusive

def tcost(names, distances, d1, d2, age):
    loc1 = -1
    loc2 = -1
    for i in range(0, len(names)):
        if names[i] == d1:
            loc1 = i
        elif names[i] == d2:
            loc2 = i
    for i in range(loc1, loc2+1):
        sum += distances[i]
    return costperkm(age) * sum