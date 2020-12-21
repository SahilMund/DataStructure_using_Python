
#! Quick Sort

'''
Quicksort is an algorithm based on divide and conquer approach in which 
the array is split into subarrays and these sub-arrays are recursively called to sort the elements.
'''


#  Function to partition the array on the basis of pivot element
def partition(A, low, high):
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            i = i + 1
        while i <=j and A[j] > pivot:
            j = j - 1
        if i <= j:
            (A[i], A[j]) = (A[j], A[i])
        else:
            break
    (A[low], A[j]) = (A[j], A[low])
    return j


def quicksort(A, low, high):
    if low < high:
        # Select pivot position and put all the elements smaller 
        # than pivot on left and greater than pivot on right
        pi = partition(A, low, high)

        # Sort the elements on the left of pivot
        quicksort(A, low, pi - 1)

        # Sort the elements on the right of pivot
        quicksort(A, pi + 1, high)



A = [3, 5, 8, 9, 6, 2]
print('Original Array:',A)
quicksort(A, 0, len(A)-1)
print('Sorted Array:',A)


'''
#! Quicksort Complexity:-

# ? Time Complexities

Worst Case Complexity [Big-O]: O(n2)
    It occurs when the pivot element picked is either the greatest or the smallest element.
    This condition leads to the case in which the pivot element lies in an extreme end of the sorted array. One sub-array is always empty and another sub-array contains n - 1 elements. Thus, quicksort is called only on this sub-array.
    However, the quick sort algorithm has better performance for scattered pivots.

Best Case Complexity [Big-omega]: O(n*log n)
    It occurs when the pivot element is always the middle element or near to the middle element.
Average Case Complexity [Big-theta]: O(n*log n)
    It occurs when the above conditions do not occur.


# ? Space Complexity

The space complexity for quicksort is O(log n).

# ! Quicksort Applications

- the programming language is good for recursion
- time complexity matters
- space complexity matters
'''