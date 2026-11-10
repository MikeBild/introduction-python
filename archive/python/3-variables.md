# Variables, Booleans, Comparison and None

## Variables

Variables are easy to understand. They simply **point to values**.

```python
>>> a = 1   # create a variable called a that points to 1
>>> b = 2   # create another variable
>>> a       # get the value that the variable points to
1
>>> b
2
>>>
```

To do something to a variable (for example, to add something to it) we can also use `+=`, `-=`, `*=` and `/=` instead of `+`, `-`, `*` and `/`. The "advanced" `%=`, `//=` and `**=` also work.

```python
>>> a += 2          # a = a + 2
>>> a -= 2          # a = a - 2
>>> a *= 2          # a = a * 2
>>> a /= 2          # a = a / 2
>>>
```

This is not limited to integers.

```python
>>> a = 'hello'
>>> a *= 3
>>> a += 'world'
>>> a
'hellohellohelloworld'
>>>
```

## Good and bad variable names

Variable names are case-sensitive, like many other things in Python. Variable names can be multiple characters long. They can contain uppercase characters, numbers and some other characters, but most of the time we should use simple, lowercase variable names. We can also use underscores. For example, these variable names are good:

```python
>>> magic_number = 123
>>> greeting = "Hello World!"
```

Don't use variable names like this, **these variables are _bad_**:

```python
>>> magicNumber = 3.14          # looks weird
>>> Greeting = "Hello there!"   # also looks weird
>>> x = "Hello again!"          # what the heck is x?
```

## None

None is Python's "nothing" value.

```python
>>> thingy = None
>>> print(thingy)
None
```

## Comparing operators

So far we've used `==`, but there are other operators also. This list probably looks awfully long, but it's actually quite easy to learn.

| Usage    | Description                     | True examples      |
| -------- | ------------------------------- | ------------------ |
| `a == b` | a is equal to b                 | `1 == 1`           |
| `a != b` | a is not equal to b             | `1 != 2`           |
| `a > b`  | a is greater than b             | `2 > 1`            |
| `a >= b` | a is greater than or equal to b | `2 >= 1`, `1 >= 1` |
| `a < b`  | a is less than b                | `1 < 2`            |
| `a <= b` | a is less than or equal to b    | `1 <= 2`, `1 <= 1` |

We can also combine multiple comparisons. This table assumes that a and b are Booleans.

| Usage     | Description                               | True example                      |
| --------- | ----------------------------------------- | --------------------------------- |
| `a and b` | a is True and b is True                   | `1 == 1 and 2 == 2`               |
| `a or b`  | a is True, b is True or they're both True | `False or 1 == 1`, `True or True` |

`not` can be used for negations. If `value` is True, `not value` is False, and if `value` is False, `not value` is True.

There's also `is`, but don't use it instead of `==` unless you know what you are doing. We'll learn more about it later.

## Summary

* Variables have a name and a value. We can create or change variables with `name = value`.
* `thing += stuff` does the same thing as `thing = thing + stuff`.
* Use lowercase variable names and remember that programmers hate figuring out what x is.
* `=` means assigning and `==` means comparing.
* True and False are Booleans. Comparing values results in a Boolean.
* None is a value that we'll find useful later. When error messages say `NoneType object` they mean None.
