#task1

def square(n):
    for number in range(1, n + 1):
        yield number * number

for i in square(10):
    print(i)

#task2
    
n = int(input())

def even(n):
    for number in range(1, n):
        if number % 2 == 0:
            yield str(number)

for i in even(n):
    print(i, end = ",")

print("")

 #task3
    
def divisibility(n_3):
    for i in range(1, n_3):
        if i % 12 == 0:
            yield i

for number in divisibility(100):
    print(number)

#task4

a = 7
b = 15
def square_interval(a, b):
    for i in range(a, b + 1):
        yield i*i

for number in square_interval(a, b):
    print(number)

#task5

n_5 = int(input())    
def reverse(n_5):
    while n_5 >= 0:
        n_5 -= 1
        yield n_5 + 1

for i in reverse(n_5):
    print(i)
