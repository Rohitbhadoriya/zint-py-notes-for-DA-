#  PART 1: FOUNDATION
## TOPIC 1: DICTIONARY KYA HAI?

### Definition:
#  "Dictionary Python ka ek **built-in data type** hai jo **key-value pairs** ka **ordered** (Python 3.7+) collection hota hai. Har key **unique** hoti hai, aur har key ka ek **value** hota hai. Dictionary **mutable** hai, matlab aap ise change kar sakte hain."

### Simple Real-Life Analogy:
# "Socho aapki **phone book** hai. Naam = Key, Number = Value. Ya **student roll number** — Roll No = Key, Student Name = Value. Ya **Aadhaar card** — Aadhaar Number = Key, Details = Value."

### Problem Without Dictionary:

#  List approach - confusing
student = ["Rohit", 21, "Bhopal"]
print(student[1])  # 21 — par ye kya hai? Age? Marks? Pata nahi!


### With Dictionary:

student = {
    "name": "Rohit",
    "age": 21,
    "city": "Bhopal"
}
print(student["age"])  # 21 — clear!


### Kyu Exist Karti Hai:"Jab data ke har element ka ek **meaningful label** ho, tab dictionary use karte hain. List mein index yaad rakhna padta hai, dictionary mein key se direct access."

## TOPIC 2: KEY AUR VALUE KYA HOTI HAI?

### Definition:"**Key** = Label (naam), **Value** = Content (data). Har key unique hoti hai, value kuch bhi ho sakti hai."

### Diagram:

# KEY (Label)          →    VALUE (Content)
# ────────────────────────────────────
# "Sugar"              →    "1 kg white sugar"
# "Salt"               →    "500 gm pink salt"
# "Tea"                →    "Assam tea leaves"


### Example:

kitchen = {
    "Sugar": "1 kg white sugar",
    "Salt": "500 gm pink salt",
    "Tea": "Assam tea leaves"
}

sugar_content = kitchen["Sugar"]
print(sugar_content)  # 1 kg white sugar


### Important Rules:
# Key **hashable** honi chahiye (immutable)
# Value **kuch bhi** ho sakti hai
# Key **unique** hoti hai
# Value **duplicate** ho sakti hai



## TOPIC 3: LIST VS DICTIONARY (COMPARISON)

### List Approach:

student = ["Rohit", 21, "Bhopal"]
print(student[0])  # Rohit
print(student[1])  # 21


#Problem: `student[1]` — bachche ko yaad rakhna padega ki index 1 par age hai.

### Dictionary Approach:

student = {
    "name": "Rohit",
    "age": 21,
    "city": "Bhopal"
}
print(student["age"])  # 21 — self-explanatory!


### Comparison Table:

# | Feature | List | Dictionary |
# |---------|------|------------|
# | **Structure** | Ordered collection | Key-value pairs |
# | **Access** | Index se (`list[0]`) | Key se (`dict["name"]`) |
# | **Search** | O(n) — slow | O(1) — fast |
# | **Duplicates** | Allowed | Keys unique |
# | **Meaningful** | Nahi | Haan |
# | **Memory** | Kam | Zyada (hash table overhead) |
# | **Use Case** | Ordered data | Key-value mapping |

### Real-World Connection:

# API response
user = {
    "id": 101,
    "name": "Rohit",
    "email": "rohit@example.com",
    "is_active": True
}

print(user["email"])  # rohit@example.com

# **Main Point:** Dictionary tab use hoti hai jab data ke har element ka ek **meaningful label** ho.



## TOPIC 4: DICTIONARY KYU USE KARTE HAIN?

### Reason 1: Key-Value Mapping
# "Jab data ko **naam se access** karna ho."

### Reason 2: Fast Search (O(1))
# "List mein search O(n), dictionary mein O(1)."

### Reason 3: Meaningful Data
#"List mein `[21, 'Rohit']` — kaunsa kya? Dictionary mein `{'age': 21, 'name': 'Rohit'}` — clear."

### Reason 4: Flexible Data Structure
# "Nested data rakh sakte ho — list, dict, tuple sab kuch."

### Reason 5: Real-World Data (JSON/API)
#"API responses, config files — sab dictionary format mein."

### Industry Example:

# Zomato order
order = {
    "order_id": "ZOM123",
    "customer": "Rohit",
    "items": ["Pizza", "Garlic Bread"],
    "total": 450,
    "status": "Delivered"
}
print(order["status"])  # Delivered


## TOPIC 5: REAL-WORLD EXAMPLES (PROBLEM → SOLUTION)

