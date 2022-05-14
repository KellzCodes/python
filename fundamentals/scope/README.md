# scope

### a variable declared in a function is not accessible outside of the function

This program won't output anything and will actually raise an exception. This is because `x` isn't defined in the global scope and therefore can't be accessed there.

```
def foo():
    x = "hello world"

foo()
print(x)
```

### immutable global values cannot be changed in functions

This program prints `5`, which is the value of the `x` that's passed to the print function. This is because this `x` is immutable and is defined in the global scope as `5`. Therefore, the call to `foo` doesn't change the value of this `x`.

Inside of `foo`, the parameter `x` that's passed to `foo` gets reassigned to `4`, but this isn't the same `x` that gets printed.

```
x = 5

def foo(x):
    x = 4

foo(x)
print(x)
```

This program prints `5`, which is the value of the `x` that's passed to the print function. This is because this `x` is immutable and is defined in the global scope as `5`. Therefore, the call to `foo` doesn't change the value of this `x`.

Inside of `foo`, a new `x` is declared and set to `4`, but this isn't the same `x` that gets printed.

```
x = 5

def foo(y):
    x = 4
    y = x

foo(x)
print(x)
```

### mutable objects can be changed in functions

This program prints `[1]`, which is the value of the `x` that's passed to the `print` function. This is because this `x` is mutable and is passed to `foo` as the parameter `y`. This means that `y` is simply an alias of this `x`, and any changes to the list stored in `y` affect this `x`; `x` and `y` store the same list.

```
x = []

def foo(y):
    y.append(1)

foo(x)
print(x)
```

### setting a variable that contains a mutable object `=` to something else just reassigns the variable without modifying the object

The program prints `[1]`, which is the value of the `x` that's passed to the `print` function. This is because this `x` is mutable and is passed to `foo` as the parameter `y`. This means that `y` is simply an alias of this `x`, and any changes to the list stored in `y` affect this `x`; `x` and `y` store the same list.

The line `y = [2]` inside the `foo` function doesn't change the value of `x` because it simply reassigns the variable `y` to a new list without modifying the list stored in `y`.

```
x = []

def foo(y):
    y.append(1)
    y = [2]

foo(x)
print(x)
```

### `global` keyword

The `global` keyword is typically considered bad practice and should be avoided. 

The reason for this is that the `global` keyword adds side-effects to a function and makes it dependent on something referenced outside the function scope. This means changes to the globally referenced object can change the behaviour of the function and be difficult to detect, especially if a bug or issue arises. In summary, the `global` keyword often introduces unnecessary complexity and can almost always be avoided.

The below program prints `global,local,local`

The first call to the `print` function that gets executed is the first one inside of the `foo` function. This call prints `global,`, because at that execution point in the program, `x` has only been defined as `"global"` in the global scope.

However, after this first `print` statement, we assign `x` to the new value of `"local"`, meaning that when `x` is printed again right after, we print `"local"`. We do not create a new `x` in the local scope, instead we change the value of the `x` in the global scope.

Finally, the last call to `print` takes in the `x` defined in the global scope, which was modified in the `foo` function because of the presence of the `global` keyword. Therefore, this call prints `"local"`.

```
x = "global"

def foo():
    global x
    print(x, end=",")
    x = "local"
    print(x, end=",")

foo()
print(x, end="")
```
