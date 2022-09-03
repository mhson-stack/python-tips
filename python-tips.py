# 10 Python Tips and Tricks For Writing Better Code
# https://www.youtube.com/watch?v=C-gEQdGVXbk&ab_channel=CoreySchafer

# 1 Conditional Statments

## Not app
condition = True

if condition:
    x = 1
else:
    x = 0

## Instead Use #1
x = 0
if condition:
    x = 1

## Istead Use #2
x = 1 if condition else 0

# 2 Format large numbers with underscore
num1 = 100_000_000
num2 = 10_000_000_000
total = num1 + num2
print(f"{total:,}")


# 3 When openning file use context manager
# For more watch https://www.youtube.com/watch?v=-aKFBoZpiqA&ab_channel=CoreySchafer
## Not 
# f = open("test.txt", "r")
# file_contents = f.read()
# f.close()

# ## Instead use context manager
# with open("test.txt", "r") as f:
#     file_contents = f.read()
#     words = file_contents.split(" ")
#     word_count = len(words)


# 4 Enumerate function for counter
names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heros = ["Spidername", "Superman", "Deadpool", "Batman"]

for idx, name in enumerate(names, start = 1):
    print(f"index : {idx}, name : {name}")

# 5 Zip
for idx, (name, hero) in enumerate(zip(names, heros)):
    print(f"index : {idx}, name : {name}, hero: {hero}")

# 6 Unpacking
items = [1, 2]
a, b = items

## * used to unpack rest of the items
items = [1, 2, 3, 4, 5]
a, *b = items
print(b)

# 7 setattr, getattr
class Person():
    pass


person = Person()
first_key = "first"
first_value = "Corey"
setattr(person, first_key, first_value)

print(getattr(person, first_key))
print(person.first)


person_info = {"first" : "Corey", "last" : "Schafer"}
for key, value in person_info.items():
    setattr(person, key, value)


for key in person_info:
    print(getattr(person, key))


# 8 Input sensitive info
# Wrong way
from getpass import getpass
# username = input("Username: ")
# password = getpass("Password: ")

# 9
# Why use python -m not python
# -m module search sys path


# 11 
a = b = c = []
a.append(1)
print(b)

print(a := 2) 
a, b = a[b] = a = [1, 2, 3], 2
# tmp = [1, 2, 3], 2
# a = [1, 2, 3], b = 2
# a[2] = [1, 2, 3], 2
# 
# a = [1, 2, [[1, 2, 3], 2]], b = 2
# a = [1, 2, 3], 2
print(a)


# 12 
# lamda functions
# lambda argument : (true return) if (condition) else (false return)
only_pos = lambda x : x if x > 0 else 0