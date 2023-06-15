# Introduction to Scripting with Python

## What is Scripting?

Scripting involves writing and executing scripts to automate tasks or perform specific functions. Python is a popular scripting language known for its simplicity and versatility.

## Scripting Basics with Python

### Python Environment Setup

1. Install Python: Download and install Python from the official website (https://www.python.org) based on your operating system.

2. Verify Installation: Open a terminal or command prompt and type `python --version` to ensure Python is properly installed.

### Basics of Scripting

Python provides several built-in modules that offer additional functionality. Here are a few examples:

#### Using the `os` module

The `os` module allows you to interact with the operating system. Here are a few examples:

```python
import os

# Echo to the terminal
os.system('echo "Hello world"')

# Create a directory
directory = "test_dir"
parent_dir = "C:/Users/Mushahid"
path = os.path.join(parent_dir, directory)
os.mkdir(path)

# Putting a new file in the new directory
filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(filepath, "w") as file1:
    toFile = "contents of the file are written here"
    file1.write(toFile)

print("File", filename, "created in", directory, "folder")
```
## Using Core Modules

Python has several core modules that provide useful functionality. Here's an overview:
- `sys`: Provides system-specific parameters and functions.
```python
import sys
print(sys.version)
```
- `subprocess`: Allows the execution of external commands.
```python
#example running external files
import subprocess
subprocess.run(["python", "hello_world.py"])
```
- `math`: Provides mathematical functions and constants.
```python
#example
import math
pi = math.pi
pi_string = str(pi)
print("The value of pi is " + pi_string)
```
- `random`: Generates random numbers and selections.
```python
#Generating a random number
import random
random_num = random.randrange(1, 10)
print(random_num)
```
- `datetime`: Manipulates dates and times.
```python
#getting current time and date
import datetime
current_date = datetime.datetime.now()
print(current_date)
```
- `json`: Deals with JSON data (serialization and deserialization).
```python
#working on JSON data
import json
x = {
    "name": "jason",
    "age": 30,
    "city": "liverpool"
}
y = json.dumps(x)
print(y)
print(type(y))  # Changes the dictionary to a string
print(type(x))
```
## Conclusion
Python offers powerful scripting capabilities, allowing you to automate tasks and perform various operations. By leveraging the os module and understanding the basics of scripting with core modules, you can expand your scripting skills and accomplish a wide range of tasks.