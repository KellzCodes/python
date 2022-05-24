# Linked Lists

1. [Memory](#memory)
2. [Complexity](#complexity)
  - [Accessing middle node](#accessing-a-middle-node)
  - [Setting middle node](#setting-a-middle-node)
  - [Initializing a linked list](#initializing-a-linked-list)
  - [Copying a linked list](#copying-a-linked-list)
  - [Traversing a linked list](#traversing-a-linked-list)
  - [Inserting a node at the beginning](#inserting-a-node-at-the-beginning)
  - [Inserting a node in the middle](#inserting-a-node-in-the-middle)
  - [Inserting a node at the tail](#inserting-a-node-at-the-tail)

![image](https://user-images.githubusercontent.com/19383145/169917628-f83f67a9-ddf1-49a3-a86c-a51e44456d32.png)

![image](https://user-images.githubusercontent.com/19383145/169917754-1409b8cd-7563-425c-a478-28b233e73d9d.png)

![image](https://user-images.githubusercontent.com/19383145/169917797-6bab9fc7-d1bf-4886-b36e-0def5cd114eb.png)

## Memory

Below is a memory canvas representing 25 memory slots and a linked list. This will be used for example purposes and does not represent actual memory in a system.

![image](https://user-images.githubusercontent.com/19383145/170099720-ec5b9323-fec6-41ec-8aee-45631e594b33.png)

Unlike arrays, linked lists do not need contiguous (or back to back) memory slots. 

Linked lists are going to store elements in the list anywhere in memory. They are going to connect the elements using pointers. 

Pointers are this tool that allows you to have one memory slot, let's say memory slot 20, point to another memory slot just by storing the other memory slot's address. You can have memory slot 20 point to memory slot 10 which can pont to memory slot 1 which can point to memory slot 22 and so forth.

![image](https://user-images.githubusercontent.com/19383145/170101729-d2bdfeb3-8e09-42e7-a428-18e1e9f3a770.png)

Let's look at how a linked list is stored in memory. We would create a structure likely called a "node". Each node in the linked list has both a value (such as 3 or 1) and a pointer to the next node in the linked list. So the first node that has value 3 would have a pointer that points to the next node in the linked list... the node with value 1. 

We would store this in memory by having two back to back memory slots for each node where one memory slot holds the value and the 2nd memory slot holds the pointer. Then the next node in the linked list could be anywhere in the memory canvas. 

So we can put node value 3 at memory slot 21 then have a pointer starting at memory slot 22 (value and pointer have to be back to back) then pointing to memory slot 5. Below, we are using arrows but in memory, the number 5 would be written in binary (101). At memory slot 5, we will store the value 1. Then have a pointer starting at memory slot 6 that points to memory slot 2. Memory slot 2 will store the value 4. Then have a pointer starting at memory slot 3 that points to memory slot 16. Memory slot 16 will store the value 2. Then have a pointer starting at memory slot 17 that points to `null` address.

In memory, there are certain memory addresses that kind of act like the null value or the non-value in coding. They are sort of like memory addresses where if you operating system ever reaches them, it kind of knows that it doesn't have to go anywhere else. Below, we can depict it as an orange 0. 

![image](https://user-images.githubusercontent.com/19383145/170106257-f38afd5a-554b-4c09-b318-970f2bf49a2c.png)

## Complexity

### Accessing a middle node

Accessing a middle node runs in `O(N)` time and `O(1)` space.  

You have to start at the first node called the head then traverse the entire linked list until you find the index you are looking for. 

So this will take `O(index)` time. Because you're not storing any additional memory, this will take `O(1)` space. 

### Setting a middle node

Setting a middle node runs in `O(N)` time and `O(1)` space.

Once you find the value at the ith index which takes `O(index)` time, then you can set it instantly by swapping the value for another number. No extra space which would be `O(1)`

There actually isn't really a concept of setting a value in a linked list because that doen't really work. There aren't really indices in linked lists which is why when you implement the linked list you typically don't even have the concept of indices. They are not like arrays. 

### Initializing a linked list

Initializing a linked list runs in `O(N)` time and space. 

You've got a total of 2N memory slots for each node which is `O(2N)` space. Allocating those chunks of memory is going to take `O(N)` time. 

### Copying a linked list

Copying a linked list will run in `O(N)` time and space.

You would have to traverse through the entire linked list of N nodes which will take `O(N)` time. Then you are allocating 2N more memory slots for the copied linked list which will take `O(2N)` space. 

### Traversing a linked list

Traversing a linked list will run in `O(N)` time and `O(1)` space.

When you are traversing, you are not allocating new memory which is why it is `O(1)` space. You are going through all N nodes which takes `O(N)` time. 

### Inserting a node at the beginning

O(1)` time and space.

You create a new head node which will be stored in memory then have its pointer point to the old head. Then you set the head variable equal to the new head. 

This will take `O(1)` time because all we did was create one new node of two memory slots, just shifted a couple of pointers, and overwrote one memory address.  

### Inserting a node in the middle 

`O(N)` to access + `O(1)` time and `O(1)` space.

First we have to traverse through the linked list until we get to the node we want to insert to. This will be an `O(N)` time operation. Then create one new node and shift the pointers. Shifting pointers are `O(1)` time operations. 

If you already have a reference to the node you want to insert to, then it would take `O(1)` time. 

### Inserting a node at the tail

`O(N)` to access + `O(1)` time and `O(1)` space.

First we have to traverse through the linked list until we get to the end. This will be an `O(N)` time operation. Then create one new node and shift the pointers. Shifting pointers are `O(1)` time operations. 

If you already have a reference to the tail, then it would take `O(1)` time. 
