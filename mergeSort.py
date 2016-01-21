##merge sort
##import vimpdb

def merge_sort(array, p, r):
    if p<r:                          ##n
        q = (r+p)//2                 ##n
        merge_sort(array, p, q)      
        merge_sort(array, q+1, r)
        #vimpdb.set_trace()
        merge(array, p, q, r)

def merge(array, p, q, r):
    n1 = q-p+1
    n2 = r-q

    left = []
    right = []

    for g in range(0, n1):
        left.append(array[p+g])

    for h in range(0, n2):
        right.append(array[q+h+1])

    i = 0
    j = 0

    for k in range(p, r+1):
        if i<len(left) and (j==len(right) or left[i] <= right[j]):
            array[k]  = left[i]
            i+=1
        else:
            array[k] = right[j]
            j+=1


array = [10, 23, 212 , 15, 13, 25, 36, 40, 10, 2, 4, 65]
merge_sort(array, 0, len(array)-1)
print array
