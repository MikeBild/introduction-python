# List
names = ['John', 'Mike', 'Max']
print "List:", names, "Length:", len(names)

names += ['Peter']
print "Concat:",names, "Length:", len(names)
print "Slice:", names[1:3]
print "Every second:", names[::2]
print "Sorted (lexicographical):", sorted(names)
print "Sorted (custom):", sorted(names, key=lambda x: len(x))
print "Join:", "|".join(names)
print "Map:", map(lambda x: x + x, names)
print "Filter:", filter(lambda x: len(x) > 3, names)
print "Reduce:", reduce(lambda x,y: x + '|' + y, names)

names_repeat = (names + ['Klaus']) * 2
print "Repeat:", names_repeat, len(names_repeat)

# Tuple
thing = (1, 2, 3)
thing += 4,
print "Tuple:", thing

# Dictionary
names_and_ages = {
  'Max': 12,
  'Mike': 38
}

print "Dictionary:", names_and_ages, "Length:", len(names_and_ages)
print "Index access:", names_and_ages['Mike']