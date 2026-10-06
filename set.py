# "Set Python ka ek built-in data type hai jo unique elements "
# "ka unordered collection hota hai. Iska matlab — agar aap "
# "set mein duplicate value daalenge, to wo automatically "
# "remove ho jayegi. Aur set mein indexing nahi hoti, "
# "matlab aap set[0] nahi likh sakte."

# "Set ka concept mathematics se aaya hai. Jaise math mein "
# "set hota hai — {1, 2, 3} — wahi concept Python mein "
# "implement kiya gaya hai. Isliye set operations bhi "
# "math wale hain — union, intersection, difference."


# "Socho aapke paas ek attendance register hai. Agar Rohit 3 baar aaya, aap usse sirf ek baar "
# "likhenge. Wahi kaam Set karta hai — duplicate hata deta hai. "
# "Ya phir socho Aadhaar card — har vyakti ka ek hi hota hai, "
# "duplicate nahi. Set bhi wahi — har element unique."

# Ab sawal ye hai — jab List, Tuple already hai, to Set kyu use 
# karein? 
# Iske 4 bade reasons hain:"

# "Agar aapke paas ek list hai jisme duplicate values hain, "
# "aur aap chahte ho ki sirf unique values rahein — to Set "
# "sabse fast tarika hai. "
# "list(set(my_list)) — bas ek line."


# Fast Search (O(1))

# "List mein agar aapko check karna hai ki koi element hai ya nahi, "
# "to wo O(n) time leta hai — matlab poora list scan karna padta hai. "
# "Set mein ye O(1) hota hai — matlab ek hi step mein pata chal jata hai. "
# "Kyu? Kyu ki Set hash table use karta hai."

# "Union, intersection, difference — ye operations "
# "Set ke saath bahut easy hain."
# " List mein ye karna bahut mushkil hota hai."


# "Jab aapko sirf unique values chahiye — jaise unique visitors, "
# "unique emails, unique skills — Set best hai. Note: "
# "Set memory-efficient nahi hota, kyunki hash table structure ki wajah se additional "
# "memory overhead hota hai. "
# "Par duplicate handling ke liye ye best hai."


# Method 1: Curly Braces {}

my_set = {1, 2, 3, 4, 5}
print(my_set)        # {1, 2, 3, 4, 5}
print(type(my_set))  # <class 'set'>
# "Dhyan dena — {} se set banta hai, par khaali {} se set nahi banta, wo dictionary banta hai."


# Method 2: set() Constructor
my_set = set([1, 2, 3, 4, 5])
print(my_set)  # {1, 2, 3, 4, 5}

# Method 3: String se Set
my_set = set("hello")
print(my_set)  # {'h', 'e', 'l', 'o'}
# "Dekho, 'hello' mein 'l' do baar tha, par set mein sirf ek baar aaya."

# Method 4: Range se Set
my_set = set(range(5))
print(my_set)  # {0, 1, 2, 3, 4}

# Method 5: List se Set (Duplicate Remove)
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = set(nums)
print(unique)  # {1, 2, 3, 4}

# Set Constructor Edge Cases:

print(set([1, 2, 2, 3]))    # {1, 2, 3}
print(set((1, 2, 2, 3)))    # {1, 2, 3}
print(set("hello"))         # {'h', 'e', 'l', 'o'}
print(set(10))              #  TypeError: 'int' object is not iterable
# "set() sirf iterable se set banata hai. Integer directly nahi de sakte."

# TOPIC 5: EMPTY SET (IMPORTANT)

empty = {}          # Ye DICTIONARY hai, set nahi!
empty = set()       # Ye EMPTY SET hai

print(type({}))     # <class 'dict'>
print(type(set()))  # <class 'set'>

# Boolean Behavior:
s = set()
print(bool(s))  # False

s.add(10)
print(bool(s))  # True

if not s:
    print("Set is empty")

#  TOPIC 6: SET MEIN ALLOWED AUR DISALLOWED ELEMENTS

# Allowed (Hashable):

s = {1, 2, 3}           # int 
s = {1.5, 2.5}          # float 
s = {"apple", "banana"} # string 
s = {(1, 2), (3, 4)}    # tuple 
s = {True, False}       # bool 

# Disallowed (Unhashable):
s = {1, 2, [3, 4]}      #  list
s = {1, 2, {3, 4}}      #  set
s = {1, 2, {"a": 1}}    #  dict

# Tuple Limitation:

s = {(1, 2), (3, 4)}    #  Valid

s = {(1, [2, 3])}       #  TypeError

# "Tuple immutable hai, lekin agar tuple ke andar mutable object hai, "
# "toh poora tuple hashable nahi ho sakta."


# TOPIC 7: SET INTERNALLY KAISE KAAM KARTA HAI?
# "Set andar se Hash Table use karta hai. Jab aap koi element add karte ho, Python us element ka hash value calculate karta hai. Phir us hash value ko table ke size se divide karke index nikalta hai. Us index pe element store hota hai."

# No Indexing Example:
s = {1, 2, 3}
print(s[0])  #  TypeError: 'set' object is not subscriptable
# No Slicing:
s = {1, 2, 3, 4, 5}
print(s[1:3])  #  Error

# TOPIC 9: SET ITERATION
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)
# "Set ko iterate kar sakte hain, lekin iteration order guaranteed nahi hota."

# 10.1 add() — Ek Element Add Karna
# Kya: Set mein ek naya element add karta hai.

# Kab: Jab ek hi element add karna ho.

# Kaise:

fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # {'apple', 'banana', 'cherry'}

# Kyu: Simple, fast, O(1) average.

# Important: Agar element already exist karta hai, to kuch nahi hota (error nahi).

# Return Value: None
result = fruits.add("mango")
print(result)  # None

# 10.2 update() — Multiple Elements Add Karna
# Kya: Ek saath multiple elements add karta hai (list, tuple, set, string sab se).

# Kab: Jab bulk mein elements add karne ho.

# Kaise:

