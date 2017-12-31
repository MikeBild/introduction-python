# Classes

```python
class Website:
  # constructor
  def __init__(self, url, founding_year, free_to_use):
    self.url = url
    self.founding_year = founding_year
    self.free_to_use = free_to_use
  # method
  def info(self):
    print("URL:", self.url)
    print("Founding year:", self.founding_year)
    print("Free to use:", self.free_to_use)

github = Website('https://github.com/', 2008, True)
github.info()
```

## Class attributes

```python
Website.is_online = True
```

## Example

* [Classes](../examples/classes.py)

## Summary

* Object-orientated programming is programming with custom data types. In Python that means using classes and instances.
* Use CapsWords for class names and lowercase_words_with_underscores for other names. This makes it easy to see which objects are classes and which objects are instances.
* Calling a class as if it was a function makes a new instance of it.
* `foo.bar = baz` sets `foo`'s attribute `bar` to `baz`.
* Use class attributes for functions and instance attributes for other things.
* Functions as class attributes can be accessed as instance methods. They get their instance as the first argument. Call that `self` when you define the method.
* `__init__` is a special method, and it's ran when a new instance of a class is created. It does nothing by default.
* Don't use classes if your code is easier to read without them.
