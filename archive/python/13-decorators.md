# Decorators

Even though it is the same underlying concept, we have two different ways to develop decorators in Python:

* Function decorators
* Class decorators

## Function decorator

```python
def functional_decorator(f):
  def helper():
    print("Decorating", f.__name__)
    print("Before calling " + func.__name__)
    f()
    print("After calling " + func.__name__)
  return helper
```

## Call by function composition

```python
def functional():
  print("inside functional()")

functional = functional_decorator(functional)
functional()
```

### Call by @decorator syntax

```python
@functional_decorator
def functional_decorated():
  print("inside functional_decorated()")

functional_decorated()
```

## Class decorator

```python
class class_decorator:
  def __init__(self, f):
    self.f = f

  def __call__(self):
    print("Decorating", self.f.__name__)
    self.f()

@class_decorator
def class_decorated():
    print("inside class_decorated()")

class_decorated()
```

## Decorators with Parameters

```python
def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator

@greeting("καλημερα")
def foo(x):
    print(42)

foo("Hi")
```

## Passing-Through all parameters

```python
def call_counter(func):
  def function_wrapper(*args, **kwargs):
    function_wrapper.calls += 1
    return func(*args, **kwargs)
  function_wrapper.calls = 0

  return function_wrapper

@call_counter
def succ(x):
  return x + 1
```
