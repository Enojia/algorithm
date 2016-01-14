## insertionSort

def insertionSort(array, n):
    if(n>1):
        insertionSort(array, n-1)

    key= array[n]

    while(n>0 and array[n-1]>=key):
        temp = array[n]
        array[n] = array[n-1]
        array[n-1] = temp
        n-=1

array = [12, 32, 11, 1, 32, 31, 23, 14, 6]
insertionSort(array, len(array)-1)
print array