fruits = {"apple", "banana"}
fruits.update(["cherry", "mango", "grape"])
print(fruits)  # {'apple', 'banana', 'cherry', 'mango', 'grape'}

# Multiple sets bhi
A = {1, 2, 3}
B = {3, 4, 5}
C = {5, 6, 7}
A.update(B, C)
print(A)  # {1, 2, 3, 4, 5, 6, 7}
# Return Value: None
# add() vs update():
# add()    →  Ek element
# update() →  Multiple elements
# 10.3 remove() — Specific Element Hatana (Error Ke Saath)
# Kya: Specific element ko set se remove karta hai.

# Kab: Jab aap sure ho ki element exist karta hai.

# Kaise:


# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)  # {'apple', 'cherry'}

# Important: Agar element nahi mila to KeyError aayega.
fruits.remove("mango")  #  KeyError: 'mango'
# Return Value: None

# 10.4 discard() — Specific Element Hatana (Bina Error)
# Kya: Specific element remove karta hai, par agar nahi mile to koi error nahi deta.

# Kab: Jab aap sure nahi ho ki element exist karta hai ya nahi.

# Kaise:

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)  # {'apple', 'cherry'}

fruits.discard("mango")  #  Koi error nahi

# remove()  →  Element na mile to ERROR
# discard() →  Element na mile to SILENT (no error)

# 10.5 pop() — Arbitrary Element Hatana
# Kya: Set se ek arbitrary element remove karta hai aur return karta hai.

# Kab: Jab aapko koi bhi ek element hatana ho, specific nahi.

# Kaise:

s = {10, 20, 30}
removed = s.pop()
print(removed)  # Koi bhi ek element
print(s)        # Baaki elements

# Kyu: Arbitrary removal ke liye.

# Important: Set unordered hai isliye kaunsa element pop hoga, iski koi guarantee nahi hoti.

#  Empty set pe pop():
s = set()
s.pop()  #  KeyError: 'pop from an empty set'

# 10.6 clear() — Poora Set Empty Karna
# Kya: Set ke saare elements remove kar deta hai.

# Kab: Jab poora data reset karna ho.

# Kaise:

fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)  # set()

# Return Value: None

# Note: Set object rehta hai, sirf elements hate hain.

# 10.7 copy() — Shallow Copy
# Kya: Set ki ek nayi copy banata hai.

# Kab: Jab original set ko protect karna ho.

# Kaise:
original = {1, 2, 3}
backup = original.copy()
backup.add(4)
print(original)  # {1, 2, 3}   Original unchanged
print(backup)    # {1, 2, 3, 4}

# Return Value: New set.
# Bina copy ke:

o1 = {1, 2, 3}
o2 = o1        #  Ye copy nahi, same reference hai
o2.add(4)
print(o1)      # {1, 2, 3, 4}  ← Original bhi change ho gaya!

# TOPIC 11: SET METHODS KE RETURN VALUES
s = {1, 2, 3}
result = s.add(4)
print(result)  # None
print(s)       # {1, 2, 3, 4}


# 12.1 union() ya | — Sab Elements (A ∪ B)
# Kya: Dono sets ke saare elements ka naya set banata hai (duplicate ek baar).

# Kab: Jab dono sets ko combine karna ho.

# Kaise:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))  # {1, 2, 3, 4, 5, 6}
print(A | B)       # {1, 2, 3, 4, 5, 6}

# Multiple sets
C = {5, 6, 7, 8}
print(A.union(B, C))  # {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B | C)      # {1, 2, 3, 4, 5, 6, 7, 8}

# Kyu: Combine karne ke liye.
# Note: Original sets change nahi hote.

# 12.2 intersection() ya & — Common Elements (A ∩ B)
# Kya: Sirf woh elements return karta hai jo dono sets mein hain.
# Kab: Jab common elements nikalne ho.

# Kaise:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.intersection(B))  # {3, 4}
print(A & B)              # {3, 4}

# Multiple sets
C = {4, 5, 6}
print(A.intersection(B, C))  # {4}


# 12.3 difference() ya - — A Mein Hai Par B Mein Nahi (A - B)
# Kya: A ke woh elements return karta hai jo B mein nahi hain.

# Kab: Jab ek set se dusre set ke elements hatane ho.

# Kaise:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.difference(B))  # {1, 2}
print(A - B)            # {1, 2}
print(B - A)            # {5, 6}

# Kyu: Difference nikalne ke liye.

# Important: A - B aur B - A alag hote hain.

# 12.4 symmetric_difference() ya ^ — Sirf Ek Mein Hone Wale (A △ B)
# Kya: Woh elements return karta hai jo sirf ek set mein hain, dono mein nahi.

# Kab: Jab common elements nahi chahiye.

# Kaise:

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.symmetric_difference(B))  # {1, 2, 5, 6}
print(A ^ B)                      # {1, 2, 5, 6}

# TOPIC 13: IN-PLACE UPDATE METHODS
# "Ye methods original set ko modify karte hain, naya set return nahi karte."

# update()
A = {1, 2, 3}
B = {3, 4, 5}
A.update(B)
print(A)  # {1, 2, 3, 4, 5}

# intersection_update()

A = {1, 2, 3}
B = {2, 3, 4}
A.intersection_update(B)
print(A)  # {2, 3}

# difference_update()

A = {1, 2, 3}
B = {2, 3, 4}
A.difference_update(B)
print(A)  # {1}

# symmetric_difference_update()

A = {1, 2, 3}
B = {2, 3, 4}
A.symmetric_difference_update(B)
print(A)  # {1, 4}

# 14.1 issubset() — Kya A, B ka Subset Hai?
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))  # True
print(B.issubset(A))  # 

# 14.2 issuperset() — Kya A, B ka Superset Hai?
A = {1, 2}
B = {1, 2, 3, 4}

print(B.issuperset(A))  # True
print(A.issuperset(B))  # False

# 14.3 isdisjoint() — Kya Dono Mein Koi Common Nahi?

A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))  # True (koi common nahi)

# TOPIC 15: SET COMPARISON OPERATORS

