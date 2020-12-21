## Divide & conquer Algorithm

A divide and conquer algorithm is a strategy of solving a large problem by

- breaking the problem into smaller sub-problems
- solving the sub-problems, and
- combining them to get the desired output.
  

To use divide and conquer algorithms, recursion is used.

> sorting an array using the divide and conquer approach (ie. merge sort).

1. Let the given array be:

<img alt="" src="https://cdn.programiz.com/sites/tutorial2program/files/divide-and-conquer-0.png">

2. Divide the array into two halves.

<img alt="" src="https://cdn.programiz.com/sites/tutorial2program/files/divide-and-conquer-1.png">

Again, divide each subpart recursively into two halves until you get individual elements.

<img alt="" src="https://cdn.programiz.com/sites/tutorial2program/files/divide-and-conquer-2.png">


3. Now, combine the individual elements in a sorted manner. Here, conquer and combine steps go side by side.

<img alt="" src="https://cdn.programiz.com/sites/tutorial2program/files/divide-and-conquer-3.png">



## Complexity :-
The complexity of the divide and conquer algorithm is calculated using the master theorem.

```
T(n) = aT(n/b) + f(n),
where,
n = size of input
a = number of subproblems in the recursion
n/b = size of each subproblem. All subproblems are assumed to have the same size.
f(n) = cost of the work done outside the recursive call, which includes the cost of dividing the problem and cost of merging the solutions

```

For a merge sort, the equation can be written as:

```
T(n) = aT(n/b) + f(n)
     = 2T(n/2) + O(n)
Where, 
a = 2 (each time, a problem is divided into 2 subproblems)
n/b = n/2 (size of each sub problem is half of the input)
f(n) = time taken to divide the problem and merging the subproblems
T(n/2) = O(n log n) (To understand this, please refer to the master theorem.)

Now, T(n) = 2T(n log n) + O(n)
          ≈ O(n log n)

```



## Advantage of Divide and Conquer Algorithm

- The complexity for the multiplication of two matrices using the naive method is O(n3), whereas using the divide and conquer approach (ie. Strassen's matrix multiplication) is O(n2.8074). Other problems such as the Tower of Hanoi are also simplified by this approach.
  
- This approach is suitable for multiprocessing systems.
- It makes efficient use of memory caches.


## Applications :-

- Binary Search
- Merge Sort
- Quick Sort
- Strassen's Matrix multiplication
- Karatsuba Algorithm