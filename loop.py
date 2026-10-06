# 🎯 Python Loops — **FINAL COMPLETE MASTERCLASS NOTES** (Sab Kuch Included)

Bhai ye lo — **poora content**, **zero se advanced tak**, **har missing topic ke saath** — **comprehension advanced**, **for-else detailed**, **itertools**, **try-except**, **infinite loop patterns**, **break 3 methods**, **zip/enumerate advanced** — **sab kuch**. Aap **seedha record kar sakte ho**. 🎙️🔥

---

# 📚 PYTHON LOOPS — COMPLETE MASTERCLASS

---

## 🎬 INTRO (Bolne Ke Liye)

> "Namaste doston! Aaj hum baat karenge Python ke **loops** ke baare mein — **while loop** aur **for loop**. Loops kya hain? Loops ek aisa tarika hai jisse hum **ek hi code ko baar-baar** chala sakte hain. Jaise aap **100 students ke marks** print karna chahte ho — bina loop ke 100 baar print likhna padega. Loop se sirf 3 line mein kaam ho jata hai. Aaj hum loops ko **zero se advanced level** tak cover karenge. Har ek concept, har ek example, har ek use case — sab kuch detail mein. Toh chaliye shuru karte hain!"

---

# 📖 PART 1: FOUNDATION

---

## TOPIC 1: LOOP KYA HAI? (WHAT)

### Definition:
> "Loop ek **control structure** hai jo code ke ek block ko **multiple times** execute karta hai, jab tak koi condition **True** rahe ya koi collection khatam na ho jaye."

### Real-Life Analogy:
> "Socho aap **gym** mein ho. Aapko 10 push-ups karne hain. Aap ek-ek karke karte ho — 1, 2, 3... 10. Ye hai loop. Ya phir **playlist** — ek gaana khatam, next gaana, phir next — jab tak playlist khatam na ho."

### Simple Example:
```python
for i in range(5):
    print("Hello")
```

**Output:**
```
Hello
Hello
Hello
Hello
Hello
```

### Kyu Zaroori Hai:
> "Bina loops ke, repetitive kaam ke liye code **baar-baar** likhna padta. Loops se code **short, readable, aur maintainable** ho jata hai."

### Real-World Connection:
- **Instagram feed** — har post render karna
- **Netflix** — har movie list karna
- **Zomato** — har order process karna
- **Bank** — har transaction check karna

---

## TOPIC 2: LOOP KE TYPES

Python mein **2 main loops** hain:

| Loop | Kab Use Karein | Example |
|------|---------------|---------|
| **`for` loop** | Jab iterations **known** ho | `for i in range(5)` |
| **`while` loop** | Jab iterations **unknown** ho | `while condition:` |

### Diagram:
```
┌─────────────────────────────────────────┐
│           PYTHON LOOPS                  │
├─────────────────┬───────────────────────┤
│   FOR LOOP      │     WHILE LOOP        │
│                 │                       │
│  Known count    │   Unknown count       │
│  Collection     │   Condition-based     │
│  range(), list  │   True/False          │
└─────────────────┴───────────────────────┘
```

---

## TOPIC 3: `while` LOOP

### Definition:
# "`while` loop tab tak chalta hai jab tak condition **True** hai. Jaise hi condition **False** ho jaati hai, loop **stop** ho jata hai."

### Syntax:

# while condition:
    # code to execute
    # update condition (warna infinite loop!)


### Diagram:

#         ┌─────────────┐
#         │  Condition  │
#         └──────┬──────┘
#                │
#          ┌─────┴─────┐
#        True        False
#          │           │
#          ▼           ▼
#    ┌──────────┐  ┌──────────┐
#    │ Execute  │  │  Exit    │
#    │  Block   │  │  Loop    │
#    └────┬─────┘  └──────────┘
#         │
#         └──────┐
#                │
#         (wapas condition check)


### Basic Example:

count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1

print("Loop ended")


# **Output:**

# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5
# Loop ended


### Line-by-Line Explanation:
# - `count = 1` → Initialize
# - `while count <= 5:` → Condition check (1 <= 5 True)
# - `print(count)` → Execute
# - `count += 1` → Update (2)
# - Wapas condition check (2 <= 5 True)
# - ... 5 tak
# - `count = 6` → 6 <= 5 False → Loop exit
# - `print("Loop ended")` → Bahar ka code



###  Infinite Loop (Bahut Important):

# INFINITE LOOP — count update nahi ho raha
count = 1
while count <= 5:
    print(count)
    # count += 1 missing!


# "Agar condition **kabhi False na ho**, to loop **infinite** chalega. Isse **CPU 100%** ho jayega, program **hang** ho jayega."

### Industry Use Case — User Input:

password = ""

while password != "admin123":
    password = input("Enter password: ")

print("Login successful")


 #"Yahan humein **nahi pata** kitni baar input lena padega. Isliye `while` use kiya."

### Industry Use Case — Menu System:

choice = 0

while choice != 4:
    print("\n1. Add\n2. View\n3. Delete\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Added")
    elif choice == 2:
        print("Viewed")
    elif choice == 3:
        print("Deleted")

print("Exited")


