import logging
import time
# def main():
#     def func1(a, b, c):
#         print(a, b, c)

#     func1(1, 2, 3)
#     func1(c=6, a=1, b=2)


# if __name__ == "__main__":
#     main()

# def f1(func):
#     def wrapper():
#         print("Started")
#         func()
#         print("Ended")
    
#     return wrapper

# @f1
# def f():
#     print("Hello")


# f()


dic_list = {i : i * i for i in range(10)}
list = [i for i in range(10)]
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# for key, value in dic_list.items():
#     print(f"Key : {key}, Value : {value}")

# for key in dic_list:
#     print(key)

# for idx, item in enumerate(list):
#     print(item)


# for idx, (num, alpha) in enumerate(zip(list, alpha)):
#     print(f"index : {idx}, num : {num}, alpha : {alpha}")

def timer():
    start = time.perf_counter()
    time.sleep(1)
    end = time.perf_counter()
    print(end - start)

timer()

condition = True
if condition:
    x = 1
else:
    x = 0


print(x)

x = 0
if condition:
    x = 1

print(x)

x = 1 if condition else 0


print(x)


num1 = 10_000_000_000
print(f'{num1:,}')


# with open('test.txt', 'rb') as f:
#     file_contents = f.read()
#     words = file_contents.split(' ')
#     print(len(words))


names = ["Peter Parker", "Clark Kent", "Wade Wilson", "Bruce Wayne"]
heros = ["Spidername", "Superman", "Deadpool", "Batman"]

for idx, (name, hero) in enumerate(zip(names, heros)):
    print(f"{name} is actually {hero}")


a, b, *c = (1, 2, 3, 4, 5)
print(c)