
#! Merge Sort
#Merge Sort is a kind of Divide and Conquer algorithm in computer programming,so it uses recursive approach.




def mergesort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        # divide approach
        mergesort(A, left, mid)
        mergesort(A, mid+1, right)
        # conquer approach
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    i = left
    j = mid+1
    k = left #for temp list
    # temp list
    B = [0] * (right+1)
    while i <= mid and j <= right:
        if A[i] < A[j]:
            B[k] = A[i]
            i = i + 1
        else:
            B[k] = A[j]
            j = j + 1
        k = k + 1

    while i <= mid:
        B[k] = A[i]
        i = i + 1
        k = k + 1

    while j <= right:
        B[k] = A[j]
        j = j + 1
        k = k + 1

    # copying all items from to B
    for x in range(left,right+1):
        A[x] = B[x]

# Driver program
if __name__ == '__main__':
        A = [3, 5, 8, 9, 6, 2]
        print('Original Array:',A)
        mergesort(A,0,len(A)-1)
        print('Sorted Array:',A)

'''
#! Merge Sort Complexity

# ? Time Complexity

Best Case Complexity: O(n*log n)

Worst Case Complexity: O(n*log n)

Average Case Complexity: O(n*log n)

#? Space Complexity
The space complexity of merge sort is O(n).

#! Merge Sort Applications
- Inversion count problem
- External sorting
- E-commerce applications

'''