A = {1, 2}
B = {1, 2, 3}

print(A <= B)  # True (subset)
print(A < B)   # True (proper subset)
print(B >= A)  # True (superset)
print(B > A)   # True (proper superset)

# Equality
A = {1, 2, 3}
B = {3, 2, 1}
print(A == B)  # True (order matter nahi karta)

# TOPIC 16: MEMBERSHIP OPERATORS
skills = {"Python", "JavaScript", "React"}

print("Python" in skills)      # True
print("Java" not in skills)    # True
# "Set mein membership checking average-case O(1) hoti hai, kyunki hash table use hota hai."

# TOPIC 17: BUILT-IN FUNCTIONS WITH SET

s = {5, 2, 8, 1, 9, 3}

len(s)      # 6  → Length
sum(s)      # 28 → Total
max(s)      # 9  → Maximum
min(s)      # 1  → Minimum
sorted(s)   # [1, 2, 3, 5, 8, 9] → Sorted LIST (set nahi)
any(s)      # True (koi bhi truthy hai)
all(s)      # True (sab truthy hain)

# "Dhyan dena — sorted(s) list return karta hai, set nahi."
# TOPIC 18: SET COMPREHENSION
# Kya: Ek line mein set banane ka tarika.
# Syntax:
# Bina condition
# {expression for item in iterable}

# # With condition
# {expression for item in iterable if condition}
# 1. Squares
squares = {x**2 for x in range(5)}
print(squares)  # {0, 1, 4, 9, 16}

# 2. Even numbers
evens = {x for x in range(10) if x % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}

# 3. Unique lengths of words
words = ["apple", "banana", "cherry", "date"]
lengths = {len(w) for w in words}
print(lengths)  # {4, 5, 6}

# 4. String se unique characters
unique_chars = {ch for ch in "hello world"}
print(unique_chars)

# TOPIC 19: FROZENSET (Immutable Set)
# Kya: Set ka immutable version.

# Kab: Jab set ko change nahi karna ho, ya dictionary key banana ho.

# Kaise:

fs = frozenset([1, 2, 3, 4])
print(fs)  # frozenset({1, 2, 3, 4})

# fs.add(5)  #  AttributeError
# Kyu Use Karein:
# Dictionary key banane ke liye

# Dusre set ke element banane ke liye

# Constant data ke liye

A = frozenset([1, 2, 3])
B = frozenset([3, 4, 5])

print(A | B)  # frozenset({1, 2, 3, 4, 5})
print(A & B)  # frozenset({3})
print(A - B)  # frozenset({1, 2})

# Practical Use Cases:
# 1. Dictionary Key:
permissions = frozenset({"read", "write"})
roles = {permissions: "Editor"}
print(roles[permissions])

# 2. Set Ke Andar Frozenset:
groups = {
    frozenset({"A", "B"}),
    frozenset({"C", "D"})
}
print(groups)


# ┌────────────────────────────────────────────┐
# │  SET              │  FROZENSET             │
# ├───────────────────┼────────────────────────┤
# │  Mutable          │  Immutable             │
# │  {1, 2, 3}        │  frozenset({1, 2, 3})  │
# │  add/remove     │  add/remove          │
# │  Dict key       │  Dict key           │
# │  Set element    │  Set element         │
# └────────────────────────────────────────────┘


# TOPIC 20: HASHABILITY (Advanced)
# Set ke elements hashable hone chahiye.

# Hashable objects ka hash stable hona chahiye.

# Mutable objects jaise list, dict, set directly elements nahi ban sakte.

# frozenset hashable ho sakta hai, agar uske elements hashable hon.


s = {frozenset({1, 2}), frozenset({3, 4})}
print(s)  # {frozenset({1, 2}), frozenset({3, 4})}

# TOPIC 22: SET KI LIMITATIONS
# Indexing nahi hoti.

# Slicing nahi hoti.

# Duplicate values preserve nahi hoti.

# Order-based operations ke liye suitable nahi.

# Elements hashable hone chahiye.

# Set ko sort karne ke liye sorted() use karna padta hai, jo list return karta hai.

A = {1, 2, 3}

print(A.union([3, 4, 5]))  #  Valid
print(A | [3, 4, 5])       #  TypeError

# TOPIC 24: REAL-WORLD USE CASES
# Duplicate Remove
nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print(unique)  # [1, 2, 3, 4, 5]  ← Order guaranteed nahi

# Order Preserve Karte Hue Duplicate Remove

nums = [3, 1, 3, 2, 1, 4]
unique = list(dict.fromkeys(nums))
print(unique)  # [3, 1, 2, 4]  ← Order preserved

# Common Friends (Intersection)

rohit_friends = {"Aman", "Sagar", "Priya", "Rahul"}
priya_friends = {"Sagar", "Priya", "Neha", "Karan"}

common = rohit_friends & priya_friends
print(common)  # {'Sagar', 'Priya'}

# Fast Membership Check
valid_users = {"rohit", "priya", "aman", "sagar"}
if "rohit" in valid_users:  # O(1)
    print("Access granted")

# Unique Visitors Count

visitors = ["user1", "user2", "user1", "user3", "user2"]
unique_visitors = set(visitors)
print(len(unique_visitors))  # 3

# Unique Email IDs

emails = ["a@gmail.com", "b@gmail.com", "a@gmail.com"]
unique_emails = set(emails)
print(unique_emails)  # {'a@gmail.com', 'b@gmail.com'}

# Common Skills

developer1 = {"Python", "SQL", "Git"}
developer2 = {"Python", "React", "Git"}

common_skills = developer1 & developer2
print(common_skills)  # {'Python', 'Git'}

# Missing Permissions

required = {"read", "write", "delete"}
available = {"read", "write"}

missing = required - available
print(missing)  # {'delete'}

# Anagram Check (Correct Way)
from collections import Counter

def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("aabb", "ab"))        # False

# Set se anagram check galat hai:
#  GALAT
def is_anagram(s1, s2):
    return set(s1) == set(s2)

