# Testing

## PyTest - Test-Runner

```bash
python -m unittest testing.py
python testing.py
```

**testing_sut.py**

```python
def func(x):
  return x + 1
```

**testing.py**

```python
import unittest
import testing_sut

class MyTestClass(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    pass

  @classmethod
  def tearDownClass(cls):
    pass
  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_answer_should_success(self):
    assert testing_sut.func(3) == 4

  def test_answer_should_fail(self):
    assert testing_sut.func(3) == 5

if __name__ == '__main__':
  unittest.main()
```

## Mock

```bash
pip install mock
```

## Multi-Environment / Parameter Tests

```bash
pip install tox
```
