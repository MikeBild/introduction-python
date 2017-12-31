# Functions

## First functions

The `pass` keyword does nothing.

```python
pass
```

Let's use it to define a function that does nothing.

```python
def do_nothing():
  pass
do_nothing
do_nothing()
```

```python
def print_hi():
  print "Hi!"
print_hi()
```

## Parameters

```python
def print_message(message):
  print(message)

print_message("Hello World!")
```

## Return a value

```python
def get_username():
  return input("Username: ")

get_username()
```

## Return values via construction / destruction

```python
def get_password():
  password = raw_input("Password: ")
  verify = raw_input("Verify: ")
  return (password, verify)

(password, verify) = get_password()
print "Your password:", password
print "Your verify: ", verify
```

## Lambda functions

```python
add = lambda x,y: x + y # lamdba function
add5 = lambda y: add(5, y) # partial application function
print "Lambda add:", add(5, 5)
print "Lambda add5:", add5(10)
```

## Examples

* [Functions](../examples/functions.py)

## Summary

* Functions are a way to write code once, and then use that same code in multiple places.
* Functions can take **arguments** and they can behave differently depending on what arguments they get. Arguments are just local variables.
* Functions can also **return** one value, like the built-in input function does. Returning also ends the function immediately.
* Return a value instead of printing it if you need to do something with it after calling the function.
* Remember that `thing`, `thing()`, `print(thing)` and `print(thing())` do different things.
