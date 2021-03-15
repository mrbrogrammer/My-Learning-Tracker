# Python Notes

## Classes

Syntax:

```py
class Point():
    # A method defining how to create a point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(2, 4)

```

- ```self``` is used to represent the object we are currently working with. ```self``` should be the first argument for any method within a Python class.

## Decorators

Decorcators consists of 5 important elements and they are in order: The **head** with any desired parameter *(keep in mind that the parameter will be represented as a function)*. The **wrapper** which has the logic and the head returns. Inside the wrapper we also have the **function variable** that will be called *remember the function variable is declared as a parameter in the head*. We can then apply this decorator using an ```py@``` symbol or ```py @head``` followed by what the function variable should implement. 

Syntax:

```py
import sleep

def signal():
    def wrapper():
        sleep(3)
        f()
        sleep(3)
        print("LESSSS GOOOO!")
    return wrapper

@signal
def alarm:
    print("Wake up")

alarm()

""" Output:
Wake up!
LESSSS GOOOO!
"""

```

### Lambda

The **lambda** function is an other way of writing functions, a lot like a expression operator. Where the Input is on the left of ```:``` and Output is on the right. Percisely this is where the logic goes.

Syntax:

```py
square = lambda x : x ** x

objects.sort(key= lambda obj: obj["hype"])
```

### Exceptions

We’ll run into problems when we attempt to divide by 0. This is where ```py try:``` and ```py exception:``` comes in. We'll first ```try:``` or attempt to get the result from ```x / y``` ``` except``` when we get a ```ZeroDivisionError```.

![](https://cs50.harvard.edu/web/2020/notes/2/images/dividebad.png)

Syntax:

```py
try: 
    x / y 

except ZeroDivisionError: 
    print("Error: Cannot divide by 0.")
    #exit the program

```

[Read more](https://cs50.harvard.edu/web/2020/notes/2/)