print(is_anagram("aabb", "ab"))  # True (galat!)
# "Set sirf unique characters check karta hai, frequency nahi. Isliye anagram ke liye Counter ya sorted use karo."

#  TOPIC 26: COMMON MISTAKES
# Mistake 1: Empty set galat banana
s = {}       # Ye dict hai
s = set()    #  Ye set hai

# Mistake 2: Indexing karna
s = {1, 2, 3}
print(s[0])  #  TypeError

# Mistake 3: Unhashable daalna
s = {1, 2, [3, 4]}  #  TypeError

# Mistake 4: Iterate karte waqt modify karna

s = {1, 2, 3}
for x in s:
    s.add(x + 10)  #  RuntimeError

# Solution:
for x in list(s):  # list() se copy
    s.add(x + 10)
# Mistake 5: remove() vs discard() confuse karna

s = {1, 2, 3}
s.remove(5)   #  KeyError
s.discard(5)  #  No error

# Mistake 6: list(set()) order preserve nahi karta
nums = [3, 1, 3, 2, 1, 4]
print(list(set(nums)))  # Order guaranteed nahi
# Solution:
unique = list(dict.fromkeys(nums))
print(unique)  # [3, 1, 2, 4]
# Mistake 7: Anagram ke liye set use karna
#  GALAT
set("aabb") == set("ab")  # True (galat!)

# Solution:
from collections import Counter
Counter("aabb") == Counter("ab")  # False 

# TOPIC 27: INTERVIEW QUESTIONS
# Q1: Set aur List mein difference?
# "Set unordered, unique, no indexing, O(1) search. List ordered, duplicates allowed, "
# "indexing, O(n) search."
# Q2: Set duplicate kaise remove karta hai?
# "Hash table use karta hai. Har element ka hash calculate karta hai. "
# "Agar hash already exist karta hai to add nahi karta."
# Q3: remove() vs discard() vs pop()?
# "remove() error deta hai agar element na mile. discard() silent rehta hai. pop() arbitrary element hatata hai."
# Q4: Frozenset kab use karte hain?
# "Jab immutable set chahiye — dictionary key ya dusre set ka element banane ke liye."
# Q5: Set mutable hai ya immutable?
# "Set mutable hai, par uske elements immutable hone chahiye."
# Q6: {} se empty set kyu nahi banta?
# "Kyu ki {} Python mein dictionary ke liye reserved hai."
# Q7: Set mein order kyu nahi hota?
# "Kyu ki ye hash table pe based hai. Elements hash ke hisaab se store hote hain."
# Q8: |, &, -, ^ kya karte hain?
# "Union, Intersection, Difference, Symmetric Difference."
# Q9: Set comprehension kya hai?
# "Ek line mein set banane ka tarika — {x**2 for x in range(5)}."
# Q10: Set mein in O(1) kyu?
# "Hash table use hota hai. Direct bucket mein check karta hai."
# Q11: Set comparison operators kya hain?
# "<=, <, >=, >, == — subset, proper subset, superset, proper superset, equality."

# Q12: Methods vs operators mein difference?
# "Operators sirf set ke saath kaam karte hain. Methods kisi bhi iterable ke saath."

# TOPIC 28: PRACTICE QUESTIONS
# Beginner:
# Empty set create karo aur check karo ki empty hai ya nahi.

# Set mein 5 elements add karo.

# Set se ek element remove karo using discard().

# String se unique characters nikalo.

# Set ko loop se iterate karo.

# [1, 2, 2, 3, 4, 4, 5] se duplicate remove karke set banao.

# Do sets banao aur union, intersection, difference nikaalo.

# Check karo {1, 2} {1, 2, 3, 4} ka subset hai ya nahi.

# Intermediate:
# Set comprehension se 1-20 ke prime numbers nikaalo.

# Do lists ke common elements nikaalo.

# discard() aur remove() ka difference dikhao.

# Frozenset banao aur dictionary key banao.

# Do lists ke unique elements nikaalo.

# Duplicate values remove karo, original order preserve karte hue.

# Check karo ki ek set doosre ka proper subset hai ya nahi.

# Set comprehension se 1–50 ke even numbers banao.

# Multiple developers ki common skills nikalo.

# Advanced:
# Function banao jo do lists ka symmetric difference return kare.

# Set use karke anagram check karo (Counter se).

# Required aur available permissions ka difference nikalo.

# Frozenset ko dictionary key ke roop mein use karo.

# Do strings ke character frequencies compare karke anagram check karo.

# Set operations ka use karke do groups ke unique members nikalo.

# Nested frozenset banao.

# Set ki time complexity analyze karo different operations ke liye.





















Main structure ye rakhunga:

* **70+ questions**
* Har question ka **clear answer**
* **Why / reasoning**
* Jahan relevant ho **code + output**
* **Tricky follow-up**
* **Real-world scenario**
* Beginner → Intermediate → Advanced → Interview Trap → Industry Scenario
* Answers tumhare current notes ke terminology/coverage ke according rahenge. 

# 🐍 Python Set — 70+ Interview Questions With Solutions

---

# 🟢 PART 1 — FUNDAMENTALS

## Q1. Python Set kya hota hai?

### Answer

`set` Python ka built-in data type hai jo **unique elements ka collection** store karta hai.

Iski important properties:

* Duplicate values automatically remove hoti hain.
* Indexing nahi hoti.
* Slicing nahi hoti.
* Set mutable hota hai.
* Elements hashable hone chahiye.
* Membership checking average-case mein `O(1)` hoti hai.

```python
numbers = {10, 20, 30, 20}

print(numbers)
```

Conceptually result:

```text
{10, 20, 30}
```

`20` duplicate tha, isliye ek hi baar raha. 

### Interview Follow-up

**Interviewer:** Set ka main purpose kya hai?

**Answer:**
Jab hume **unique values** maintain karni ho ya **fast membership checking** aur mathematical set operations karni ho, tab Set useful hota hai.

---

# Q2. Set aur List mein kya difference hai?