### Example 1: Student Record
# **Problem:** Student ka data store karna hai.
# **Dictionary Kyu:** Har field ka label ho.

student = {
    "name": "Rohit",
    "roll_no": 101,
    "marks": {"math": 95, "science": 88}
}
print(student["marks"]["math"])  # 95


### Example 2: Phone Book
# **Problem:** Naam se number dhundhna hai.
# **Dictionary Kyu:** Naam = key, number = value.

phone_book = {
    "Rohit": "9876543210",
    "Sagar": "9876543211"
}
print(phone_book.get("Rohit"))  # 9876543210


### Example 3: Word Frequency
# **Problem:** Text mein har word kitni baar aaya.
# **Dictionary Kyu:** Word = key, frequency = value.

text = "hello world hello python world"
frequency = {}
for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)  # {'hello': 2, 'world': 2, 'python': 1}


### Example 4: Config Management
# **Problem:** App settings store karni hain.
# **Dictionary Kyu:** Setting name = key, value = value.

config = {
    "database": {"host": "localhost", "port": 5432},
    "api": {"key": "abc123", "timeout": 30}
}
print(config["database"]["host"])  # localhost


## TOPIC 6: DICTIONARY KI PROPERTIES

# | Property | Explanation |
# |----------|-------------|
# | **Key-Value Pairs** | Har element key-value pair |
# | **Unique Keys** | Duplicate keys allowed nahi |
# | **Mutable** | Add/Update/Remove possible |
# | **Ordered (3.7+)** | Insertion order preserve |
# | **No Indexing** | `d[0]` se access nahi |
# | **Hashable Keys** | Sirf immutable keys |
# | **Any Type Values** | Values kuch bhi |

### Ordered Carefully Explain:
#"Python 3.7+ mein dictionary **insertion order preserve** karti hai. Matlab jis order mein keys insert hoti hain, iteration mein wahi order milta hai."


data = {}
data["name"] = "Rohit"
data["age"] = 21
data["city"] = "Bhopal"
print(data)
# {'name': 'Rohit', 'age': 21, 'city': 'Bhopal'}


###  Important Clarification:
# Dictionary **index-based collection nahi hai**
# Order preserve hone ka matlab ye nahi ki `d[0]` valid hai
# Order aur indexing alag concepts hain

print(data[0])  #  KeyError


## TOPIC 7: DICTIONARY CREATE KARNA

### Beginner Methods:

# **1. Direct Creation:**

student = {
    "name": "Rohit",
    "age": 21
}


# **2. Empty Dictionary:**

student = {}
student["name"] = "Rohit"


# **3. `dict()` Constructor:**

student = dict(name="Rohit", age=21)


### Intermediate Methods:

# **4. List of Tuples:**

student = dict([("name", "Rohit"), ("age", 21)])


# **5. `zip()` Se:**

keys = ["name", "age"]
values = ["Rohit", 21]
student = dict(zip(keys, values))


### Advanced/Utility:

# **6. `fromkeys()`:**

keys = ["name", "age"]
student = dict.fromkeys(keys, "Unknown")


### Kyu Beginner Mein Sirf 3 Methods:
#"Pehle normal use seekho. Data transformation baad mein."


## TOPIC 8: EMPTY DICTIONARY


empty = {}
print(empty)        # {}
print(type(empty))  # <class 'dict'>
print(len(empty))   # 0


### Important Comparison:

empty = {}       #  Dictionary
empty = set()    # Set
# Dono alag hain!


### Boolean Truthiness:

data = {}
if not data:
    print("Dictionary empty hai")


## TOPIC 9: DUPLICATE KEYS KA BEHAVIOR


student = {"name": "Rohit", "name": "Sagar"}
print(student)  # {'name': 'Sagar'}  ← Last value wins!


#"Duplicate keys allowed nahi. Same key dobara likho, **last value** rakh leta hai."

### Industry Warning:

#  BUG
config = {
    "host": "localhost",
    "host": "production.com"  # Pehla lost!
}


## TOPIC 10: VALID AUR INVALID KEYS

### Allowed (Hashable):

d = {1: "int"}           # 
d = {"name": "str"}      # 
d = {(1, 2): "tuple"}    # 
d = {True: "bool"}       # 
d = {frozenset({1, 2}): "frozenset"}  # 
d = {None: "None"}       # 


### Disallowed (Unhashable):

d = {[1, 2]: "list"}     #  TypeError
d = {{1, 2}: "set"}      #  TypeError
d = {{"a": 1}: "dict"}   #  TypeError


### Tuple Limitation:

