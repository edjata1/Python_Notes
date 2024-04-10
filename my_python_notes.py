# Break each section down into different pages to run ALL WORKS!

import sys
# My freeCodeCamp study notes for Python 3 By Beau 

# Tiobe, shellscripting, django, animation, web development, data analysis, 
# machine learning, make games, work with embedded devices

# create replit.com IDE account -> create a repl -> python 

# create variable_name = some_value
print("------------ Variables --------------")
name = "Beau" # "Beau" assigned to name
__name_last__ = "Smith" # "Smith" assigned to __name_last__ 
age = 39
ADDRESS = "123 Main St"
_city_ = "Boston"; print(name) # print name, poor formatting 

# CAN NOT USE KEYWORD for variable_name, SUCH AS: for, if, while, import

print() # new line

print("------------ Expressions & Statements --------------")
# Expressions: any code that returns a value
print(1 + 1) # Expressions
print("Beau") # Expressions
# Statements: operation on a value
name = "Empress" # Statements: assigns value to name
print(name) # Statements: doing something to value

# data types: string, 

# check datatype 
print(type(name)) # "Beau" is a string --> <class, str>
print(type(name) == str) # compare datatype = string --> True
print(isinstance(name, str)) # is instance of string --> True

age = 2
print(isinstance(age, int)) # is instance of integer --> True

print(isinstance(age, float)) # is instance of float --> False

age = float(2) # convert (2): make it a float
print(isinstance(age, float)) # is instance of float --> True

age = int("20")
print(isinstance(age, int)) # is instance of integer --> True

number = "20"
new_age = int(number) # casting (number): make string an integer
print(isinstance(new_age, int)) # is instance of integer --> True
# common datatypes:
# complex for complex numbers
# bool for booleans
# list for lists
# tuple for tuples
# range for ranges
# dict for dictionaries
# set for sets

print()
print("------------------------Game-------------------")

# ------------------------RPS_Game-------------------
# print("Select one, (r) rock, (p) paper, (s) scissors")
import random

def greeting():
  name = input("Enter your name: ")
  return "Hi " + name.title() + ", good luck!"

print(greeting())
response = greeting()
print(response)

def get_choices():
  player_choice = input("Enter selection (rock, paper, scissors): ")

  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player" : player_choice.lower(), "computer" : computer_choice}

  return choices 

# choices = get_choices()
# print(choices)

def check_win(player, computer):
  print(f"You chose \'{player}\', computer chose \'{computer}\'.")

  if player == computer:
    return "It's a tie" 

  elif player == "rock": 
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else: # computer == "paper"
      return "Paper covers rock! You loser..."

  elif player == "paper": 
    if computer == "rock":
      return "Paper covers rock! You win!"
    else: # computer == "scissors"
      return "scissors cut up paper! You loser..."

  elif player == "scissors": 
    if computer == "paper":
      return "scissors cut up paper! You win!"
    else: # computer == "rock"
      return "Rock smashes scissors! You loser..."

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)

# example: Accessing dictionary using ["key"] to get "value"
choices = {"player" : "rock", "computer" : "paper"}
p_choice = choices["player"]
c_choice = choices["computer"]


# --------------------RPS_GAME_OVER-------------------------


dict = {"name" : "Empress", "color" : "red"} # example dictionary
dict2 = {"name" : "Empress", "selection" : choices}

food_list = ["pizza", "carrots", "eggs"] # example list
dinner = random.choice(food_list)




print()
# Operators
print("------------ Assignment Operators --------------")
age = 20 # assignment operator
print("------------ Arithmetic Operators --------------")
1 + 1 # equals: 2
1 + -1 # equals: 0
2 - 1 # equals: 1
2 * 2 # equals: 4
4 / 2 # equals: 2
4 % 3 # remainder: 1
4 ** 2 # squared: 16
5 // 2 # floor division, divide & round down: 2

