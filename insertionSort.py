## insertionSort

def insertion_sort(array):
    for i in range(1,len(array)):
        j = i-1
        while(array[j+1]<array[j] and j>=0 ):
            temp = array[j+1]
            array[j+1] = array[j]
            array[j] = temp
            j-=1

array = [2, 3, 1, 10, 8]
insertion_sort(array)
print array
