# Data-Types

## Lists

```python
names = ['John', 'Mike', 'Max']
print names, len(names)
```

```python
names += ['Peter'] # create a new list with me in it
names * 2 # repeating
# seq = L[start:stop:step]
names[:2] # first two names
names[1:3] # slice
names[::2] # every second

# item = L[index]
names[0] # index - the first name

# Join
print "Join:", "|".join(names)

# Searching
'Mike' in names # exists
['Mike', 'Peter'] in names # exists

# Sorting
print "Sorted (lexicographical):", sorted(names)
print "Sorted (custom):", sorted(names, key=lambda x: len(x))

# Filter, Map, Reduce
print "Map:", map(lambda x: x + x, names)
print "Filter:", filter(lambda x: len(x) > 3, names)
print "Reduce:", reduce(lambda x,y: x + '|' + y, names)
```

[More on Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

## Tuples

Tuples are a lot like lists, but they're immutable so they can't be changed in-place. We create them like lists, but with `()` instead of `[]`.

```python
thing = (1, 2, 3)
thing += 4,
print "Tuple:", thing
```

## Dictionaries

```python
names_and_ages = {
  'Max': 12,
  'Mike': 38
}

print "Dictionary:", names_and_ages, "Length:", len(names_and_ages)
print "Index access:", names_and_ages['Mike']
```

## Examples

* [Data-Types](examples/data-types.py)

## Summary

* Lists are a way to store multiple values in one variable.
* Lists can be changed in-place and they have methods that change them in-place, like append, extend and remove.
* Slicing lists returns a **new** list, and indexing them returns an item from them.
* `thing = another_thing` does not create a copy of `another_thing`.
* Tuples are like lists, but they **can't be changed in-place**. They're also used in different places.
* Dictionaries consist of `key: value` pairs.
* Variables are stored in a dictionary with their names as keys, so dictionaries behave a lot like variables:
  * Dictionaries are not ordered.
  * Setting or getting the value of a key is simple and fast.
  * Dictionaries can't contain the same key more than once.
* For-looping over a dictionary loops over its keys, and checking if something is in the dictionary checks if the dictionary has a key like that. The `values()` and `items()` methods return things that behave like lists of values or `(key, value)` pairs instead.
