switch = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2
}

calulation = raw_input("Choose calculation: ")
factor = raw_input("Enter a factor: ")

print "Result: ", switch[calulation](int(factor))