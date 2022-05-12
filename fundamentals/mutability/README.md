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


