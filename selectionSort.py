##selection sort algo

def selectionSort(array):
    for i in range(0,len(array)):
        key = array[i]

        for j in range(i+1, len(array)):
            if array[j] < key:
                temp = array[j]
                array[j] = key
                array[i] = temp
                key = array[i]
    return array


def main():
    array = [10, 23, 12, 32, 22, 32, 1, 2]
    sortedArray= selectionSort(array)
    print sortedArray

main()