age = 8
age += 8 # used arithmetic operators with ='s': age = age value + 8
print(age)
print(1 + -1)
print ("Scamp" + " is a good dog") # + , also used to concatenate 

age = 8
age *= 8
print(age)

print()
print("------------ Comparison Operators --------------")
a = 1
b = 2

a == b # False
a != b # True, not =
a > b # False, greater than
a <= b # True, less than or =

print()
print("------------ Boolean Operators: ----------------")
condition1 = True
condition2 = False

# Boolean Operators
print("------------ \"not, and, or Operators\" ----------------")
not condition1 # False, not true
condition1 and condition2 # False, both must be true
condition1 or condition2 # True, only 

# if x is false, then y, else x. ex: print(x or y)
print(0 or 1) # 1st. value, not false
print(False or 'hey') # hey, true value
print('hi' or 'hey') # hi, true value
print([] or False) # False
print(False or []) # [], false value

# and only evaluates the second argument, only if the 1st. one is true
# if x is false, then x, else y. ex: print(x and y)
print(0 and 1) # 0, false value
print(1 and 0) # 0, false value
print(False and 'hey') # False
print('hi' and 'hey') # hey
print([] and False) # []
print(False and []) # False

# Bitwise Operators
# & : performs binary AND
# | : performs binary OR
# ^ : performs binary XOR operation
# ~ : performs a binary NOT operation
# << : shift left operation
# >> : shift right operation 

# other Operators
# is : identitity Operators: compare two objects, returns true, if both are same objects
# in : membershit Operators: if value is contained in list or sequence

print()
# ternary Operators : quickly define conditional 
# example long way
print("------------ function using ternary operators --------------")
def is_adult(age):
    if age > 18:
        return True
    else:
        return False
# ternary
def is_adult2(age):
    return True if age > 18 else False # define result if true, evaulate condition, define result if false

print()
print("------------ strings --------------")
# string
myname = "mike"
myname += "Davis"
print(myname)
yourname = 'mike'
phase = name + " davis " + "is my name."
name += phase
print(name)
age3 = str(39)
print(type(age3))
# multi-line string
print(""" Empress is

      29

      years

      old!
""")

print()
print("------------ built-in methods --------------")
print("empress".upper()) # capitalize upper case
print("EmPRess".lower()) # lower case
print("empress djata".title()) # capitalize first letter
print("Empress".islower()) # check is lower case
print("Empress".isupper()) # check is upper case
print("Empress".startswith("Em")) # check start with
print("Empress".endswith("Em")) # check ends with
# print("Empress".replace("Enid")) FIX
print("Empress".split("pr")) # split, cut out "pr"
print("Empress".strip()) # strip, cut out whitespace
print("Empress".join("XYZ")) # append new letters to string
print("Empress".isalpha()) # True, contains only chars
print("Empress".isalnum()) # True, contains chars or digits & is !empty
print("Empress".isdecimal()) # False, contains digits & is !empty
print("Empress".find("s")) # 5th index

# they all return a new modified string
name = "Empress"
print(name.lower()) # change to lowercase 
print(name) # no change
# global function with strings
print(len(name)) # length of string
print("mpre" in name) # is in --> True
name = "Dj\"ata" # add "
print(name)
name = "Dj\nata" # add new line
print(name)
name = "Djata"
print(name[1]) # 1 index
print(name[-1]) # counting at end
print(name[1:4]) # range start at - end before
print(name[:3]) # up too char 3
print(name[2:]) #  from 2 to end of string

print()
# boolean
print("------------ boolean & control statements --------------")
done = True
if done:
  print("Yes, complete!") # evaluate true
else:
  print("Oh, Sorry not done.")

done = 0
if done:
  print("Yes, complete!")
else:
  print("Oh, Sorry not done.") # evaluate false

done = 10
if done:
  print("Yes, complete!") # evaluate true
else:
  print("Oh, Sorry not done.")

done = False
if done:
  print("Yes, complete!")