d = {(1, 2): "valid"}       # 
d = {(1, [2]): "invalid"}   #  (tuple ke andar list)


### Boolean Aur Integer Collision:

d = {True: "boolean", 1: "integer"}
print(d)  # {True: 'integer'}  ← True == 1


# 📖 PART 2: BASIC OPERATIONS



## TOPIC 11: VALUE ACCESS USING `[]`

### Definition:
#"Square brackets `[]` se key ki value access karte hain."

### Basic Example:

student = {"name": "Adarsh", "age": 20}
print(student["name"])  # Adarsh


### Missing Key Aur KeyError:

print(student["phone"])  # ❌ KeyError: 'phone'


### Kyu Dangerous:
#"Production code mein crash kar sakta hai. Isliye `get()` use karo."

### When To Use `[]`:
# - Jab aap **sure** ho ki key exist karti hai
# - Performance critical ho (`[]` slightly faster)
# - Constants/config ke liye

### When NOT To Use:
# - User input, API data (key missing ho sakti hai)
# - Production code
# - Graceful handling chahiye



## TOPIC 12: `.get()` — SAFE ACCESS

### Definition:
#"`get(key, default=None)` method value return karta hai agar key exist karti hai, warna default value (None agar specify nahi kiya). **Kabhi KeyError nahi deta.**"

### Kyu Exist Karta Hai:
"Real applications mein data incomplete ho sakta hai — user ne phone nahi diya, API mein email missing, product mein discount field nahi. `get()` in cases mein safe hai."

### Kab Use Karna Hai:
# - Jab key missing ho sakti hai
# - Default value chahiye
# - Production code

### Syntax:

d.get(key, default)


### Basic Example:

student = {"name": "Unnati", "age": 17}

print(student.get("city"))            # None
print(student.get("city", "Unknown")) # Unknown


### Safe Nested Access (Chained `.get()`):

user_data = {
    "id": 101,
    "address": {"city": "London"}
}

city = user_data.get("address", {}).get("city")
print(city)  # London

# Missing address
city = user_data.get("address1", {}).get("city", "N/A")
print(city)  # N/A


### Return Value:
# - Value (agar key exist)
# - Default (agar key missing)

### Common Mistake:

#  Ye hamesha default return karega
student.get("city", "Unknown")  # Chained .get() ke bina




## TOPIC 13: NEW KEY ADD KARNA


student = {"name": "Deeksha", "age": 25}
student["city"] = "Gwalior"
print(student)  # {'name': 'Deeksha', 'age': 25, 'city': 'Gwalior'}


#"Agar key exist nahi karti, to `[]` se **nayi key add** ho jaati hai."



## TOPIC 14: EXISTING VALUE UPDATE KARNA


student = {"name": "Deeksha", "age": 25}
student["age"] = 26
print(student)  # {'name': 'Deeksha', 'age': 26}


"Agar key exist karti hai, to `[]` se **value update** ho jaati hai."



## TOPIC 15: `len()` — LENGTH


student = {"name": "Deeksha", "age": 25, "city": "Gwalior"}
print(len(student))  # 3


#"Total key-value pairs count karta hai."



## TOPIC 16: `in` AND `not in` — MEMBERSHIP

### Definition:
#"`in` operator check karta hai ki key dictionary mein hai ya nahi."

### Important:

student = {"name": "Rohit", "age": 21}

print("name" in student)      # True (key check)
print("Rohit" in student)     # False (value check nahi hota)
print("city" not in student)  # True


### Values Check Karne Ke Liye:

print("Rohit" in student.values())  # True


### Key-Value Pair Check:

print(("name", "Rohit") in student.items())  # True


## TOPIC 17: `del` KEYWORD

### Definition:
#"`del` Python ka **keyword/statement** hai, method nahi. Specific key remove karta hai."


student = {"name": "Rohit", "age": 21}
del student["age"]
print(student)  # {'name': 'Rohit'}


### Difference From `pop()`:

student.pop("age")  # removed value return karega
del student["age"]  # kuch return nahi karta


### Poora Dictionary Delete:

del student
# print(student)  #  NameError




## TOPIC 18: `pop()` — KEY REMOVE

### Definition:
#"Specific key remove karta hai aur uski value return karta hai."

### Kab Use Karein:
#"Jab specific key hatani ho aur value bhi chahiye."


cart = {"laptop": 1, "mouse": 2}
removed_qty = cart.pop("mouse")
print(removed_qty)  # 2
print(cart)         # {'laptop': 1}


### Safe Removal:

