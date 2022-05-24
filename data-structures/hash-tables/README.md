# Hash Tables

![image](https://user-images.githubusercontent.com/19383145/170123377-8cbd5c4e-a415-448d-8eb8-8d44bcfcfb61.png)

In python, dictionaries are hash tables. 

Below is a hash table where we've got 3 keys, "foo", "bar", and "hash". All 3 keys are mapped respectively to the values 1, 2, and 3. 

![image](https://user-images.githubusercontent.com/19383145/170128770-7e916f3c-4690-46b0-926b-d74ebd0c3727.png)

The idea behind a hash table is that you can access a value given a key. For instance, we can very easily access the number one given the key "foo". But we wouldn't be able to do the opposite. We would not be able to find the key "foo" given value 1. 

The beauty behind a hash table is that insertion of a new key-value pair, deletion of a key-value pair, or searching for a value given a key are all operations that run in constant time on average. 

![image](https://user-images.githubusercontent.com/19383145/170129377-f399d5dd-aef9-4666-92b8-a9f425bc2b67.png)

The keys in hash tables do not have to be integers or indices like in an array. Keys can be strings or other data types. 

### How is it possible to have a constant time look up with a key that is not a number or an integer?

Hash tables are built on top of arrays. 

Under the hood, we have an array. For now, the array will have three indices. We will be storing the values of our hash table in the array. That's what's going to allow us to have constant time look up given an index. 

When you're inserting a key-value pair inside a hash table, you use what's called a hash function to transform the key into an index. 

![image](https://user-images.githubusercontent.com/19383145/170133335-81d02462-7e3a-476c-9df0-52f83f5e25cf.png)

### What happens when your hash table is full?

When your hash table has a lot of giant linked lists, it's going to lead to `O(N)` insertion, deletion, and searching.  

To handle this, you can implement a hash table that resizes itself. 
