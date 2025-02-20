```python

## this is single line comment
'''
this is a exmaple of
multiline comments
'''
```

## Python program to check if a variable is of a specific data type.
```python
var = 10.5
if isinstance(var, float):
    print(f"{var} is a float")
else:
    print(f"{var} is not a float")
```

## Python program to reverse a string.
```python
string = input("Enter a string: ")
reversed_string = string[::-1]
print(f"The reversed string is: {reversed_string}")
```

## Python program to check if a string is a palindrome.
```python
string = input("Enter a string: ")
if string == string[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
```

## Loop Control Statements
```python
break
## The break statement exits the loop permaturely
continue
## The continue statement skips the current iteration and continues with the next.
pass
## The pass statement is a null operation; it does nothing.

```

## List Comprehension
```python
Basics Syantax            [expression for item in iterable]

with conditional logic    [expression for item in iterable if condition]

Nested List Comprehension [expression for item1 in iterable1 for item2 in iterable2]
```
---

# Functions in Python: Default, Positional, `*args`, and `**kwargs`
## Function Syntax
```python
## syntax
def function_name(parameters):
    """Docstring"""
    # Function body
    return expression
```

## 1. Default Arguments
Default arguments allow you to assign default values to function parameters. If the caller doesn’t provide a value for a parameter, the default value is used.

### Example:
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet()         # Output: Hello, Guest!
```

### Key Points:
- Default arguments must appear **after** positional (non-default) arguments in the function definition.

```python
def greet(name, greeting="Hello"):  # Correct
    print(f"{greeting}, {name}!")

def greet(greeting="Hello", name):  # SyntaxError
    print(f"{greeting}, {name}!")
```

---

## 2. Positional Arguments
Positional arguments are passed to a function in the order in which they are defined.

### Example:
```python
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8
```

### Key Points:
- The order of arguments matters.
- All arguments without default values must be provided by the caller.

---

## 3. `*args` (Variable-Length Positional Arguments)
The `*args` syntax allows a function to accept any number of positional arguments. These arguments are collected into a tuple.

### Example:
```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3))  # Output: 6
print(sum_numbers(4, 5))     # Output: 9
print(sum_numbers())         # Output: 0
```

### Key Points:
- `*args` is commonly used when the number of arguments is unknown.
- You can mix `*args` with other arguments, but `*args` must come **after** the fixed positional arguments.

```python
def multiply(factor, *args):
    return [factor * num for num in args]

print(multiply(2, 1, 2, 3))  # Output: [2, 4, 6]
```

---

## 4. Keyword Arguments
Keyword arguments are passed using the `key=value` syntax, allowing you to specify which parameter you’re assigning a value to.

### Example:
```python
def describe_person(name, age):
    print(f"{name} is {age} years old.")

