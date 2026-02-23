# Introduction
Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

### Python Variables
Variables are created when you assign a value to it:

### Comments
```
#This is a comment.
```

### Python Output
Print Without a New Line: print("Hello World!", end=" ")

### Python Variables

#### Rules for Python variables:
- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.

#### Many Values to Multiple Variables: 
```
x, y, z = "Orange", "Banana", "Cherry"
```

#### Unpack a Collection: 
```
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
```

#### The global Keyword
```
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

#### Casting
```
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

#### Get the Type
```
print(type(x))
```

#### Python Data Types
- Text Type: str
- Numeric Types: int, float, complex (ex: z = 1j)
- Sequence Types: list, tuple, range
- Mapping Type: dict
- Set Types: set, frozenset
- Boolean Type: bool
- Binary Types: bytes, bytearray, memoryview

- None Type: NoneType


### Numbers
#### Random Number
```
import random
print(random.randrange(1, 10))
```

### Strings
#### Multiline Strings (using triple double/single quotes)
```
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

#### Strings are Arrays
Strings in Python are arrays of unicode characters. Python does not have a character data type, a single character is simply a string with a length of 1.
```
a = "Hello, World!"
print(a[1])
```

#### String Length
```
print(len(a))
```

#### Check String (using in)
```
print("free" in txt)
#or
if "free" in txt:
  print("Yes, 'free' is present.")

# using not in 
print("expensive" not in txt)
```

#### Slicing Strings
```
print(b[2:5]) # doesn't includes last char
# Slice From the Start
print(b[:5])
# Slice To the End
print(b[2:])
# negative indexes to start the slice from the end of the string
print(b[-5:-2])
```

#### Modify Strings
```
# Upper Case
print(a.upper())

# Lower Case
print(a.lower())

# Remove Whitespace
print(a.strip())

# Replace String
print(a.replace("H", "J"))

# Split String
print(a.split(","))
```

#### Format - Strings
```
# F-Strings
txt = f"My name is John, I am {age}"

