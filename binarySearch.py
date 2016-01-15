import sys

def Binsearch(array, value, hi, lo):

    while hi>lo:
        mid = (hi+lo)/2
        if array[mid]>value:
            hi = mid
            Binsearch(array, value, hi, lo)
        elif array[mid]<value:
            lo = mid+1
            Binsearch(array, value, hi, lo)
        elif array[mid] == value:
            print "object find at %d" %(mid)
            return
    print "value not find in the array"



array = [2, 4, 13, 24, 25]
Binsearch(array, 0, len(array), 0)
