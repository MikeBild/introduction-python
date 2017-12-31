# Conditional Statements

## Using if / else statements

```python
its_raining = True
if its_raining:
  its_raining = False
else:
  print("It's not raining, but this still doesn't run.")
```

## Using elif statements

```python
print("Hello!")
word = input("Enter something: ")

if word == "hi":
  print("Hi to you too!")
elif word == "hello":
  print("Hello hello!")
elif word == "howdy":
  print("Howdyyyy!")
elif word == "hey":
  print("Hey hey hey!")
elif word == "gday m8":
  print("Gday 4 u 2!")
else:
  print("I don't know what", word, "means.")
```

## Examples

* [if/else/Elif](examples/conditionals.py)
* [switch case alternative](examples/switch-alternative.py)

## Summary

* Indentation is important in Python.
* Indented code under an if statement runs if the condition is true.
* We can also add an else statement. Indented code under it will run if the code under the if statement does not run.
* elif is short for else if.
* `switch/case` statements doesn't exists in Python.
