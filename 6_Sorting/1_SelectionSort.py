
#! Selection Sort
# Selection sort is an algorithm that selects the smallest element from an unsorted list in each iteration and places that element at the beginning of the unsorted list.


def selectionsort(A):
    for i in range(len(A)-1):
        minimum_index = i
        for j in range(i+1, len(A)):
            if A[j] < A[minimum_index]:
                minimum_index = j
        # temp = A[i]
        # A[i] = A[minimum_index]
        # A[minimum_index] = temp

        # Swapping the two values
        (A[i],A[minimum_index]) = (A[minimum_index],A[i])


A = [3, 5, 8, 9, 6, 2]
print('Original Array:',A)
selectionsort(A)
print('Sorted Array:',A)

#? Complexity :-

'''
Number of comparisons: (n - 1) + (n - 2) + (n - 3) + ..... + 1 = n(n - 1) / 2 nearly equals to n2.

#! Complexity = O(n2)

Also, we can analyze the complexity by simply observing the number of loops. There are 2 loops so the complexity is n*n = n2.

#? Time Complexities:

Worst Case Complexity: O(n2)
    If we want to sort in ascending order and the array is in descending order then, the worst case occurs.
Best Case Complexity: O(n2)
    It occurs when the array is already sorted
Average Case Complexity: O(n2)
    It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

The time complexity of the selection sort is the same in all cases. At every step, you have to find the minimum element and put it in the right place.
The minimum element is not known until the end of the array is not reached.

#? Space Complexity:

Space complexity is O(1) because an extra variable temp is used.

'''

#?Selection Sort Applications
'''
- a small list is to be sorted
- cost of swapping does not matter
- checking of all the elements is compulsory
- cost of writing to a memory matters like in flash memory (number of writes/swaps is O(n) as compared to O(n2) of bubble sort)
'''