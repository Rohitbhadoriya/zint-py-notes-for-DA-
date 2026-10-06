# **Python Sets – 40 Interview Questions**  
# (20 Theory + 20 Practical)  
# Saare questions aapke notes ke concepts se hain.

# ---

# ## Part 1: Theory Questions (1–20)

# **1.** Set kya hota hai? Uske 3 main characteristics batao.

# **Answer:**  
# Unordered collection of unique elements.  
# Characteristics:  
# - Duplicates allowed nahi  
# - Indexing/slicing nahi hoti  
# - Hash table pe based → average O(1) membership

# ---

# **2.** List already hai to Set kyun use karein? 4 reasons do.

# **Answer:**  
# 1. Fast duplicate removal  
# 2. O(1) membership check  
# 3. Easy union/intersection/difference  
# 4. Unique values store karne ke liye best (visitors, emails, skills)

# ---

# **3.** Empty set kaise banate hain? `{}` se kyun nahi banta?

# **Answer:**  
# `s = set()` se banta hai.  
# `{}` Python mein dictionary ke liye reserved hai.

# ---

# **4.** Set ke elements hashable kyun hone chahiye?

# **Answer:**  
# Set hash table use karta hai. Har element ka hash calculate hota hai. Mutable objects (list, dict, set) ka hash stable nahi hota, isliye TypeError aata hai.

# ---

# **5.** `add()` aur `update()` mein kya farak hai?

# **Answer:**  
# - `add()` → sirf ek element add karta hai  
# - `update()` → multiple elements (kisi bhi iterable se) add karta hai  
# Dono in-place hote hain aur `None` return karte hain.

# ---

# **6.** `remove()`, `discard()` aur `pop()` ka clear difference batao.

# **Answer:**  

# | Method    | Element na mile to | Return          |
# |-----------|--------------------|-----------------|
# | remove()  | KeyError           | None            |
# | discard() | Silent             | None            |
# | pop()     | KeyError (empty)   | Removed element |

# ---

# **7.** Set mutable hai ya immutable? Uske elements?

# **Answer:**  
# Set khud **mutable** hai, lekin uske elements **immutable (hashable)** hone chahiye.

# ---

# **8.** Union, Intersection, Difference, Symmetric Difference ke operators aur methods likho.

# **Answer:**  
# ```
# |  / .union()
# &  / .intersection()
# -  / .difference()
# ^  / .symmetric_difference()
# ```

# ---

# **9.** Operators (`| & - ^`) aur Methods mein kya farak hai?

# **Answer:**  
# Operators sirf set ke saath kaam karte hain.  
# Methods kisi bhi iterable (list, tuple, set) ko accept karte hain.

# ---

# **10.** In-place update methods kaunse hain?

# **Answer:**  
# `update()`, `intersection_update()`, `difference_update()`, `symmetric_difference_update()`

# ---

# **11.** `issubset()`, `issuperset()`, `isdisjoint()` kya karte hain? Unke operators bhi batao.

# **Answer:**  
# - `A.issubset(B)` → `A <= B`  
# - `A.issuperset(B)` → `A >= B`  
# - `A.isdisjoint(B)` → koi common element nahi  
# Proper subset/superset ke liye `<` aur `>` use hote hain.

# ---

# **12.** Frozenset kya hai? Kab use karte hain?

# **Answer:**  
# Frozenset immutable set hai.  
# Use cases:  
# - Dictionary key banana  
# - Set ke andar set rakhna  
# - Constant data ke liye

# ---

# **13.** Set ki time complexity batao (add, membership, remove).

# **Answer:**  
# Average case: O(1)  
# Worst case (hash collision): O(n)

# ---

# **14.** Set iterate karte waqt modify kyun nahi kar sakte?

# **Answer:**  
# Size change hone se RuntimeError aata hai.  
# Solution: pehle `list(s)` bana lo.

# ---

# **15.** `list(set(my_list))` order preserve kyun nahi karta? Alternative kya hai?

# **Answer:**  
# Set unordered hota hai.  
# Alternative: `list(dict.fromkeys(my_list))` (Python 3.7+)

# ---

# **16.** Anagram check ke liye set kyun galat hai?

# **Answer:**  
# Set sirf unique characters dekhta hai, frequency nahi.  
# Sahi tareeka: `collections.Counter`

# ---

# **17.** Set comprehension ka syntax aur use batao.

# **Answer:**  
# ```python
# {expression for item in iterable if condition}
# ```
# Ek line mein set banane ke liye use hota hai.

# ---

# **18.** `sorted()` set pe lagane se kya return hota hai?

# **Answer:**  
# Ek **list** return hoti hai, set nahi.

# ---

# **19.** Set ki 5 major limitations batao.

# **Answer:**  
# 1. Indexing nahi  
# 2. Slicing nahi  
# 3. Order guaranteed nahi  
# 4. Elements hashable hone chahiye  
# 5. Duplicate preserve nahi hote

# ---

# **20.** Real-world mein Set ke 4 common use-cases batao.

