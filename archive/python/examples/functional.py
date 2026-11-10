print(''.join(['-' for x in range(70)]))
# Functions are objects
def my_func(x):
  print("Functions are objects:", x, my_func.foo)
my_func.foo = 'foo'
print(dir(my_func))

print(''.join(['-' for x in range(70)]))
# Named and anonymous functions
my_lambda = lambda x: print("Lambda:", x, my_lambda.bar)
my_lambda.bar = 'bar'
my_lambda(42)

print(''.join(['-' for x in range(70)]))
# Functions inside functions
def f():
  def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")

  print("This is the function 'f'")
  print("I am calling 'g' now:")
  g()

f()

print(''.join(['-' for x in range(70)]))
# Function as parameter
def g():
  print("Hi, it's me 'g'")
  print("Thanks for calling me")

def f(func):
  print("Hi, it's me 'f'")
  print("I will call 'func' now")
  func()

f(g)

print(''.join(['-' for x in range(70)]))
# Returning a function
def f(x):
  def g(y):
    return y + x + 3
  return g

nf1 = f(1)

print(nf1(1))
print(f(3)(1))