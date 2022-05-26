# Validate Subsequence

![image](https://user-images.githubusercontent.com/19383145/170588638-560bd9b4-af5a-485d-a81d-7acaf3b0364e.png)

![image](https://user-images.githubusercontent.com/19383145/170588741-fcc3623e-dbf8-4af2-9939-58aae761fbd5.png)

## Solution Walkthrough

We will likely have to traverse both arrays. The question is how?

Because the order of the elements of the sequence and subsequence matters....at the beginning we're really looking for the first element in the potential subsequence.

If we can't find the first element, it doesn't matter if we find the other elements. A subsequence cares about order.

So we're going to initialize a pointer underneath the first element of our subsequence. 

Let's traverse our main array until we find the first element our pointer is pointing to. 

So we're going to put another pointer under the first element in our main array. 

![image](https://user-images.githubusercontent.com/19383145/170590102-ffab7040-4723-4f57-b04a-c0aa47c152f2.png)

We will iterate through the array until we find the first element from the subsequence. 

When you find the first element in the subsequence, look for the next element. 

So we're going to move the pointer to the next element in the subsequence. 

And we're going to move our pointer in our main array forward. We move forward because we already found the first element. So that means that any future elements we're looking for will be found after this element. 

Once you find all the elements in the subsequence, you can stop the algorithm. Even if there are more elements in the main array. 

The time complexity is `O(N)` time where N is the length of the main array

The space complexity is `O(1)` space because we are not storing anything extra. 
