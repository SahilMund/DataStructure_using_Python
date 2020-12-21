
#! Recurisve methods


#? Algorithms :-

'''

binarySearch(arr, x, low, high)
    if low > high
        return False 
    else
        mid = (low + high) / 2 
        if x == arr[mid]
            return mid
        else if x < data[mid]        // x is on the right side
            return binarySearch(arr, x, mid + 1, high)
        else                               // x is on the right side
            return binarySearch(arr, x, low, mid - 1)
'''
def binaryseaarch_recursive(A, key, l, r):
    # A = array , Key = value to be searched , l=left index , r=right index
    if l > r:
        return -1
    else:
        mid = (l + r) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            return binaryseaarch_recursive(A,key,l,mid-1)
        elif key > A[mid]:
            return binaryseaarch_recursive(A,key,mid+1,r)

A = [15, 21, 47, 84, 96]
key = int(input("Enter a number to search :"))
found = binaryseaarch_recursive(A,key,0,len(A)-1)

if found == -1:
    print("Result Not Found ")
else:
    print('Result Found at:',found)

# Time complextiy is olog(n) i.e. worst case scenario.

