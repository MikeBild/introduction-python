# pass
def do_nothing():
  pass

do_nothing()

# side effect

def print_hi():
  print("Hi!")

print_hi()

# parameter
def print_message(message):
  print(message)

print_message("Hello World!")

## return a value
def get_username():
  return input("Username: ")

a_username = get_username()
print("Your username:", a_username)

## return multiple values via construction/destruction
def get_password():
  password = input("Password: ")
  verify = input("Verify: ")
  return (password, verify)

(password, verify) = get_password()
print("Your password:", password)
print("Your verify: ", verify)

# lambda function
add = lambda x,y: x + y
add5 = lambda y: add(5, y)
print("Lambda add:", add(5, 5))
print("Lambda add5:", add5(10))