describe_person(name="Alice", age=25)  # Output: Alice is 25 years old.
describe_person(age=30, name="Bob")   # Output: Bob is 30 years old.
```

### Key Points:
- Keyword arguments are often used to improve code readability.
- They can appear alongside positional arguments but must come **after** positional arguments.

---

## 5. `**kwargs` (Variable-Length Keyword Arguments)
The `**kwargs` syntax allows a function to accept any number of keyword arguments. These arguments are collected into a dictionary.

### Example:
```python
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
```

### Key Points:
- `**kwargs` is used when the number of keyword arguments is unknown.
- You can mix `**kwargs` with other arguments, but `**kwargs` must come **last** in the parameter list.

```python
def full_description(title, **kwargs):
    print(f"Title: {title}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

full_description("Developer", name="Alice", skills=["Python", "SQL"], experience="5 years")
# Output:
# Title: Developer
# name: Alice
# skills: ['Python', 'SQL']
# experience: 5 years
```

---

## Combining Positional, Default, `*args`, and `**kwargs`
You can combine all these types of arguments in a single function. The order must be:
1. Positional arguments
2. Default arguments
3. `*args`
4. `**kwargs`

### Example:
```python
def combined_function(a, b=10, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

combined_function(1, 20, 30, 40, name="Alice", age=25)
# Output:
# a: 1, b: 20
# args: (30, 40)
# kwargs: {'name': 'Alice', 'age': 25}
```

---

### Summary
- **Default Arguments**: Provide default values for parameters.
- **Positional Arguments**: Pass arguments in the correct order.
- **`*args`**: Handle a variable number of positional arguments as a tuple.
- **`**kwargs`**: Handle a variable number of keyword arguments as a dictionary.
- You can combine these types of arguments, but the order matters!

---

## Lambda Functions in Python
Lambda functions are small anonymous functions defined using the **lambda** keyword. They can have any number of arguments but only one expression. They are commonly used for short operations or as arguments to higher-order functions.
```python
#Syntax
lambda arguments: expression
```
---
## The `map()` Function in Python
The map() function applies a given function to all items in an input list (or any other iterable) and returns a map object (an iterator). This is particularly useful for transforming data in a list comprehensively.
```python
#Syntax
map(function, iterable, ...)
```
---
## The `filter()` Function in Python
The `filter()` function constructs an iterator from elements of an iterable for which a function returns `True`. It is used to filter out items from a list (or any other iterable) based on a condition.

```python
#Syntax
filter(function, iterable)
```
---
## Function with Decorators

## Define a function that calculates the time taken to execute another function. Apply this decorator to a function that performs a complex calculation. Test the decorated function with different inputs. This code snippet demonstrates a **decorator** in Python, which is a way to modify or enhance the behavior of a function.

### Let's break it down step by step:

---

### **1. The `timer_decorator` function:**

This is a **decorator function**, which takes another function as input and returns a new function (a "wrapped" version of the original function).

- **Parameters:**
  - `func`: The function that the decorator is applied to.
  
- **Inner function (`wrapper`):**
  - This is where the additional functionality (timing the execution) is added.
  - It records the start time using `time.time()`.
  - Executes the original function `func` with its arguments (`*args` and `**kwargs`).
  - Records the end time.
  - Prints how long the function took to execute.
  - Returns the result of the original function.

---

### **2. Applying the decorator with `@timer_decorator`:**

The line:

```python
@timer_decorator
def complex_calculation(n):
    return sum(x**2 for x in range(n))
```

is equivalent to:

```python
def complex_calculation(n):
    return sum(x**2 for x in range(n))

complex_calculation = timer_decorator(complex_calculation)
```

The `complex_calculation` function is wrapped by the `timer_decorator`. When you call `complex_calculation`, you're actually calling the `wrapper` function inside `timer_decorator`.

---

### **3. The `complex_calculation` function:**

This function computes the sum of the squares of integers from `0` to `n-1`. 

For example:
- `complex_calculation(5)` computes \( 0^2 + 1^2 + 2^2 + 3^2 + 4^2 = 30 \).

---

### **4. Running the test:**

When you call:

```python
print(complex_calculation(10000))
```

Here’s what happens:
1. The `wrapper` function starts timing.
2. The original `complex_calculation` function is executed with `n=10000`.
   - It computes the sum of squares for numbers up to `9999`.
3. The `wrapper` function ends timing.
4. It prints the time taken by the `complex_calculation` function.
5. The result of the calculation is returned and printed.

---

### **Output Example:**

For `complex_calculation(10000)`, the output might look like this:

```
Function complex_calculation took 0.002854 seconds to execute.
333283335000
```

### **Key Concepts:**
- **Decorator:** A function that adds functionality to another function.
- **Wrapper Function:** The inner function that defines the new behavior while also calling the original function.
- **Timing Code:** `time.time()` is used to measure execution time.

This approach is useful for measuring performance or adding other functionality like logging, authentication, etc.

importing modules and packages

standard library overview in python

file operations

file paths

exceptional handling

oops - inheritance,polymorphism

encapsulation,abstraction

magic methods, operator overloading

custom exception handling

iterators

generators

decorators

numpy

pandas

data manipulation

Data source reading

logging in python

completed full python course

Handwritten Notes - file handling, exception handling, classes and objects.

Notes Completed Feb 16 and uploaded till modules should start oops, special functions.
