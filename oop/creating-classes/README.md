# Creating Classes

We know that Python comes with a variety of built-in classes; but how do we go about creating our own?

Always name a class with capital first letter and every word has capital letter.

![image](https://user-images.githubusercontent.com/19383145/168495381-c166105c-0562-45f7-ac36-1886b87b0948.png)
![image](https://user-images.githubusercontent.com/19383145/168495396-3f9ae2af-7552-413f-91be-00723513356d.png)

Class instance

![image](https://user-images.githubusercontent.com/19383145/168495451-b1bed669-a45a-4121-a1b1-9de7a9064fba.png)

class type

![image](https://user-images.githubusercontent.com/19383145/168495485-75d6b7ca-a9f0-401b-aaa4-2be4dca34d23.png)

### `__init()__` method

This method will run whenever we create a new instance of a class

![image](https://user-images.githubusercontent.com/19383145/168495669-a629eed4-7727-4d11-a75d-a5433d35710b.png)

You can pass parameter to an object instance

![image](https://user-images.githubusercontent.com/19383145/168495734-aa881582-a7ec-4e3f-86e2-ac4a645788c7.png)

![image](https://user-images.githubusercontent.com/19383145/168495766-d25eaea1-9396-4d5e-a65f-8caffe223495.png)

### Creating and Accessing Attributes

Attribute is data/objects associated with an instance of a class

In Python object oriented programming an attribute is any data/objects associated with a class or an instance of a class.

Attributes are not always defined inside of the class constructor and can be added to an instance after its creation

#### `self` 

`self` is a parameter that needs to be in all your methods, especially `__init()__` method. 

`self` is always the first parameter in a class constructor.

The `self` parameter refers to the instance of the class in which the method or constructor is being called on.

The first parameter in the class constructor (aka the `__init__()` method) is implicitly passed during the instantiation of an object and is mandatory. 

Note that the name `self` is a recommended convention in Python but not the mandatory name for this first parameter.

![image](https://user-images.githubusercontent.com/19383145/168496000-4394b7bb-4e9d-43ad-b691-280345a0dd5d.png)
![image](https://user-images.githubusercontent.com/19383145/168496200-b14c0c5a-c73f-479c-966b-6c0b27b26ccf.png)

#### modify attribute from outside of class

create new attribute

![image](https://user-images.githubusercontent.com/19383145/168496369-55e666dc-9129-426e-a33d-f711607b7d7a.png)

change an existing attribute

![image](https://user-images.githubusercontent.com/19383145/168496452-ce4729be-474e-4bac-a547-967dd5c64323.png)

### Create a fruit class

![image](https://user-images.githubusercontent.com/19383145/168496656-190b5f23-cdc9-45f0-993e-aff91f7499e6.png)

