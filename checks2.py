numbers = [7,3,2,9]
for i in range (len(numbers)) :
    for j in range (0, len(numbers)-1-i):
        if numbers [j]<numbers[j+1]:
            temp = numbers[j]
            numbers [j] =numbers [j+1]
            numbers [j+1] =temp
for i in range (len(numbers)) :
    print (numbers[i], " ", end="")