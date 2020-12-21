
#! Bubble Sort

'''
Bubble sort is an algorithm that compares the adjacent elements and 
swaps their positions if they are not in the intended order. 
The order can be ascending or descending.


'''

def bubblesort(A):
    n = len(A)
    #  After each iteration, if there is no swapping taking 
    # place then, there is no need for performing further loops.
    swapped = True
    for passes in range(n-1,0,-1):
        for i in range(passes):
            if A[i] > A[i+1]:
                # temp = A[i]
                # A[i] = A[i+1]
                # A[i+1] = temp

                (A[i],A[i+1]) = (A[i+1],A[i])
                swapped = False

        # If there is not swapping in the last swap, then the array is already sorted.
        if swapped:
            break


A = [3, 5, 8, 9, 6, 2]
# A = [1,2,3,4,5,6]
print('Original Array:',A)
bubblesort(A)
print('Sorted Array:',A)


#! Complexity

'''
#? Time Complexities:

Worst Case Complexity:O(n2)
    If we want to sort in ascending order and the array is in descending order then, the worst case occurs.

Best Case Complexity:O(n)
    If the array is already sorted, then there is no need for sorting.

Average Case Complexity:O(n2)
    It occurs when the elements of the array are in jumbled order (neither ascending nor descending).

#? Space Complexity:
Space complexity is O(1) because an extra variable temp is used for swapping.

In the optimized algorithm, the variable swapped adds to the space complexity thus, making it O(2).

'''

#? Bubble Sort Applications

# the complexity of the code does not matter.
# a short code is preferred.