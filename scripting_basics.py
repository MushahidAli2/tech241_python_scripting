# basics of scipting

# libraries and modules - module is a collectiong of function
#library is a collection of modules (bigger)

# seven "core" modules in python

import sys

# get python versio
print(sys.version)

import os
#gets current working directory
print(os.getcwd())


import subprocess

# runs an external file when executed
# subprocess.run(["python", "hello_world.py"])

import math

pi = math.pi
pi_string = str(pi)
print("the valu of pi is" + pi_string)

import random

randum = random.randrange(1, 10)
print(randum)

import datetime

WHATISTHEDATE = datetime.datetime.now()
print(WHATISTHEDATE)


import json

x = {
    "name" : "jason",
    "age" : 30,
"ciry": "liverpool"
}

y = json.dumps(x)
print(y)
print(type(y)) # changes dict to string
print(type(x))