else:
  print("Oh, Sorry not done.")  # evaluate false

done = -1
if done:
  print("Yes, complete!")  # evaluate true
else:
  print("Oh, Sorry not done.")

done = ""
if done:
  print("Yes, complete!")
else:
  print("Oh, Sorry not done.")  # evaluate false

done = "Empress"
if done:
  print("Yes, complete!")  # evaluate true
else:
  print("Oh, Sorry not done.")

# NOTE: list, tuples, set or dictionary FALSE when empty

print()
# check type is boolean 
print("------------ boolean --------------")
done = True
print(type(done) == bool)

# 'any' global function kind of like OR
book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read]) # list
print(read_any_book)

# 'all' global function kind of like AND
ingredients_purchased = True
meals_cooked = False

ready_to_serve = all([ingredients_purchased, meals_cooked])
print(ready_to_serve)

print()
# number data types, complex
# int = whole #, float = decimal #, complex = real # system written w/ j notation
print("------------ complex numbers --------------")
num1 = 2 + 3j
print(num1)

# complex constructure
num2 = complex(2, 3)
print(num2.real, num2.imag)

print()
# built-in functions that help w/numbers
print("------------ built-in functions w/#s --------------")
num3 = abs(5.5)
num4 = abs(-5.5)
print(num3)
print(num4)

num5 = round(5.5)
print(num5)

print(round(5.493, 1))

print()
# Enums (Only way to make constants)
print("------------ Enums --------------")
from enum import Enum 

# constance
class State(Enum):
  INACTIVE = 0
  ACTIVE = 1

print(State.ACTIVE)
print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])
print(State['ACTIVE'].value)
print(list(State))
print(len(State))

print()
# USER input
print("------------ input --------------")
print("What is first your name? ")
first_name = input()
print("Nice to meet you " + first_name.title())
last_name = input("What's last name? ")
print("Your last name is " + last_name.title())
age = input("Enter age ")
print("Your age is " +age)

print()
# control statements
print("------------ control statements --------------")
fluffy = False

if fluffy == True:
  print("The fluffy statement")
  print("was True")
else:
  print("The fluffy statement")
  print("was False")

condition_1 = False
client_name = "Keisha"

if condition_1 == True:
  print("The fluffy statement")
  print("was True")
elif client_name == "Keisha":
  print("Hello " + client_name)
elif client_name == "Syd":
  print("Hello " + client_name)
elif client_name == "Flavio":
  print("Hello " + client_name)
else:
  print("The condition")
  print("was False")

print()
# list (can mix datatype)
print("------------ list : mix datatypes --------------")
dogs = ["Blu", "Shug", "Syd", 1, True, "Roger", False, "Quincy", 7]
cats = []
print(dogs)
# contained in
print("Roger" in dogs)
# empty list
print("Empress" in cats)

print()
# reference item by index
print("------------ reference index --------------")
print(dogs[2]) # reference starting from front of list
print(dogs[-2]) # reference starting at end of list

print()
# update item in list
print("------------ update list --------------")
dogs[3] = "Beau"
print(dogs[3])
print(dogs)

print()
# extract part of list
print("------------ extract from list --------------")
list1 = dogs[2:4] # start @ 2 upto not including 4
print(list1)
print(dogs[2:]) # go through end of list
print(dogs[:4]) # go upto not including 4

print()
print("------------ length --------------")
print(len(dogs))
print(len(cats))

print()
print("------------ append --------------")
cats.append("John")
cats.append("Jerry")
cats.append("Max")
print(len(cats))
print(cats)
cats.extend(["Jackie", "Sar", 6]) # add items to list
print(len(cats))
print(cats)
cats += ["Rickie Rick", "Buster", 7] # same as extends
print(len(cats))
print(cats)
cats += "Buddy" # w/o [] will add individual letters
print(len(cats))
print(cats)

