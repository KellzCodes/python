# Sets

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
