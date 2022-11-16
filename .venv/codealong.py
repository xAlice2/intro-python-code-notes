print("Hello World")

# run 'import this' inside of your python terminal and see what you get

# this is comment, keep note

"""this is a multi line comment
    however proper indentation must be kept"""
    
my_first_variable=5
print("My first variable is:", my_first_variable)

# none type needs to be talked about here

# my_bank_account = '' # this is false
my_bank_account = None # this is false


if my_bank_account:
    print("yep, you have a bank account")
else:
    print("no bank account for you")
    
# booleans, case sensitive, we want True and False, not true and false

is_operating=True
is_broken=False

print("is operating:", is_operating)
print("is broken:", is_broken)

# numbers: keep in mind, int, float and complex

an_int=32
a_float=1.89456
a_complex=2+3j

print("Int:", an_int)
print("float:", a_float)
print("complex:", a_complex)

# more complex numbers

print("a_complex(2+3j) + 5 + 4j:", a_complex + 5 + 4j)

print("int divided by a float(15/5.0): ", 15/5.0)
print("int divided by int(15/5): ", 15/5)
print("int divided by int (15/6): ", 15/6)
print("force int output from two ints divided(15//6): ", 15//6)

#python is great with large numbers, unlike javascript, see how we would calulate 2 to the 999th power in js below

"""Math.pwo(2, 999) 
    => 5.357543035931337e+300"""
    
# in python, we'd do this same action with much higher detail using the '**' operator(raise to exponent)

print('a really big number:', 2 ** 999)

# strings in python work the same as in javascript

card1='ace of spaces'
card2="king of hearts"

print(card2)

print("split card 1:", card1.split(' '))
# use the unpack operator, '*', to get each character in a string
print("split a string:", [*"abcdefg"])

# some more string examples
print("position of 'x': ", "qqxzzz".index("x"))
print("To uppercase",card2.upper())
print("To lowercase",card2.lower())
print("replace example: ", card2.replace("king", "queen"))

# using in operator to see if a word is inside of a string

print("Is egg inside of 'green eggs and ham':", "egg" in "green eggs and ham")

# get the length of a string

print("length of Hawaii is: ", len("Hawaii"))

# ranges

"""Range notes
    str[index] choose one letter at index
    str[-index] choose letter at index counting backwards from the end.
    str[start:end] get a range of letters from a start to end.
    str[start:end:step] get a range of letters taking step sized steps between.
    str[:end] omit the start index and grab letters from zero up to end.
    str[start:] omit the end index and grab letters from start up to the end of the string.
    str[::-1] reverses a string by going backwards with a step of -1 from start to end.
"""

print("get last letter: ", "my code rulez"[-1])
print("get from position 3-7: ", "my code rulez"[3:7])
print("get first 2 characters: ", "my code rulez"[:2])
print("get all but first 3: ", "my code rulez"[3:])
print("Reverse string: ", "my code rulez"[::-1])
print("Take every other character: ", "peiege eleaeteiene"[::2])
# Arithmetic operators

"""_summary_
    python uses all the same mathatical operators that javascript does with some additional options
    +   - add
    -   - subtract
    /    # decimal division       4 /  3 == 1.333333
    //   # force integer division 4 // 3 == 1
    *   - multiple
    **   # exponent  2 ** 3 == 27
    %    # modulo    17 % 5 == 2

    +=
    -=
    *=
    /=
    **= -raise to a power and set equal to
"""

# logical operators

"""_summary_
Python uses mostly the same logical operators as javascript, with some difference. There is no longer an '===' or '!=='
    ==
    !=
    not
    or
    and
"""
something_false=False
something_true=True

if not something_false and something_true:
    print("shouldn't see this")
else:
    print("should see this")

# lists
"""_summary_
    array sdo not have a .length value, you must use the len() function like with string length shown above
"""

arr = [1,2,3]

print("array length:",len(arr))

five_zeroes = [0] * 5
print("shows array of 5 zeros:", five_zeroes)

print("show length of five zeros:", len(five_zeroes))


five_trues = [True] * 5
print("shows array of 5 true:", five_trues)

last_item = ["Washington", "Oregon", "California"]
print("show last item in array:", last_item[-1])

# generate a range from 1 to 10 and create list out of it.
one_through_ten = list(range(10))
print("show the array from 1-10 we generated with range:", one_through_ten)

a = [1, 23, 12, 99, 82]

print("sort in order ascending", a.sort())

print("reverse array:", a[::-1])
# add 42 to end of array
a.append(42)

# remove item from array(last item)
result = a.pop()
print("42 shouldn't be in this array", a)
print("we took 42 out of our array", result)

# add item to givne index location

a.insert(0, 123)
a.insert(2, 66)

print(a)

a.append(42)

if 42 in a:
  print("yup! it's in there.")

# Dictionaries

"""_summary_
    dictionaries are just key value paris and work the same way they work inside of javascript see examples below
    however, you cannot use dot notation in python dictionaries.
"""

dictionary={
    "name": "Joe",
    "age": 36,
    "fav_food": ['pizza', 'toast']
}

print("our dictionary:", dictionary)

print("our name:", dictionary["name"])

age_str="age"
print("our age with a variables:", dictionary[age_str])

# type conversion

"""_summary_
    you may convert types to other similar types like we do in javascript
"""
      
print("string to int: ",int("42"))

print("int to string: ",str(42))

print("int to float: ",float(42))

print("int to boolean(true): ",bool(42))

print("int to boolean again(false): ",bool(0))

print("string to boolean(true): ",bool("foo"))

print("empty string to boolean(false): ",bool(""))

# String interpolation

"""_summary_
    we do this in javascript using `${}` syntax, we can do the same in python using the below syntax to inject variables in the middle of strings
    format: f"{}"

"""

state = "Washington State"
year = 1889
n = 42
my_message = f"{state} was the {n}th state to join the union in {year}."
print("our interpolated string: ", my_message)

"""_summary_
    lets define a function to help us add some complexity to out string interpolation
"""

def st_nd_rd_th(n):
  # add one to 13 because range is exclusive at the end.
  if n in range(11, 13 + 1):
    return "th"
  if n % 10 == 1:
    return "st"
  elif n % 10 == 2:
    return "nd"
  elif n % 10 == 3:
    return "rd"
  else:
    return "th"

n_state = "Washington State"
n_year = 1889
n_n = 42
n_my_message = f"{n_state} was the {n_n}{st_nd_rd_th(n_n)} state to join the union in {n_year}."
print("our formatted string: ",n_my_message)

# control flows

"""_summary_
    same functionality as if statements in javascript however, instead of wrapping your if statement in {} you simple enter you code after a ':'
    we also no loner have 'else if', this will now be 'elif'. see examples below.
"""

vip = True
food_place = "busy"
if (food_place == "full" and not vip):
  print("Sorry, we have no room tonight.")
elif (food_place == "busy" and not vip):
  print("Please wait 10 minutes for a table.")
else:
  print("Welcome! Come sit down right away.")

# iterators

i = 1
while i < 6:
  print(i)
  i += 1
  
for i in range(0, 10):
  if i % 2 == 0:
    print("{} is even".format(i))
  if i % 2 == 1:
    print("{} is odd".format(i))
    
car = {"wheels": 4, "doors": 2, "seats": 5}
for key in car:
  print("my car has {num} {thing}".format(thing=key, num=car[key]))

# functions

"""_summary_
    making functions in python is a critical skill you must become comfortable with. lucky, this works very much the same way we define function in javascript, with different syntax.
"""

def who_is_my_friend(friend):
    print(f"my friend's name is {friend}")

who_is_my_friend("maggie")

def who_is_my_friend_with_return(friend):
    return f"my friend's name is {friend}"

print("testing our function: ", who_is_my_friend_with_return("John"))

# tuples

"""_summary_
    tuples are new, these are not like lists but appear to be in some way, They're really a simple collection of immutable(not able ot be changed) results, typically used when returning multiple results from a function
    
"""

tuple = ("Fireman", "Fire Department")
job_title, office = tuple

print(" our job title: ", job_title)
print(" our office: ", office)

# see example below in using tuples inside of a function

def divide_mod(numerator, denominator):
  division = numerator // denominator
  mod = numerator % denominator
  return (division, mod)

students = 11
group_size = 4
num_groups, left_over = divide_mod(students, group_size)
msg1 = "{n} students can be divided into {m} groups of {size}"
msg2 = "with {j} students left over."

msg1 = msg1.format(n=students, m=num_groups, size=group_size)
msg2 = msg2.format(j=left_over)

print(msg1)
print(msg2)