cart.pop("monitor", "Not Found")  # ✅ No error


### Return Value:
# - Removed value
# - Default (agar diya)



## TOPIC 19: `clear()` — POORA EMPTY


session = {"user_id": 101, "token": "abc"}
session.clear()
print(session)  # {}


### Kab Use Karein:
#"Logout ke time temporary session data clear karne ke liye."

### Return Value: `None`



## TOPIC 20: `pop()` vs `popitem()` vs `del` vs `clear()` — COMPARISON

# | Method | Kya karta hai | Value return? | Missing key par |
# |--------|--------------|--------------:|-----------------|
# | `pop(key)` | Specific key remove | Haan | `KeyError` |
# | `pop(key, default)` | Specific key remove | Haan | Default |
# | `popitem()` | Last inserted pair remove | Haan, tuple | `KeyError` (empty) |
# | `del d[key]` | Specific key remove | Nahi | `KeyError` |
# | `clear()` | Sabhi items remove | Nahi | Error nahi |

### Real-World Examples:

# **`pop()` — Cart se item remove:**

cart = {"laptop": 1, "mouse": 2}
removed_quantity = cart.pop("mouse")


# **`popitem()` — Last task remove (LIFO):**

tasks = {"task1": "HTML", "task2": "CSS", "task3": "JS"}
last_task = tasks.popitem()  # ('task3', 'JS')


# **`clear()` — Logout:**

session = {"user_id": 101, "token": "abc"}
session.clear()


#  PART 3: DICTIONARY METHODS


## TOPIC 21: `keys()` — SAARI KEYS

### Definition:
#"Dictionary ki keys ka **dynamic view** return karta hai."

### Kyu:
#"Jab sirf field names ya available attributes check karne hon."

### Syntax:

d.keys()


### Example:

student = {"name": "Rohit", "age": 21}
print(student.keys())  # dict_keys(['name', 'age'])
print(list(student.keys()))  # ['name', 'age']


### Real Case:

user = {"name": "Rohit", "email": "rohit@example.com"}
if "email" in user:
    print("Email available hai")


### Return Value: `dict_keys` view (dynamic)

### Common Mistake:

#  Ye list nahi hai
keys = student.keys()
keys[0]  # TypeError
#  List chahiye to convert karo
list(student.keys())[0]


## TOPIC 22: `values()` — SAARI VALUES

### Definition:
#"Dictionary ki values ka **dynamic view** return karta hai."

### Kyu:
#"Jab humein sirf values par kaam karna ho."

### Example:

marks = {"math": 90, "science": 85, "english": 92}
total = sum(marks.values())
print(total)  # 267


### Return Value: `dict_values` view



## TOPIC 23: `items()` — KEY-VALUE PAIRS

### Definition:
#"Key-value pairs ka **dynamic view** return karta hai. Iteration mein har item `(key, value)` tuple ke form mein milta hai."

### Kyu:
#"Jab key aur value dono ek saath chahiye."

### Example:

prices = {"laptop": 50000, "mouse": 1000, "keyboard": 2000}

for product, price in prices.items():
    print(product, price)


### Real Case — Invoice:

invoice = {"Laptop": 50000, "Mouse": 500}
for item, price in invoice.items():
    print(f"{item}: ₹{price}")


### Return Value: `dict_items` view

###  Important Correction:
#"`items()` **list of tuples return nahi karta**. Ye `dict_items` **view object** return karta hai."



## TOPIC 24: `update()` — DICTIONARY UPDATE

### Definition:
#"Dictionary mein multiple key-value pairs add ya existing keys ki values modify karta hai."

### Kyu Use Karein:
#"Jab ek-ek key manually update karne ke bajaye multiple changes ek saath karne hon."

### Kab Use Karein:
# - Profile update
# - Config merge
# - Bulk data update

### Without `update()`:

student["city"] = "Bhopal"
student["age"] = 22
student["course"] = "Python"


### With `update()`:

student.update({
    "city": "Bhopal",
    "age": 22,
    "course": "Python"
})


### Real-World Example — Profile Update:

user = {"name": "Rohit", "email": "rohit@example.com", "city": "Indore"}
new_data = {"city": "Bhopal", "age": 29}
user.update(new_data)
print(user)


### Important:
# - Existing key ki value replace
# - New key add
# - Original modify
# - Return value `None`

### Return Value: `None`



## TOPIC 25: `popitem()` — LAST ITEM REMOVE

### Definition:
#"Last inserted key-value pair remove karta hai aur tuple return karta hai."