print()
print("------------ remove from list --------------")
cats.remove("Rickie Rick")
print(cats)
print("You just popped (" + cats.pop() + ") from the list")
print(cats)

print()
print("------------ Add to list --------------")
items = ["Blu", "Shug", "Syd", 1, True, "Roger", False, "Quincy", 7]
items.insert(2, "Testing Insertion")
print(items)

print()
print("------------ Add multiple items w/ slice --------------")
items[1:1] = ["Test1", "Test2"]
print(items)

print()
print("------------ sort --------------")
items2 = ["blue", "Test1", "Test2", "Blu", "Shug", "Testing Insertion", "Syd", "Roger", "Quincy"]
items2copy = items2[:] # copy of original list
items2.sort() # needs same type, sorts Upper case 1st
print(items2)

items2.sort(key=str.lower) # sort all no matter case
print(items2) # sorted 
print(items2copy) # unchanged

print()
print("------------ sorted w/o changing original list --------------")
# sort list without modifying original list
print(sorted(items2, key=str.lower))
print(items2copy) # unchanged

print()
print("----- tuples (immutable groups of objects, can't change) -----")
tuple_names = ("Enid", "Empress")
print(tuple_names[0])
print(tuple_names.index("Empress"))
print(len(tuple_names))
print("Empress" in tuple_names)
print(tuple_names)
print(sorted(tuple_names)) # sorted no range 
print(tuple_names)
print(sorted(tuple_names[0:2])) # sorted range
print(tuple_names)
newTuple = tuple_names + ("Tammy", "Rick") # create new, can't extend tuple
print(sorted(newTuple))

print()
print("------------ Dictionaries Key, value pairs --------------")

dog = { "name" : "Rickie", "age" : 8, "color" : "golden-black"}
print(dog)
print(dog["name"])
dog["name"] = "K.C." # change name
print(dog)
print(dog.get("age"))
print(dog.get("color", "Red")) # adds default value if none
cat = { "job" : "lazying around", "name" : "Tom", "age" : 8, "color" : "golden"}
print(cat.get("color", "Red")) # has value
print(cat.pop("name")) # removes item from list
print(cat)
print("color" in cat) # contains color
print(cat.popitem()) # pop's last item key:value pair
print(cat)

print("color" in dog) # key contained in dictionary
print(dog.keys()) # get list w/ keys in dictionary
print(cat.keys())
print(list(dog.keys())) # pass keys into list, get just list part
print(list(cat.keys()))
print(dog.values()) # get list w/ values in dictionary
print(cat.values())
print(list(dog.values())) #  pass values into list, get just list part
print(list(cat.values()))
print(list(dog.items()))
dog["Favorite Food"] = "Meat" # add to dictionary
cat["Favorite Food"] = "Tuna" # add to dictionary
print(len(dog))
print(len(cat))
del dog['color'] # delete
print(dog)

dogCopy = dog.copy() # copy
print(dogCopy)

print()
print("---Sets (data structure, works like tuples but not ordered & immutable) ----")
# works like dictionary, but no keys. works like mathematical sets. can't have 2 same items

set1 = {"Kim", "Keisha"}
set2 = {"Keisha"}
intersect = set1 & set2 # the intercept "Keisha" in common
print(intersect)

set1 = {"Kim", "Keisha"}
set2 = {"Keisha"}
mod_union = set1 | set2 # the union "Kim", "Keisha" all items from both sets
print(mod_union)

set1 = {"Kim", "Keisha"}
set2 = {"Karen"}
mod_union = set1 | set2 # the union "Kim", "Keisha" "Karen" all items from both sets
print(mod_union)

set1 = {"Kim", "Keisha"}
set2 = {"Keisha"}
mod_difference = set1 - set2 # the difference between the sets is "Kim"  
print(mod_difference)

set1 = {"Kim", "Keisha"}
set2 = {"Karen"}
mod_superset = set1 > set2 # the superset is this greater than that "True" set1 has all that
print(mod_superset)

