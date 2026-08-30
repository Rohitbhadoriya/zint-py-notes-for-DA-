# Set 
# A set is built-in-python data types that store an unordered collection of unique element.
# It is mutuable(You can add/ remove elements) but the elements themeselves must be immutable 
# and hashable. Sets are optimized for fast membership testing (O(1)) and mathmatical set opertaions
# (Union, intersection, difference,etc)


# Set ek built in python data type hai jo unique elements ka unordered collection store krta h
# ye mutuable hai (app elements add/remove kar skte h) par elements immutable aur hasable hone chaiye 
# sets fast memebership testing (O(1)) aur mathematical set operations (union,intersection,difference etc)
# ke liye optimized


items = [1,2,3,4,5,6,7,7,7,8,9,10,1]
unique = []
for i in items:
    if i not in unique:
        unique.append(i)
print(unique)

# Problem:2 Finding intersection 
list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
common = []
for i in list1:
    if i in list2:
        common.append(i)
print(common)

# With set => Fats and Clean 
items11 = [1,2,2,3,3,4,4,5,6,7,8]
unique11 = list(set(items11))
print(unique11)

set12 = {1,2,3,4,4}
set13 = {4,5,6,7,1}
common12 = set12 & set13
print(common12)
# my_set = set(range())

# uniqueness 
s = {1,2,2,3,3,3,4}
print(s)

# Addding Duplicate value 
s1 = {1,2,3}
s1.add(2)
print(s1)
# Different type data 
s2 = {1,10,True}
print(s2)
s3 = {1,"i",1.1,True}
print(s3)
s4 = [1,2,2,3,3,3,4,4,4,4]
uniques = set(s4)
print(uniques)