student = {"name": "Rohit", "age": 21, "city": "Bhopal"}
item = student.popitem()
print(item)     # ('city', 'Bhopal')
print(student)  # {'name': 'Rohit', 'age': 21}


### Empty Dictionary:

d = {}
d.popitem()  #  KeyError


### Return Value: Tuple `(key, value)`



## TOPIC 26: `copy()` — SHALLOW COPY

### Definition:
# "Shallow copy **outer dictionary ki nayi copy** banati hai, lekin **nested mutable objects** ko independently copy nahi karti."

### Normal Copy:

original = {"name": "Rohit", "age": 21}
backup = original.copy()
backup["age"] = 22
print(original)  # age 21
print(backup)    # age 22


### Shallow Copy Ka Actual Meaning:

original = {
    "name": "Rohit",
    "skills": ["Python", "SQL"]
}

backup = original.copy()
backup["skills"].append("Django")

print(original)  # skills: ['Python', 'SQL', 'Django']
print(backup)    # skills: ['Python', 'SQL', 'Django']


# "Dono mein Django aa gaya, kyunki nested list **same object** hai."

### Deep Copy:

import copy
backup = copy.deepcopy(original)


### Kab Kya Use Karein:

# | Situation | Use |
# |-----------|-----|
# | Simple flat dictionary | `d.copy()` |
# | Nested mutable data independent | `copy.deepcopy()` |
# | Sirf same reference | `d2 = d1` |



## TOPIC 27: `setdefault()` — DEFAULT VALUE KE SAATH

### Definition:
#"Kisi key ki existing value return karta hai. Agar key missing ho, to default value ke saath key create karta hai aur wahi default return karta hai."

### Kyu Exist Karta Hai:
#"Grouping aur default initialization ke liye."

### Basic Example:

student = {"name": "Rohit"}
age = student.setdefault("age", 21)
print(age)      # 21
print(student)  # {'name': 'Rohit', 'age': 21}


### Existing Key Ka Behavior:

student = {"age": 25}
result = student.setdefault("age", 21)
print(result)   # 25 (default ignore)


### Real-World Use Case — Grouping:

students = [
    {"name": "Rohit", "grade": "A"},
    {"name": "Sagar", "grade": "B"},
    {"name": "Priya", "grade": "A"}
]

grouped = {}
for student in students:
    grade = student["grade"]
    grouped.setdefault(grade, []).append(student["name"])

print(grouped)
# {'A': ['Rohit', 'Priya'], 'B': ['Sagar']}


### Important Teaching Point:

grouped.setdefault(grade, [])

# - Grade nahi hai → empty list create
# - Grade already hai → existing list mile
# - Phir `.append()` naam add karega

### Return Value: Value (existing ya new)



## TOPIC 28: `fromkeys()` — KEYS SE DICTIONARY

### Definition:
# "Ek nayi dictionary banata hai jisme diye gaye iterable ke elements keys ban jaate hain aur sabhi keys ko **same default value** milti hai."

### Kyu Use Karte Hain:
# "Jab pehle se keys ka structure pata ho, lekin values abhi available nahi."

### Kab Use Karein:
# - Form fields initialize
# - Config keys ka basic structure
# - Temporary placeholders

### Real Example — Student Form:

fields = ["name", "email", "phone"]
student = dict.fromkeys(fields)
print(student)
# {'name': None, 'email': None, 'phone': None}


### Without Default Value:

keys = ['a', 'b', 'c']
emp_dict = dict.fromkeys(keys)
print(emp_dict)  # {'a': None, 'b': None, 'c': None}


### From String:

result = dict.fromkeys("ABC", 0)
print(result)  # {'A': 0, 'B': 0, 'C': 0}


### ⚠️ Mutable Default Trap:

# ❌ BUG: Same list reference
bad = dict.fromkeys(["a", "b", "c"], [])
bad["a"].append(1)
print(bad)  # {'a': [1], 'b': [1], 'c': [1]}

# ✅ Solution
good = {key: [] for key in ["a", "b", "c"]}
good["a"].append(1)
print(good)  # {'a': [1], 'b': [], 'c': []}


### Return Value: New dictionary



# 📖 PART 4: LOOPS AND DATA HANDLING



## TOPIC 29: DICTIONARY ITERATION


student = {"name": "Rohit", "age": 21, "city": "Bhopal"}

for key in student:
    print(key)
# name
# age
# city


# "Python 3.7+ mein iteration **insertion order** mein hota hai."



## TOPIC 30: KEYS PRINT KARNA


for key in student.keys():
    print(key)


## TOPIC 31: VALUES PRINT KARNA