set1 = {"Kim", "Keisha"}
set2 = {"Karen"}
mod_subset = set1 < set2 # the subset does this set2 have everything the other has "False"
print(mod_subset)


set1 = {"Kim", "Keisha"}
set2 = {"Keisha"}
intersect = len(set1) + len(set2) # the count items in set "len()" look uo
print(intersect)

set1 = {"Kim", "Keisha"}
set2 = {"Keisha"}
print(list(set1)) # the get list, list of set, list() constructure "Kim", "Keisha"

set1 = {"Kim", "Keisha", "Keisha"}
set2 = {"Keisha"}
print(list(set1)) # only 1 of each item in the set "Kim", "Keisha"


set1 = {"Kim", "Keisha"}
set2 = {"Karen"}
mod_union = set1 in set2 # the contained in set
print(mod_union)

print()
print("---- functions (readability and code reuse) -----")
# Create a set of instructtions that can be run when needed

def hello(): # Function definition, descriptive name. Decompose a program into manageable parts
  print("Hello!") # Indent 1 level on right. Body of function (set of instruction)
hello() # Run or call hello() function. readability and code reuse
hello()
hello()

# parameters : values accepted by function inside function definition
# arguments : values passed to function when called

def hello(name): # function definition (parameter) inside parameter is "name"
  print("Hello " + name) # concat string
hello("Jerry") # function called, passed argument
hello("Hank")
hello("Timmy")

def hello(name = "my friend!"): # default value
  print("Hello " + name) # concat string
hello() # function called, passed default value "my friend!"

def hello(name, age): # multiple (parameter) "name" & "age" passed by reference
  print("Hello " + name + ". You're " + str(age) + " years old.") # concat string
hello("Jerry", 21) # function called, passed argument 

# immutable: integers, booleans, floats, strings & tuples
# pass them as parameters and modify their value inside the function, new value NOT reflected outside function

# Example: immutable Functions
def change(value):
  value = 2

val = 1 # immutable
change(val) # WILL CHANGE

print(val) # output: 1


# Example: mutable Functions
def change(value):
  value ["name"] = "Sky" # key : value pair

val = {"name" : "Kerry"} # dictionary is mutable
change(val)  # WILL NOT CHANGE

print(val) # output: Sky

# function return value 
def hello(name):
  print('Hello ' + name + '!' )
  return name

hello("Empress")

def hello2(name):
  if not name:
    return
  print('Hello ' + name)

hello2(False) # returns nothing
hello2("Empress")

def hello3(name):
  print('Hello ' + name + '!')
  return name, "Niddy", 24 # return multiple values

hello3("Empress") # Hello Empress!
print(hello3("Empress")) # "Empress", "Niddy", 24

print()
print("------------ variable scope --------------")
# ------------ global variable 
age = 8 # global variable 

def test():
  print(age)

print(age) 

# ------------ local variable 
def test2():
  age2 = 8 # local variable 
  print(age2)

# ---  print(age2) not defined, NO ACCESS TO LOCAL VARIABLES
test2()

# nested functions 1
def talk(phrase):
  # hide functionality inside function
  def say(word):
    print(word)

  words = phrase.split(' ') # splits each word in talk()
  for word in words:
    say(word) # SAY EACH WORD ON NEW LINE
talk('I am going to buy the milk')

# nested functions 2
def count(): # outter function
  count = 0

  def increment(): # inner function 
    nonlocal count # to access outter function variable count
    count = count + 1
    print(count)

  increment()

count()

# nested functions 3: Closures
# if return nested function from function, nested function has access to variable from function, even if functions not active anymore
def counter():
  count = 0

  def increment():
    nonlocal count
    count = count + 1 
    return count

  return increment

increment = counter()
print(increment())
print(increment())
print(increment())

print()
print("------------ objects --------------")
# Everything in python is an object
# objects have (attributes) & (methods) that can be accessed using dot syntax

age = 7 # age has access to properties and methods defined for all integers

