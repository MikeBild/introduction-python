import collections

print(''.join(['-' for x in range(70)]))
# Named tuples
Website = collections.namedtuple('Website', ['url', 'founding_year', 'free_to_use'])
github = Website('https://github.com/', 2008, True)
print("Named tuples (all):", github)
print("Named tuples (url):", github.url)
(url, founding_year, free_to_use) = github
print("Named tuples (unpack):", url, founding_year, free_to_use)

print(''.join(['-' for x in range(70)]))
# Deque
names = collections.deque(['John', 'Mike', 'Max', 'Hans'], maxlen=3)
print("Deque:", names)
print("Deque pop (right):", names.pop())
print("Deque pop (left):", names.popleft())
print("Deque to list:", list(names))

print(''.join(['-' for x in range(70)]))
# Counter
words = ['hello', 'there', 'this', 'test', 'is', 'a', 'hello', 'test']
counts = collections.Counter(words)
print('Counter:', [str(word + ":" + str(count)) for (word, count) in counts.items()])