### `while` Loop Ke Saath `else`:

count = 1

while count <= 3:
    print(count)
    count += 1
else:
    print("Loop completed normally")


# "`else` tab chalta hai jab loop **normally** khatam ho (break se nahi)."

### `while` Loop Kab Use Karein:
# - User input (kitni baar nahi pata)
# - Menu system
# - Game loop
# - Server listening
# - Retry logic

### `while` Loop Kab Avoid Karein:
# - Jab iterations known ho (`for` better)
# - Collection iterate karni ho



## TOPIC 4: `for` LOOP

### Definition:
# "`for` loop ek **collection** (list, tuple, string, range, dict, set) ke **har element** par iterate karta hai."

### Syntax:

# for item in iterable:
    # code to execute


### Diagram:

#    ┌──────────────────┐
#    │   Iterable       │
#    │  [1, 2, 3, 4]    │
#    └────────┬─────────┘
#             │
#     ┌───────┼───────┐
#     │       │       │
#     ▼       ▼       ▼
#   Item1   Item2   Item3 ...
#     │       │       │
#     ▼       ▼       ▼
#   Block   Block   Block


### Basic Example:

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# **Output:**

# apple
# banana
# cherry


### Line-by-Line Explanation:
# - `fruits` → Iterable
# - `for fruit in fruits:` → Har element `fruit` mein aayega
# - `print(fruit)` → Print karo
# - Jab collection khatam → Loop exit



### 4.1 `for` Loop with `range()`


# for i in range(5):
#     print(i)


# **Output:**

# 0
# 1
# 2
# 3
# 4


### `range()` Ke Variations:

range(5)        # 0, 1, 2, 3, 4
range(1, 5)     # 1, 2, 3, 4
range(1, 10, 2) # 1, 3, 5, 7, 9
range(10, 0, -1)# 10, 9, 8, ..., 1


### Diagram:

# range(5)      →  [0, 1, 2, 3, 4]
# range(1, 5)   →  [1, 2, 3, 4]
# range(1, 10, 2) → [1, 3, 5, 7, 9]
# range(10, 0, -1) → [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


### Advanced `range()` Examples:

# Reverse
for i in range(10, 0, -1):
    print(i)

# Step 2
for i in range(0, 10, 2):
    print(i)

# Negative range
for i in range(-1, -10, -1):
    print(i)


### 4.2 `for` Loop with String


name = "Rohit"

for char in name:
    print(char)


# **Output:**

# R
# o
# h
# i
# t


### String with Index:

name = "Rohit"

for i, char in enumerate(name):
    print(f"{i}: {char}")


### String Reverse:

for char in reversed(name):
    print(char)


### String Slicing:

for char in name[1:4]:
    print(char)


### 4.3 `for` Loop with List


marks = [85, 90, 78, 92]

for mark in marks:
    print(f"Mark: {mark}")


### 4.4 `for` Loop with Tuple


coordinates = (10, 20, 30)

for coord in coordinates:
    print(coord)


### Tuple Unpacking:

points = [(1, 2), (3, 4), (5, 6)]

for x, y in points:
    print(f"x={x}, y={y}")


### 4.5 `for` Loop with Dictionary


student = {"name": "Rohit", "age": 21, "city": "Bhopal"}

# Keys
for key in student:
    print(key)

# Values
for value in student.values():
    print(value)

# Key-Value pairs
for key, value in student.items():
    print(f"{key}: {value}")


### Advanced Dictionary Iteration:

# Sorted keys
for key in sorted(student):
    print(key, student[key])

# Sorted by value
for key, value in sorted(student.items(), key=lambda x: x[1]):
    print(key, value)


### 4.6 `for` Loop with Set


fruits = {"apple", "banana", "cherry"}

for fruit in fruits:
    print(fruit)


#"Set unordered hai, isliye order guaranteed nahi."



### 4.7 `for` Loop with `enumerate()`


fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")


# **Output:**

# 0: apple
# 1: banana
# 2: cherry


### `enumerate()` Ke Saath Start:

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")


# **Output:**

# 1. apple
# 2. banana
# 3. cherry


### Advanced `enumerate()`:

# Reverse enumerate
for i, item in enumerate(reversed(fruits)):
    print(i, item)

# Enumerate with condition
for i, item in enumerate(fruits):
    if i % 2 == 0:
        print(item)

# Enumerate in nested
matrix = [[1, 2], [3, 4]]
for i, row in enumerate(matrix):
    for j, num in enumerate(row):
        print(f"[{i}][{j}] = {num}")


### 4.8 `for` Loop with `zip()`


names = ["Rohit", "Sagar", "Priya"]
ages = [21, 22, 20]

for name, age in zip(names, ages):
    print(f"{name}: {age}")


# **Output:**

# Rohit: 21
# Sagar: 22
# Priya: 20


### Diagram:

# names:  [Rohit, Sagar, Priya]
# ages:   [21,    22,    20   ]
#          │       │       │
#          ▼       ▼       ▼
# zip:  (Rohit,21) (Sagar,22) (Priya,20)


### Different Lengths:

names = ["Rohit", "Sagar", "Priya"]
ages = [21, 22]

