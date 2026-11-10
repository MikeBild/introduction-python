a, b, *rest = range(10)
print('Unpacking:', a, b, rest)

def f(a, b, *args, option=True):
  print('Keyword only arguments:', a, b, args, option)

f('a', 'b', 'c', option=False)

# Iterators
print('Iterators:', ', '.join(map(str, range(3))))

# Yield from
def gen():
  yield from ['a', 'b']
print('Yield from:', ', '.join(gen()))
