# Two Number Sum

![image](https://user-images.githubusercontent.com/19383145/170175879-b139f7b1-111a-40b6-9f7d-908b5b7576aa.png)

![image](https://user-images.githubusercontent.com/19383145/170175955-76486d7d-39e8-4801-9917-04316abf41e6.png)

![image](https://user-images.githubusercontent.com/19383145/170176041-f2a89753-0158-436d-940c-fd11c597cbb7.png)

### Solution 1 Walkthrough

Using two for loops can give a solution but it would cost `O(N²)` time.

The better way of solving this is to use a hash table. It's going to cause extra space but it might make our algorithm faster. 

We can traverse our array and store every number we see in a hash table. This will allow us to then access these numbers in constant time through the hash table.

Python dictionary is a hash table.

At each number we traverse, we are going to check if the number needed to sum up to the target value is stored in the hash table. 

In our example, `target sum = 10` and `current num = x`

We want to find `y`such that `x + y = 10`. In other words, we can isolate `y` so that `y = 10 - x`

![image](https://user-images.githubusercontent.com/19383145/170177535-cb8e7c76-bd1b-4220-a530-3625d2b06c20.png)

If `y` is in our hash table, then we just return `x` and `y`. Accessing the hash table can be done in `O(1)` time. 

Otherwise we keep traversing the array and we just make sure to store `x` in the hash table. 

Below is an illustration of traversing through the array. We solve for `y` and store the `x` values in the hash table as `True`

![image](https://user-images.githubusercontent.com/19383145/170178602-977a8b9d-6c14-4eb2-acc7-cf32361594a8.png)

We found that the values 11 and -1 sum up to the target sum of 10

[hashSolution.py](https://github.com/KellzCodes/python/blob/main/algorithms/arrays/two-number-sum/hashSolution.py)

### Solution 2 Walkthrough

This solution is not the most optimal because it runs in `O(log(n))` time and `O(1)` space

First you sort the array in ascending order. 

Then you set two pointers: left and right. The left pointer will point to the beginning of the array. The right pointer will point to the end of the array. 

We add the value of the left and right pointers. If they are equal to the target sum then we return an array with both values.

If the sum of the pointers are smaller than the target sum, we move the left pointer to the right to a bigger number (remember the array is sorted)

If the sum of the pointers are bigger than the target sum, we move the right pointer to the left to a smaller number.

This solution is `O(nlog(n))` because of the sorting.

![image](https://user-images.githubusercontent.com/19383145/170400383-1fb6ea16-6602-44e0-89f0-953e55d92a78.png)

[pointerSolution.py](https://github.com/KellzCodes/python/blob/main/algorithms/arrays/two-number-sum/pointerSolution.py)