# F-Strings - Placeholders and Modifiers
txt = f"The price is {price:.2f} dollars"
txt = f"The price is {20 * 59} dollars"
```

#### Escape Characters
Code:     Result
```
\'	    Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	Octal value	
\xhh	Hex value
```

#### String Methods
- capitalize(): Converts the first character to upper case

- casefold(): Converts string into lower case
- center(): Returns a centered string
- count(): Returns the number of times a specified value occurs in a string
- encode(): Returns an encoded version of the string
- endswith(): Returns true if the string ends with the specified value
- expandtabs(): Sets the tab size of the string
- find(): Searches the string for a specified value and returns the position of where it was found
- format(): Formats specified values in a string
- format_map(): Formats specified values in a string
- index(): Searches the string for a specified value and returns the position of where it was found
- isalnum(): Returns True if all characters in the string are alphanumeric
- isalpha(): Returns True if all characters in the string are in the alphabet
- isascii(): Returns True if all characters in the string are ascii characters
- isdecimal(): Returns True if all characters in the string are decimals
- isdigit(): Returns True if all characters in the string are digits
- isidentifier(): Returns True if the string is an identifier
- islower(): Returns True if all characters in the string are lower case
- isnumeric(): Returns True if all characters in the string are numeric
- isprintable(): Returns True if all characters in the string are printable. Returns false if contains non-printable control characters like newlines, tabs, and carriage returns. 
- isspace(): Returns True if all characters in the string are whitespaces
- istitle(): Returns True if the string follows the rules of a title
- isupper(): Returns True if all characters in the string are upper case
- join(): Joins the elements of an iterable to the end of the string
- ljust(): Returns a left justified version of the string
- lower(): Converts a string into lower case
- lstrip(): Returns a left trim version of the string
- maketrans(): Returns a translation table to be used in translations
- partition(): Returns a tuple where the string is parted into three parts
- replace(): Returns a string where a specified value is replaced with a specified value
- rfind(): Searches the string for a specified value and returns the last position of where it was found
- rindex(): Searches the string for a specified value and returns the last position of where it was found
- rjust(): Returns a right justified version of the string
- rpartition(): Returns a tuple where the string is parted into three parts
- rsplit(): Splits the string at the specified separator, and returns a list
- rstrip(): Returns a right trim version of the string
- split(): Splits the string at the specified separator, and returns a list
- splitlines(): Splits the string at line breaks and returns a list
- startswith(): Returns true if the string starts with the specified value
- strip(): Returns a trimmed version of the string
- swapcase(): Swaps cases, lower case becomes upper case and vice versa
- title(): Converts the first character of each word to upper case
- translate(): Returns a translated string
- upper(): Converts a string into upper case
- zfill(): Fills the string with a specified number of 0 values at the beginning

### Python Booleans
Booleans represent one of two values: True or False.

The bool() function allows you to evaluate any value, and give you True or False in return

Any string is True, except empty strings. Any list, tuple, set, and dictionary are True, except empty ones.

## Python Operators
- Arithmetic operators : +, -, *, /, %, **, //(	Floor division)
- Assignment operators : =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=, :=(we can use it like: print(x:=3) // output=3)
- Comparison operators: ==, !=, >, <, >=, <=
- Logical operators: and, or, not
- Identity operators: is, is not
- Membership operators: in, not in
- Bitwise operators: &, |, ^, ~, <<, >>

#### The Walrus Operator
```
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")
```

## Python Collections (Arrays)
There are four collection data types in the Python programming language:
- List is a collection which is ordered and changeable. Allows duplicate members.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
- Set is a collection which is unordered, mutable collection with immutable type of elements, and unindexed. No duplicate members.
- Dictionary is a collection which is ordered** and changeable. No duplicate members.

## Python Lists
Lists are used to store multiple items in a single variable.

List items are ordered, changeable, and allow duplicate values. List items can be of any data type.

Example: 
```
mylist = ["apple", "banana", "cherry"]
thislist = list(("apple", "banana", "cherry")) # double round () required
```

### List Methods
- append(): Adds an element at the end of the list
- clear(): Removes all the elements from the list
- copy(): Returns a copy of the list. Alt: list()
- count(): Returns the number of elements with the specified value
- extend(): Add the elements of a list (or any iterable), to the end of the current list
- index(): Returns the index of the first element with the specified value
- insert(): Adds an element at the specified position
- pop(): Removes the element at the specified position
- remove(): Removes the item with the specified value
- reverse(): Reverses the order of the list

- sort(): Sorts the list. Reverse sort: thislist.sort(reverse = True)

Example: 
```
# custom sort
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
```

## Python Tuples
A tuple is a collection which is ordered and unchangeable.

Example:
```
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```

### Tuple Methods
- count(): Returns the number of times a specified value occurs in a tuple
- index(): Searches the tuple for a specified value and returns the position of where it was found

## Python Sets
A set is a collection which is unordered, unchangeable*, and unindexed.

Example:
```
thisset = {"apple", "banana", "cherry"}
# thisset = set(("apple", "banana", "cherry"))
```

# Set Methods
- add(): Adds an element to the set
- clear(): Removes all the elements from the set
- copy(): Returns a copy of the set
- difference(): Returns a set containing the difference between two or more sets
- difference_update(): Removes the items in this set that are also included in another, specified set
- discard(): Remove the specified item
- intersection(): Returns a set, that is the intersection of two other sets
- intersection_update(): Removes the items in this set that are not present in other, specified set(s)
- isdisjoint(): Returns whether two sets have a intersection or not
- issubset(): Returns True if all items of this set is present in another set
- <: Returns True if all items of this set is present in another, larger set
- issuperset(): Returns True if all items of another set is present in this set
- >: Returns True if all items of another, smaller set is present in this set
- pop(): Removes an element from the set
- remove(): Removes the specified element
- symmetric_difference(): Returns a set with the symmetric differences of two sets
- symmetric_difference_update(): Inserts the symmetric differences from this set and another
- union(): Return a set containing the union of sets
- update(): Update the set with the union of this set and others

#### Python frozenset
frozenset is an immutable version of a set. Like sets, it contains unique, unordered, unchangeable elements. Unlike sets, elements cannot be added or removed from a frozenset.

Example:
```
x = frozenset({"apple", "banana", "cherry"})
```

##### Frozenset Methods
copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference(), union()

## Python Dictionaries
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#### Example
```
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict = dict(name = "John", age = 36, country = "Norway")
```

### Dictionary Methods
- clear(): Removes all the elements from the dictionary
- copy(): Returns a copy of the dictionary

- fromkeys(): Returns a dictionary with the specified keys and value
- get(): Returns the value of the specified key
- items(): Returns a list containing a tuple for each key value pair
- keys(): Returns a list containing the dictionary's keys
- pop(): Removes the element with the specified key
- popitem(): Removes the last inserted key-value pair
- setdefault(): Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
- update(): Updates the dictionary with the specified key-value pairs
- values(): Returns a list of all the values in the dictionary

## Python If Statement
Example: 
```
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# shorthands
if a > b: print("a is greater than b")
print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")
```

### The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

```
if b > a:
  pass