| Feature    | List               | Set                                  |
| ---------- | ------------------ | ------------------------------------ |
| Duplicate  | Allowed            | Automatically removed                |
| Indexing   | Yes                | No                                   |
| Slicing    | Yes                | No                                   |
| Membership | Average `O(n)`     | Average `O(1)`                       |
| Ordering   | Sequence order     | Order-based operations suitable nahi |
| Main use   | Ordered collection | Unique values / membership           |

### Interview Answer

> "List sequence-oriented data ke liye useful hai, jabki Set uniqueness aur fast membership checking ke liye useful hai."



---

# Q3. Set aur Tuple mein difference?

### Answer

Tuple:

```python
data = (10, 20, 30)
```

Set:

```python
data = {10, 20, 30}
```

Main differences:

* Tuple immutable hai.
* Set mutable hai.
* Tuple indexing support karta hai.
* Set indexing support nahi karta.
* Tuple duplicates preserve karta hai.
* Set duplicates remove karta hai.

---

# Q4. `{}` empty Set kyu nahi banata?

```python
x = {}

print(type(x))
```

Output:

```text
<class 'dict'>
```

Python mein `{}` empty dictionary represent karta hai.

Empty Set:

```python
x = set()

print(type(x))
```

Output:

```text
<class 'set'>
```



### Interview Trap

**Interviewer:** Agar mujhe empty Set banana ho?

**Answer:**

```python
set()
```

---

# Q5. Set mein duplicate values automatically kaise remove hoti hain?

```python
numbers = {1, 2, 2, 3, 3, 3}

print(numbers)
```

Result:

```text
{1, 2, 3}
```

Set internally hash-based structure use karta hai. Element ko identify karne ke liye hashing important role play karti hai. 

---

# Q6. Set unordered kyu kaha jata hai?

Set indexing/order-based operations ke liye designed nahi hai.

```python
s = {10, 20, 30}

print(s[0])
```

Error:

```text
TypeError: 'set' object is not subscriptable
```

Isliye Set ko List ki tarah position-based collection treat nahi karna chahiye. 

---

# Q7. Kya Set ko iterate kar sakte hain?

**Yes.**

```python
fruits = {"apple", "banana", "mango"}

for fruit in fruits:
    print(fruit)
```

Lekin iteration order ko guaranteed sequence order nahi maana chahiye. 

### Interview Follow-up

**Q:** Kya Set se first element reliably nikal sakte hain?

**Answer:**
Nahi, indexing available nahi hai aur Set ko ordered sequence ke roop mein use nahi karna chahiye.

---

# 🟢 PART 2 — CREATION

# Q8. Set banane ke different ways?

### Method 1

```python
s = {1, 2, 3}
```

### Method 2

```python
s = set([1, 2, 3])
```

### Method 3

```python
s = set("hello")
```

### Method 4

```python
s = set(range(5))
```

### Method 5 — Duplicate removal

```python
numbers = [1, 2, 2, 3, 3]

s = set(numbers)
```



---

# Q9. `set("hello")` kya karega?

```python
s = set("hello")
print(s)
```

Result mein unique characters honge:

```text
{'h', 'e', 'l', 'o'}
```

`l` do baar tha, lekin Set uniqueness maintain karta hai. 

---

# Q10. `set(10)` kyu error deta hai?

```python
set(10)
```

Error:

```text
TypeError: 'int' object is not iterable
```

`set()` constructor iterable se elements leta hai.

Examples:

```python
set([1, 2, 3])
set("hello")
set((1, 2, 3))
set(range(5))
```



---

# 🟡 PART 3 — HASHABILITY

# Q11. Set ke elements hashable kyu hone chahiye?

Set hash-based structure use karta hai.

Isliye Set ko element identify/store karne ke liye stable hash value chahiye.

Common hashable examples:

```python
1
1.5
"Python"
True
(1, 2)
```

Common unhashable:

```python
[1, 2]
{1, 2}
{"a": 1}
```



---

# Q12. Kya List ko Set ke andar rakh sakte hain?

Nahi.

```python
s = {1, 2, [3, 4]}
```

Error:

```text
TypeError
```

Reason: List mutable aur unhashable hai.

---

# Q13. Kya Tuple Set ke andar rakh sakte hain?

Usually yes, **agar Tuple ke saare elements hashable hain**.

```python
s = {(1, 2), (3, 4)}
```

Valid.

Lekin:

```python
s = {(1, [2, 3])}
```

Invalid.

Reason: Tuple ke andar List hai, aur List unhashable hai. 

### 🔥 Interview Follow-up

> "Tuple immutable hai, phir second example kyu fail hua?"

**Answer:**
Hashability sirf outer Tuple ke immutable hone par depend nahi karti. Uske contained objects bhi hashable hone chahiye.

---

# Q14. Frozenset kya hai?

`frozenset` Set ka **immutable version** hai.

```python
fs = frozenset([1, 2, 3])

print(fs)
```

Aap ismein:

```python
fs.add(4)
```

nahi kar sakte.



---

# Q15. Frozenset ka practical use kya hai?

Important use cases:

### Dictionary key

```python
permissions = frozenset({"read", "write"})

roles = {
    permissions: "Editor"
}
```

### Set ke andar

```python
groups = {
    frozenset({"A", "B"}),
    frozenset({"C", "D"})
}
```



---

# 🟠 PART 4 — METHODS

# Q16. `add()` kya karta hai?

Ek element add karta hai.

```python
s = {1, 2}

s.add(3)

print(s)
```

Result:

```text
{1, 2, 3}
```

Agar element already present hai, duplicate create nahi hota.

`add()` ka return value `None` hota hai. 

---

# Q17. `add()` aur `update()` mein difference?

### `add()`

Single element:

```python
s.add(10)
```

### `update()`

Multiple elements:

```python
s.update([10, 20, 30])
```



### 🔥 Trap

```python
s.add([1, 2])
```

Error ho sakta hai because List unhashable hai.

But:

```python
s.update([1, 2])
```

Valid hai because `update()` iterable ke elements add karta hai.

---

# Q18. `remove()` kya karta hai?

