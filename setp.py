items = [1,2,3,4,5,6,7,7,7,8,9,10,1]
unique = []
for i in items:
    if i not in unique:
        unique.append(i)
print(unique)


list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
common = []
for i in list1:
    if i in list2:
        common.append(i)
print(common)

items1 = [1,2,3,4,5,6,7,7,7,8,9,10,1]
unique1 = list(set(items1))
print(unique1)

myset = {
    "apple", 
    "Banana" , 
    "cherry"
    }
print(myset)
print(type (myset))

myset1 = {
    "Rohit",
    "Sohan",
    "ANchal",
    "Subh",
    25,
    28,
    True,
    1,
    0,
    False
}
print(myset1)

# Set items Data Types
set1 = {"apple", "Banana", "Cherry"}
set2 = {1, 5, 7, 8, 9}
set3 = {True, False, True}
print(set1)
print(set2)
print(set3)


# Constructor Method
thisset1 = set(("Kanchan","Falguni","Deeksha","Swati"))
print(type(thisset1))
print("Swati" in thisset1)
print("Rohit" not in thisset1)
thisset1.add("Mansee Don")
print(thisset1)

# Update
thiset2 = {"kiwi","Dragon Fruit","Chikoo"}
tropical = {"pineapple","mango","papaya"}
thiset2.update(tropical)
print("mein update hu", thiset2)


# Remove
# To remove an item in a set use he remove(), or he discard() method
removeset3 = {"kiwi","Dragon Fruit","Chikoo", "Kiwi"}
removeset3.remove("kiwi")
print(removeset3)


zintstrdnt = {"Monika","Nishank","Riya","Kanchan","Mansee","Kiran","Monika","Rohit","Riya"}
# zintstrdnt.discard("Monika")
# zintstrdnt.pop()
# print(zintstrdnt)

x = zintstrdnt.pop()
print(x)
print(zintstrdnt)


# => The union() method returns a new set with all items from both setrs
set12 = {"name","age","gender"}
set13 = {"Rohit",25,"Male"}
set14 = set12.union(set13)
print("mein union hu", set14)


set15 = {"name","age","gender"}
set16 = {"rohit",24,"male"}
# set17 = set15 + set16
set17 = set15 | set16
print(set17)


set18 = {"a","b","c"}
set19 = {1,2,3}
set20 = {"jhon","apple","cat"}
set21 = {"amma","apppa","guru","karan"}
myset134 = set18.union(set19,set20,set21)
print(myset134)


# Questions
names = [
    "Rohit",
    "Amit",
    "Rohit",
    "Priya",
    "Amit",
    "Neha",
    "Priya"
]

# Set ka use karke unique names nikalo.
unique_names = set(names)

print(unique_names)

# amazon = {"mobile", "laptop", "watch", "keyboard"}

# flipkart = {"mobile", "watch", "mouse", "keyboard"}
# Dono websites par available products.
# Sirf Amazon ke products.
# Sirf Flipkart ke products.
# Total unique products.


amazon = {"mobile", "laptop", "watch", "keyboard"}
flipkart = {"mobile", "watch", "mouse", "keyboard"}

# 1. Common
print(amazon.intersection(flipkart))

# 2. Only Amazon
print(amazon.difference(flipkart))

# 3. Only Flipkart
print(flipkart.difference(amazon))

# 4. Total unique
print(amazon.union(flipkart))



# python = {"Rohit", "Amit", "Neha", "Priya"}

# javascript = {"Amit", "Priya", "Rahul", "Neha"}

# react = {"Neha", "Priya", "Karan"}

# Python + JavaScript students.
# JavaScript + React students.
# Sirf Python students.
# Total unique students.





python = {"Rohit", "Amit", "Neha", "Priya"}
javascript = {"Amit", "Priya", "Rahul", "Neha"}
react = {"Neha", "Priya", "Karan"}

# 1. Python + JavaScript
print("df",python.intersection(javascript))

# 2. JavaScript + React
print("kk",javascript.intersection(react))

# 3. Only Python
print("kucku", python.difference(javascript))

# 4. Total unique students
print("sab", python.union(javascript, react))