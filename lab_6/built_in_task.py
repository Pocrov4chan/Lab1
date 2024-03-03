#Task 1
count = 3
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = map(lambda x: 3 * x, my_list)
print(*new_list)

#Task2

a = input()
up_letters = 0
low_letters = 0
for letter in a:
    if letter == letter.lower():
        low_letters += 1
    elif letter == letter.capitalize():
        up_letters += 1

print(up_letters, low_letters)

#Task 3

q = "1221"
print(list(reversed(q)))
if list(q) == list(reversed(q)):
    print('Horraaay')

#Task 4
import time
import math

def square_root_after_milliseconds(number, milliseconds):
    time.sleep(milliseconds / 1000)
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

number = int(input("Enter the number: "))
milliseconds = int(input("Enter the milliseconds to wait: "))
square_root_after_milliseconds(number, milliseconds)

#Task 5
d = (1,2,3,4,'asdds')
print(any(d))
