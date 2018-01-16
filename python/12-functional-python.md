# Functional Python - FuncTools

**Functions are objects**

```python
def my_func(x):
  print("Functions are objects:", x, my_func.foo)
my_func.foo = 'foo'
print(dir(my_func))
```

**Use `lambda` to create named and anonymous functions.**

```python
my_lambda = lambda x: print("Lambda:", x, my_lambda.bar)
my_lambda.bar = 'bar'
my_lambda(42)
```

## Functions inside functions

```python
def f():
  def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")

  print("This is the function 'f'")
  print("I am calling 'g' now:")
  g()

f()
```

## Higher Order Functions

### Function as parameter

```python
def g():
  print("Hi, it's me 'g'")
  print("Thanks for calling me")

def f(func):
  print("Hi, it's me 'f'")
  print("I will call 'func' now")
  func()

f(g)
```

### Returning a function

```python
def f(x):
  def g(y):
    return y + x + 3
  return g

nf1 = f(1)

print(nf1(1))
print(f(3)(1))
```

## Examples

* [Functional Python](../examples/functional.py)
