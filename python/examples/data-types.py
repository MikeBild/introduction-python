from functools import reduce

print(''.join(['-' for x in range(70)]))
# List
names = ['John', 'Mike', 'Max']
print("List:", names, "Length:", len(names))

names += ['Peter']
print("Concat:",names, "Length:", len(names))
print("Slice:", names[1:3])
print("Every second:", names[::2])
print("Sorted (lexicographical):", sorted(names))
print("Sorted (custom):", sorted(names, key=lambda x: len(x)))
print("Join:", "|".join(names))
print("Map:", map(lambda x: x + x, names))
print("Filter:", filter(lambda x: len(x) > 3, names))
print("Reduce:", reduce(lambda x,y: x + '|' + y, names))

names_repeat = (names + ['Klaus']) * 2
print("Repeat:", names_repeat, len(names_repeat))

print("Comprehensions:", [len(x) for x in names])
print("Comprehensions (conditional):", [x+x for x in names if len(x) > 3])
print("Comprehensions (nested):", [(x,y) for x in names for y in [1, 2, 3]])

for name in names:
  print("Loop:", name)

for index, item in enumerate(names):
  print("Enumerate", index, item)

names_iterator = iter(names)
print("Iterator:", names_iterator.__next__())
print("Iterator:", names_iterator.__next__())

names.append('Klaus')
print("Append:", names)
names.reverse()
print("Reverse:", names)
names.extend(['Charli'])
print("Extend:", names)
names.insert(3, 'Kate')
print("Insert:", names)
names.remove('Kate')
print("Remove:", names)
print("Pop:", names.pop(), names)

print(''.join(['-' for x in range(70)]))
# Tuple
thing = (1, 2, 3)
thing += 4,
print("Tuple:", thing)

print(''.join(['-' for x in range(70)]))
# Set

helloworld = {'Hello', 'World'}
print("Set basic:", [x for x in helloworld])

# Create a set from sequence
hello = set('hello')
print("Set from sequence:", [x for x in hello])

# Modify set

helloworld.add('Python')
print("Set add:", [x for x in helloworld])
helloworld.remove('Python')
print("Set remove:", [x for x in helloworld])

print(''.join(['-' for x in range(70)]))
# Dictionary
names_and_ages = {
  'Max': 12,
  'Mike': 38
}
print("Dictionary:", names_and_ages, "Length:", len(names_and_ages))
print("Index access:", names_and_ages['Mike'])
print("Values:", names_and_ages.values())
print("Items:", names_and_ages.items())
print("Find:", ('Mike', 38) in names_and_ages.items())
for name, age in names_and_ages.items():
  print("Loop:", name, age)