print(age.real)
print(age.imag)
print(age.bit_length())

# variable hold list value has access to different methods defined for all list
items = [1, 2]
items.append(3)
items.append(5)
items.pop()
print(id(items)) # location in memory

# immutable objects : object can't provides methods to change its content
age = 8

age = age + 1 # creates a new obect

# mutable objects : object provides methods to change its content
name = {"John", "Jack", "Jimmy"}

print()
print("------------ Loop --------------")
# while & for loops

# continues loop until false
condition = True
while condition == True: # never ends
  print("The condition is True")
  condition = False

# while loop with counter
count = 0
while count < 10:
  print("The condition is True")
  count += 1

print("After the loop")

# for loop
items = [1, 2, 3, 4]
for item in items: # iterate over each items in list
  print(item)

# for loop iterate a # of times
for item in range(20): # iterate over each items in range start index 0
  print(item)

# for loop each item & index
items = [1, 2, 3, 4]
print('index', 'item')
for index, item in enumerate(items): # iterate over each items in list

  print(index, item)

items = ['Mike', 'Timmy', 'Sally', 'Sarah']
print('index', 'item')
for index, item in enumerate(items): # iterate over each items in list
  print(index, item)

# continue loop
items = [1, 2, 3, 4]
for item in items:
  if item == 2:
    continue # skips 2 and continues loop
  print(item)

# break loop
for item in items:
  if item == 2:
    break # stops when gets to 2, break out of loop
  print(item)

print()
print("------------ Classes --------------")

# declare class
# from classes, can instantiate objects
# object is instance of class
# class is type of object

class Dog: # create class

  # class method
  def bark(self): # self points to current object instance
    print("woof!")

# instance of class 
roger = Dog()

print(type(roger))

 # create class with constructor
class Dog: # create class
  # constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # class method
  def bark(self): # self points to current object instance
    print("woof, woof!")

# instance of class 
roger = Dog("Shug", 7)

print(roger.name)
print(roger.age)
print(roger.bark()) # print not need output: None
roger.bark()

# inheritance, important feature of class
class Animal: 
  def walk(self):
    print("Walking...")

class Cat(Animal):
  # constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # class method
  def talk(self): # self points to current object instance
    print("meow, meow!")

# instance of class 
roger = Cat("Shugger", 11)

print(roger.name)
print(roger.age)
roger.talk()
roger.walk()

print()
print("------------ Modules --------------")
# every python file is a module
# import module from other files
# 1 file acts as entery point, other files are modules expose functions to call

# import external file dog.py
import dog as dg

dg.wild_bark()

# or use "from import" import specific functions needed
from dog import wild_bark
wild_bark()

from libs import cat as ct

ct.wild_meow()

from libs import cat

ct.wild_meow()

from libs.cat import wild_meow
wild_meow()

# python libraries(COMMON): per built modules

# math for math utilities 
# re for regular expressions
# json to work with JSON
# datetime to work with dates
# sqlite3 to use SQLite
# os for Operating System utilities
# random for random number generation 
# statistics for statistics utilities
# http to create HTTP servers
# urllib to manage URLs

import math

print(math.sqrt(64))

# OR

from math import sqrt
print(sqrt(64))


print()
print("------------ Accepting Arguments (Advance Topic) --------------")
# Accept aguments from command line (shell)
import sys
print(sys.argv)

name = sys.argv[1]

print("Hello " + name)

# Accept aguments color
import argparse 

parser = argparse. ArgumentParser(
  description = 'This part of the program  name dags'
)

parser.add_argument('-c', '--color', metavar = 'color', required = True, help = 'the color to search for')

args = parser.parse_args()
print(args.color)

# Accept aguments color choices
import argparse

parser = argparse. ArgumentParser(
  description = 'This part of the program  name dags'
)

parser.add_argument('-c', '--color', metavar = 'color', required = True, choices = {'red', 'black', 'green'}, help = 'the color to search for')

