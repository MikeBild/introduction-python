#!/usr/bin/env python3

# Simple types
boolean = True and False
string = 'Hello World!'
integer = 0
complex = 0j
float = 0.0
none = None

print('Simple:', string)

# Sequences
list = [1, 'a', 0.0]
tuple = (1, 'a', 0.0)
dictionary = {
  'key1': 'value 1',
  'key2': 'value 2'
}
immutable_set = set(['a', 'b'])

for item in list:
  # continue
  # break
  print(item)

# Conditions
if list:
  print('Is a list')
elif not list:
  print('Is not a list')
else:
  print('What else ;-)')

something = '123' if list else '456'

# Function definition
def my_function(name='Mike'):
  """A 'Hello World!' function"""
  return 'Hello ' + name

print("Output:", my_function('John'))

# DocString
help(my_function.__doc__)

# Lambda
my_func = lambda name='Mike': 'Hello ' + name
print("Output:", my_func('John'))

# Input/Output
input = input("Input please: ")
print('Output:', input)

# Class
class Parent(object):
  value = 0
  __private_value = 0
  def __init__(self, value = 100):
    self.__private_value = value
    self.value = value + value
  def getInstance(self):
    return self
  def getPrivateValue(self):
    return self.__private_value

parent = Parent(10)
print(dir(parent))
print('Class:', parent.value, parent.getPrivateValue())

# Module

import sys
print('Module Search Path:', sys.path)
from sys import path
print('Module Search Path:', path)