# **Answer:**  
# 1. Unique visitors / unique emails  
# 2. Fast membership check  
# 3. Common skills / common friends (intersection)  
# 4. Missing permissions (difference)

# ---

# ## Part 2: Practical Questions (21–40)

# **21.** Empty set banao aur check karo ki empty hai ya nahi.

# **Solution:**  
# ```python
# s = set()
# print(len(s) == 0)      # True
# print(bool(s))          # False
# ```

# ---

# **22.** String se unique characters nikaalo.

# **Solution:**  
# ```python
# s = set("hello world")
# print(s)
# ```

# ---

# **23.** List se duplicates hatao (order matter nahi karta).

# **Solution:**  
# ```python
# nums = [1, 2, 2, 3, 3, 3, 4]
# unique = set(nums)
# print(unique)
# ```

# ---

# **24.** Output predict karo:
# ```python
# s = {1, 2, 3}
# print(s.add(4))
# print(s)
# ```

# **Solution:**  
# ```
# None
# {1, 2, 3, 4}
# ```

# ---

# **25.** `remove()` vs `discard()` ka difference code se dikhao.

# **Solution:**  
# ```python
# s = {1, 2, 3}
# s.discard(10)     # No error
# # s.remove(10)    # KeyError
# ```

# ---

# **26.** Do sets ka union, intersection, difference nikaalo.

# **Solution:**  
# ```python
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A | B)
# print(A & B)
# print(A - B)
# ```

# ---

# **27.** In-place intersection update karo.

# **Solution:**  
# ```python
# A = {1, 2, 3, 4}
# B = {3, 4, 5}
# A.intersection_update(B)
# print(A)   # {3, 4}
# ```

# ---

# **28.** Check karo `{1, 2}` , `{1, 2, 3, 4}` ka subset hai ya nahi.

# **Solution:**  
# ```python
# A = {1, 2}
# B = {1, 2, 3, 4}
# print(A.issubset(B))   # True
# print(A < B)           # True (proper)
# ```

# ---

# **29.** Set comprehension se 1–20 ke even numbers banao.

# **Solution:**  
# ```python
# evens = {x for x in range(1, 21) if x % 2 == 0}
# print(evens)
# ```

# ---

# **30.** Frozenset banao aur dictionary key banao.

# **Solution:**  
# ```python
# fs = frozenset(["read", "write"])
# roles = {fs: "Editor"}
# print(roles[fs])
# ```

# ---

# **31.** List se duplicates hatao **order preserve** karke.

# **Solution:**  
# ```python
# nums = [3, 1, 3, 2, 1, 4]
# unique = list(dict.fromkeys(nums))
# print(unique)   # [3, 1, 2, 4]
# ```

# ---

# **32.** Do lists ke common elements nikaalo.

# **Solution:**  
# ```python
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7]
# common = set(list1) & set(list2)
# print(common)
# ```

# ---

# **33.** Unique visitors count nikaalo.

# **Solution:**  
# ```python
# visitors = ["u1", "u2", "u1", "u3", "u2"]
# print(len(set(visitors)))   # 3
# ```

# ---

# **34.** Missing permissions nikaalo.

# **Solution:**  
# ```python
# required = {"read", "write", "delete"}
# available = {"read", "write"}
# missing = required - available
# print(missing)   # {'delete'}
# ```

# ---

# **35.** Symmetric difference nikaalo.

# **Solution:**  
# ```python
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# print(A ^ B)   # {1, 2, 5, 6}
# ```

# ---

# **36.** Output predict karo:
# ```python
# s = {10, 20, 30}
# print(s.pop())
# print(s)
# ```

# **Solution:**  
# Koi bhi ek element print hoga (order guaranteed nahi), baaki set mein rahenge.

# ---

# **37.** Set ko iterate karte waqt safely modify karo.

# **Solution:**  
# ```python
# s = {1, 2, 3}
# for x in list(s):
#     s.add(x + 10)
# print(s)
# ```

# ---

# **38.** Function likho jo do lists ka symmetric difference return kare.

# **Solution:**  
# ```python
# def sym_diff(a, b):
#     return list(set(a) ^ set(b))
# ```

# ---

# **39.** Check karo do sets disjoint hain ya nahi.

# **Solution:**  
# ```python
# A = {1, 2, 3}
# B = {4, 5, 6}
# print(A.isdisjoint(B))   # True
# ```

# ---

# **40.** Practical: Do developers ki common skills aur sirf pehle developer ki unique skills nikaalo.

# **Solution:**  
# ```python
# dev1 = {"Python", "SQL", "Git", "Docker"}
# dev2 = {"Python", "React", "Git"}
# common = dev1 & dev2
# only_dev1 = dev1 - dev2
# print(common)
# print(only_dev1)
# ```

# ---

# **Summary for Interview:**

# - Theory mein clear definitions + differences + time complexity  
# - Practical mein output prediction + real use-cases + short code  

# Agar aapko in questions ka **PDF format**, ya **answers ke saath detailed explanation**, ya **sirf coding problems** chahiye to bata dena.