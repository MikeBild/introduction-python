try:
  int('lol')
except Exception:
  print("Oops!")


try:
  123 + 'hello'
except ValueError:
  print('wrong value')
except TypeError:
  print('wrong type')

import sys

text = input("Enter a number: ")
try:
  number = int(text)
except ValueError:
  print("'%s' is not a number." % text, file=sys.stderr)
  sys.exit(1)
print("Your number doubled is %d." % (number * 2))