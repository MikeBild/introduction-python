# if/else example

password = input("Enter your password: ")
if password == "secret":
    print("That's correct, welcome!")
else:
    print("Access denied.")

# elif example

word = input("Enter something: ")
print(word)
if word == "hi":
  print("Hi to you too!")
elif word == "hello":
  print("Hello hello!")
else:
  print("I don't know what", word, "means.")