# Slices

![image](https://user-images.githubusercontent.com/19383145/167231030-b5f82978-ea4f-4370-9030-7b167cf0c068.png)

A slice is an operator that we can use on a collection data type. 

A slice allows us to actually get a subset of the collection. 

So we can slice a list, string, tuple, etc. into a new list, string, tuple, etc. 

When you take a slice of a data type, you can pass a start value, a stop value, and a step value. These are the indices you want to retrieve from this list.

#### slice the first two elements of a list

![image](https://user-images.githubusercontent.com/19383145/167231719-f6edad3d-1012-4403-8000-66de07c3a84d.png)

When you use a slice, you do not have to pass both the start and the step. 

You must pass a stop. 

![image](https://user-images.githubusercontent.com/19383145/167237255-91991874-6854-4ef6-94e3-401114a23a3f.png)

#### Negative slicing - Go backwards

Start at index 8, stop at index 0 (not inclusive), step by -1 (backwards)

![image](https://user-images.githubusercontent.com/19383145/167237462-a87ab7cb-06ed-4049-bb0c-50e69a32e686.png)

#### The single colon

When you do a slice, the only thing required is single colon. 

By default, the right will be the start (beginning of list) and the left will be the end (end of the list).

![image](https://user-images.githubusercontent.com/19383145/167237628-2ea58051-22f7-40c5-91d3-ab7a51c5b9a1.png)

#### slice every other element in a list

![image](https://user-images.githubusercontent.com/19383145/167237694-e1dafacb-3a45-4548-8e31-c386996cf434.png)

