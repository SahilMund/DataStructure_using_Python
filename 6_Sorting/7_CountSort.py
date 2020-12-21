
#! Count Sort

'''
Counting sort is a sorting algorithm that sorts the elements of an array by counting the number of occurrences of each unique element in the array.
The count is stored in an auxiliary array and the sorting is done by mapping the count as an index of the auxiliary array.
'''

def countsort(A):
    n = len(A)
    maxsize = max(A)
    cArray = [0] * (maxsize + 1)
    for i in range(n):
        cArray[A[i]] = cArray[A[i]] + 1
    i = 0 #index of cArray
    j = 0 #index of A
    while i < maxsize + 1:
        if cArray[i] > 0:
            A[j] = i
            j = j + 1
            cArray[i] = cArray[i] - 1
        else:
            i = i + 1


A = [3, 5, 8, 9, 6, 2, 3, 5, 5]
print('Original Array:',A)
countsort(A)
print('Sorted Array:',A)




'''
#! Complexity :-

#? Time Complexity
Worst Case Complexity: O(n+k)
Best Case Complexity: O(n+k)
Average Case Complexity: O(n+k)

In all the above cases, the complexity is the same because no matter how the elements are placed in the array, the algorithm goes through n+k times.

There is no comparison between any elements, so it is better than comparison based sorting techniques. But, it is bad if the integers are very large because the array of that size should be made.

#? Space Complexity:

The space complexity of Counting Sort is O(max). Larger the range of elements, larger is the space complexity.

# ! Counting Sort Applications

- there are smaller integers with multiple counts.
- linear complexity is the need.
'''

