##merge sort
##import vimpdb

def insertion_sort(array, p, r):
    for i in range(p+1, r+1):
        j = i-1
        while (array[j+1]<array[j] and j>=p):
            temp = array[j+1]
            array[j+1] = array[j]
            array[j] = temp
            j-=1


def mixed_sort(array, p, r):
    if p >= r:
        print "Error need debugging"
        return
    if r-p < 15:
        print array[p:r]
        print "beginning"
        insertion_sort(array,p,r)
        print array[p:r]
        return

    else:                          ##n
        q = (r+p)//2                 ##n
        mixed_sort(array, p, q)
        mixed_sort(array, q+1, r)
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


array = [10, 23, 212 , 15, 13, 25, 36, 40, 10, 2, 4, 65, 78, 89, 2, 23, 41, 34, 3, 1,45, 65, 63, 23, 13]
mixed_sort(array, 0, len(array)-1)
print array
