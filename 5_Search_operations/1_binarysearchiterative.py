# for binary search the array(or)list  must be in sorted order otherwise it will not work.

# In this approach, the element is always searched in the middle of a portion of an array.

#? Binary Search Algorithm can be implemented in two ways which are discussed below.

#! Iterative Method :-

#? Algorithms :-
'''
do until the pointers low and high meet each other.
    mid = (low + high)/2
    if (x == arr[mid])
        return mid
    else if (x > A[mid]) // x is on the right side
        low = mid + 1
    else                       // x is on the left side
        high = mid - 1

'''

#? Code:-

def binarysearch_iterative(A, key):
    l = 0
    r = len(A)-1
    while l <= r:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            r = mid - 1
        elif key > A[mid]:
            l = mid + 1
    return -1

A = [15,21,47,84,96]
key = int(input("Enter a number to search :"))
found = binarysearch_iterative(A,key)

if found == -1:
    print("Result Not Found ")
else:
    print('Result Found at:',found)


#?  Complexities
'''
Time Complexity :-

Best case complexity: O(1)
Average case complexity: O(log n)
Worst case complexity: O(log n)

Space Complexity:-

The space complexity of the binary search is O(n).

'''

#? Applications:-
#While debugging, the binary search is used to pinpoint the place where the error happens.