for name, age in zip(names, ages):
    print(f"{name}: {age}")


# **Output:**

# Rohit: 21
# Sagar: 22


# "`zip()` **chhoti list** ke hisaab se ruk jata hai."

### Advanced `zip()`:

# Multiple lists
for a, b, c in zip(list1, list2, list3):
    print(a, b, c)

# zip with enumerate
for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)

# zip to dict
student = dict(zip(keys, values))

# Unzip
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(numbers)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')


### 4.9 Nested `for` Loop


for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# **Output:**

# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1


### Diagram:

# Outer loop i=0:
#     Inner loop j=0 → print
#     Inner loop j=1 → print
# Outer loop i=1:
#     Inner loop j=0 → print
#     Inner loop j=1 → print


### Industry Example — Multiplication Table:

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()


# **Output:**

#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25


### `for` Loop Ke Saath `else`:


for i in range(3):
    print(i)
else:
    print("Loop completed")


#"`else` tab chalta hai jab loop **normally** khatam ho (break se nahi)."

### Industry Example — Search with `else`:

numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print("Found")
        break
else:
    print("Not found")


# **Output:**

# Not found


### Prime Check with `for-else`:

num = 17

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime")


### Search User with `for-else`:

users = [
    {"id": 101, "name": "Rohit"},
    {"id": 102, "name": "Sagar"}
]

search_id = 103

for user in users:
    if user["id"] == search_id:
        print(f"Found: {user['name']}")
        break
else:
    print(f"User {search_id} not found")


### `for-else` Kab Use Karein:
# - Search operations
# - Validation
# - "Not found" scenarios
# - Prime check



### `for` Loop Kab Use Karein:
# - Known iterations
# - Collection iterate
# - Range ke saath
# - String characters
# - Dictionary items
# - Nested data

### `for` Loop Kab Avoid Karein:
# - Unknown iterations (`while` better)
# - User input (kitni baar nahi pata)



## TOPIC 5: `while` vs `for` — COMPARISON

# | Feature | `while` | `for` |
# |---------|---------|-------|
# | **Iterations** | Unknown | Known |
# | **Condition** | True/False | Iterable |
# | **Use Case** | User input, menu | List, range |
# | **Infinite Loop Risk** | High | Low |
# | **Readability** | Sometimes complex | Clean |
# | **Update** | Manual | Automatic |

### Example Comparison:

# **`while` (Unknown count):**

password = ""
while password != "admin123":
    password = input("Enter password: ")


# **`for` (Known count):**

for i in range(5):
    print(i)


### Decision Diagram:

# Kitni baar loop chalana hai?
#         │
#    ┌────┴────┐
#    │         │
# Pata hai   Pata nahi
#    │         │
#    ▼         ▼
#  FOR      WHILE


## TOPIC 6: `break` STATEMENT

### Definition:
# "`break` loop ko **turant** exit kar deta hai. Loop ke baaki iterations skip ho jaate hain."

### Syntax:

for item in iterable:
    if condition:
        break
    # code


### Basic Example:

for i in range(10):
    if i == 5:
        break
    print(i)


# **Output:**

# 0
# 1
# 2
# 3
# 4


### Line-by-Line:
# - `i=0` → print 0
# - `i=1` → print 1
# - ...
# - `i=5` → condition True → break → loop exit
# - `6, 7, 8, 9` → skip

### Diagram:

#    ┌──────────────────┐
#    │   for i in range │
#    └────────┬─────────┘
#             │
#    ┌────────┴────────┐
#    │   i == 5 ?      │
#    └────────┬────────┘
#         Yes │ No
#             │  │
#             ▼  ▼
#         BREAK  Continue
#             │
#             ▼
#         Exit Loop


### Industry Example — Search:

users = [
    {"id": 101, "name": "Rohit"},
    {"id": 102, "name": "Sagar"},
    {"id": 103, "name": "Priya"}
]

target_id = 102

for user in users:
    if user["id"] == target_id:
        print(f"Found: {user['name']}")
        break


# "Jab target mil gaya, to **baaki users check karne ki zaroorat nahi**."

### `while` Ke Saath `break`:

while True:
    password = input("Enter password: ")
    if password == "admin123":
        print("Login successful")
        break
    print("Wrong password, try again")


### Advanced `break` Patterns:

# Search and break
for user in users:
    if user["id"] == target_id:
        print("Found")
        break

# Find first match
for num in numbers:
    if num > 100:
        print(f"First > 100: {num}")
        break

# Validation
for field in required_fields:
    if field not in data:
        print(f"Missing: {field}")
        break

## TOPIC 7: `continue` STATEMENT

### Definition:
# "`continue` current iteration ko **skip** kar deta hai aur next iteration par chala jata hai."

### Syntax:

for item in iterable:
    if condition:
        continue
    # code (skip if condition True)


### Basic Example:

for i in range(5):
    if i == 2:
        continue
    print(i)


# **Output:**

# 0
# 1
# 3
# 4


### Line-by-Line:
# - `i=0` → print 0
# - `i=1` → print 1
# - `i=2` → condition True → continue → print skip
# - `i=3` → print 3
# - `i=4` → print 4

### Diagram:

