full_content = ''
with open('hello.txt', 'r') as f:
  full_content = f.read()
print("Full content:", full_content)

lines = []
with open('hello.txt', 'r') as f:
  for line in f:
    lines.append(line)
print("Lines:", lines)

with open('hello-new.txt', 'w') as f:
  print("Hello World!", file=f)

with open('hello.txt', 'a') as f:
  print("Hello World!", file=f)