```

## Python Match
The match statement is used to perform different actions based on different conditions.

Syntax: 
```
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
```

Example:
```
month = 5
day = 4
match day:
  case 1 | 2 | 6: # combine values
    print("Today is Saturday")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")
```

## While Loops
Example:
```
i = 1
while i < 6:
  print(i)
  if i == 3:
    break # continue 
  i += 1
else:
  print("i is no longer less than 6")
```

## For Loops
```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
else:
  print("Finally finished!")

# using range
for x in range(6):
  print(x)
```

## Python Functions
```
def my_function():
  print("Hello from a function")

my_function()
```

#### Default Parameter Values
```
def my_function(name = "friend"):
  print("Hello", name)
```

#### Keyword Arguments
if no keyword arg used then it is Positional Arguments
```
def my_function(animal, name):
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")
```

#### Positional-Only Arguments
To specify positional-only arguments, add , / after the arguments:
```
def my_function(name, /):
  print("Hello", name)
```

#### Keyword-Only Arguments
To specify that a function can have only keyword arguments, add *, before the arguments:
```
def my_function(*, name):
  print("Hello", name)
```

#### Combining Positional-Only and Keyword-Only
/ must be ahead of *
```
def my_function(a, b, /, *, c, d):
  return a + b + c + d
```

### *args
The *args parameter allows a function to accept any number of positional arguments. args becomes a tuple containing all the passed arguments.
```
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total
print(my_function(1, 2, 3))
```

### **kwargs
allows a function to accept any number of keyword arguments.
```
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")
```

#### Unpacking Arguments
If you have values stored in a list, you can use * to unpack them into individual arguments and If you have keyword arguments stored in a dictionary, you can use ** to unpack them.
```
def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers)

#  using **
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)
```

### Nonlocal Keyword
The nonlocal keyword makes the variable belong to the outer function.
```
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())
```

### LEGB Rule
Python follows the LEGB rule when looking up variable names, and searches for them in this order:

- Local - Inside the current function
- Enclosing - Inside enclosing functions (from inner to outer)
- Global - At the top level of the module
- Built-in - In Python's built-in namespace

### Python Decorators
Decorators let you add extra behavior to a function, without changing the function's code.

Define the decorator first, then apply it with @decorator_name above the function. You can use multiple decorators on one function.
```
def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"
print(myfunction())
```
 
### Preserving Function Metadata
Python has metadata that can be accessed using the __name__ and __doc__ attributes.

### Python Lambda
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Ex:
```
x = lambda a : a + 10
```

### Python Generators
Generators are functions that can pause and resume their execution. When a generator function is called, it returns a generator object, which is an iterator. Generators are memory-efficient because they generate values on-the-fly instead of storing everything in memory.

```
def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)
```

The yield keyword is what makes a function a generator.

-> next() with Generators:
```
gen = simple_gen()
print(next(gen))
```

#### Generator Methods
- send(): allows you to send a value to the generator
    ```
    def echo_generator():
    while True:
      received = yield
      print("Received:", received)
    gen = echo_generator()
    next(gen) # Prime the generator
    gen.send("Hello")
    gen.send("World")
    ```
- close(): stops the generator

## Python range
returns an immutable sequence of numbers, commonly used for looping a specific number of times.

Syntax:
```
range(start, stop, step)
```

## Python Arrays
An array can hold many values under a single name, and you can access the values by referring to an index number.

### Array Methods
- append(): Adds an element at the end of the list
- clear(): Removes all the elements from the list
- copy(): Returns a copy of the list
- count(): Returns the number of elements with the specified value
- extend(): Add the elements of a list (or any iterable), to the end of the current list
- index(): Returns the index of the first element with the specified value
- insert(): Adds an element at the specified position

- pop(): Removes the element at the specified position
- remove(): Removes the first item with the specified value
- reverse(): Reverses the order of the list
- sort(): Sorts the list

## Python Modules
A file containing a set of functions you want to include in your application.

To create a module just save the code you want in a file with the file extension .py.
Use a Module: import mymodule

Example:
```
import mymodule as mx
a = mx.person1["age"]
print(a)
```

### Built-in Modules
```
import platform

