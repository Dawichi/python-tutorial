# ┌────────────────────────────────────────────────────────────
# │
# │                   PYTHON TUTORIAL NOTES
# │
# │             from w3schools - by github.com/dawichi
# │
# └────────────────────────────────────────────────────────────
#
#   INDEX:
#   1. Variables
#   2. Functions
#   3. Data Types
#   4. Numbers
#   5. Strings
#   6. Boolean Values
#   7. Operators   
#   8. Lists
#
#
# ┌────────────────────────────────────────────────────────────
# │	1. Variables
# └────────────────────────────────────────────────────────────

# var without defined type, you can modify the type later
x = 4
x = "Sally"


# var with defined type
x = str(3)   # x = '3'
x = int(3)   # x = 3
x = float(3) # x = 3.0


# Get var type
print(type(x))


# vars are case sensitive
a = 4
A = 4 # A !== a


# --- Var Names Rules ---
# 1. must start with letter or _
# 2. must not start with a number
# 3. only alphanumeric characters (A-z, 0-9 and  _)
# 4. are case sensitive (Age != aGe != agE)
myVar = 'ok'
My_Var = 'ok'
_my_var= 'ok'
# 2myvar = ERROR
# my-var = ERROR
# my var = ERROR


# Multiple words var names standards:
myVarName = 'Camel case'
MyVarName = 'Pascal case'
my_var_name = 'snake case'


# Assign multiple variables
x, y, z = 'Orange', 'Banana', 'Cherry'
print(x, y, z) # Orange Banana Cherry

x = y = z = 'Orange'
print(x, y, z) # Orange Orange Orange


# Unpack array in variables
fruits = ['apple', 'banana', 'cherry']
x, y, z = fruits
print(x, y, z)


# concat text with +
x = 'awesome'
print('python is ' + x)
y = 'python is '
z = y + x
print(z)


# with numbers, the + sums
x = 5
y = 10
print(x + y) # 15



# ┌────────────────────────────────────────────────────────────
# │        2. Functions
# └────────────────────────────────────────────────────────────

# using external function var
x = 'awesome'
def myfunc():
    print('python is ' + x)

myfunc()


# renaming local var inside function
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is " + x) # fantastic

myfunc()
print("Python is " + x) # awesome


# create a global var inside a function
def myfunc():
    global x
    x = 'fantastic'

myfunc()
print("Python is " + x)



# ┌────────────────────────────────────────────────────────────
# │        3. Data Types
# └────────────────────────────────────────────────────────────

'''
    Text:       str
    Numeric:    int, float, complex
    Sequence:   list, tuple, range
    Mapping:    dict
    Set:        set, frozenset
    Boolean:    bool
    Binary:     bytes, bytearray, memoryview
'''

# print data type
x = 5
print(type(x))


# set defined data type
x = int(20)



# ┌────────────────────────────────────────────────────────────
# │        4. Numbers
# └────────────────────────────────────────────────────────────

'''
3 numeric types: int, float, complex
'''
x = 1 # int
y = 2.8 # float
z = 1j # complex

# 4.1 - Intenger: a whole number without decimals and unlimited length
x = 1
y = 53425782562
z = -5348523572

# 4.2 - Floating point number: intenger with decimals
x = 1.5
y = 923.252752
z = -12.472223

# floats can also specify e to represent the power of 10
x = 35e3
y = 12E4
z = -87.7e100

# 4.3 - complex numbers, written with a j to represent the imaginary part
x = 3+5j
y = 5j
z = -5j

# 4.4 - convert types to another
x = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(x)   # int -> float
b = int(y)     # float -> int
c = complex(x) # int -> complex

# NOTE: you can't convert any complex number into another

# 4.5 - Random number
# python does not have a random() function, but there is a built-in module
import random
print(random.randrange(1, 10))



# ┌────────────────────────────────────────────────────────────
# │        5. Strings
# └────────────────────────────────────────────────────────────

# multiline strings - the breakpoints are inserted in the same position
x = '''Texto multilinea
que conserva los saltos
de línea al imprimirlo
en la consola'''
print(x)


# 5.1 String are arrays
# Like other popular programming languages, strings in Python are arrays of bytes representing unicode characters
# However, Python does not have a character data type, a single character is simply a string with a length of 1
# Square brackets can be used to access each character of the string
x = 'My text'
print(x[0]) # 'M'
print(x[2]) # ' '


# looping in a string - if a string is an array, we can loop through with a for
for x in 'banana':
    print(x)


# string length - len()
a = 'banana'
print(len(a)) # 6


# 5.2 check if a phrase or character is present in a string - in
txt = 'I am free!'
print('free' in txt) # True


# only print if free is present
txt = 'I am free!'
if 'free' in txt:
    print('yes, "free" is present.')


# 5.3 check if not
txt = 'that thing is so good!'
if 'bad' not in txt:
    print('Yes, "bad" is NOT present.')


# 5.4 slicing strings
x = 'Hello world'
print(x[2:5]) # 'llo'
print(x[3:9]) # 'lo wor'

print(x[:5]) # slice from the start
print(x[5:]) # slice to the end


