# Collection

> `import collections` - High performance container types

## Named tuples

```python
Website = collections.namedtuple('Website', ['url', 'founding_year', 'free_to_use'])
github = Website('https://github.com/', 2008, True)
print("Named tuples (all):", github)
print("Named tuples (url):", github.url)
(url, founding_year, free_to_use) = github
print("Named tuples (unpack):", url, founding_year, free_to_use)
```

## Deque

Deques are often used as queues. It means that items are always added to one end and popped from the other end.

```python
names = collections.deque(['John', 'Mike', 'Max'], maxlen=2)
print("Deque:", names)
print("Deque pop (right):", names.pop())
print("Deque pop (left):", names.popleft())
print("Deque to list:", list(names))
```

## Counter

```python
words = ['hello', 'there', 'this', 'test', 'is', 'a', 'hello', 'test']
counts = collections.Counter(words)
print('Counter:', [str(word + ":" + str(count)) for (word, count) in counts.items()])
```

## Examples

* [Collection](../examples/collection.py)

## Summary

* Duck typing means requiring some behavior instead of some type.
* Collections module are handy. Use them.
