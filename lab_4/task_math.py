import math 

#task1

degree = int(input("Input Degree: "))
print(math.radians(degree))

#task2

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print(0.5 * (a + b) * h)

#task3

n = int(input("Input number of sides: "))
s = int(input("Input the length of a side: "))
print("The area of the polygon is:", int((n * (s ** 2)) / (4 * math.tan(math.pi / n))))

#task

n_t = int(input("Length of base: "))
h_t = int(input("Height of parallelogram: "))
print("Expected Output:", float(n_t * h_t))
 