#    ┌──────────────────┐
#    │   for i in range │
#    └────────┬─────────┘
#             │
#    ┌────────┴────────┐
#    │   i == 2 ?      │
#    └────────┬────────┘
#         Yes │ No
#             │  │
#             ▼  ▼
#       CONTINUE  Print
#             │
#             ▼
#       Next Iteration


### Industry Example — Skip Invalid:

marks = [85, -1, 90, -1, 78]

for mark in marks:
    if mark < 0:
        continue  # Invalid mark skip
    print(f"Valid mark: {mark}")


### Advanced `continue` Patterns:

# Skip None values
data = [1, None, 2, None, 3]

for item in data:
    if item is None:
        continue
    print(item)

# Skip based on condition
for user in users:
    if not user.get("is_active"):
        continue
    send_email(user)

# Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


### `break` vs `continue`:

# | Feature | `break` | `continue` |
# |---------|---------|------------|
# | **Effect** | Loop exit | Skip current iteration |
# | **Next iteration** | Nahi chalega | Chalega |
# | **Use Case** | Found, stop | Skip invalid |

### Diagram:

# break:              continue:
#    │                    │
#    ▼                    ▼
# Loop Exit          Next Iteration




## TOPIC 8: NESTED LOOPS

### Definition:
# "Jab ek loop ke andar doosra loop ho, use **nested loop** kehte hain."

### Syntax:

for i in range(3):
    for j in range(2):
        print(i, j)


### Diagram:

# Outer Loop (i)
#     │
#     ├── Inner Loop (j) → Complete
#     │
#     ├── Inner Loop (j) → Complete
#     │
#     └── Inner Loop (j) → Complete


### Industry Example — Matrix:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()


# **Output:**

# 1 2 3
# 4 5 6
# 7 8 9


### `break` in Nested Loops — 3 Methods:

# **Method 1: Flag**

found = False

for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break
    if found:
        break


# **Method 2: Function + return**

def find_target():
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                return (i, j)
    return None

result = find_target()


# **Method 3: for-else**

for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            break
    else:
        continue
    break


### Complete Exit from Nested:

found = False

for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break
    if found:
        break


## TOPIC 9: LOOP CONTROL STATEMENTS — SUMMARY

# | Statement | Effect |
# |-----------|--------|
# | `break` | Loop exit |
# | `continue` | Skip current iteration |
# | `pass` | Kuch nahi karta |
# | `else` (loop) | Normally complete hone par |

### `pass` in Loop:

for i in range(5):
    if i == 2:
        pass  # Placeholder
    print(i)


## TOPIC 10: `range()` FUNCTION

### Definition:
# "`range()` ek **sequence** generate karta hai — numbers ka. Ye mostly `for` loop ke saath use hota hai."

### Syntax:

# range(stop)
# range(start, stop)
# range(start, stop, step)


### Examples:

# 0 se 4 tak
list(range(5))         # [0, 1, 2, 3, 4]

# 1 se 4 tak
list(range(1, 5))      # [1, 2, 3, 4]

# 1 se 9 tak, step 2
list(range(1, 10, 2))  # [1, 3, 5, 7, 9]

# 10 se 1 tak, reverse
list(range(10, 0, -1)) # [10, 9, 8, ..., 1]


### Diagram:

# range(5)         → [0, 1, 2, 3, 4]
#                     ↑            ↑
#                   start       stop-1

# range(1, 5)      → [1, 2, 3, 4]

# range(1, 10, 2)  → [1, 3, 5, 7, 9]
#                     ↑  ↑  ↑  ↑  ↑
#                   step=2


### Important:
#"`range()` **stop value ko include nahi karta**. `range(5)` mein 0 se 4 tak hai, 5 nahi."



## TOPIC 11: LOOP WITH `else`

### Definition:
# "Python mein loops ke saath `else` use kar sakte hain. `else` tab chalta hai jab loop **normally complete** ho (break se nahi)."

### Example:

for i in range(5):
    print(i)
else:
    print("Loop completed")


# **Output:**

# 0
# 1
# 2
# 3
# 4
# Loop completed


### Break Ke Saath:

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")  # Ye nahi chalega


# **Output:**

# 0
# 1
# 2


# "Break hone par `else` skip ho jata hai."

### `while-else`:

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed")  # Chalega


### `while-else` with Break:

count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
else:
    print("Ye nahi chalega")  # Skip


### Retry Logic with `while-else`:

attempts = 3
while attempts > 0:
    if login():
        print("Success")
        break
    attempts -= 1
else:
    print("All attempts failed")


### Industry Example — Search:

numbers = [1, 3, 5, 7, 9]
target = 5

for num in numbers:
    if num == target:
        print("Found")
        break
else:
    print("Not found")


### Kab Use Karein:
# - Search operations
# - Validation
# - "Not found" scenarios



## TOPIC 12: `enumerate()` FUNCTION

### Definition:
# "`enumerate()` iterable ke saath **index** bhi deta hai."

### Syntax:

enumerate(iterable, start=0)
```

### Example:
```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

**Output:**
```
0: apple
1: banana
2: cherry
```

### Start Se:
```python
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")
```

**Output:**
```
1. apple
2. banana
3. cherry
```

