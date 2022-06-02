# Non-Constructible Change

![image](https://user-images.githubusercontent.com/19383145/171516816-f78f619f-4058-44e3-8079-65703d05410b.png)

![image](https://user-images.githubusercontent.com/19383145/171516869-cc726fc0-e823-486e-95b0-aaaa5680201b.png)

![image](https://user-images.githubusercontent.com/19383145/171516954-a59465e3-d48a-4b82-9dd4-0ed7ad039232.png)

## Concept Walkthrough

Let's look at an example array

![image](https://user-images.githubusercontent.com/19383145/171517337-defd6d4a-90af-45f8-bb36-da1317f54aa0.png)

Let's sort the input array first. 

![image](https://user-images.githubusercontent.com/19383145/171517985-2bf7171c-45c6-4c02-bb8f-aeb7409d302a.png)

let's create a variable called `change = k`. This going to tell us how much change we can currently create. We can currently make `1 to k` change with the change we already have. So we can make all the values between 1 and k including 1 and k. 

So the idea is to loop through all the coins in ascending order then see how much change we can make with those coins. So we consider one new coin at a time and then compare that to the amount of change we could make previously. 

So let's set `change = 0` and start by iterating our sorted input array. 

![image](https://user-images.githubusercontent.com/19383145/171518526-8b6ad33c-b765-471b-87b1-6fada81f81ea.png)

At value 1, we can make one cent of change. So we can set `change = 1`. 

Note, if the first value in our sorted input list is not one, that means we can not make one cent worth of change. So we'd just return one because that is the minimum amount of change we cannot create. 

Let's go to the next value which is 1 again. This means we can now make 2 cents. 

![image](https://user-images.githubusercontent.com/19383145/171518968-4e79dec3-d1ec-48c7-b7ca-33a414ed51ea.png)

The next value is 2. This means we can make 4 cents of change. Actually, this means we can make 1, 2, 3, and 4 cents of change. 

![image](https://user-images.githubusercontent.com/19383145/171519176-51fd3e8a-b7fe-46ba-8b09-1c8b1a5e6a8e.png)

Let's move to the next coins. 

![image](https://user-images.githubusercontent.com/19383145/171519492-8084b430-821c-4dac-ad36-85e846739ba9.png)

![image](https://user-images.githubusercontent.com/19383145/171519552-ad078e9f-b6d9-47fc-b5be-8db9e97a3ee6.png)

![image](https://user-images.githubusercontent.com/19383145/171519630-8d9ad1ae-9506-4484-9be4-00cf095bc7e5.png)

Let's move the pointer over once more. Now we are at 22. We can make 41 cents but can we make 20, 21, 22, etc? 

The answer is no. In fact, we cannot make 20 cents. This is because 22 is greater than the amount of change we have plus one. 

If you looked at all the previous coins, notice that when we were adding all of these up, we never had a coin that was greater than the amount of change we previously had plus one. 

## Solution

The solution will run in `O(nlog(n))` time | `O(1)` space where n is the number of integers in the input array. 

[solution code](https://github.com/KellzCodes/python/blob/main/algorithms/arrays/non-constructible-change/nonConstructibleChange.py)

If we have a set of coins and we'll call the set `u`. We are going to start with just one coin in the set: `u = {1}`. We have some `c` value which will stand for the change that we can create with these coins. It will be equal to whatever the second makes: `c = 1`. 

Imagine we have one individual coin called `V = 1` and we add it to the individual set. We can say that if `V` is greater than `c + 1` we cannot make `c + 1` change. 

The equation is $V > c + 1$. This means we cannot make `c + 1` change and we return `c + 1`

If $V <= c + 1$ that mean we can make from `c` plus `V`

So we want to have a set of coins and slowly add one more coin to it as we go through until we eventually reach the one coin that is greater than `change` plus one. If we reach that scenario, we just return `change` plus one. 

Remember, if the coin we add to `change` is less than `change` plus one, we can make all the values up to `change` plus the new coin. 

We will start by sorting the input array in ascending order. Then we loop through on coin at a time, keep track of how much `change` we can currently create, and then check for some coin that we add that is greater than our amount of `change` plus one. Once we find that, we just return the `change` plus one. 

If we were to make it to the very end of our list and never hit the condition where $V > c + 1$, that would mean we cannot make one more than the change we have at the end of the list
