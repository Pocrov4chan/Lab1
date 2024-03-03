import os

#task1
dir_contents = os.listdir('example')
print("Only dict")
for content in dir_contents:
    if(os.path.isdir(os.path.join('example', content))):
        print(content)
print('--' * 20)

print("Only files")
for content in dir_contents:
    if(os.path.isfile(os.path.join('example', content))):
        print(content)
print('--' * 20)

print("Both")
for content in dir_contents:
    if os.path.isdir(os.path.join('example', content)) or os.path.isfile(os.path.join('example', content)):
        print(content)
print('--' * 20)

#Task2

print('Read', os.access('example', os.R_OK))
print('Write', os.access('example', os.W_OK))
print('Execute', os.access('example', os.X_OK))
print('Exist', os.access('example', os.F_OK))
print('--'* 20)
#Task 3

if (os.path.exists('example\\1q')):
    head, tail = os.path.split('example\\1q')
    print(head, tail)
print('--'* 20)

#Task 4
with open('example\\qwe') as file:
    count = 0
    for _ in file:
        count +=1


print(count)
print('--'* 20)

#Task 5

my_list = ['Hello', 'my', 'name', 'is', 'Dmytro']
with open('example\\qwe', 'w') as my_file:
    for item in my_list:
        my_file.write(item+ '\n')

#Task 6
# for i in range(26):
    # os.remove(f'{chr(i + 65)}.txt')
    # my_file = open(f'{chr(i + 65)}.txt', 'w')
    # my_file.close()

#Task 7

with open('example\\qwe') as file:
    with open('example\\wq', 'a') as copy_file:
        for line in file:
            copy_file.write(line)
        
#Task 8

my_path = 'example//12d3'
if os.path.exists(my_path) and os.access('example', os.X_OK):
   os.remove(my_path)



