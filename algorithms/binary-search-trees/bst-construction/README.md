# BST Construction

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

