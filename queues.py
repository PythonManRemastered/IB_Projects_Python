import numpy as np
queue = [0,0,0,0]
while True: 
    x = int(input("Choose: 1.) Enter Data (Enqueue) 2.) Find last element (peek) 3.) Dequeue 4.) Check empty 5.) Leave \n"))
    if x == 1:
        n = int(input("Enter number of inputs (4 max, rear to front): "))
        for i in range(min(4,n)-1, -1, -1):
            queue[i] = int(input("Enter element: "))
        print("Queue: ", queue)

    elif x == 2:
        frontElement = queue[0]
        print("Front: ", frontElement)
        
    elif x == 3:
        k = int(input("Enter number of elements you want to dequeue: "))
        while k>len(queue):
            print("No!!!!!")
            k = int(input("Enter number of elements you want to dequeue: "))
        for i in range(0, k):
            queue[i] = 0
        print("Queue after Dequeue: ", queue)
        
    elif x == 4:

        try: print(not bool(np.unique(queue)))
        except: print(False)

    elif x == 5:
        break