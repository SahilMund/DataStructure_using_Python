
#! Linear Search

#Linear search is the simplest searching algorithm that searches for an element in a list in sequential order. 

#? Algorithms ?
'''
LinearSearch(array, key)
  for each item in the array
    if item == value
      return its index
'''

#? Complexity:
'''
Time Complexity: O(n)

Space Complexity: O(1)

'''

def linearsearch(A, key):
    index = 0
    while index < len(A):
        if A[index] == key :
            return index
        index = index + 1
    return -1


A = [84, 21, 47, 96, 15]
key = int(input("Enter a number to search :"))
found = linearsearch(A,key)

if found == -1:
    print("Result Not Found ")
else:
    print('Result Found at:',found)