Specific element remove karta hai.

```python
s = {1, 2, 3}

s.remove(2)
```

Agar element exist nahi karta:

```python
s.remove(5)
```

to `KeyError` aayega. 

---

# Q19. `discard()` kya karta hai?

Element remove karta hai, lekin missing element par error nahi deta.

```python
s = {1, 2, 3}

s.discard(5)

print(s)
```

No error.



---

# Q20. `remove()` vs `discard()`?

| Method      | Element present | Element absent |
| ----------- | --------------- | -------------- |
| `remove()`  | Remove          | `KeyError`     |
| `discard()` | Remove          | No error       |

### Interview Rule

> Agar existence guaranteed hai → `remove()`
> Agar existence uncertain hai → `discard()`

---

# Q21. `pop()` kya karta hai?

Set se **arbitrary element** remove karke return karta hai.

```python
s = {10, 20, 30}

x = s.pop()

print(x)
```

Kaunsa element milega, assume nahi karna chahiye.

Empty Set:

```python
set().pop()
```

`KeyError` deta hai. 

---

# Q22. `clear()` kya karta hai?

Poore Set ko empty karta hai.

```python
s = {1, 2, 3}

s.clear()

print(s)
```

Output:

```text
set()
```

Object exist karta hai; elements remove hote hain. 

---

# Q23. `copy()` aur assignment mein difference?

```python
a = {1, 2, 3}

b = a
c = a.copy()
```

`b` same object/reference ko point karta hai.

`c` new Set hai.

```python
b.add(4)

print(a)
print(b)
print(c)
```

Result:

```text
a → {1, 2, 3, 4}
b → {1, 2, 3, 4}
c → {1, 2, 3}
```



---

# 🔵 PART 5 — SET OPERATIONS

# Q24. Union kya hai?

Dono Sets ke saare unique elements.

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))
```

Result:

```text
{1, 2, 3, 4, 5}
```

Operator:

```python
A | B
```



---

# Q25. Intersection kya hai?

Common elements.

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(A & B)
```

Result:

```text
{2, 3}
```



---

# Q26. Difference kya hai?

A mein hain but B mein nahi.

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(A - B)
```

Result:

```text
{1}
```

Important:

```python
A - B
```

aur

```python
B - A
```

same nahi hote. 

---

# Q27. Symmetric Difference kya hai?

Jo elements **sirf ek Set mein** hain.

```python
A = {1, 2, 3}
B = {2, 3, 4}

print(A ^ B)
```

Result:

```text
{1, 4}
```



---

# Q28. Ye solve karo:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

### `A | B`

```text
{1, 2, 3, 4, 5, 6}
```

### `A & B`

```text
{3, 4}
```

### `A - B`

```text
{1, 2}
```

### `B - A`

```text
{5, 6}
```

### `A ^ B`

```text
{1, 2, 5, 6}
```

---

# 🟣 PART 6 — IN-PLACE OPERATIONS

# Q29. `update()` aur `union()` mein difference?

### union

New Set return karta hai:

```python
C = A.union(B)
```

Original `A` unchanged.

### update

Original `A` modify karta hai:

```python
A.update(B)
```



---

# Q30. `intersection()` vs `intersection_update()`?

```python
A.intersection(B)
```

New result deta hai.

```python
A.intersection_update(B)
```

Original `A` modify karta hai.

Same concept:

```text
difference()
difference_update()

symmetric_difference()
symmetric_difference_update()
```

---

# 🟤 PART 7 — SUBSET / SUPERSET

# Q31. Subset kya hota hai?

Agar A ke **saare elements B mein present hain**, to A, B ka subset hai.

```python
A = {1, 2}
B = {1, 2, 3}

print(A.issubset(B))
```

Output:

```text
True
```



---

# Q32. Superset kya hota hai?

```python
B.issuperset(A)
```

Agar B mein A ke saare elements hain, B A ka superset hai.



---

# Q33. `<` aur `<=` mein difference?

```python
A = {1, 2}
B = {1, 2, 3}
```

```python
A < B
```

True → proper subset.

```python
A <= B
```

True → subset.

Difference: Proper subset mein dono equal nahi hone chahiye.

---

# Q34. Set equality mein order matter karta hai?

No.

```python
A = {1, 2, 3}
B = {3, 2, 1}

print(A == B)
```

Output:

```text
True
```

Set uniqueness/membership based comparison karta hai, sequence ordering based nahi. 

---

# 🔴 PART 8 — MEMBERSHIP & COMPLEXITY

# Q35. Set mein `in` fast kyu hota hai?

```python
users = {"rohit", "aman", "sagar"}

print("rohit" in users)
```

Set hash-table based structure use karta hai, isliye average-case membership checking `O(1)` hoti hai. 

---

# Q36. Kya Set ki har operation O(1) hoti hai?

**Interview mein blindly "yes" mat bolna.**

Better answer:

> "Set membership aur common hash-table operations average-case `O(1)` hote hain, but every operation universally O(1) nahi hoti. Complexity operation aur implementation details par depend karti hai."

Ye answer interviewer ko dikhaata hai ki candidate sirf shortcut yaad nahi kar raha.

---

# Q37. Set ka memory overhead kyu ho sakta hai?

Set hash-table structure maintain karta hai.

Isliye same number of elements ke liye Set ka overhead List se different/higher ho sakta hai.

Tumhare notes bhi specifically mention karte hain ki Set **memory-efficient nahi maana jata** because hash-table structure additional memory overhead create karta hai. 

---

# 🟢 PART 9 — BUILT-IN FUNCTIONS

# Q38. Set ke saath `len()`?

```python
s = {1, 2, 3}

print(len(s))
```

Output:

```text
3
```

---

# Q39. `sum()`, `min()`, `max()`?

```python
s = {5, 2, 8, 1}

print(sum(s))
print(min(s))
print(max(s))
```

Output:

```text
16
1
8
```

---

# Q40. `sorted(set)` ka return type kya hai?

Important interview question.

```python
s = {5, 2, 8, 1}

