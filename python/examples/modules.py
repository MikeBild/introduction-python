import random
print("A random number between 1 and 3:", random.randint(1, 3))

from random import randint
print("A random number between 1 and 3:", randint(1, 3))

from random import randint, shuffle
numbers = [1,2,randint(3, 6)]
shuffle(numbers)
print("List shuffle:", numbers)

import mymodule
print("My module random:", mymodule.rand())