# 5.5 Modify strings
x = 'hello world'
print(x.upper()) # to uppercase
print(x.lower()) # to lowercase
print(x.strip()) # remove start or end whitespaces (not in the middle)
print(x.replace('he', 'hi he')) # replace: returns "hi hello world" 
print(x.split(' ')) # split: returns ['hello', 'world']


# 5.6 String concatenation
a = 'hello'
b = 'world'
c = a + ' ' + b
print(c)


# 5.7 String format
# we cannot concat numbers and strings

''' ERROR:
age = 36
txt = 'I am ' + age
'''

# 2 solutions: 1. str()
age = 36
txt = 'I am ' + str(age)
print(txt)

# or 2. format() method!
# the format() takes passed args, formats them, and places them in the string where the placeholders {} are
age = 36
txt = 'I am {}'
print(txt.format(age))

# the format method can take unlimited arguments
name = 'david'
age = 21
day = 'monday'
txt = 'I am {}, {} yo. Today is {}'
print(txt.format(name, age, day))


# scape characters
txt = "I am \"coding\" in python"
txt = 'I am "coding" in python'

# Other scape characters:
#   \'  single quote
#   \"  doble quote
#   \\  backslash
#   \n  new line
#   \r  carriage return
#   \t  tab
#   \b  backspace
#   \f  form feed
#   \ooo    octal value
#   \xhh    hex value

# NOTE: All sting methods
# https://www.w3schools.com/python/python_strings_methods.asp



# ┌────────────────────────────────────────────────────────────
# │        6. Boolean Values
# └────────────────────────────────────────────────────────────

# True or False
print(10 > 9)  # true
print(10 == 9) # false
print(10 < 9)  # false


# 6.1 conditions
a = 67
b = 12
if b > a:
    print('b is greeter than a')
else:
    print('a is greeter than b')


# 6.2 Evaluate boolean content
print(bool('hello'))
print(bool(92))

# NOTE: 
#   1. Any string is true, except empty string
#   2. Any number is true, except 0

# false values
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# Functions can return boolean
def myfunc():
    return True

print(myfunc())

# you can execute code based in the answer
if myfunc():
    print('was true!')
else:
    print('was false!')


# python has many built-in functions that return boolean, like isinstance()
# it can be used to determine if an object is of a certain data type
x = '200'
print(isinstance(x, str)) # true
print(isinstance(x, int)) # false



# ┌────────────────────────────────────────────────────────────
# │        7. Operators
# └────────────────────────────────────────────────────────────
x = 1
y = 2

# 7.1 Arithmetic operators
x + y  # addition
x - y  # subtraction
x + y  # multiplication
x / y  # division
x % y  # modulus
x ** y # exponentiation
x // y # floor division


# 7.2 Assignment operators
'''
Operator    Example     Equals
=           x = 5       x = 5
+=          x += 3      x = x + 3
-=          x -= 3      x = x - 3
*=          x *= 3      x = x * 3
/=          x /= 3      x = x / 3
%=          x %= 3      x = x % 3
//=         x //= 3     x = x // 3
**=         x **= 3     x = x ** 3
&=          x &= 3      x = x & 3
|=          x |= 3      x = x | 3
^=          x ^= 3      x = x ^ 3
>>=         x >>= 3     x = x >> 3
<<=         x <<= 3     x = x << 3
'''


# 7.3 Comparison operators
'''
Operator    Example     Name
==          x == y      equal
!=          x != y      not equal
>           x > y       greater than
<           x < y       less than
>=          x >= y      greeter than or equal to
<=          x <= y      less than or equal to
'''


# 7.4 Logical operators
'''
and     true if both statements are true
or      true if at least one of the statements is true
not     reverse the result
'''


# 7.5 Identity operators
'''
is          returns true if both vars are pointing to the same memory space
is not      returns false if ""
'''
x = ['hi', 'hello']
y = ['hi', 'hello']
z = x

print(x is z) # true, same memory space
print(x is y) # false! same value but different object
print(x == y) # true! same value. thats the different between == and is


# 7.6 Membership operatos
'''
in          returns true if a sequence with the specified value is present in the object
not in      returns false if ""
'''
x = ['apple', 'banana']
print('banana' in x) # true


# 7.7 Bitwise operators
'''
Operator    Name    Desc
&           AND     Sets each bit to 1 if both bits are 1 
|           OR      Sets each bit to 1 if one of two bits is 1
^           XOR     Sets each bit to 1 if only one of two bits is 1
~           NOT     Inverts all the bits

<<          Zero fill left shift    Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>          Signed right shift      Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
'''



# ┌────────────────────────────────────────────────────────────
# │        8. Lists
# └────────────────────────────────────────────────────────────

# Python collections (arrays)
# There are 4 collection data types:
#
#   name            ordered     changeable  allows_duplicate
#   1. List         yes         yes         yes
#   2. Tuple        yes         no          yes
#   3. Set          no          unindexed   no
#   4. Dictionary   no          no          no
#

# First, lets see Lists:

mylist = ['banana', 'apple', 'cherry']

