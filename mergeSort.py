##merge sort
import vimpdb

def merge_sort(array, p, r):
    if p<r:
        q = (r+p)/2
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        #vimpdb.set_trace()
        return merge(array, p, q, r)

def merge(array, p, q, r):
    n1 = q-p+1
    n2 = r-q

    left = []
    right = []

    for i in range(0, n1):
        left.insert(0,array[p+i])

    for i in range(0, n2):
        right.insert(0,array[q+i+1])

    print left
    print right

    i = 0
    j = 0
    sortArray = []

    for h in range(0, r-p+1):
        sortArray.append(0)

    print "sortArray"
    print sortArray

    for k in range(p, r):
        if i<=q and left[i] <= right[j]:
            array[k]  = left[i]
            i+=1
        elif j<=r:
            array[k] = right[j]
            j+=1
    return array


array = [10, 23, 212, 23, 15, 13, 25, 36, 40]
merge_sort(array, 0, len(array))

