# Modules

```python
import random
print ("A random number between 1 and 3:", random.randint(1, 3))

from random import randint
print("A random number between 1 and 3:", randint(1, 3))

from random import randint, shuffle
numbers = [1,2,randint(3, 6)]
shuffle(numbers)
print("List shuffle:", numbers)
```

## Overview of the standard library

* [random](https://docs.python.org/3/library/random.html)
* [sys](https://docs.python.org/3/library/sys.html)
* [math](https://docs.python.org/3/library/math.html)
* [time](https://docs.python.org/3/library/time.html)
* [os](https://docs.python.org/3/library/os.html)
* [functools](https://docs.python.org/3/library/functools.html)
* [itertools](https://docs.python.org/3/library/itertools.html)

## Exmaples

* [Modules](../examples/modules.py)
* [My module](../examples/mymodule.py)

## Summary

* Modules wasn't loaded twice. **All Modules are cached!**
* Most modules are files on our computers, but some of them are built in to Python. We can use modules in our projects by importing them, and after that using `modulename.variable` to get a variable from the module.
* Some of the most commonly used modules are random, sys, math, time and os.
* Avoid creating `.py` files that have the same name as a name of a module you want to use.
* Python comes with many modules, and we can install even more modules if we want to.
