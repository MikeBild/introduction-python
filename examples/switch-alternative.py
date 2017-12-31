switch = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2
}

calulation = input("Choose calculation: ")
factor = input("Enter a factor: ")

print ("Result: ", switch[calulation](int(factor)))