for value in student.values():
    print(value)


## TOPIC 32: KEY-VALUE PAIRS PRINT KARNA


for item in student.items():
    print(item)
# ('name', 'Rohit')
# ('age', 21)
# ('city', 'Bhopal')


## TOPIC 33: `items()` KE SAATH UNPACKING


for key, value in student.items():
    print(f"{key}: {value}")
# name: Rohit
# age: 21
# city: Bhopal


### Industry Example — Invoice:

invoice = {"Laptop": 50000, "Mouse": 500, "Keyboard": 1500}

print("=" * 30)
print("INVOICE")
print("=" * 30)
for item, price in invoice.items():
    print(f"{item:<15} ₹{price:>10,}")
print("=" * 30)
print(f"{'TOTAL':<15} ₹{sum(invoice.values()):>10,}")


## TOPIC 34: NESTED DICTIONARY

### Definition:
# "Jab ek dictionary ke andar doosri dictionary, list ya complex data structure store hota hai, use nested data structure kehte hain."

### Kyu Use Karte Hain:
# "Related data ko ek structured form mein rakhne ke liye."

### Real-World Example — Product:

product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000,
    "seller": {
        "name": "ABC Store",
        "city": "Bhopal"
    },
    "specifications": {
        "ram": "16GB",
        "storage": "512GB SSD"
    }
}


### Access:

print(product["seller"]["city"])         # Bhopal
print(product["specifications"]["ram"])  # 16GB


### Update:

product["specifications"]["ram"] = "32GB"


### Kab Use Karein:
# - API responses
# - Product details
# - User profiles
# - Config files
# - Student records
# - Order details

### Loop:

for key, value in product.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for k, v in value.items():
            print(f"  {k}: {v}")
    else:
        print(f"{key}: {value}")


## TOPIC 35: LIST OF DICTIONARIES


employees = [
    {"id": 101, "name": "Rohit", "dept": "Engineering"},
    {"id": 102, "name": "Sagar", "dept": "Marketing"},
    {"id": 103, "name": "Priya", "dept": "Engineering"}
]

# Filter
engineers = [emp for emp in employees if emp["dept"] == "Engineering"]
print(engineers)


#"Database rows ki tarah use hota hai."


## TOPIC 36: DICTIONARY COMPREHENSION

### Normal Loop:

squares = {}
for x in range(1, 6):
    squares[x] = x ** 2


### Dictionary Comprehension:

squares = {x: x ** 2 for x in range(1, 6)}


### Kyu Use Karein:
# - Repetitive dictionary creation short
# - Transformation readable
# - Filtering aur mapping ek expression mein

### Kab Avoid Karein:

#  Difficult to read
result = {
    user["id"]: {"name": user["name"], "active": user["status"] == "active"}
    for user in users if user.get("role") == "admin"
}
#  Normal loop better


### Examples:

# Condition ke saath
evens = {x: x**2 for x in range(10) if x % 2 == 0}

# If-else
label = {x: "even" if x % 2 == 0 else "odd" for x in [1,2,3,4]}

# Swap
swapped = {v: k for k, v in {"a": 1, "b": 2}.items()}


## TOPIC 37: DICTIONARY SORTING

### Keys Ke Basis Par:

marks = {"Rohit": 85, "Sagar": 92, "Priya": 78}
sorted_marks = dict(sorted(marks.items()))
print(sorted_marks)


### Values Ke Basis Par:

sorted_marks = dict(sorted(marks.items(), key=lambda item: item[1]))
print(sorted_marks)


### Descending:

sorted_marks = dict(sorted(marks.items(), key=lambda item: item[1], reverse=True))


### Important:
# - `sorted()` list return karta hai
# - `dict()` us sorted pairs ko dict mein convert karta hai
# - Original dictionary modify nahi hoti



## TOPIC 38: MERGING DICTIONARIES

### Method 1: `|` Operator (Python 3.9+)

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1 | d2
print(merged)  # {'a': 1, 'b': 3, 'c': 4}


### Method 2: `update()`

d1.update(d2)


### Method 3: `{**d1, **d2}`

merged = {**d1, **d2}


### Comparison:

d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
print(d1 == d2)  # True (order matter nahi)


### Dictionaries Directly Compare Nahi Kar Sakte:

d1 < d2  # TypeError


# 📖 PART 5: PRACTICAL APPLICATIONS



## TOPIC 39-45: REAL-WORLD USE CASES

### 1. Student Record

student = {
    "name": "Rohit",
    "roll_no": 101,
    "marks": {"math": 95, "science": 88}
}


