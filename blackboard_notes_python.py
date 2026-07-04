"""
==========================================================
  PYTHON — BLACKBOARD SPACE NOTES
==========================================================
Running reference. Open in VS Code for color (syntax highlighting).
Run it with:  python blackboard_notes_python.py

MAP OF THIS FILE:
  1. Variables & Data Types
  2. Booleans & Comparisons
  3. Lists — basics (make, add, access)
  4. Lists — methods (insert, pop, remove, count, sort, len)
  5. Indexing & Slicing (negative index, [start:stop])
  6. 2D Lists
  7. range()
  8. The Mental Checklist
  9. GOTCHAS & QUESTIONS  <-- the stuff that tripped me up
==========================================================
"""


# ==========================================================
# 1. VARIABLES & DATA TYPES
# ==========================================================

# Variables are set with the  =  sign:
lunch_today = "chicken"

# print() shows a result on screen. Pass it a string or a variable.
# You mostly use it to CHECK "did I get the right thing?"
# print("hello")     # shows text
# print(lunch_today) # shows the variable's value

# Numbers: float vs int
example_float = 2.0     # float   -> has a decimal
example_int = 2         # integer -> whole number

# Strings: either quote style works the same
string_double = "x"
string_single = 'x'

# PUTTING A VARIABLE INSIDE A STRING — two ways:
num_pizzas = 7

# Way 1 — f-string (easiest). Put f before the quotes, {variable} in the text:
print(f"We sell {num_pizzas} kinds")     # We sell 7 kinds

# Way 2 — concatenation with + . You MUST turn the number into text with str():
print("We sell " + str(num_pizzas) + " kinds")   # ✅ text + text
# print("We sell " + num_pizzas)                 # ❌ CRASH: can't add text + number
# str(7) becomes "7", so now it's all text and + can glue them together.


# ==========================================================
# 2. BOOLEANS & COMPARISONS
# ==========================================================

# A comparison asks a yes/no question -> answer is True or False:
#   X == Y   equal
#   X != Y   NOT equal
#   X <  Y   smaller
#   X >  Y   bigger
#   X <= Y   smaller or equal
#   X >= Y   bigger or equal

X = 5
Y = 10
print(X == Y)   # False  (5 does not equal 10)
print(X < Y)    # True   (5 is smaller than 10)

# Combine conditions with logic keywords:
#   and  -> True only if BOTH are true
#   or   -> True if AT LEAST ONE is true
#   not  -> flips the result
print(X < Y and Y > 0)   # True   (both sides true)
print(X > Y or Y > 0)    # True   (at least one true)
print(not X == Y)        # True   (flips False -> True)


# ==========================================================
# 3. LISTS — BASICS
# ==========================================================

# A list is written with square brackets  [ ]
grocery_list = [1, 2, 3, 4, 5, 6, 7, 8]
empty_list = []          # an empty list is []   (NOT {} -- that's a dict!)

# ADD to the end with .append()
grocery_list.append(9)   # -> [1,2,3,4,5,6,7,8,9]

# COMBINE lists with  +
orders = ["daisy", "buttercup", "lily"]
new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders   # both lists joined into one

# ACCESS an item by index. Lists are ZERO-INDEXED (first item = 0).
first_order = orders[0]   # "daisy"
last_order = orders[-1]   # "lily"   (negative counts from the end)

# REPLACE an item by assigning to its index:
orders[1] = "rose"        # buttercup -> rose


# ==========================================================
# 4. LISTS — METHODS
# ==========================================================

fruits = ["apple", "banana", "cherry"]

# .insert(index, item)  -> put an item AT a position
fruits.insert(0, "pineapple")   # pineapple goes to the front

# .pop(index)  -> remove the item AT that position (and hand it back)
fruits.pop(0)                   # removes "pineapple"
# fruits.pop()                  # no number = removes the LAST item

# .remove(value)  -> remove the first item that MATCHES this value
fruits.remove("banana")

# .count(value)  -> how many times a value appears
apple_count = fruits.count("apple")

# .sort()  -> sorts the list IN PLACE (changes the list itself)
nums = [3, 1, 2]
nums.sort()                     # nums is now [1, 2, 3]
nums.sort(reverse=True)         # [3, 2, 1]  -> reverse=True sorts backwards

# len()  -> how many items are in the list
count = len(fruits)


# ==========================================================
# 5. INDEXING & SLICING
# ==========================================================

# NEGATIVE INDEX = count from the back, starting at -1
#   [0] = always the first item
#   [-1] = always the last item
inventory = ["a", "b", "c", "d"]
print(inventory[-1])    # "d"

