# Mutability

![image](https://user-images.githubusercontent.com/19383145/167977498-d913f52e-abb5-465a-977c-8b88335e3900.png)

![image](https://user-images.githubusercontent.com/19383145/167977699-7f2a1114-346b-43e9-a20d-0623515c09d2.png)

### `is` keyword on mutable data types

`is` tells you if two objects are the same

`x` and `y` are two different lists that are equivalent but they are not the same object

![image](https://user-images.githubusercontent.com/19383145/167978570-0e7ed1e0-4b34-408b-a86a-272643a4fe3b.png)

setting `y` = `x` is creating another name or alias for x. Now y and x are interchangeable when referencing the same object. 

Any operation we do on both will affect both of them. 

![image](https://user-images.githubusercontent.com/19383145/167978911-70120ef4-96f7-499c-aed5-36313038b510.png)

### `is` keyword on immutable data types

setting `b = a` is creating another name or alias for a. Now a and b are interchangeable when referencing the same object.

changing `a` to `a += 1` will not change `b`. `a` will change to the new value. `b` will stay the value that it was when it was set to `a`.

![image](https://user-images.githubusercontent.com/19383145/168182163-538930e7-6869-4989-ba0d-5c9cda4137d6.png)

### `id()` function

This will let you see an object's location in random access memory

setting `b = a` will give both `a` and `b` the same id

![image](https://user-images.githubusercontent.com/19383145/168182480-0b1b8120-5eb7-481b-81c9-d0e8570adab7.png)

setting both variables to different values will give different `id()` values

![image](https://user-images.githubusercontent.com/19383145/168182607-61000c1d-84a6-4d21-b537-187a179dbdd4.png)

Python likes to optimize very small integers to save space. So setting `a` and `b` to the same small integer will return the same id.

![image](https://user-images.githubusercontent.com/19383145/168182834-30c23608-e718-41eb-83de-088e838d5900.png)


### copy mutable objects

To make a copy of a list that is a brand new different object, make a slice instead of using `=`

![image](https://user-images.githubusercontent.com/19383145/168184845-a8d0b8a2-d2e0-46ad-8187-843b91a18d79.png)
![image](https://user-images.githubusercontent.com/19383145/168184930-5f5a4cd6-7fec-4df0-bd7d-5dfddef7ea54.png)

good practice to copy the parameter of a function if you do not want to change the original list

![image](https://user-images.githubusercontent.com/19383145/168185257-99cc9a43-5dba-4c63-b2bf-84445fa5f287.png)

copy sets and dictionaries using `copy()`

![image](https://user-images.githubusercontent.com/19383145/168185983-5e27b1f8-8636-4d69-8255-a8bb876e17cf.png)
![image](https://user-images.githubusercontent.com/19383145/168186671-f43bbbfc-5df6-4586-9d06-5cd056a6eb6d.png)

### nested mutable objects

you can change a list that is stored inside of a dictionary

![image](https://user-images.githubusercontent.com/19383145/168187625-2368e9cb-64e8-4e08-ba4d-ca44f1c91e43.png)

You can change a mutable object that is stored inside of an immutable object

![image](https://user-images.githubusercontent.com/19383145/168187968-3cccbec9-32bd-4b41-8dfa-de6d896f9e0c.png)

### Shallow copy

When you set `c = a[0]`, you reference the nested mutable object. 

This object is actually being stored by both `a` and `b` inside of the list. 

![image](https://user-images.githubusercontent.com/19383145/168201008-8051b981-c168-4c43-915e-806ef9f99aa9.png)

`a` and `b` are not the same object

![image](https://user-images.githubusercontent.com/19383145/168201120-51cb7569-7857-4489-8c9d-f75f5cc69cb0.png)

If you append an integer to `a`, it won't be added to `b`

![image](https://user-images.githubusercontent.com/19383145/168201271-c5e96555-2b70-4dd8-9d8d-fddcf0608ee2.png)

Since we have the same mutable object being stored in both `a` and `b`, when you make a change to that mutable object, it makes a change in both `a` and `b`

When you make a copy of a mutable object, it doesn't just copy everything inside of the object. 

It will copy the object itself but is not copying all of the potentially mutable objects that are inside of the object. 

This is known as a shallow copy. 