### 2. Phone Book

phone_book = {"Rohit": "9876543210", "Sagar": "9876543211"}


### 3. Word Frequency

text = "python java python sql java python"
frequency = {}
for word in text.split():
    frequency[word] = frequency.get(word, 0) + 1
print(frequency)


**Real-world use:** Search suggestions, text analytics, log analysis.

### 4. Counting Occurrences

fruits = ["apple", "banana", "apple", "cherry"]
count = {}
for fruit in fruits:
    count[fruit] = count.get(fruit, 0) + 1


### 5. Grouping Data

students = [
    {"name": "Rohit", "grade": "A"},
    {"name": "Sagar", "grade": "B"},
    {"name": "Priya", "grade": "A"}
]
grouped = {}
for student in students:
    grouped.setdefault(student["grade"], []).append(student["name"])


### 6. Product Data

product = {
    "id": 101,
    "name": "Laptop",
    "price": 55000,
    "seller": {"name": "ABC Store", "city": "Bhopal"}
}


### 7. Config Data

config = {
    "database": {"host": "localhost", "port": 5432},
    "api": {"key": "abc123", "timeout": 30}
}


### 8. JSON Handling

import json

# JSON → Dict
data = json.loads('{"name": "Rohit", "age": 21}')

# Dict → JSON
json_text = json.dumps(data)
print(type(json_text))  # str


###  Important:
# "JSON ek **text-based data format** hai. Python dictionary ek **Python object** hai. JSON object Python dictionary **jaisa dikhta hai**, lekin dono **same cheez nahi** hain."



#  PART 6: ADVANCED AND INTERVIEW



## TOPIC 46: HASH TABLE INTERNALS

# "Dictionary andar se **Hash Table** use karta hai. Key ka hash calculate, index nikaalo, value store karo."

### Diagram:

Dictionary: {"name": "Rohit", "age": 21}

# ┌──────────────────────────────────┐
# │     HASH TABLE (Size = 8)        │
# ├─────────┬──────────┬─────────────┤
# │  Index  │  Key     │  Value      │
# ├─────────┼──────────┼─────────────┤
# │    1    │  "age"   │  21         │
# │    3    │  "name"  │  "Rohit"    │
# └─────────┴──────────┴─────────────┘


# **Disclaimer:** Simplified conceptual model.

### Kyu Fast:
#"Key ka hash → direct bucket → O(1)."

### Hash Collision:
# "Do alag keys ka same hash ho sakta hai. Python open addressing aur probing se solve karta hai."


## TOPIC 47: TIME COMPLEXITY

# | Operation | Average | Explanation |
# |-----------|--------:|-------------|
# | `d[key]` | O(1) | Key lookup |
# | `d[key] = value` | O(1) | Add/update |
# | `del d[key]` | O(1) | Delete |
# | `key in d` | O(1) | Key membership |
# | `d.get(key)` | O(1) | Lookup |
# | `d.keys()` | O(1) | View create |
# | `d.values()` | O(1) | View create |
# | `d.items()` | O(1) | View create |
# | `list(d.keys())` | O(n) | Copy |
# | Iteration | O(n) | Visit all |
# | `copy()` | O(n) | Outer copy |
# | `update(other)` | O(k) | k items |

### Important:
# "View banate waqt O(1), iterate karne par O(n)."



## TOPIC 48: SHALLOW VS DEEP COPY

# | Situation | Use |
# |-----------|-----|
# | Simple flat dictionary | `d.copy()` |
# | Nested mutable independent | `copy.deepcopy()` |
# | Sirf same reference | `d2 = d1` |



## TOPIC 49: `defaultdict`


from collections import defaultdict

text = ["apple", "banana", "apple", "orange"]
count = defaultdict(int)
for word in text:
    count[word] += 1
print(dict(count))


### Grouping:

grouped = defaultdict(list)
for category, item in data:
    grouped[category].append(item)


## TOPIC 50: `Counter`


from collections import Counter

text = "python java python sql"
count = Counter(text.split())
print(count.most_common(2))




## TOPIC 51: COMMON MISTAKES

### 1. Non-existent Key Access

d = {"a": 1}
print(d["b"])      #  KeyError
print(d.get("b"))  # None


### 2. Unhashable Key

d = {[1, 2]: "value"}  #  TypeError


### 3. Iterate Karte Waqt Modify

for key in list(d.keys()):  #  Safe
    del d[key]


### 4. Same Reference Copy

d2 = d1.copy()  # 


### 5. `fromkeys()` Mutable Trap

d = {key: [] for key in ["a", "b"]}  # 


