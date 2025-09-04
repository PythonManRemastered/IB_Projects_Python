# crazy 2am programming motivation
# no gpt somehow :)
# modelling average primary diagonal sums for randomised boolean matrices with various matrix sizes
# initial observed outcome: generally increasing average diagonal sums with increases in matrix sizes
import time
import random
import numpy as np
import matplotlib.pyplot as plt
avg = []
# hello 
times = []
def dig_sum(matrix_1):
    sum = 0
    for i in range(0, len(matrix_1)):
        sum += matrix_1[i][i]
    return sum
for n in range(1,100):
    start = time.time()
    existence = []
    for k in range(n):
        arr_matrix = []
        for j in range(n):
            arr_inter = []
            for i in range(n):
                arr_inter.append(random.randint(0,1))
            arr_matrix.append(arr_inter)
        existence.append(dig_sum(arr_matrix))
    end = time.time()
    print("With trial repetition size of " + str(n) + " the average primary diagonal value is " + str(np.average(existence)))
    times.append(start-end)
    avg.append(np.average(existence))


plt.subplot()

plt.plot([i for i in range(1,100)], avg)
plt.title("DSum")

plt.subplot()
plt.plot([i for i in range(1,100)], times)
plt.title("Times")

plt.show()