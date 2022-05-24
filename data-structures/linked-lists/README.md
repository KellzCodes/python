# Linked Lists

1. [Memory](#memory)
2. [Complexity](#complexity)

![image](https://user-images.githubusercontent.com/19383145/169917628-f83f67a9-ddf1-49a3-a86c-a51e44456d32.png)

![image](https://user-images.githubusercontent.com/19383145/169917754-1409b8cd-7563-425c-a478-28b233e73d9d.png)

![image](https://user-images.githubusercontent.com/19383145/169917797-6bab9fc7-d1bf-4886-b36e-0def5cd114eb.png)

## Memory

Below is a memory canvas representing 25 memory slots and a linked list. 

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