args = parser.parse_args()
print(args.color)


print()
print("------------ Lambda Functions --------------")

# no name & 1 expression for body. lambda argument : expression "RETURN VALUE"!!!
lambda num : num * 2 

multiple = lambda a, b : a * b
print(multiple(6, 4))


print()
print("------------ Map(), Filter(), Reduce() --------------")
# map over each item in map change values ------------------
numbers = [1, 2, 3]
def double(a):
  return a * 2

result = map(double, numbers) # get new list
print(result) # map object location

print(list(result)) # new list

# OR map using lambda ---------------------------------------

numbers2 = [1, 2, 3, 4]

double = lambda  a : a * 4
result = map(double, numbers2)
print(list(result)) # map object location

# OR map using lambda -----------------------------------------

numbers3 = [1, 2, 3, 4, 5]

result = map(lambda  a : a * 5, numbers3) # using lambda function
print(list(result)) # map object location

# filter takes iteratable and return a filtered object -------------

numbers4 = [1, 2, 3, 4, 5, 6, 7]

# gets even number
def isEven(n):
  return n % 2 == 0 # if even, returns True
result = filter(isEven, numbers4) # return all even numbers
print(list(result))

# OR filter lambda gets even number

result = filter(lambda n : n % 2 == 0, numbers4)
print(list(result))

# OR filter lambda gets odd number

result = filter(lambda n : n % 2 == 1, numbers4)
print(list(result))

# reduce : calculate value out of sequence --------------------------------
expenses = [('Dinner', 80), ('Car Repair', 120)]

# long way of doing it w/o reduce
sum = 0
for expense in expenses:
  sum += expense[1]

print(sum)

# reduce
from functools import reduce

# reduce(lambda reduction function, iterable)
sum2 = reduce(lambda a, b : a[1] + b[1], expenses)
print(sum2)

print()
print("------------ Recursion --------------")
# Recursion function in python that calls itself
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
  if n == 1 : return 1 # base case, when to stop exit function
  return n * factorial(n - 1) # Recursion, when to continue

print(factorial(3))
print(factorial(4))
print(factorial(5))

print()
print("------------ Decorators --------------")
# a way to change, enhance ot alter in any way how function works 
# using @ decorator name before function definition
# Examples of use: add logging, test performance, perform caching, verify 
# permissions, run same code on multiple functions & so on 

def logtime(func):
  def wrapper():
    # do something before, like
    print("Before")
    val = func()
    # do something after, like
    print("After")
    return val
  return wrapper

# used to change the behavior of the function w/out changing the function itself
@logtime
def hello():
  print("Hello")

hello()

print()
print("------------ Docstrings --------------")
# """ Docstrings format, common to place at top of file, & can use help()"""
""" Dog module

This module does ... bla bla bla and provides the 
following classes:

- Dog
...
"""


def increment(n):
  """ Increment a number """
  return n + 1

print(increment(5))

class Dog:
  """ A class representing a dog """
  def __init__(self, name, age):
    """ Initialize a new dog """
    self.name = name
    self.age = age

def bark(self):
  """ Let the dog bark """
  print('WOOF!')

# helper method & other helper methods can be used
# print(help(Dog))

print()
print("------------ Annotations --------------")
# REMEMBER: Python is dynamically typed, for variable datatypes
# BUT, Annotations allow you to optionally do that

# function w/out Annotations
def increment(n):
  return n + 1
print(increment(5))
# function w/ Annotations
def increment(n: int ) -> int:
  return n + 1
print(increment(5.2)) # PYTHON WILL IGNORE these Annotations, 
# variables w/ Annotations
count: int = 0 # PYTHON WILL IGNORE these Annotations, 
# tool called mypy to check for type errors & mismatch errors statically while coding

print()
print("------------ Exceptions --------------")
# try:
  # some lines of code
# except EOFError: # file error
  # handles file error "END OF FILE"
