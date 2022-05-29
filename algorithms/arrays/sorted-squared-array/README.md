# Sorted Squared Array

![image](https://user-images.githubusercontent.com/19383145/170863148-0c7b1412-aaf2-4d13-8015-b1bbb6a876fd.png)

![image](https://user-images.githubusercontent.com/19383145/170863198-8cd6392f-6064-4173-8aa6-2db2bad036a3.png)

## Solution Walkthrough

This can be solved in linear time because the input array is sorted in ascending order. 

This solution will run in `O(N)` time where N is the number of integers in the array. `O(N)` space where N is the number of integers 

This solution will only work because the array is already sorted.

Let's initialize an empty output array that has a bunch of zeros. 

![image](https://user-images.githubusercontent.com/19383145/170892177-02bfd851-a476-4ef5-af9b-f04fb0db0ce1.png)

As we go further left into the negatives of our array and further right into the positives of our array, the squares of the values continue to get larger. 

Let's draw a number line here

![image](https://user-images.githubusercontent.com/19383145/170892262-7917c18e-77a1-4029-a961-90bf1161214b.png)

The further right we go from zero and the further left we go from zero, the larger the square values become. 

We can actually look at the absolute value of any of these values to determine which squares are going to be the largest. 

For example, if i'm comparing the integer -3 to and the integer 2 and trying to determine which is going to have a larger square, all I need to do is take the absolute value of these two values. 

I'll see that 3 is larger than two. That means that -3 is going to have a larger square than two. That is because $-3 * -3 = 9$. 

Let's look at the values at the beginning and end of our array

![image](https://user-images.githubusercontent.com/19383145/170892538-daabdccc-123b-4dc6-ac9a-8363b8d38704.png)

So now we can compare the values at the beginning and end of our array to determine which is larger. That will tell us which position we should be inserting these elements in the array. 

The largest positive value must be at the very end of our array and the largest negative value must be at the very beginning. These are the two values that are kinda gonna be competing for that spot at the very end of our output array to have the largest square. 

If we compare these two values and see the value that is the largest, we can simply take the square of that value and insert it at the end of the array, because we know no value will have a larger square than that. 

Then we can move over to the next element and continue along with the process. 

So you can start by creating two pointers: `start` and `end`

![image](https://user-images.githubusercontent.com/19383145/170892722-b3520cee-d744-40e1-930f-635d3b69fd8a.png)

We know that these pointers will be at the smallest value and the largest value. We know that one of these two values will be at the end of our output array. The reason we know is because one is the largest positive value and one is the largest negative value. One will have the largest square out of all of the values in this input array. 

We are going to compare these values specifically by their absolute values. Whichever one has the largest absolute value, we'll take its square and insert it at the last position in our output array. 

So we are going to start building our output array from the very end. Ant the position we want to start at will be `i` which is marked on the diagram below.

![image](https://user-images.githubusercontent.com/19383145/170893149-0eef8a67-c07b-4db2-83cc-0710b9e8ed26.png)

So we compared |-7| to |9|. 9 is larger so we squared it then placed the square at position `i`.

Then we move `i` to the left because we have filled the last position. We also move our `end` pointer to the number 8. We leave the `start` pointer at -7 and start the process again where we compare the `start` and `end` absolute values.

![image](https://user-images.githubusercontent.com/19383145/170893273-36239e30-e572-4953-a341-c1c24f70d94f.png)

![image](https://user-images.githubusercontent.com/19383145/170893310-2200bcbe-932e-4689-bf69-bb295ebc2817.png)

![image](https://user-images.githubusercontent.com/19383145/170893340-96627e3c-e1f4-44be-85d7-9da0dda2c974.png)

![image](https://user-images.githubusercontent.com/19383145/170893363-8edce9b7-8bbe-4c21-a880-329062b38d66.png)

![image](https://user-images.githubusercontent.com/19383145/170893374-7d23749d-95c6-40ce-aa09-e6fc1a7b2738.png)

![image](https://user-images.githubusercontent.com/19383145/170893381-248211cc-6a22-4c5c-8cde-718a9cd77bd3.png)

## Solution Files

Brute force solution will run in `O(nlog(n))` time because of sorting method. And `O(N)` space where N is the number of integers in the input array. 

[bruteForce.py](https://github.com/KellzCodes/python/blob/main/algorithms/arrays/sorted-squared-array/bruteForce.py)

[linearSolution.py](https://github.com/KellzCodes/python/blob/main/algorithms/arrays/sorted-squared-array/linearSolution.py)

