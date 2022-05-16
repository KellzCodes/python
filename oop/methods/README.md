# methods

![image](https://user-images.githubusercontent.com/19383145/168502118-4b5f2c3d-2416-40b5-b2ba-c237462b0aa3.png)

![image](https://user-images.githubusercontent.com/19383145/168502187-dcf40e96-4f46-453c-b5e5-5a1b098feb95.png)

### setter methods

![image](https://user-images.githubusercontent.com/19383145/168502564-4ad28747-7775-43c3-bdff-572e827f768c.png)

### getter methods

you need to make sure the attribute you are getting are already defined in the `__init__() method before you call this getter method

![image](https://user-images.githubusercontent.com/19383145/168502872-edd66c2d-4423-4685-9ce7-184f25b7da52.png)

### Counter class example

![image](https://user-images.githubusercontent.com/19383145/168503193-799cc267-c969-46bb-8098-948825b39281.png)

#### create a lock that tells us whether or not we can increment or decrement the counter

```
class Counter:
  def __init__(self):
    self.count = 0
    self.locked = False
    
  def toggle_lock(self):
    self.locked = not self.locked
    
  def increment(self):
    if self.locked:
      raise Exception("The counter is locked!")
    self.count += 1
    
  def decrement(self):
    if self.locked:
      raise Exception("The counter is locked!")
    self.count -= 1
    
  def print_count(self):
    print(f"The current count is {self.count}")
    
counter = Counter()
counter.increment()
counter.increment()
counter.increment()
counter.decrement()
counter.print_count()
counter.toggle_lock()
counter.increment()
```

output:

![image](https://user-images.githubusercontent.com/19383145/168503957-97ef7d47-26ea-45ee-b220-821544ebcd36.png)