# SLICING: list[start:stop]  -> stop is NOT included
example_list = [10, 20, 30, 40, 50]
sliced = example_list[1:3]      # [20, 30]   (index 1 and 2, NOT 3)

# Handy slice pattern — this ruler makes it click:
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
#             0        1        2        3        4          5
#            -6       -5       -4       -3       -2         -1
last_two = suitcase[-2:]        # ["pajamas", "books"]  (2nd-to-last -> end)


# ==========================================================
# 6. 2D LISTS  (lists inside a list)
# ==========================================================

# Each item in the outer list is its own list (a "row").
# Access with TWO indices:  list[ROW][COLUMN]
students = [
    ["Jenny", 90],       # row 0
    ["Alexus", 85.5],    # row 1
    ["Sam", 83]          # row 2
]

print(students[0][0])    # "Jenny"   (row 0, item 0)
print(students[1][1])    # 85.5      (row 1, item 1)
print(students[2][0])    # "Sam"

# First bracket  = which row (which person)
# Second bracket = which item in that row

# ADD a whole new row with .append():
students.append(["Ellie", 100])   # (["name", score]) -> new row at the end


# ==========================================================
# 7. range()  —  a number generator
# ==========================================================

# range() is an INSTRUCTION to count, not a list yet.
# Wrap it in list() to actually see the numbers.
# print(range(8))         # range(0, 8)          <- just the instruction
# print(list(range(8)))   # [0,1,2,3,4,5,6,7]    <- the real numbers

# range(start, stop, step)  -> stop is NOT included
#   range(8)        -> 0,1,2,3,4,5,6,7
#   range(2, 8)     -> 2,3,4,5,6,7
#   range(5, 15, 3) -> 5, 8, 11, 14   (start 5, before 15, jump by 3)

# ==========================================================
# 8.  gg
# ==========================================================


# ==========================================================
# 8. THE MENTAL CHECKLIST  (signal words -> tool)
# ==========================================================
"""
When you read a problem, listen for SIGNAL WORDS that point to a tool:

  WHEN YOU HEAR / SEE...                        THINK...                 TOOL
  ---------------------------------------------------------------------------
  "depending on which..." / "if this, do that"  a decision               if / elif
  "for each..." / "go through all..."           repeat something         for loop
  "keep going until..." / "as long as..."       repeat with a condition  while loop
  "store this" / "remember this value"          hold a value             a variable
  "a list of things"                            many values together     a list
  "is X equal to / bigger / smaller"            a yes/no question        == > <

THE 3 QUESTIONS to ask on EVERY problem:
  1. What do I have?              (the inputs)
  2. What do I want at the end?   (the goal)
  3. What has to happen between?  (the middle step -> tells you the tool)

PRO HABIT - shrink the problem:
  Get ONE case working first, then repeat the same shape.
"""


# ==========================================================
# 9. GOTCHAS & QUESTIONS  (things that tripped me up)
# ==========================================================
"""
Q: .pop() vs .remove() — what's the difference?
   .remove(value) -> delete by VALUE (the thing itself). e.g. .remove("banana")
   .pop(index)    -> delete by POSITION, and hands the item back. e.g. .pop(2)
   Rule: know the value -> remove. know the position -> pop.

Q: How does empty .pop() remove the LAST item?
   .pop() with NOTHING inside the () defaults to "just grab the last one."
   These all remove the last item:
       my_list.pop()     # no number = last item
       my_list.pop(-1)   # -1 = last item
   And to remove the 5th element, it's .pop(4)  (5th element = index 4,
   because counting starts at 0).

Q: Does .remove() delete ALL matching items?
   NO. It only deletes the FIRST match. Removing every match needs a loop
   (that's a preview of why loops exist — coming in the loops module).

Q: Why does calls[4/2] crash?
   Because 4/2 = 2.0, a FLOAT. List indexes must be whole numbers (int).
   Fix: calls[int(4/2)]  ->  int() chops off the decimal, 2.0 becomes 2.

Q: Why doesn't print(range(8)) show numbers?
   range() is lazy — it holds the instruction, not the numbers.
   Wrap it: list(range(8)) to actually build [0,1,2,3,4,5,6,7].

Q: sorted_list = my_list.sort()  -> why is it None?
   .sort() sorts the list IN PLACE and returns None. It does NOT give a new list.
   If you want a NEW sorted list, use sorted():   new = sorted(my_list)

Q: Why .remove("x") and not .remove["x"] ?
   Methods (actions) use ROUND brackets ( ).
   Square brackets [ ] are only for INDEXING (picking a position).

Q: {} vs [] ?
   []  = empty LIST
   {}  = empty DICTIONARY (a different thing — key/value pairs)
"""


# ==========================================================
# ( add a new section here as you finish each module )
# ==========================================================
