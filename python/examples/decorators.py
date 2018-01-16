print(''.join(['-' for x in range(70)]))
# Functional decorator
def functional_decorator(f):
  def function_wrapper():
    print("Decorating", f.__name__)
    print("Before calling " + f.__name__)
    f()
    print("After calling " + f.__name__)
  return function_wrapper

# Call by function composition
def functional():
  print("inside functional()")

functional = functional_decorator(functional)
functional()

print(''.join(['-' for x in range(70)]))
# Call by @decorator syntax
@functional_decorator
def functional_decorated():
  print("inside functional_decorated()")

functional_decorated()

print(''.join(['-' for x in range(70)]))
# Decorator with Parameter
def greeting(expr):
  def greeting_decorator(func):
    def function_wrapper(x):
      print(expr + ", " + func.__name__ + " returns:")
      func(x)
    return function_wrapper
  return greeting_decorator

@greeting("Hello!!!")
def foo(x):
  print(x, 42)
foo("Hi")

print(''.join(['-' for x in range(70)]))
# Passing-Through all parameters
def call_counter(func):
  def function_wrapper(*args, **kwargs):
    function_wrapper.calls += 1
    return func(*args, **kwargs)
  function_wrapper.calls = 0

  return function_wrapper

@call_counter
def succ(x):
  return x + 1

print("Success calls before:", succ.calls)
for i in range(10):
  succ(i)
print("Success calls after:", succ.calls)

print(''.join(['-' for x in range(70)]))
# Class decorator
class class_decorator:
  def __init__(self, f):
    self.f = f

  def __call__(self):
    print("Decorating", self.f.__name__)
    print("Before calling " + self.f.__name__)
    self.f()
    print("After calling " + self.f.__name__)

@class_decorator
def class_decorated():
    print("inside class_decorated()")

class_decorated()