# except <ERROR1>:
  # handler <ERROR1>
# except <ERROR2>:
  # handler <ERROR2>
# OR TO CATCH ALL ERRORS
# except:
  # RUNS IF NO ERRORS
  # all except type errors
# OR CAN PUT AN ELSE BLOCK IF NO EXCEPTIONS ARE FOUND
# else:
  # "code to run" if 'try' block works & no errors
# finally:
 # do something in any case, runs if (ERRORS OR NO ERRORS)

# example
try:
  result = 2 / 0
except ZeroDivisionError:
  print('Can\'t divide by zero!')
finally:
  result = 1

print(result)

# TO RAISE YOUR OWN EXCEPTIONS - general exception
# raise Exception ('AN ERROR! HAHAHA')

try:
  raise Exception ('AN ERROR! HA HA HA')
except Exception as error:
  print(error)

# define own exception class extending from exception 
class DogNotFoundException(Exception):
  pass # means nothing. used with class w/out methods or function w/out code

try:
  raise DogNotFoundException()
except DogNotFoundException:
  print('Dog not found!')



# Can do something inside exception 
class DogNotFoundException(Exception):
  print("inside exception")
  pass # means nothing. used with class w/out methods or function w/out code

try:
  raise DogNotFoundException()
except DogNotFoundException:
  print('Dog not found!')


print("------------ With statement --------------")
# with can do alot 
# simplify working with exception handling 
# example without 'with'
filename = 'flavio/test.txt'

try:
  file = open(filename, 'r')
  content = file.read()
  print(content)
finally:
  file.close()

# OR use with --- with will close file at end

with open(filename, 'r') as file:
  content = file.read()
  print(content)

print()
print("------------ 3rd. party packages --------------")
# pip
# install 3rd. party packages using 'pip'
# modules are all collected in a single place called : 
# "Python package index" find at pypi.org

# go to shell or console on computer --> clear --> type: pip install "package name "

# pip install requests

# Upgrade 
# pip install -U requests

# uninstall 
# pip uninstall requests

# specific version 
# pip install -U requests

# show 
# pip show requests
print()
print("------------- list compressions - Advance list -----------------")
# list compressions : create list in very concise way

numbers = [1, 2, 3, 4, 5] 

# list compressions, using "numbers list elements" to the power of 2
numbers_power_2 = [n**2 for n in numbers] # used sometimes over loops 
print(numbers_power_2)

# or loop 
numbers_power_2 = []
for n in numbers:  
  numbers_power_2.append(n**2)

print(numbers_power_2)

# or map 
numbers_power_2 = list(map(lambda n : n**2, numbers))
print(numbers_power_2)

print()
print("------------- Polymorphism -----------------")
# Polymorphism generalizes a functionality so we can work on different types

class Dog:
  def eat(self):
    print ('Eating dog food')

class Cat:
  def eat(self):
    print('Eating cat food')

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat()

print()
print("------------- Operator Overloading -----------------")
# used to make classes compareable & work with python operators

# class 
class Wild_Dog:
  # function
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # function Operator Overloading
  def __gt__(self, other):
    return True if self.age > other.age else False

# objects 
miles = Wild_Dog('Miles', 16)
millie = Wild_Dog('Millie', 25)

print(miles.name)
print(miles.age)
print(millie.name)
print(millie.age)
print( miles > millie)

# Other methods that can be created 
# __add__() respond to the + operator 
# __sub__() respond to the - operator 
# __mul__() respond to the * operator 
# __truediv__() respond to the / operator 
# __floordiv__() respond to the // operator 
# __mod__() respond to the % operator 
# __pow__() respond to the ** operator 
# __rshift__() respond to the >> operator 
# __lshift__() respond to the << operator 
# __and__() respond to the & operator 
# __or__() respond to the | operator 
# __xor__() respond to the ^ operator 
# __gt__() respond to the > operator 
# __lt__() respond to the < operator 

































































































































