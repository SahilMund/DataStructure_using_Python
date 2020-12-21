
#! Queue
# It is similar to the ticket queue outside a cinema hall, where the first person entering the queue is the first person who gets the ticket.

#TODO : Principle , Operations , Working , Limitations, Time Complexity , Applications , Code

#? Principle:
# FIFO (First In First Out)

#? Basic Opeartions associated with Queue :-
'''
Queue is an abstract data structure(ADT) .

1. Enqueue: Add an element to the end of the queue
2. Dequeue: Remove an element from the front of the queue
3. IsEmpty: Check if the queue is empty
4. IsFull: Check if the queue is full
5. Peek: Get the value of the front of the queue without removing it
'''

#? Working of Queue :-

'''
- two pointers FRONT and REAR
- FRONT track the first element of the queue
- REAR track the last elements of the queue
- initially, set value of FRONT and REAR to -1
'''
# Enqueue Operation:-
'''
- check if the queue is full
- for the first element, set value of FRONT to 0
- increase the REAR index by 1
- add the new element in the position pointed to by REAR

'''

# Dequeue Operation
'''
- check if the queue is empty
- return the value pointed by FRONT
- increase the FRONT index by 1
- for the last element, reset the values of FRONT and REAR to -1

'''
#? Complexity Analysis
'''
The complexity of enqueue and dequeue operations in a queue using an
array is O(1).
'''

#? Applications of Queue Data Structure
'''
- CPU scheduling, Disk Scheduling
- When data is transferred asynchronously between two processes.The queue is used for synchronization. eg: IO Buffers, pipes, file IO, etc
- Handling of interrupts in real-time systems.
- Call Center phone systems use Queues to hold people calling them in an order
'''

#? Queue implementation in Python
class Queue:

    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Display  the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("After removing an element")
q.display()



#? Limitations
'''
As you can see in the image below, after a bit of enqueuing and dequeuing,
the size of the queue has been reduced.The indexes 0 and 1 can only be used after the queue is reset when all the elements have been dequeued.
'''

# TO overcome this limitation circular queue is used.