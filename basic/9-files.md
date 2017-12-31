# Files

## Read file

```python
full_content = ''
with open('hello.txt', 'r') as f:
  full_content = f.read()
print("Full content:", full_content)
```

## Read file line by line

```python
lines = []
with open('hello.txt', 'r') as f:
  for line in f:
    lines.append(line)
print("Lines:", lines)
```

## Write file

```python
# Write to file
with open('hello-new.txt', 'w') as f:
  print("Hello World!", file=f)

# Append to file
with open('hello.txt', 'a') as f:
  print("Hello World!", file=f)
```

| Mode | Short for | Meaning                                                              |
| ---- | --------- | -------------------------------------------------------------------- |
| `r`  | read      | Read from an existing file.                                          |
| `w`  | write     | Write to a file. **If the file exists, its old content is removed.** |
| `a`  | append    | Write to the end of a file, and keep the old content.                |

## Examples

* [Files](../examples/files.py)
