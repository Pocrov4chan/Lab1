                                            #EXAMPLES FROM ARTICLES
#Python booleans
print(10 > 9)
print(10 == 9)
print(10 < 9) 

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") 

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) 

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) 

def myFunction() :
  return True

print(myFunction()) 

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") 

x = 200
print(isinstance(x, int)) 

#Python Operators
print(10 + 5) 
print((6 + 3) - (6 + 3)) 
print(100 + 5 * 3) 
print(5 + 4 - 7 + 3) 

#Python Lists
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)