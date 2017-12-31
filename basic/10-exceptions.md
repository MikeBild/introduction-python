# Exceptions

```python
try:
  int('ABC')
except Exception:
  print("Oops!")
```

## Specific exceptions

```python
try:
  123 + 'hello'
except ValueError:
  print('wrong value')
except TypeError:
  print('wrong type')
```

## Raising exceptions

```python
oops = ValueError("ABC is not a number")
raise oops
```

## Exception hierarchy

    Exception
    ├── ArithmeticError
    │   ├── FloatingPointError
    │   ├── OverflowError
    │   └── ZeroDivisionError
    ├── AssertionError
    ├── AttributeError
    ├── BufferError
    ├── EOFError
    ├── ImportError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── MemoryError
    ├── NameError
    │   └── UnboundLocalError
    ├── OSError
    │   ├── BlockingIOError
    │   ├── ChildProcessError
    │   ├── ConnectionError
    │   │   ├── BrokenPipeError
    │   │   ├── ConnectionAbortedError
    │   │   ├── ConnectionRefusedError
    │   │   └── ConnectionResetError
    │   ├── FileExistsError
    │   ├── FileNotFoundError
    │   ├── InterruptedError
    │   ├── IsADirectoryError
    │   ├── NotADirectoryError
    │   ├── PermissionError
    │   ├── ProcessLookupError
    │   └── TimeoutError
    ├── ReferenceError
    ├── RuntimeError
    │   └── NotImplementedError
    ├── StopIteration
    ├── SyntaxError
    │   └── IndentationError
    │       └── TabError
    ├── SystemError
    ├── TypeError
    ├── ValueError
    │   └── UnicodeError
    │       ├── UnicodeDecodeError
    │       ├── UnicodeEncodeError
    │       └── UnicodeTranslateError
    └── Warning
        ├── BytesWarning
        ├── DeprecationWarning
        ├── FutureWarning
        ├── ImportWarning
        ├── PendingDeprecationWarning
        ├── ResourceWarning
        ├── RuntimeWarning
        ├── SyntaxWarning
        ├── UnicodeWarning
        └── UserWarning

## Examples

* [Exceptions](../examples/exceptions.py)

## Summary

* Exceptions are classes and they can be used just like all other classes.
* ValueError and TypeError are some of the most commonly used exceptions.
* The `try` and `except` keywords can be used for attempting to do something and then doing something else if we get an error. This is known as catching exceptions.
* It's possible to raise exceptions with the `raise` keyword. This is also known as throwing exceptions.
* Raise exceptions if they are meant to be displayed for programmers and use `sys.stderr` and `sys.exit` otherwise.