# List items are orederedm changeable and allow duplicate values
# List items are indexed: list[0], list[1], ...

# we can determine list length with
print(len(mylist))


# lists allow any data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ['abc', 34, True]


# from python's perspective, lists are defined as objects with data type 'list'
print(type(list1)) # <class 'list'>


# another way to create lists is the list() constructor
list5 = list((1, 2, 3))
print(list5) # [1, 2, 3]


# 8.1 Access Items
mylist = ['hi', 'hello', 'world']
print(mylist[1]) # hello

# negative indexing: starts from the end
# -1 = last item
# -2 = second last item
print(mylist[-1]) # world

# range of indexes
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist[2:5])
# prints 3º item to 5º
# the list[5] is NOT included

print(mylist[:5]) # range from beginning to [5] NOT included
print(mylist[5:]) # range from [5] to the end

# negative range
print(mylist[-4:-1]) # range from [-4] to [-1] NOT included

# check if item exist in a list
if 'apple' in mylist:
    print('yeah, its on the list!')


# 8.2 Change list items
mylist = [1, 1, 3, 4]
mylist[1] = 2
print(mylist) # [1, 2, 3, 4]

# modify ranges
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
mylist[1:3] = ["blackcurrant", "watermelon"] # modify 'banana' and 'cherry'
print(mylist) 

# you can also insert ranges in just 1 item (adding 1 to the list length) or insert 1 item into a rang (making the length -1 than the original)
mylist = [1, 2, 3, 4]
mylist[3:] = [4, 5] # replace the 4 with 4,5 -> [1,2,3,4,5]
print(mylist)

mylist[1:3] = [0, 0] # [1, 0, 0, 4, 5]
print(mylist)

# another way to insert items is insert() method
mylist = [1, 2, 4, 5]
mylist.insert(2, 3) #insert in list[2] the value '3' -> [1, 2, 3, 4, 5]
# note that other list items has been moved 1 position

# Append items: append()
mylist = ['hi', 'hello']
mylist.append('world')
print(mylist) # ['hi', 'hello', 'world']

# Extend list: extend()
list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
print(list1) # [1, 2, 3, 4]

# Remove a element: remove()
list1 = [1, 2, 3, 4]
list1.remove(3)
print(list1) # [1, 2, 4]

# Remove a index: pop()
list1 = [1, 2, 3, 4]
list1.pop(0)
print(list1) # [2, 3, 4]

# if pop does not recieve any index, deletes the last item
list1.pop()
print(list1) # [2, 3]

# Remove a index with 'del'
del list1[0] # removes the item index
print(list1) # [3]

# Clear the list: clear()
list1.clear()
print(list1) # []


# Loops on list items
arr = ['uno', 'dos', 'tres']
for x in arr:
    print(x) # x values: uno, dos, tres

# Loop on list indexes
for x in range(len(arr)):
    print(arr[x]) # x values: 0, 1, 2

# Loop with while
i = 0 # counter
while i < len(arr):
    print(arr[i])
    i = i + 1

# Shorthand loop to print all items in a list
[print(x) for x in arr]



# List Comprehesion
# for example, create a new list with the items containing letter 'a'
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
a_fruits = []

for x in fruits:
    if 'a' in x:
        a_fruits.append(x)

print(a_fruits) # ['apple', 'banana', 'mango']

# using list comprehesion, we can write all that code in just 1 line
new_a_fruits = [x for x in fruits if 'a' in x]
print(new_a_fruits)
# SYNTAX: newlist = [expression for item in iterable if condition == True]]

# you can iterate with range()
arr = [x for x in range(10)] # [0, 1, 2, ..., 8, 9]

# only numbers lower than 5
arr = [x for x in range(10) if x < 5] # [0, 1, 2, 3, 4]

# the 'expression' is the outcome, so you can manipulate it
arr = [x.upper() for x in fruits] # ['APPLE', 'BANANA', ...]

# example: replace all the values with 'hello'
arr = ['hello' for x in fruits] # ['hello', 'hello', ...]

# example: return orange instead of banana
arr = [x if x != 'banana' else 'orange' for x in fruits]


# Sort lists - sort()
# that method will sort the list alphanumerically ascending
arr = [6, 3, 7, 1]
arr.sort()
print(arr) # [1, 3, 6, 7]

# descending
arr.sort(reverse = True)
print(arr) # [7, 6, 3, 1]


# customize Sort function
# you can customize the sort with: sort(key = function)
def myfunc(n):
    return abs(n - 50)

arr = [100, 50, 65, 82, 23]
arr.sort(key = myfunc)
# this will order the numbers by how close they are from number 50


# By default sort() is case sensitive, so capital letteres go before lower ones
# to sort ignoring them:
arr = ['banana', 'Orange', 'Kiwi', 'cherry']
arr.sort(key = str.lower)

# reverse
arr.reverse()


# Copy Lists
# You cannot copy a list with {list2 = list1} because list2 will be a reference to list1, so every change to list1 will apply to list2
# So, to make a copy of the list, need to use copy() method
new_arr = arr.copy()

# another way to copy a list is list()
new_arr = list(arr)



