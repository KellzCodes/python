# BST Construction

[iterative solution](https://github.com/KellzCodes/python/blob/main/algorithms/binary-search-trees/bst-construction/iterativeSolution.py)
[recursive solution]()

![image](https://user-images.githubusercontent.com/19383145/171542575-ad2f60c3-8abf-4e3f-a870-1058f3555b96.png)

![image](https://user-images.githubusercontent.com/19383145/171542602-c0bc5d1b-ea43-4678-b10c-e6f10bfd6dd8.png)

![image](https://user-images.githubusercontent.com/19383145/171542652-b2d73959-860f-49f2-ad6e-4469a88d2a1d.png)

## BST Property

Every node in a BST has to satisfy the BST property. The BST property says that a node's value must be strictly greater than all of the values of the nodes to its left. The value of a node must be less than or equal to all of the values of the nodes to its right. 

Let's look at an example BST

![image](https://user-images.githubusercontent.com/19383145/171543368-6df78498-b6a3-4a21-9536-0e1601d23af7.png)

The node at the top is called the root node. The root node that has a value of 10 is a BST node if and only if its value is strictly greater than all the values of the nodes to its left. And its value is less than or equal to the values of all the nodes to its right. 

For the BST property to hold, the left and right children nodes have to also themselves be BSTs and satisfy the BST property. 

## Concept Walkthrough

This question is defines the BST property as: every node to the left has to have a value strictly less than the parent node....every node to the right has to have a value equal to or greater than the parent node. 

Duplicate values will go on the right side of parent node. 

The main methods a BST must support are insertion, searching and deletion. 

### Insertion

Let's say we want to insert the number 12 into the BST. First thing we do is call the insertion method on the root node. 

From there, we start by comparing the value of the node that we are at which is 10 to 12. Is 10 greater than, less than, or equal to 12? 

In this case, 10 is smaller than 12. This tells us that we want to insert 12 to the right of 10. This will satisfy the BST property.

This means we can eliminate the entire left subtree as circled below. 

![image](https://user-images.githubusercontent.com/19383145/171546991-2630331d-bfd5-4985-b600-fb275d68c4ad.png)

We no longer need to explore the left of the subtree because we know that 12 will not be located in it. 

Now we compare 15 to 12. 15 is greater than 12. That tells that every value to the right of 15 is also greater than 12. So we want 12 to be on the left of 15. 

So we can eliminate the entire right subtree as circled below. We will not have to explore it at all. 

![image](https://user-images.githubusercontent.com/19383145/171547377-3623b2e9-8427-4b80-b4ca-76ed49014aca.png)

Next we compare 12 to 13. Now we can eliminate the entire right subtree circled below. 

![image](https://user-images.githubusercontent.com/19383145/171550190-0aa2474c-1c3e-4875-8d71-317862f63f22.png)

We go further down the tree and realize there is a null value to the left of 13. So we can insert the number 12 there. 

![image](https://user-images.githubusercontent.com/19383145/171764440-2eca5709-2169-4aba-93f2-62f82690132f.png)

The key logic here is the idea of eliminating half of the BST at every node that you traverse or explore. 

### Searching

Let's say we are searching for the number 12. We start at the top by calling the search method on the root node. 

![image](https://user-images.githubusercontent.com/19383145/171765359-e3f26be9-1268-4406-987a-d08f732980b9.png)

Just like we did with insertion, we compare the value of our node which is 10 to the value 12. We notice that 10 is smaller than 12. Therefore, if 12 is contained in this BST, it will have to be to the right of 10. 

Once again, we can eliminate the entire left subtree. 

![image](https://user-images.githubusercontent.com/19383145/171768813-d23ce9d1-eb7b-444a-9636-da2817e95fe5.png)

Now we compare 15 to 12. 15 is greater than 12 therefore we eliminate the entire right subtree.

![image](https://user-images.githubusercontent.com/19383145/171768927-16d5b24d-4272-430d-a878-84a2762f1469.png)

13 is greater than 12 so we eliminate another right subtree

![image](https://user-images.githubusercontent.com/19383145/171769005-42e18369-d7ca-45fe-85b3-ee793e837156.png)

Finally we have found 12. 

### Deletion

#### Deleting a leaf

Let's say we want to remove the number 1. 1 is a leaf. 

![image](https://user-images.githubusercontent.com/19383145/171771270-2a220b64-b530-49cd-812c-c9255db64192.png)

First we compare 1 to 10. 10 is greater than 1 so we eliminate the entire right subtree

![image](https://user-images.githubusercontent.com/19383145/171771358-4d6b842f-af48-4251-b62e-79e44e047ac2.png)

The we move down and eliminate more subtrees until we get to 1

![image](https://user-images.githubusercontent.com/19383145/171771460-37c7ecd1-3279-4e54-9b4f-3e40dfb36746.png)

It's easy to delete a leaf because it does not have any children nodes. So we can just remove it and set it to null. 

![image](https://user-images.githubusercontent.com/19383145/171771627-8a47a440-8400-42a9-9024-0ec0a70417b3.png)

#### Deleting a node with one child

Let's delete 2. 2 has one child node. 

![image](https://user-images.githubusercontent.com/19383145/171771855-7ced3acf-b53f-43de-ad82-f97ec9d53424.png)

Theoretically, we would have to grab the 2 and erase it then grab the one and connect it to the 5. 

#### deleting a node with 2 children

What if we want to remove the root node number 10?

![image](https://user-images.githubusercontent.com/19383145/171772911-6fcdeea9-ae17-4779-a8f8-e744871d3392.png)

You can't just erase it or move it's children because the children have their own children nodes. 

You grab the smallest value in the right subtree of that node. In other words, you grab the left most value in the right subtree of that node. 

We start at 10 and go to the right subtree to look for the smallest value in the right subtree. The smallest and left most value in the right subtree is 12. 

So we traverse the right subtree and find the 12. We grab the 12 and keep track of its value. We erase the 10 then replace it with 12. 

![image](https://user-images.githubusercontent.com/19383145/171773533-7ad9b690-4dac-4c65-8630-fcb29f21275c.png)

We moved the 12 because it was greater than or equal to 10 and it was strictly greater than all the values that were to the left of 10. Because it was the smallest and left most value in the right subtree, we know that it is smaller than all the values above it. So it was ok to put it at the root. It was also the easiest to delete from the bottom of the BST. 

## Complexity

### Time Complexity 

Average `O(log(N))` time where N is the number of nodes in our BST.

It is `O(log(N))` because we did not traverse the entire tree when we deleted, inserted, and searched. At every node we explored, we eliminated half of the remaining BST. 

This is only the average case because there are some cases where the logic to eliminate half the BST is impossible. One such case is if every node is a left child and we don't have a right side to eliminate. 

The worst case is `O(N)` time where N is the number of nodes in the BST

### Space Complexity

The space complexity is `O(log(N))` if we implement the algorithm recursively. If you implement recursively, you are effectively using up frames on the call stack. 

There is a point where the maximum memory usage is `O(log(N))` space where N is the depth or height of the BST, meaning the length of its longest branch. 

The worst case for space complexity is `O(N)` because if you're only going through one branch then you are effectively storing on the call stack. 

If you implement the algorithm iteratively instead of recursively, the space complexity is `O(1)` space. 

