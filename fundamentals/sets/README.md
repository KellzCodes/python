# Sets

[Practice Question](#Practice-Question)

![image](https://user-images.githubusercontent.com/19383145/167455179-7f3ed7d1-612d-4db2-ba7f-9315acf0ee7d.png)

![image](https://user-images.githubusercontent.com/19383145/167455483-61b9580f-65eb-4bc9-bbc5-d8dd07d3b38b.png)

#### A set is a unique collection of elements which means it will not have duplicates. 

Checking to see if an element exists in a set is instant.

#### Create a set

Use `set()` function to create an empty set. 

Use `{}` to create a set with elements in it.

If you use just the `{}` to create an empty collection, it will be a dictionary and not a set

![image](https://user-images.githubusercontent.com/19383145/167456550-db8e1703-420b-4a7c-956b-158d74c58932.png)
![image](https://user-images.githubusercontent.com/19383145/167456654-3e79c9db-0e52-4d7b-acee-ba1d374a5c5b.png)

#### add elements to a set

Remember, a set does not have duplicates.

![image](https://user-images.githubusercontent.com/19383145/167456918-92d269bc-cb8f-4ef8-849e-6cfe7bde30a7.png)

`add()` method

Make sure to add an element that is not already in the set. If you try to add something that is already there, you will get an error.

![image](https://user-images.githubusercontent.com/19383145/167457261-4e4dbfc3-5959-416c-862f-377984c530a0.png)

#### `remove()` method

Make sure remove something that is actually inside the set. If you try to remove something that is not there, you will get an error.

![image](https://user-images.githubusercontent.com/19383145/167457695-4e8a3e39-3bff-42d0-9e05-f7829394035b.png)

#### `clear()` method

`clear()` will remove all elements 

![image](https://user-images.githubusercontent.com/19383145/167458075-7267ecf9-b079-4b48-9c5e-571375ece57c.png)

#### `len()` method

This will tell you how many unique items are in the set

![image](https://user-images.githubusercontent.com/19383145/167458914-ced7a09a-4077-4492-a648-6e520a8999f0.png)

#### Can add multiple data types to set

![image](https://user-images.githubusercontent.com/19383145/167459289-ad1c5db3-a114-4050-b595-31ae894de30b.png)

You cannot add any mutable objects to a set. You cannot add a set, list, or dictionary to a set. 

#### `in` operator

Check to see if something exists in a set

![image](https://user-images.githubusercontent.com/19383145/167534817-2ba240fa-acb8-4a7b-8ac3-f04908533b69.png)

#### `union()` method

combines sets together

![image](https://user-images.githubusercontent.com/19383145/167535099-cd3ef751-9e8e-4d97-bf28-489ab5174f48.png)

you can also combine sets using `|`. This only works on sets.

![image](https://user-images.githubusercontent.com/19383145/167535178-81b13a45-902d-4536-862a-08f51e08284b.png)

#### `intersection()` method

The intersection of sets is simply the items contained in both sets

![image](https://user-images.githubusercontent.com/19383145/167535640-e2eba701-522e-45e6-8e6e-b5684726022c.png)

You can also intersect using `&`.

![image](https://user-images.githubusercontent.com/19383145/167535775-e018fe4a-083c-49b2-acb8-57f84e202be7.png)

#### `difference()` method

The difference between 2 sets is all of the elements contained in one set that is not contained in the other

![image](https://user-images.githubusercontent.com/19383145/167536133-7478ea1e-0fb9-4db8-a7ed-293e2beba9fb.png)
![image](https://user-images.githubusercontent.com/19383145/167536185-3d4b062c-7345-4536-8b3a-3dd1bd6e1620.png)

You can also difference using `-`.

![image](https://user-images.githubusercontent.com/19383145/167536428-8d364387-296e-4d1f-9ec5-2f5da8a81518.png)

#### `symmetric_difference()` method

The symmetric difference is the elements not shared between the two sets

![image](https://user-images.githubusercontent.com/19383145/167536688-e3e893eb-cec0-4a52-9140-f91d4eb0aa32.png)

you can also symmetric difference using `^`.

![image](https://user-images.githubusercontent.com/19383145/167536919-8d50b457-24ee-477e-882a-3dda88cd46fc.png)

#### `update()` method

Update adds all the elements from one set to another

This method actually modifies a set

![image](https://user-images.githubusercontent.com/19383145/167743965-25a76407-36c4-4bc5-b5bd-dff0404659f3.png)
![image](https://user-images.githubusercontent.com/19383145/167744023-a5db4d02-f78a-4f1e-8af8-a4f9a4320b28.png)

#### `difference_update()` method

This will modify a set so that it is equal to the difference between two sets

![image](https://user-images.githubusercontent.com/19383145/167744143-1558d492-ac12-4af8-aef7-8d0aeb56dc7a.png)

#### `symmetric_difference_update()` method

This will modify a set so that it is equal to the symmetric difference between two sets

![image](https://user-images.githubusercontent.com/19383145/167744320-147b57b8-c7e7-4d80-b758-b6c40090fbf6.png)

#### Superset and Subset

A superset of another set means that this set contains all of the elements and potentially more of another set.

A subset of another set means that all of the elements of this set is contained in the other set. 

Below, `y` is a superset of `x` and `x` is a subset of `y`

`x = {1, 2, 3}`
`y = {1, 2, 3, 4}`

#### `issubset()` method

This tells you if a set is a subset

![image](https://user-images.githubusercontent.com/19383145/167745742-b29f7056-eb2f-4256-9693-5aa05c0eaa7e.png)
![image](https://user-images.githubusercontent.com/19383145/167745775-31fa381c-b031-4d8e-ae9d-4968a2c0c325.png)

You can also use `<=` to check for a subset

![image](https://user-images.githubusercontent.com/19383145/167745997-80e45d4e-aeaf-4021-9ea9-d1a54045a7cd.png)

#### `issuperset()` method

This tells you if a set is a superset

![image](https://user-images.githubusercontent.com/19383145/167746128-7669cf47-a501-4aac-a397-7d1d43e69db3.png)

You can also use `>=` to check for a superset

![image](https://user-images.githubusercontent.com/19383145/167746747-67197a1c-3d62-43c1-a3e3-35f5a14fd7ee.png)

#### Proper superset and proper subset

A proper superset or subset means that this set is not equal to the other set. 

If I want to check that `y` is a proper subset of `x`, that would mean `y` needs to contain at least on element that's not in `x`

proper superset

![image](https://user-images.githubusercontent.com/19383145/167747499-92355894-42a4-4328-9332-cf662a3fe351.png)

proper subset

![image](https://user-images.githubusercontent.com/19383145/167747548-15b4ac46-93b9-4859-b6ea-49912f121306.png)

#### convert a list to a set

convert the list to a set

![image](https://user-images.githubusercontent.com/19383145/167747930-eeebdc1c-ecf0-41f6-ab35-d797b1b17e10.png)

#### Ask user to give numbers then stop when given duplicate number

![image](https://user-images.githubusercontent.com/19383145/167748348-21da942f-5fa7-4def-a0d5-6da2e4cee6b3.png)

#### when to use a set

A set is really only to be used when you care about if something exists inside the set. 

If you don't care about the frequency or order....then use a set.

If you care if something exists and you want to store information with that, then you use a dictionary. 

### Practice Question

#### Write a program that continually asks the user to enter characters until the user enters a previously entered character or more than one character at a time. After, the program should print the number of unique characters that were entered. Use a set to accomplish this

![image](https://user-images.githubusercontent.com/19383145/167749578-dc1361f9-b3e5-4742-aaed-8ba501cdf46f.png)

[Answer](https://github.com/KellzCodes/python/blob/main/fundamentals/sets/practice1.py)