result = sorted(s)

print(type(result))
```

Output:

```text
<class 'list'>
```

`sorted()` Set ko Set mein convert nahi karta; sorted **List** return karta hai. 

---

# 🟡 PART 10 — SET COMPREHENSION

# Q41. Set comprehension kya hai?

One-line Set creation syntax:

```python
{x for x in iterable}
```

Example:

```python
squares = {x**2 for x in range(5)}

print(squares)
```

Result:

```text
{0, 1, 4, 9, 16}
```



---

# Q42. Set comprehension se even numbers?

```python
evens = {
    x
    for x in range(10)
    if x % 2 == 0
}
```

Result:

```text
{0, 2, 4, 6, 8}
```

---

# Q43. Unique word lengths?

```python
words = ["apple", "banana", "cherry", "date"]

lengths = {len(word) for word in words}

print(lengths)
```

Result:

```text
{4, 5, 6}
```



---

# 🔥 PART 11 — REAL INTERVIEW SCENARIOS

# Q44. List se duplicates remove karne hain.

```python
nums = [1, 2, 2, 3, 4, 4]

unique = set(nums)

print(unique)
```

Efficient simple approach:

```python
set(nums)
```

---

# Q45. Lekin duplicates remove karte waqt original order preserve karna ho?

Ye important interview trap hai.

```python
nums = [3, 1, 3, 2, 1, 4]

unique = list(dict.fromkeys(nums))

print(unique)
```

Output:

```text
[3, 1, 2, 4]
```

`list(set(nums))` ko blindly use nahi karna chahiye jab order preservation requirement ho. 

---

# Q46. Do developers ki common skills find karo.

```python
developer1 = {"Python", "SQL", "Git"}
developer2 = {"Python", "React", "Git"}

common = developer1 & developer2

print(common)
```

Result:

```text
{"Python", "Git"}
```

Real-world: candidate matching, skill comparison, team capability analysis.



---

# Q47. Required aur available permissions mein missing permissions?

```python
required = {"read", "write", "delete"}
available = {"read", "write"}

missing = required - available

print(missing)
```

Output:

```text
{"delete"}
```

Ye backend authorization systems mein conceptually useful pattern hai. 

---

# Q48. Unique visitors count kaise karoge?

```python
visitors = [
    "user1",
    "user2",
    "user1",
    "user3",
    "user2"
]

unique_visitors = set(visitors)

print(len(unique_visitors))
```

Output:

```text
3
```



---

# Q49. Unique email IDs kaise find karoge?

```python
emails = [
    "a@gmail.com",
    "b@gmail.com",
    "a@gmail.com"
]

unique_emails = set(emails)
```

Result:

```text
{
    "a@gmail.com",
    "b@gmail.com"
}
```



---

# 🔥 PART 12 — ANAGRAM TRAP

# Q50. Kya Set se anagram check karna correct hai?

**Not by itself.**

Wrong approach:

```python
set("aabb") == set("ab")
```

Result:

```text
True
```

But:

```text
"aabb"
"ab"
```

anagrams nahi hain because character frequencies different hain.

Set sirf **unique characters** dekhta hai; frequency preserve nahi karta. 

Correct approach:

```python
from collections import Counter

Counter("aabb") == Counter("ab")
```

Result:

```text
False
```

### 🔥 Interview Follow-up

**Interviewer:** "To Set ka anagram mein koi use hi nahi?"

Answer:

> "Set unique-character comparison ke liye useful ho sakta hai, but complete anagram validation ke liye frequency bhi compare karni hoti hai, isliye Counter ya sorted approach better hai."

---

# 🔴 PART 13 — COMMON MISTAKES

# Q51. Ye mistake identify karo:

```python
s = {}
```

Answer:

`dict`, Set nahi.

Correct:

```python
s = set()
```

---

# Q52. Ye mistake:

```python
s = {1, 2, 3}

print(s[0])
```

Answer:

Set subscriptable/indexed collection nahi hai.

---

# Q53. Ye mistake:

```python
s = {1, 2, [3, 4]}
```

Answer:

List unhashable hai.

---

# Q54. Iteration ke andar Set modify kar sakte hain?

Dangerous/invalid pattern:

```python
s = {1, 2, 3}

for x in s:
    s.add(x + 10)
```

Ye runtime error situation create kar sakta hai because iteration ke dauran collection change ho raha hai. 

Safer approach:

```python
for x in list(s):
    s.add(x + 10)
```

---

# 🟣 PART 14 — ADVANCED INTERVIEW

# Q55. Set mutable hai ya immutable?

**Set mutable hai.**

```python
s = {1, 2}

s.add(3)
```

Valid.

Lekin Set ke **elements hashable** hone chahiye.



---

# Q56. Set aur Frozenset mein difference?

| Set              | Frozenset       |        |
| ---------------- | --------------- | ------ |
| Mutable          | Immutable       |        |
| `add()`          | No `add()`      |        |
| `remove()`       | No mutation     |        |
| Hashable itself? | Can be hashable |        |
| Dict key         | Generally not   | Can be |
| Set element      | No              | Yes    |



---

# Q57. Frozenset dictionary key kyu ban sakta hai?

Because `frozenset` immutable and hashable ho sakta hai, provided its elements hashable hain.

```python
permissions = frozenset({"read", "write"})

roles = {
    permissions: "Editor"
}
```



---

# Q58. Kya Set ke andar Frozenset rakh sakte hain?

Yes.

```python
groups = {
    frozenset({"A", "B"}),
    frozenset({"C", "D"})
}
```

Because Frozenset hashable ho sakta hai. 

---

# Q59. `union()` aur `|` exactly same hain?

Conceptually dono union perform karte hain.

Lekin important difference:

```python
A.union([1, 2])
```

method iterable ke saath work kar sakta hai.

While:

```python
A | [1, 2]
```

operator ke operands Set-compatible hone chahiye; List ke saath TypeError aa sakta hai.

Tumhare notes mein exact example diya hai. 

---

# Q60. Set mein `==` kaise kaam karta hai?

Set equality mein:

* Elements same hone chahiye.
* Order matter nahi karta.

```python
{1, 2, 3} == {3, 2, 1}
```

Result:

```text
True
```

---

# 💀 PART 15 — MENTAL INTERVIEW ROUND

Ab ye questions bachche ko **sochne** par majboor karenge.

## Q61.

```python
a = {1, 2, 3}
b = a

