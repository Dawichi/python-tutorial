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
#
#
#
# ┌────────────────────────────────────────────────────────────
# │     1. Variables
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
>>          Signed right shift      Shift right by pushing copies of the leftmost bit in from the left, and let the right
most bits fall off
'''



