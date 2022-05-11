# Exceptions

![image](https://user-images.githubusercontent.com/19383145/167750277-77aa3c74-f35a-4b61-84c7-c053e56df09d.png)

![image](https://user-images.githubusercontent.com/19383145/167750412-43ac3f0d-1472-42f5-8a44-6b3e0ad8c66c.png)

#### Handling Exceptions

We handle exceptions by using something called a `try` and `except` block. 

Inside the `try` statement, we put the code we want to try to run. 

This code usually is prone to exceptions, and we know an exception might occur. So we put it inside of this `try` block. 

If an exception occurs, whatever is inside of the except block will actually run.

![image](https://user-images.githubusercontent.com/19383145/167751647-a7fd0932-7c04-4367-93bd-abd6616809f9.png)

This is what happens if an exception is not thrown

![image](https://user-images.githubusercontent.com/19383145/167751725-c97f9289-37eb-4528-9992-54d01124af4e.png)

#### Handling specific exceptions

Let's say you only want to handle an exception of a specific type, you can say `except` and then the type of exception you want to handle. Then you store the exception as a variable. 

Then it will only accept that specific error.  

![image](https://user-images.githubusercontent.com/19383145/167752272-459ffd71-67d4-4e1d-9c7c-089d08afa4d2.png)
![image](https://user-images.githubusercontent.com/19383145/167753124-f61dd470-8835-4159-8263-0effebe44bdc.png)

#### handling multiple exceptions

![image](https://user-images.githubusercontent.com/19383145/167754697-b18ad945-4766-4c7a-b971-3cc58c595f41.png)
![image](https://user-images.githubusercontent.com/19383145/167754746-4c034697-b495-41ac-bcfb-e63894a102a4.png)
![image](https://user-images.githubusercontent.com/19383145/167754834-4575428c-2c65-47e2-a771-642499897b44.png)

#### General exception

![image](https://user-images.githubusercontent.com/19383145/167755097-a59e9d4a-4ea9-4881-b22c-4a640325dded.png)

#### `finally` block

The `finally` block will always run whether an exception is caught or not

![image](https://user-images.githubusercontent.com/19383145/167755663-642e0128-4f1e-4b13-a661-daf572df9c10.png)
![image](https://user-images.githubusercontent.com/19383145/167755714-a0b99853-aa6a-443f-9bc8-25329671f497.png)

The point of a `finally` block is to perform cleanup operations no matter what happens in the `try` block

#### raise an error

![image](https://user-images.githubusercontent.com/19383145/167756185-8ddba034-be60-4f63-8ab9-72e32ade75d9.png)

#### Custom exception

![image](https://user-images.githubusercontent.com/19383145/167756829-700ca0f2-47f1-4a34-b813-bb54d4a5ae84.png)

#### take user input and throw an exception until the user enters a float

![image](https://user-images.githubusercontent.com/19383145/167757504-67fe30cb-517c-4619-a239-e9a07375f52a.png)

#### Run-time and compile-time errors

![image](https://user-images.githubusercontent.com/19383145/167762246-93252286-f4bc-4446-a39d-8edfe2117fda.png)

## Practice Question

![image](https://user-images.githubusercontent.com/19383145/167763113-1d742e7f-8c93-4d8d-a5a6-2e71376966ed.png)

![image](https://user-images.githubusercontent.com/19383145/167763147-ec704858-597c-45ab-a36d-db63784f849c.png)

[answer 1](https://github.com/KellzCodes/python/blob/main/fundamentals/exceptions/practice1.py)

[answer 2](https://github.com/KellzCodes/python/blob/main/fundamentals/exceptions/practice2.py)
