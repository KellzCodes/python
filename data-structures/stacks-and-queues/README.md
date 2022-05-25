# Stacks and Queues

![image](https://user-images.githubusercontent.com/19383145/170151227-972c4970-b688-469d-b203-fd30c5e44744.png)

![image](https://user-images.githubusercontent.com/19383145/170151260-0ff51577-0985-4905-aa7f-d50e58b61d13.png)

### Inserting or deleting from stack / queue

`O(1)` space and time. 

This is because we are inserting or removing from the beginning or end of a linked list. 

### Searching for an element in a stack / queue

`O(N)` time and `O(1)` space

We have to traverse through N nodes which takes `O(N)` time. There is no additional space used. 

### Storing a stack / queue

`O(N)` space and `O(1)` time

Typically, a stack or queue is initialized as an empty stack and nodes are inserted. Insertions are `O(1)` time. Storing N nodes in a stack or queue will take `O(N)` space.

### Peeking in a stack or queue

`O(1)` space and time.

You are just looking at the first or last element. 
