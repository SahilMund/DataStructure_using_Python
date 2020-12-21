
#! Shell Sort

'''
Shell sort is an algorithm that first sorts the elements far apart from each other and successively reduces the interval between the elements to be sorted.
It is a generalized version of insertion sort.

In shell sort, elements at a specific interval are sorted. The interval between the elements is gradually decreased based on the sequence used. The performance of the shell 
sort depends on the type of sequence used for a given input array.
'''

def shellsort(A):
    n = len(A)
    gap = n//2
    while gap > 0:
        i = gap
        while i < n:
            temp = A[i]
            j = i - gap
            while j >= 0 and A[j] > temp:
                A[j+gap] = A[j]
                j = j - gap
            A[j+gap] = temp
            i = i + 1
        gap = gap // 2


A = [3, 5, 8, 9, 6, 2]
print('Original Array:',A)
shellsort(A)
print('Sorted Array:',A)


#! Complexity
'''
Shell sort is an unstable sorting algorithm because this algorithm does not examine the elements lying in between the intervals.

#? Time Complexity
Worst Case Complexity: less than or equal to O(n2)
Worst case complexity for shell sort is always less than or equal to O(n2).

According to Poonen Theorem, worst case complexity for shell sort is Θ(Nlog N)2/(log log N)2) or Θ(Nlog N)2/log log N) or Θ(N(log N)2) or something in between.
Best Case Complexity: O(n*log n)
When the array is already sorted, the total number of comparisons for each interval (or increment) is equal to the size of the array.
Average Case Complexity: O(n*log n)
It is around O(n1.25).

The complexity depends on the interval chosen. The above complexities differ for different increment sequences chosen. Best increment sequence is unknown.

#? Space Complexity:
The space complexity for shell sort is O(1).
'''


#! Shell Sort Applications

# calling a stack is overhead. uClibc library uses this sort.
# recursion exceeds a limit. bzip2 compressor uses it.
# Insertion sort does not perform well when the close elements are far apart. Shell sort helps in reducing the distance between the close elements. Thus, there will be less number of swappings to be performed.