b.add(4)

print(a)
```

### Answer

```text
{1, 2, 3, 4}
```

Because `b = a` copy nahi hai.

---

## Q62.

```python
a = {1, 2, 3}
b = a.copy()

b.add(4)

print(a)
print(b)
```

### Answer

```text
{1, 2, 3}
{1, 2, 3, 4}
```

---

## Q63.

```python
s = {1, 2, 3}

x = s.add(4)

print(x)
```

### Answer

```text
None
```

Important: `add()` Set return nahi karta; Set ko modify karta hai.

---

## Q64.

```python
s = {1, 2, 3}

x = s.pop()

print(x)
```

### Answer

`x` ko exact value assume nahi karni chahiye. `pop()` arbitrary element remove karta hai.

---

## Q65.

```python
A = {1, 2}
B = {1, 2}

print(A < B)
print(A <= B)
print(A == B)
```

### Answer

```text
False
True
True
```

Reason:

* A proper subset nahi hai because equal hai.
* A subset hai.
* Dono equal hain.

---

# 🔥 PART 16 — INDUSTRY-LEVEL SCENARIOS

## Q66. Authentication system mein Set kahan useful hai?

Suppose:

```python
allowed_users = {
    "rohit",
    "aman",
    "sagar"
}
```

Request:

```python
username = "rohit"

if username in allowed_users:
    print("Access Granted")
```

Membership checking ke liye Set appropriate hai because average-case lookup `O(1)` hota hai. 

---

# Q67. Aapke paas 10 lakh user IDs hain. List vs Set?

Agar primary operation:

> "Kya ye user ID exist karti hai?"

hai, to Set appropriate ho sakta hai.

Reason:

```text
List → average O(n) membership
Set  → average O(1) membership
```

Lekin Set ka memory overhead higher ho sakta hai, isliye memory requirements bhi consider karni hongi.

---

# Q68. Agar user IDs ko exact insertion order mein maintain karna ho?

Sirf Set par depend nahi karna chahiye.

Requirement agar:

> uniqueness + order

hai, to data structure choice carefully karni hogi.

Tumhare notes mein bhi order-preserving duplicate removal ke liye:

```python
list(dict.fromkeys(nums))
```

approach diya gaya hai. 

---

# Q69. E-commerce application mein unique visitors count?

```python
visitors = [
    "u1",
    "u2",
    "u1",
    "u3",
    "u2"
]

unique_users = set(visitors)

count = len(unique_users)
```

Result:

```text
3
```

---

# Q70. Role-based permissions system?

```python
required = {
    "read",
    "write",
    "delete"
}

user_permissions = {
    "read",
    "write"
}
```

Missing:

```python
missing = required - user_permissions
```

Result:

```text
{"delete"}
```

---

# 🚀 Q71. Senior Interview — Set kab use nahi karna chahiye?

Set use nahi karna chahiye jab:

* Indexing required ho.
* Duplicate values preserve karni hon.
* Sequence order fundamental requirement ho.
* Positional operations important hon.

Aise case mein List jaise sequence-oriented structure better fit ho sakta hai.

Tumhare notes ki limitation section bhi indexing, slicing, duplicate preservation aur order-based operations ko Set ki limitations batata hai. 

---

# 🚀 Q72. Set ka sabse important trade-off kya hai?

### Benefit

Fast average-case membership checking.

### Cost

Hash-table structure ke karan additional memory overhead.

Interview mein ideal answer:

> "Set is not simply a faster List. It is optimized for uniqueness and hash-based membership operations, but it has different memory and ordering characteristics."

---

# 🚀 Q73. Interviewer pooche — "Set ka underlying concept kya hai?"

### Strong Answer

> "Python Set hash-table based data structure hai. Elements ko hash kiya jata hai aur hashing membership lookup ko average-case O(1) banane mein help karti hai. Isi wajah se Set unique elements aur fast membership testing ke liye useful hai."



---

# 🚀 Q74. Set ke major limitations batao.

### Answer

1. Indexing nahi.
2. Slicing nahi.
3. Duplicate values preserve nahi hoti.
4. Order-based operations ke liye suitable nahi.
5. Elements hashable hone chahiye.
6. Hash-table overhead ki wajah se memory cost ho sakti hai.
7. `sorted()` use karne par List milti hai, Set nahi.



---

# 🔥 Q75. FINAL MASTER QUESTION

Interviewer:

> **"Why would you choose Set over List in a real production application?"**

### Weak Answer ❌

> "Sir Set fast hai."

### Strong Answer ✅

> "I would choose a Set when my requirement is primarily uniqueness and fast membership checking. Set uses a hash-based structure, so membership checks are average-case O(1), whereas List membership is generally O(n). However, I would not choose Set if I need indexing, duplicate preservation, or sequence ordering. I would also consider the additional memory overhead of the hash-based structure."

**Ye answer interview mein actual understanding show karta hai.**

---

# 🧠 Bachche ko Interview ke liye kaise prepare karna hai

Main tumhare notes mein questions ko **4 layers** mein rakhne ki strongly recommendation dunga:

### Layer 1 — Remember

```text
What is Set?
What is frozenset?
What is union?
What is intersection?
```

### Layer 2 — Understand

```text
Why no indexing?
Why hashable elements?
Why O(1)?
Why {} is dict?
```

### Layer 3 — Apply

```text
Remove duplicates
Common skills
Missing permissions
Unique visitors
Membership checking
```

### Layer 4 — Think

```text
Why Set instead of List?
When should you NOT use Set?
Why Set consumes additional memory?
Why set() cannot check anagram frequency?
What happens if collection is modified during iteration?
```
