"""
========================================
  PYTHON - BLACKBOARD SPACE NOTES
========================================
Running reference. Open in VS Code for color (syntax highlighting).
Comments = one color, strings = another, numbers/keywords each their own.
You can also run it:  python blackboard_notes_python.py
"""


# ==========================================================
# 1. VARIABLES & DATA TYPES
# ==========================================================
# general thing with printing you basically want to have like print (" ") or print (variable) and then you can see the result of what you are trying to do.
# So basically either print a string or print a variable and then you can see the result of what you are trying to do.
# Numbers can be a float or not:
example_float = 2.0        # float   -> has a decimal
example_int = 2            # integer -> whole number

# Strings use either quote style - both work the same:
string_double = "x"
string_single = 'x'

# Printing is simple - mainly to check a result. Handy, not always needed.
# print(example_float)

# Variables are set with the  =  sign:
lunch_today = "chicken"


# ==========================================================
# 2. BOOLEAN OPERATORS
# ==========================================================

# Comparisons ask a yes/no question -> answer is True or False:
#
#   X == Y   ->  X equals Y
#   X != Y   ->  X differs from Y (not equal)
#   X <= Y   ->  X is smaller than or equal to Y
#   X >= Y   ->  X is bigger than or equal to Y
#   X >  Y   ->  X is bigger than Y
#   X <  Y   ->  X is smaller than Y

X = 5
Y = 10
print(X == Y)   # False  (5 does not equal 10)
print(X != Y)   # True   (they differ)
print(X < Y)    # True   (5 is smaller than 10)

# Logic keywords combine conditions:
#
#   and  ->  True only if BOTH conditions are true
#   or   ->  True if AT LEAST ONE condition is true
#   not  ->  flips the result (True -> False, False -> True)

print(X < Y and Y > 0)   # True  (both sides true)
print(X > Y or Y > 0)    # True  (at least one side true)
print(not X == Y)        # True  (flips False into True)


# ==========================================================
# 2. Lists
# ==========================================================


# List is often indicated with a [] 
# Lists can be empty so for instance 

grocery_list = {}

# Lists have a function called append so basically if there is an exisiting list and we want to add something to it all we have to do is just 

grocery_list = [1,2,3,4,5,6,7,8]
grocery_list.append(9)
# append is a way to add something to the end of a list.
# 
#you can also for instance add something to a list by inserting the + sign and then the list you want to add to it. 
items_sold_new = items_sold + [9,10,11]
#
#  when adding it can also happen in two ways :
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:

new_orders = ["lilac" , "iris"]
orders_combined = orders + new_orders
broken_prices = [5, 3, 4, 5, 4] + [4]

# Python lists are zero-indexed, meaning the first item is at index 0, the second at index 1, and so on. You can access items in a list using their index:
first_order = orders[0]  # "daisy"  

print(calls[4/2])         # ❌ ERROR — 4/2 = 2.0 (a float)
print(calls[2])           # ✅ Works — 2 is an integer
print(calls[int(4/2)])    # ✅ Works — int(2.0) becomes 2

#index -1 to select the last item in a list, -2 for the second-to-last, and so on. This is called negative indexing.
# if we want to replace something in a list ususally wuith strings we can set the list variable [1] = "new value" and then it will replace the value in the list.

# we can also remove items in a list by the command .remove("item") and it will remove the item from the list.
.remove("item")  # Removes the first occurrence of "item" from the list

# remember variable.append to add and variable.remove to remove an item from a list.

variable.append
variable.remove


# ==========================================================
# 3. 2D Lists
# ==========================================================




# 2D lists are lists of lists. Each element in the main list is itself a list. You can access elements in a 2D list using two indices: the first for the row and the second for the column.
#an example of a 2D list is a list of lists, where each inner list represents a row in a grid or table. For example:
[[1, 2, 3],]


# Quick reference for accessing elements in a 2D list:
Element	Index
"Noelle"	heights[0][0]
61	heights[0][1]
"Ali"	heights[1][0]
70	heights[1][1]
"Sam"	heights[2][0]
67	heights[2][1]

# Example: Student names and their scores
# Access with TWO indices: [row][column]
# First index = which row (which list)
# Second index = which item in that row (which column)

students[0][0]  # "Jenny"    (row 0, column 0)
students[0][1]  # 90         (row 0, column 1)
students[1][0]  # "Alexus"   (row 1, column 0)
students[1][1]  # 85.5       (row 1, column 1)
students[2][0]  # "Sam"
students[3][1]  # 101.5      (Ellie's score)


#Delete by value (the thing itself)	.remove( )	.remove(False)
#Delete by position (the index)	.pop( )	.pop(2)
#Read an item at a position	[ ]	[2]

# quick tips to add to 2d list i need to do gradebook.append(["computer science", 100]) so basically (["subject", score]) and then it will add it to the end of the list.


# ==========================================================
# 3. Insert, Pop , Range , Slice, and Sort
# ==========================================================



#to insert an item into a list at a specific index you can use the .insert 
#Inserting looks like this :
front_display_list.insert(0, "Pineapple")
# you have to give it the index n where it is going to be and then the i that will be inserted.

#to remove an item from a list at a specific index you can use the .pop
#Popping looks like this :
front_display_list.pop(0)
# you have to give it the index n where it is going to be removed.

# Range is a built-in function that generates a sequence of numbers. It can be used in for loops to iterate over a specific range of values. For example, range(5) generates the numbers 0, 1, 2, 3, and 4.
for example in range(5):
    print(example)  # Prints numbers 0 to 4 

# also with range it does not list numbers so for instance if you wanted to list numbers you would have to do something like this :
range(8)           # just the INSTRUCTION "count to 8" — numbers not shown yet
list(range(8))     # actually BUILDS the list so you see [0, 1, 2, 3, 4, 5, 6, 7]


# in the example below it will start at 5 and go to 15 but it will skip every 3 numbers so it will be 5, 8, 11, 14. , the last number is basically the skipping the first is start and second is end.
range_five_three = range(5, 15, 3)


# the command len returns how many items in the list or variable or list 
len(variable)  # Returns the number of items in the list or variable
len(list_example)  # Returns the number of items in list_example

# when indexing a list the numbers [x:y] also start end basically consider number 0 as 1 then 2 then 3 here is an example of how to use it :
example_list = [10, 20, 30, 40, 50]
# Get items from index 1 to 3 (not including index 3)
sliced_list = example_list[1:3]  # [20, 30] 
# so basically 1 will count as 20 and 2 will count as 30 but 3 will not be included so it will only be [20, 30].

s
















# ==========================================================
# 3. THE MENTAL CHECKLIST  (signal words -> tool)
# ==========================================================
"""
When you read a problem, listen for SIGNAL WORDS that point to a tool:

  WHEN YOU HEAR / SEE...                       THINK...                  TOOL
  ---------------------------------------------------------------------------
  "depending on which..." / "if this, do that"  a decision               if / elif
  "for each..." / "go through all..."           repeat something         for loop
  "keep going until..." / "as long as..."       repeat with a condition  while loop
  "store this" / "remember this value"          hold a value             a variable
  "a list of things"                            many values together     a list
  "is X equal to / bigger / smaller"            a yes/no question        ==  >  <

THE 3 QUESTIONS to ask on EVERY problem:
  1. What do I have?              (the inputs)
  2. What do I want at the end?   (the goal)
  3. What has to happen between?  (the middle step -> tells you the tool)

PRO HABIT - shrink the problem:
  Get ONE case working first (e.g. if planet == 1),
  then the rest is the same shape repeated.
"""


# ==========================================================
# ( add a new section here as you finish each module )
# ==========================================================