### Industry Example — Menu:
```python
menu = ["Pizza", "Burger", "Pasta", "Sandwich"]

for i, item in enumerate(menu, start=1):
    print(f"{i}. {item}")
```

### `enumerate()` vs Manual Counter:

**Without `enumerate()`:**
```python
index = 0
for fruit in fruits:
    print(f"{index}: {fruit}")
    index += 1
```

**With `enumerate()`:**
```python
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

> "`enumerate()` **Pythonic** hai, manual counter se better."

---

## TOPIC 13: `zip()` FUNCTION

### Definition:
> "`zip()` multiple iterables ko **parallel** iterate karta hai. Har iteration mein ek-ek element sab se."

### Syntax:
```python
zip(iterable1, iterable2, ...)
```

### Diagram:
```
names:  [Rohit, Sagar, Priya]
ages:   [21,    22,    20   ]
         │       │       │
         ▼       ▼       ▼
zip:  (Rohit,21) (Sagar,22) (Priya,20)
```

### Example:
```python
names = ["Rohit", "Sagar", "Priya"]
ages = [21, 22, 20]

for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

**Output:**
```
Rohit: 21
Sagar: 22
Priya: 20
```

### Different Lengths:
```python
names = ["Rohit", "Sagar", "Priya"]
ages = [21, 22]

for name, age in zip(names, ages):
    print(f"{name}: {age}")
```

**Output:**
```
Rohit: 21
Sagar: 22
```

> "`zip()` **chhoti list** ke hisaab se ruk jata hai."

### Industry Example — Dictionary:
```python
keys = ["name", "age", "city"]
values = ["Rohit", 21, "Bhopal"]

student = dict(zip(keys, values))
print(student)
# {'name': 'Rohit', 'age': 21, 'city': 'Bhopal'}
```

---

## TOPIC 14: LOOP WITH `reversed()` AND `sorted()`

### `reversed()`:
```python
fruits = ["apple", "banana", "cherry"]

for fruit in reversed(fruits):
    print(fruit)
```

**Output:**
```
cherry
banana
apple
```

### `sorted()`:
```python
marks = [85, 90, 78, 92]

for mark in sorted(marks):
    print(mark)
```

**Output:**
```
78
85
90
92
```

### Descending:
```python
for mark in sorted(marks, reverse=True):
    print(mark)
```

---

## TOPIC 15: LIST COMPREHENSION (Loop Ka Alternative)

### Definition:
> "List comprehension ek **one-liner** hai list banane ka. Ye `for` loop ka shortcut hai."

### Normal Loop:
```python
squares = []
for x in range(5):
    squares.append(x ** 2)
```

### List Comprehension:
```python
squares = [x ** 2 for x in range(5)]
```

### Diagram:
```
Normal Loop:              List Comprehension:
┌──────────────┐          ┌──────────────────────┐
│ squares = [] │          │ squares = [x**2      │
│ for x in ... │          │           for x in.. │
│   append     │          │           ]          │
└──────────────┘          └──────────────────────┘
```

### Condition Ke Saath:
```python
evens = [x for x in range(10) if x % 2 == 0]
```

### If-Else:
```python
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
```

### Nested List Comprehension:
```python
# Matrix flatten
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6]
```

