
#! Circular Queue

#? How Circular Queue Works
'''
Circular Queue works by the process of circular increment i.e. when we try to increment the pointer and we reach the end of the queue,
we start from the beginning of the queue.

Here, the circular increment is performed by modulo division with the queue size. That is:-

if REAR + 1 == 5 (overflow!), REAR = (REAR + 1)%5 = 0 (start of queue)

'''

#? Operations :-
'''
The circular queue work as follows:

- two pointers FRONT and REAR
- FRONT track the first element of the queue
- REAR track the last elements of the queue
- initially, set value of FRONT and REAR to -1
'''
# 1. Enqueue Operation
'''
- check if the queue is full
- for the first element, set value of FRONT to 0
- circularly increase the REAR index by 1 (i.e. if the rear reaches the end, next it would be at the start of the queue)
- add the new element in the position pointed to by REAR
'''
# 2. Dequeue Operation
'''
- check if the queue is empty
- return the value pointed by FRONT
- circularly increase the FRONT index by 1
- for the last element, reset the values of FRONT and REAR to -1

'''

#? To check the queue is full :-
'''
Case 1 : FRONT = 0 && REAR == SIZE-1
Case 2:- FRONT = REAR -1
'''

#? Time complexity
'''
The complexity of the enqueue and dequeue operations of a circular queue
is O(1) for (array implementations).
'''

#? Applications of Circular Queue
'''
- CPU scheduling
- Memory management
- Traffic Management
'''
#? Circular Queue implementation in Python
class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)

#  circular queue is empty
obj.printCQueue()

obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)

print("Initial queue")
obj.printCQueue()

# C queue is fulled
obj.enqueue(10)

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()




