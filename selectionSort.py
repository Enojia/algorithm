##selection sort algo

def selectionSort(array):
    for i in range(0,len(array)-1):    ## (n-1)
        key = array[i]                 ##1

        for j in range(i+1, len(array)):  ##(n-1)
            if array[j] < key:   ## 1
                temp = array[j]  ## 1
                array[j] = key   ## 1
                array[i] = temp  ## 1
                key = array[i]   ## 1
    return array ## 1
## best case scenario theta(n²) running time: n²
# worst case scenraio theta(n²) running time: 6n² - 11n + 5

def main():
    array = [10, 23, 12, 32, 22, 32, 1, 2]
    sortedArray= selectionSort(array)
    print sortedArray

main()