### Dictionary Comprehension:
```python
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Set Comprehension:
```python
evens = {x for x in range(10) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

### Generator Expression:
```python
gen = (x**2 for x in range(5))
print(list(gen))  # [0, 1, 4, 9, 16]
```

### Multiple Conditions:
```python
result = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(result)  # [0, 6, 12, 18]
```

### Walrus Operator in Comprehension:
```python
data = [1, 2, 3, 4, 5]
result = [y for x in data if (y := x * 2) > 5]
print(result)  # [6, 8, 10]
```

### Kab Use Karein:
- Simple transformation
- Filtering
- One-liner

### Kab Avoid Karein:
- Complex logic
- Multiple nested loops
- Readability kharab ho

---

## TOPIC 16: LOOP PERFORMANCE

### Time Complexity:

| Loop | Complexity |
|------|-----------|
| Single loop | O(n) |
| Nested loop | O(n²) |
| Triple nested | O(n³) |

### Example:
```python
# O(n)
for i in range(n):
    print(i)

# O(n²)
for i in range(n):
    for j in range(n):
        print(i, j)
```

### Optimization Tips:
1. **Break early** — jab kaam ho jaye
2. **Continue** — skip invalid
3. **Local variables** — global se fast
4. **List comprehension** — loop se fast
5. **Built-in functions** — `sum()`, `max()` fast
6. **Generator** — memory efficient

### Performance Examples:
```python
# Local variable fast
def process():
    local_range = range(1000000)
    for i in local_range:
        pass

# Built-in fast
total = sum(range(1000000))

# List comprehension fast
squares = [x**2 for x in range(1000)]

# Generator memory efficient
squares = (x**2 for x in range(1000000))
```

---

## TOPIC 17: `for` vs `while` — KAB KYA

### Decision Guide:

| Situation | Use |
|-----------|-----|
| List iterate | `for` |
| Range iterate | `for` |
| String characters | `for` |
| Dictionary items | `for` |
| Known iterations | `for` |
| User input | `while` |
| Menu system | `while` |
| Game loop | `while` |
| Retry logic | `while` |
| Unknown iterations | `while` |

### Industry Examples:

**`for` — Data Processing:**
```python
users = [{"name": "Rohit"}, {"name": "Sagar"}]
for user in users:
    process(user)
```

**`while` — Server:**
```python
while server_running:
    request = get_request()
    handle(request)
```

---

## TOPIC 18: INFINITE LOOP PATTERNS (Industry)

### Pattern 1: Server
```python
while True:
    request = get_request()
    if not request:
        break
    handle(request)
```

### Pattern 2: Menu
```python
while True:
    choice = input("Choice: ")
    if choice == "exit":
        break
    process(choice)
```

### Pattern 3: Retry
```python
while True:
    try:
        result = risky_operation()
        break
    except Exception:
        print("Retrying...")
```

### Pattern 4: Game Loop
```python
while game_running:
    handle_events()
    update()
    render()
```

---

## TOPIC 19: LOOP WITH `try-except` (Error Handling)

### Definition:
> "Loops ke saath error handling zaroori hai. Agar ek element pe error aaya, to loop crash nahi hona chahiye."

### Example:
```python
numbers = [10, 20, "abc", 40]

for num in numbers:
    try:
        print(10 / num)
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error: {e}")
        continue
```

**Output:**
```
1.0
0.5
Error: unsupported operand type(s) for /: 'int' and 'str'
0.25
```

### Industry Example — API Calls:
```python
users = [101, 102, 103, 104]

for user_id in users:
    try:
        user = fetch_user(user_id)
        print(user["name"])
    except Exception as e:
        print(f"Failed to fetch user {user_id}: {e}")
        continue
```

### Retry Logic:
```python
max_retries = 3

for attempt in range(max_retries):
    try:
        result = risky_operation()
        break
    except Exception as e:
        print(f"Attempt {attempt + 1} failed: {e}")
else:
    print("All attempts failed")
```

---

## TOPIC 20: `itertools` MODULE (Advanced Loops)

### Definition:
> "`itertools` module advanced iteration tools provide karta hai."

### `chain()` — Multiple Iterables:
```python
import itertools

for item in itertools.chain([1, 2], [3, 4]):
    print(item)
# 1, 2, 3, 4
```

### `product()` — Cartesian Product:
```python
for pair in itertools.product([1, 2], ['a', 'b']):
    print(pair)
# (1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')
```

### `combinations()`:
```python
for combo in itertools.combinations([1, 2, 3], 2):
    print(combo)
# (1, 2), (1, 3), (2, 3)
```

### `permutations()`:
```python
for perm in itertools.permutations([1, 2, 3], 2):
    print(perm)
# (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)
```

### `cycle()`:
```python
count = 0
for item in itertools.cycle([1, 2, 3]):
    if count > 5:
        break
    print(item)
    count += 1
```

### `repeat()`:
```python
for item in itertools.repeat("Hello", 3):
    print(item)
# Hello, Hello, Hello
```

---

## TOPIC 21: LOOP WITH NESTED DATA

### List of Dicts:
```python
users = [
    {"name": "Rohit", "age": 21},
    {"name": "Sagar", "age": 22}
]

for user in users:
    for key, value in user.items():
        print(f"{key}: {value}")
```

### Dict of Lists:
```python
data = {
    "fruits": ["apple", "banana"],
    "veggies": ["carrot", "radish"]
}

for category, items in data.items():
    print(f"{category}:")
    for item in items:
        print(f"  - {item}")
```

### Nested List:
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

for row in matrix:
    for num in row:
        print(num, end=" ")
    print()
```

---

# 🌍 PART 2: REAL-WORLD USE CASES

### 1. Print Multiplication Table
```python
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
```

### 2. Sum of Numbers
```python
total = 0
for i in range(1, 101):
    total += i
print(total)  # 5050
```

### 3. Factorial
```python
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(fact)  # 120
```

### 4. Fibonacci Series
```python
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

### 5. Prime Check
```python
num = 17
is_prime = True

for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
        is_prime = False
        break

print("Prime" if is_prime else "Not Prime")
```

### 6. Pattern Printing
```python
# Triangle
for i in range(1, 6):
    print("*" * i)

# Output:
# *
# **
# ***
# ****
# *****
```

### 7. User Login (Retry)
```python
attempts = 3
while attempts > 0:
    password = input("Enter password: ")
    if password == "admin123":
        print("Login successful")
        break
    attempts -= 1
    print(f"Wrong! {attempts} attempts left")
else:
    print("Account locked")
```

### 8. Menu System
```python
while True:
    print("\n1. Add\n2. View\n3. Exit")
    choice = input("Choice: ")

    if choice == "1":
        print("Added")
    elif choice == "2":
        print("Viewed")
    elif choice == "3":
        break
```

### 9. Find Max in List
```python
numbers = [45, 78, 23, 90, 12]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print(max_num)  # 90
```

### 10. Count Vowels
```python
text = "Hello World"
count = 0

for char in text.lower():
    if char in "aeiou":
        count += 1

print(count)  # 3
```

### 11. Remove Duplicates
```python
numbers = [1, 2, 2, 3, 3, 4]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)  # [1, 2, 3, 4]
```

### 12. Nested Loop — Matrix Addition
```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = []

for i in range(len(A)):
    row = []
    for j in range(len(A[i])):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print(C)  # [[6, 8], [10, 12]]
```

---

# ⚠️ PART 3: COMMON MISTAKES

### Mistake 1: Infinite `while` Loop
```python
# ❌ Count update nahi
count = 1
while count <= 5:
    print(count)

# ✅
count = 1
while count <= 5:
    print(count)
    count += 1
```

### Mistake 2: `range()` Off-by-One
```python
# ❌ 0-9 chahiye tha
for i in range(1, 10):
    pass

# ✅
for i in range(10):
    pass
```

### Mistake 3: Loop Variable Modify
```python
# ❌ Loop ke andar modify
for i in range(5):
    i = i * 2  # Ye next iteration pe reset ho jayega

# ✅
for i in range(5):
    print(i * 2)
```

### Mistake 4: `break` in Nested — Sirf Inner
```python
# ❌ Sirf inner break
for i in range(3):
    for j in range(3):
        if i == 1:
            break  # Sirf inner

# ✅ Flag use karo
found = False
for i in range(3):
    for j in range(3):
        if i == 1:
            found = True
            break
    if found:
        break
```

### Mistake 5: Modify List While Iterating
```python
# ❌ RuntimeError
numbers = [1, 2, 3]
for num in numbers:
    numbers.remove(num)

# ✅ Copy banao
for num in numbers[:]:
    numbers.remove(num)
```

### Mistake 6: `else` Confusion
```python
# ❌ else kabhi nahi chalega
for i in range(5):
    if i == 2:
        break
else:
    print("Done")  # Break hua, else skip

# ✅
for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("Done")  # Ye nahi chalega
```

### Mistake 7: `continue` Before Increment
```python
# ❌ Infinite loop
count = 0
while count < 5:
    if count == 2:
        continue  # count increment skip!
    count += 1

# ✅
count = 0
while count < 5:
    count += 1
    if count == 2:
        continue
```

### Mistake 8: Expensive Operations Inside Loop
```python
# ❌ Har iteration pe expensive
for i in range(1000):
    result = expensive_function()

# ✅ Loop ke bahar
result = expensive_function()
for i in range(1000):
    use(result)
```

### Mistake 9: `range()` with Float
```python
# ❌ TypeError
for i in range(0, 1, 0.1):
    pass

# ✅
import numpy as np
for i in np.arange(0, 1, 0.1):
    pass
```

### Mistake 10: Wrong Loop Choice
```python
# ❌ for loop for user input
for i in range(100):
    password = input("Password: ")
    if password == "admin":
        break

# ✅ while loop
while True:
    password = input("Password: ")
    if password == "admin":
        break
```

---

# 🎤 PART 4: INTERVIEW QUESTIONS

### Q1: `for` aur `while` mein difference?
> "`for` known iterations ke liye, `while` unknown iterations ke liye."

### Q2: `break` aur `continue` mein difference?
> "`break` loop exit, `continue` current iteration skip."

### Q3: Infinite loop kaise banate hain?
> "`while True:` se. Exit ke liye `break` use karo."

### Q4: `range()` kya karta hai?
> "Numbers ka sequence generate karta hai."

### Q5: `range(5)` mein 5 include hota hai?
> "Nahi. `range(5)` → 0, 1, 2, 3, 4. Stop exclusive hai."

### Q6: Loop ke saath `else` kab chalta hai?
> "Jab loop normally complete ho (break se nahi)."

### Q7: `enumerate()` kya karta hai?
> "Iterable ke saath index deta hai."

### Q8: `zip()` kya karta hai?
> "Multiple iterables ko parallel iterate karta hai."

### Q9: Nested loop mein `break` kya karta hai?
> "Sirf inner loop se bahar nikalta hai. Outer continue."

### Q10: Loop mein list modify kar sakte hain?
> "Nahi, RuntimeError aayega. Copy banao."

### Q11: `pass` loop mein kya karta hai?
> "Kuch nahi. Placeholder."

### Q12: `for` loop mein `range()` ke bina?
> "Iterable chahiye — list, tuple, string, dict, set."

### Q13: `while` loop mein update zaroori kyu?
> "Warna infinite loop."

### Q14: Loop performance kaise improve karein?
> "Break early, local variables, list comprehension, built-in functions."

### Q15: `for _ in range(5)` mein `_` kya hai?
> "Convention — loop variable use nahi ho raha."

### Q16: List comprehension vs `for` loop?
> "Comprehension fast aur short. Complex logic ke liye `for` better."

### Q17: `reversed()` kya karta hai?
> "Iterable ko reverse order mein deta hai."

### Q18: `sorted()` loop mein?
> "Sorted list return karta hai, loop us par chalta hai."

### Q19: `while` loop kab use karein?
> "User input, menu, game loop, retry logic."

### Q20: `for` loop kab avoid karein?
> "Jab iterations unknown ho — `while` better."

### Q21: `break` ke baad `else` chalta hai?
> "Nahi. Break se loop abnormally exit, else skip."

### Q22: Loop variable scope?
> "Python mein loop variable loop ke bahar bhi accessible hai."

### Q23: `for` loop mein `continue` ke baad?
> "Next iteration pe jata hai. Code skip."

### Q24: `while` loop mein `continue`?
> "Condition check pe wapas. Update miss mat karo."

### Q25: Nested loop complexity?
> "O(n²) for double, O(n³) for triple."

### Q26: `itertools` kya hai?
> "Advanced iteration tools ka module."

### Q27: `itertools.chain()` kya karta hai?
> "Multiple iterables ko ek mein combine karta hai."

### Q28: `itertools.product()` kya karta hai?
> "Cartesian product deta hai."

### Q29: Loop mein error handling kaise?
> "`try-except` use karo, `continue` se skip karo."

### Q30: Generator expression vs list comprehension?
> "Generator lazy hai, memory efficient. List turant banati hai."

---

# 📝 PART 5: PRACTICE QUESTIONS

### Beginner:
1. 1 se 10 tak print karo (`for`).
2. 10 se 1 tak print karo (`while`).
3. Even numbers 1-20 print karo.
4. Sum 1-100 calculate karo.
5. Multiplication table (5 ka).
6. Factorial calculate karo.
7. String ke characters print karo.
8. List ke elements print karo.
9. Countdown timer banao.
10. 5 baar "Hello" print karo.

### Intermediate:
11. Prime numbers 1-50.
12. Fibonacci series (10 terms).
13. Pattern printing (triangle, pyramid).
14. Reverse a number.
15. Palindrome check.
16. Find max/min in list.
17. Count vowels in string.
18. Remove duplicates from list.
19. Nested loop — matrix print.
20. Menu-driven calculator.
21. List comprehension se squares.
22. Dict comprehension se squares.
23. Set comprehension se evens.
24. Generator expression se squares.
25. `enumerate()` se menu print.

### Advanced:
26. User login with 3 attempts.
27. ATM simulation.
28. Number guessing game.
29. Shopping cart with menu.
30. Bubble sort implement karo.
31. Binary search implement karo.
32. Prime factorization.
33. Armstrong number check.
34. Pyramid patterns.
35. Student grade calculator with loops.
36. `itertools.chain()` se multiple lists.
37. `itertools.product()` se combinations.
38. Loop with `try-except` — API calls.
39. Nested list comprehension — matrix flatten.
40. Generator expression — memory efficient.

---

# ✅ PART 6: SUMMARY

| Topic | Key Point |
|-------|-----------|
| **Loop** | Repeated execution |
| **`while`** | Condition-based, unknown count |
| **`for`** | Iterable-based, known count |
| **`range()`** | Number sequence |
| **`break`** | Loop exit |
| **`continue`** | Skip iteration |
| **`pass`** | Placeholder |
| **`else`** | Normally complete hone par |
| **Nested** | Loop ke andar loop |
| **`enumerate()`** | Index + value |
| **`zip()`** | Parallel iteration |
| **Comprehension** | One-liner loop |
| **`itertools`** | Advanced iteration |
| **`try-except`** | Error handling |

---

# 🎬 CLOSING (Bolne Ke Liye)

> "Toh doston, ye tha Python Loops ka **complete masterclass** — zero se advanced tak. Humne cover kiya: `while` loop, `for` loop, `range()`, `break`, `continue`, nested loops, `enumerate()`, `zip()`, list comprehension, dictionary comprehension, set comprehension, generator expression, `itertools` module, error handling, infinite loop patterns, aur bahut kuch. Saath mein real-world use cases, common mistakes, interview questions, aur practice questions bhi. Agar aapko ye video helpful laga, to **like, share, aur subscribe** karna mat bhoolna. Milte hain next video mein. **Dhanyavaad!**"

---

# 📋 LECTURE RECORDING CHECKLIST

- [ ] Intro — Loop kya hai
- [ ] Loop ke types
- [ ] `while` loop
- [ ] `while` — infinite loop warning
- [ ] `for` loop
- [ ] `for` with `range()`
- [ ] `for` with string, list, tuple, dict, set
- [ ] `for` with `enumerate()`
- [ ] `for` with `zip()`
- [ ] Nested `for`
- [ ] `for` vs `while` comparison
- [ ] `break` statement
- [ ] `continue` statement
- [ ] `break` vs `continue`
- [ ] Nested loops — 3 break methods
- [ ] Loop with `else` (for & while)
- [ ] `range()` function
- [ ] `enumerate()` function
- [ ] `zip()` function
- [ ] `reversed()` and `sorted()`
- [ ] List comprehension (basic + advanced)
- [ ] Dict comprehension
- [ ] Set comprehension
- [ ] Generator expression
- [ ] Loop performance
- [ ] Infinite loop patterns
- [ ] Loop with `try-except`
- [ ] `itertools` module
- [ ] Loop with nested data
- [ ] Real-world use cases (12)
- [ ] Common mistakes (10)
- [ ] Interview questions (30)
- [ ] Practice questions (40)
- [ ] Summary
- [ ] Closing