x = platform.system()
print(x)
```

## Python Datetime
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

```
import datetime
x = datetime.datetime.now()
print(x)
```

### timedelta
The Python timedelta class, part of the built-in datetime module, represents a duration or the difference between two dates or times.

```
from datetime import datetime, timedelta
print("Current time: ", datetime.now())
print(datetime.now() - timedelta(days=5, hours=-5))
```

#### The strftime() Method
formatting date objects into readable strings.
```
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
```

## Python Math
### Built-in Math Functions
- min()
- max()
- abs()
- pow(x,y)

#### Math Module
```
import math
x = math.sqrt(64)
print(x)
```
- math.ceil(1.4)
- math.pi

## Python JSON

#### Convert from JSON to Python
```
import json
x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])
```

#### Convert from Python to JSON
```
import json
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
# json.dumps(x, indent=4, sort_keys=True)
print(y)
```

## Python RegEx
```
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
```

#### RegEx Functions
- findall: Returns a list containing all matches
- search: Returns a Match object if there is a match anywhere in the string
- split: Returns a list where the string has been split at each match
- sub: Replaces one or many matches with a string

## Python Try Except
```
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# using else
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```

-> Raise an exception: throws an exception
```
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
```

## Python None
None is a special constant in Python that represents the absence of a value.
```
x = None
print(type(x))
```

## Python User Input
```
name = input("Enter your name:")
print(f"Hello {name}")
```

## Python Virtual Environment
A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.

#### Creating a Virtual Environment
```
python -m venv myfirstproject
```

#### Activate env
```
myfirstproject\Scripts\activate
```

#### Deactivate Virtual Environment
```
deactivate
```

#### Delete Virtual Environment
```
rmdir /s /q myfirstproject
```

# Python OOP
Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

## Classes and Objects

#### Create a Class
```
class MyClass:
  x = 5
```

#### Create Object
```
p1 = MyClass()
print(p1.x)
```

#### Delete Objects
```
del obj
```

### The __init__() Method
used to assign values to object properties, or to perform operations that are necessary when the object is being created.
```
class Person:
  def __init__(self, name, age):
  # def __init__(self, name, age=18): default values
    self.name = name
    self.age = age
```

The self parameter is a reference to the current instance of the class. It is used to access properties and methods that belong to the class. self Does Not Have to Be Named "self".

### Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

#### Create a Child Class
```
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    # super().__init__(fname, lname)
```

-> Types:
- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierarchical Inheritance
- Hybrid Inheritance

#### Diamond problem in python
Python solves the "diamond problem" by using a specific and predictable Method Resolution Order (MRO).

-> How Python's MRO Works
- Predictable Order
- Left-to-Right Precedence
- Cooperative Calling with super()

```
# Check the MRO
print(D.__mro__)
```

## Polymorphism

### Function Polymorphism
e.g.: len()

### Class Polymorphism
Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

### Encapsulation
Encapsulation is about protecting data inside a class. It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

-> Private Properties: 
In Python, you can make properties private by using a double underscore __ prefix

#### Why Use Encapsulation?
Encapsulation provides several benefits:
- Data Protection: Prevents accidental modification of data
- Validation: You can validate data before setting it
- Flexibility: Internal implementation can change without affecting external code
- Control: You have full control over how data is accessed and modified

-> Protected Properties:
Python also has a convention for protected properties using a single underscore _ prefix

-> Private Methods:
You can also make methods private using the double underscore prefix

### Accessing Inner Class from the Outside
To access the inner class, create an object of the outer class, and then create an object of the inner class:
```
outer = Outer()
inner = outer.Inner()
inner.display()
```

### Accessing Outer Class from Inner Class
Inner classes in Python do not automatically have access to the outer class instance.

If you want the inner class to access the outer class, you need to pass the outer class instance as a parameter:
```
outer = Outer()
inner = outer.Inner()
inner.display()
```