### 6. Duplicate Keys

d = {"a": 1, "a": 2}  # {'a': 2}


### 7. `in` Values Check Nahi Karta

"Rohit" in d  # False
"Rohit" in d.values()  # True


### 8. Shallow Copy Trap

import copy
backup = copy.deepcopy(original)  


## TOPIC 52: INTERVIEW QUESTIONS

### Q1: Dictionary aur List mein difference?
#"Dictionary key-value pairs, O(1) lookup, unique keys. List ordered, index access, duplicates allowed, O(n) search."

### Q2: Dictionary mein order hota hai?
#"Python 3.7+ se haan, insertion order preserve."

### Q3: `d["key"]` vs `d.get("key")`?
#"`[]` KeyError deta hai. `get()` None ya default."

### Q4: Dictionary ki keys unique kyu?
#"Dictionary mein ek key ke liye ek hi associated value maintain hoti hai. Same key dobara assign → purani value replace. Hash table fast lookup mein help karta hai, lekin duplicate-key rule ka direct reason 'same hash' nahi hai."

### Q5: Kaunsi keys allowed hain?
# "Sirf **hashable** keys — str, int, float, bool, tuple, frozenset, provided unke andar ke elements bhi hashable hon."

### Q6: `pop()` vs `popitem()`?
#  "`pop(key)` specific key. `popitem()` last inserted item."

### Q7: Dictionary copy kaise?
#  "`d.copy()` shallow. `copy.deepcopy()` nested ke liye."

### Q8: Dictionary merge kaise?
#  "Python 3.9+: `d1 | d2`. Pehle: `d1.update(d2)`."

### Q9: Dictionary comprehension kya hai?
#  "`{k: v for k, v in iterable}` — one-liner."

### Q10: `setdefault()` kab use?
# "Default value set karni ho, aur existing value mile. Grouping ke liye best."

### Q11: Dictionary iteration order guaranteed?
#  "Python 3.7+ se haan — insertion order."

### Q12: `keys()`, `values()`, `items()` return?
# "View objects. List ke liye `list()` use karo."

### Q13: Shallow vs Deep copy?
# "Shallow: nested objects share. Deep: nested objects bhi copy."

### Q14: JSON aur Dictionary same hain?
# "Nahi. JSON text-based format hai. Python dictionary Python object hai. JSON object dictionary jaisa dikhta hai, par same nahi."

### Q15: Dictionary thread-safe hai?
#  "Nahi, multi-threading mein lock use karo."



## TOPIC 53: PRACTICE QUESTIONS

### Beginner:
# 1. Student dictionary banao aur print karo.
# 2. `[]` aur `get()` se value access karo.
# 3. Nayi key add, ek key delete karo.
# 4. `keys()`, `values()`, `items()` print karo.
# 5. Check karo key exist karti hai ya nahi.

# ### Intermediate:
# 6. Word frequency counter banao.
# 7. Do dictionaries merge karo (3 tarike se).
# 8. Dictionary comprehension se squares banao.
# 9. Dictionary invert karo.
# 10. Nested dictionary se data access karo.
# 11. `setdefault()` se grouping karo.
# 12. Dictionary ko value se sort karo.

### Advanced:
# 13. Function banao jo do dicts merge kare, duplicate keys ki values add kare.
# 14. Nested dictionary flatten karo.
# 15. `Counter` use karke top 3 frequent words.
# 16. JSON string → dict → JSON string.
# 17. Log file se error count.
# 18. E-commerce cart total (GST ke saath).
# 19. Multi-tenant app data structure.
# 20. Cache class banao.
# 21. Group sales data by region.
# 22. Recommendation system.
# 23. Duplicate values remove.
# 24. Deep copy vs shallow copy demonstrate.
# 25. API response parse.



## TOPIC 54: SUMMARY

# | Topic | Key Point |
# |-------|-----------|
# | **Dictionary** | Key-Value pairs, Mutable, Ordered (3.7+) |
# | **Keys** | Unique, Hashable |
# | **Values** | Kuch bhi |
# | **Access** | `d[key]` ya `d.get(key)` |
# | **Search** |  O(1) average |
# | **Methods** | get, keys, values, items, update, setdefault, pop, popitem, clear, copy, fromkeys |
# | **Operations** | Merge, Comparison |
# | **Comprehension** | `{k: v for item in iterable if cond}` |
# | **Nested** | Dictionary ke andar dictionary |
# | **Use Case** | API, Config, JSON, Counting, Grouping |
# | **Limitation** | Keys hashable honi chahiye |









