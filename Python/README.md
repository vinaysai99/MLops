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


functions - default,positional *args,keyword arguments **kwargs

lambda functions - one expression only

map function - apply a function to a iterable like values in a list

filter function - use a function to filter elements in a list that satisfy that function conditions.

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
