import math
import random

#Task_1
def grams_to_ounces(grams):
    return 28.3495231 * grams

#Task_2

def conversion(F):
    return (5 / 9) * (F - 32)

#Task_3

def solve(numheads, numlegs):
    for chicken in range(numheads):
        rabbit = numheads - chicken
        if numlegs == 2*chicken + 4*rabbit:
            return chicken, rabbit
    return "No"

numheads = 35
numlegs = 94
solution = solve(numheads, numlegs)


#Task_4

def is_prime(n):
    n = int(n)
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n // 2 + 1):
        if(n % i == 0):
            return False

    return True

numbers = input().split(" ")
prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)

#Task 5
def permutations(my_string):
    for i in range(len(my_string)):
        for j in range(i, len(my_string)):
            print(my_string[i:j+1])

permutations("abc")


#Task 6

def my_reverse(my_str):
    reversed_str =  my_str.split()[::-1]
    return " ".join(reversed_str)
print(my_reverse("Hello world my friend"))

#Task 7
def has_33(nums):
    new_nums = [str(i) for i in nums]
    new_nums = "".join(new_nums)
    return "33" in new_nums

print(has_33([1, 3, 3]))

#Task 8
def spy_game(nums_8):
    new_nums_8 = [str(i) for i in nums_8]
    new_nums_8 = "".join(new_nums_8)
    return "007" in new_nums_8

print(spy_game([1,1,1,1,1,0,0,7]))

#Task 9

def sphere(radius):
    return math.pi*0.75*(radius**3) 

#Task 10

def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

#Task 11

def is_palindrome(word):
    return word == word[::-1]


#Task 12

def histogram(numbers):
    for num in numbers:
        output = '*' * num
        print(output)

#Task 13

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    my_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())

        guesses_taken += 1

        if guess <  my_number:
            print("Your guess is too low.")
        elif guess >  my_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
#Task 14
