# Dictionaries

- [Practice Questions](#Practice-Questions)

![image](https://user-images.githubusercontent.com/19383145/167268713-018b6e09-1822-4a74-8384-43bd4566920c.png)

![image](https://user-images.githubusercontent.com/19383145/167268747-f7dffc1e-2971-431d-b40b-e4724b9fd44c.png)

Dictionaries allow us to store key value pairs.

![image](https://user-images.githubusercontent.com/19383145/167268833-a74998c8-0c1f-437d-810b-0e0550f895f2.png)
![image](https://user-images.githubusercontent.com/19383145/167268853-a7f2cfaf-d795-4d1f-bf01-f4e8962ae2ec.png)

#### adding elements to the dictionary

![image](https://user-images.githubusercontent.com/19383145/167277993-d9bd2eea-83a5-4786-b4e6-6bb4f0a65a14.png)
![image](https://user-images.githubusercontent.com/19383145/167278027-49789184-7a90-4e25-868b-e6dc8e4bc480.png)

#### deleting an element from the dictionary

![image](https://user-images.githubusercontent.com/19383145/167278110-3cf62f0f-947a-4a5e-b8cc-5771c62579ae.png)

#### check to see if a key exists in a dictionary

This only checks for a key, not a value

![image](https://user-images.githubusercontent.com/19383145/167278148-d6be5d4e-1ecd-475f-931c-5b30418da9d0.png)

#### `values()` method

![image](https://user-images.githubusercontent.com/19383145/167321354-706fbda6-3d89-4f71-976f-b9b2f2e83d4c.png)

Here is how to access a value using the `values()` method

![image](https://user-images.githubusercontent.com/19383145/167321416-49f7b466-1b0e-4014-96d2-bde7ad4a4598.png)

#### `keys()` method

![image](https://user-images.githubusercontent.com/19383145/167321443-ef47003d-452f-4b59-9805-9ac3f8e104ba.png)

Here is how to access a key using the `keys()` method

![image](https://user-images.githubusercontent.com/19383145/167321472-4c3f81d1-0624-4c6a-8192-e033d0dab132.png)

#### `items()` method

This will print a list of tuples. Each tuple is a key-value pair.

![image](https://user-images.githubusercontent.com/19383145/167321529-7ff5fa7d-16f9-4e83-876d-4c66d340a069.png)

Here is how to access an item using the `items()` method

![image](https://user-images.githubusercontent.com/19383145/167321564-725ff120-a040-4528-979d-0f426ee8146c.png)

#### `len()` method - get the length of a dictionary

Each key-value pair is one item

![image](https://user-images.githubusercontent.com/19383145/167331657-3b30a9fa-8947-42b7-96a0-b05c45e99a33.png)

#### Loop through a dictionary

A dictionary is an unordered collection of items. 

The items in a dictionary are not necessarily going to be maintained in the order in which we insert them. 

We can't loop through the indices or the length of the dictionary using the `range()` function.

We need to loop through all of the keys in the dictionary then access the values based on those keys.

![image](https://user-images.githubusercontent.com/19383145/167332663-1e58030d-ef06-4f42-82d5-0e09ef7ec4d1.png)
![image](https://user-images.githubusercontent.com/19383145/167332719-727a833b-dec4-45bc-9de8-aa314d57902b.png)

`get()` method

`x.get()` will actually give us the value of the key. 

For example, If key 4 does not exist in the dictionary, it will instead return whatever we put as the second argument. 

If key 4 exists, it returns whatever value is associated with 4.

If key 4 doesn't exist in the dictionary, it just gives us 0. 

In the below example, If key 4 doesn't exist, return 0 and then add 1 to it. Otherwise, we will add one to whatever the value associated with key 4 is.

![image](https://user-images.githubusercontent.com/19383145/167333549-61887cd3-b154-41a0-85dd-365c26d14a29.png)
![image](https://user-images.githubusercontent.com/19383145/167333589-6742d55e-3f70-4606-ad9b-708bd9593161.png)

#### build a dictionary by looping through a string

This will keep track of the frequency of each character of the string

![image](https://user-images.githubusercontent.com/19383145/167334040-02f609e1-bb9b-46ec-a677-f217319b7ef2.png)

#### count how many characters user inputs to console

![image](https://user-images.githubusercontent.com/19383145/167334861-ec9b889b-8986-4b5e-b06f-8996b2e73629.png)

#### When to use a dictionary

A dictionary is an unordered collection of key-value pairs. 

It is useful for storing an unordered collection.

If you need to store the order in which items were inserted, then you need to use something like a list. 

Dictionaries are really good for doing things like frequency counting. 

An operation to check if an element exists in a dictionary can process instantly, whereas in a list, it will take a long time depending on how long the list is.

Whenever you're doing an operation where you want to see if something exists, you should favor using a dictionary over using a list, unless there is a specific reason you need to use a list. 

## Practice Questions

#### Write a program that asks the user to enter a string and prints the string's characters and their frequencies in any order and in the following format: `key: frequency`

![image](https://user-images.githubusercontent.com/19383145/167336216-7e1267b7-3390-48a9-9fb1-dcfb0bfcbedc.png)

[answer 1](https://github.com/KellzCodes/python/blob/main/fundamentals/dictionaries/practice1.py)

[answer 2](https://github.com/KellzCodes/python/blob/main/fundamentals/dictionaries/practice2.py)
