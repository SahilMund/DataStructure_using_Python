
#! Insertion Sort
'''
Insertion sort works similarly as we sort cards in our hand in a card game.

We assume that the first card is already sorted then, we select an unsorted card. If the unsorted card is greater than the card in hand, it is placed on the right otherwise, 
to the left. In the same way, other unsorted cards are taken and put at their right place.

'''


def insertionsort(A):
    n = len(A)
    for i in range(1,n):
        keyVal = A[i]
        position = i
        while position > 0 and A[position-1] > keyVal:
            A[position] = A[position-1]
            position = position - 1
        A[position] = keyVal


A = [3,5,8,9,6,2]
print('Original Array:',A)
insertionsort(A)
print('Sorted Array:',A)

#! Complextiy :-
'''

#? Time Complexities

Worst Case Complexity: O(n2)
Suppose, an array is in ascending order, and you want to sort it in descending order. In this case, worst case complexity occurs.

Each element has to be compared with each of the other elements so, for every nth element, (n-1) number of comparisons are made.

Thus, the total number of comparisons = n*(n-1) ~ n2
Best Case Complexity: O(n)
When the array is already sorted, the outer loop runs for n number of times whereas the inner loop does not run at all. So, there are only n number of comparisons. Thus, complexity is linear.
Average Case Complexity: O(n2)
It occurs when the elements of an array are in jumbled order (neither ascending nor descending).

# ? Space Complexity

Space complexity is O(1) because an extra variable key is used.

'''

# ? Insertion Sort Applications

# the array is has a small number of elements
# there are only a few elements left to be sorted
