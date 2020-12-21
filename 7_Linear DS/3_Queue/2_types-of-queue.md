## Types of Queue:-

1. Simple Queue 
2. Circular Queue
3. Priority Queue
4. Deque(Double Ended Queue)

### Simple Queue:-
insertion takes place at the rear and removal occurs at the front. It strictly follows FIFO rule.

<img src="https://cdn.programiz.com/sites/tutorial2program/files/simple-queue_0.png" alt="">

### Circular Queue:-

The last element points to the first element making a circular link.
<img src="https://cdn.programiz.com/sites/tutorial2program/files/circular-queue.png" alt="">

The main advantage of a circular queue over a simple queue is better memory utilization. If the last position is full and the first position is empty then, an element can be inserted in the first position. This action is not possible in a simple queue.

### Priority Queue :-
A priority queue is a special type of queue in which each element is associated with a priority and is served according to its priority. If elements with the same priority occur, they are served according to their order in the queue.


<img src="https://cdn.programiz.com/sites/tutorial2program/files/priority-queue.png" alt="">

Insertion occurs based on the arrival of the values and removal occurs based on priority.

### Deque (Double Ended Queue) :-
Double Ended Queue is a type of queue in which insertion and removal of elements can be performed from either from the front or rear. Thus, it does not follow FIFO rule (First In First Out).

<img src="https://cdn.programiz.com/sites/tutorial2program/files/double-ended-queue.png" alt="">
