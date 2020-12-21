
#! Radix Sort

'''
adix sort is a sorting technique that sorts the elements by first grouping the individual digits of the same place value.
 Then, sort the elements according to their increasing/decreasing order.
'''
def radixsort(A):
    n = len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    l = []
    bins = [l] * 10
    for i in range(digits):
        for j in range(n):
            e = int((A[j] / pow(10, i)) % 10)
            if len(bins[e]) > 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]

                
        k = 0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k = k + 1


A = [63, 250, 835, 947, 651, 28]
print('Original Array:',A)
radixsort(A)
print('Sorted Array:',A)

'''
#! Complexity

Since radix sort is a non-comparative algorithm, it has advantages over comparative sorting algorithms.

For the radix sort that uses counting sort as an intermediate stable sort, the time complexity is O(d(n+k)).

Here, d is the number cycle and O(n+k) is the time complexity of counting sort.

Thus, radix sort has linear time complexity which is better than O(nlog n) of comparative sorting algorithms.

If we take very large digit numbers or the number of other bases like 32-bit and 64-bit numbers then it can perform in linear time however the intermediate sort takes large space.

This makes radix sort space inefficient. This is the reason why this sort is not used in software libraries.

# ? Radix Sort Applications

DC3 algorithm (Kärkkäinen-Sanders-Burkhardt) while making a suffix array.
places where there are numbers in large ranges.
'''