#!/python

def bubbleSort(array):
    for j in range(len(array)-1, 0, -1):
        for i in range(0,j):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp


array = [15, 2, 23, 43, 23, 12, 23, 4, 1]
bubbleSort(array)
print array
