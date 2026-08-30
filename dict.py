# what is dictonary 
# A Dictonary is a built in python types that stores date in key and value pairs
#  It is and unordered list (Python 3.7+ maintains insertion orders). mutubale are indexed collection 


phonebook = {
    "Mum": 9126775106,
    "Dad": 8744097045,
    "Me": 9533725861,
}
print(phonebook)

# Why Dict Exists 

names = ["Rohit","Falguni","Kanchan","Deeksha","Punisha","Arpita","Archit","Mohit"]
ages = [30,27,31,30,32,32,30,31]
city = ["Gwalior","London","California","Delhi","Canda","Punjab","Chennai","Gwalior"]
archit_index = names.index("Archit")
# print(archit_index)
archit_age = ages[archit_index]
print(archit_age)


# sloutions with dictonary

dost = {
    "Rohit":{"age":25,"city":"Gwalior"},
    "Falguni":{"age":27,"city":"London"},
    "Kanchan":{"age":31,"city":"California"}
}


# falni_singh = dost["Kanchan"]["age"]
# print(falni_singh)
print(dost["Kanchan"]["age"])

# When to use dict

school_students = {
    "name":"Shubh Sharma",
    "age":48, 
}

user_data={
    "id":101,
    "name":"Shivam"
}

product_db = {
    "P001":{"name":"laptop","price":23456}
}

# api in json 
api_response = {
    "status":"success",
    "data":[{}]
}

gropued_data = {
    "fruits":{"apple","banana","grapess"},
    "veggies":{"carrot","raddish"}
}

# Don't use Dict
fruits = ["apple","grappes","Papaya"]
days = ["Monday","Tuesday"]
num1 = [1,2,3,4]

for i in range(50):
    print(i)

# Memory is very limited
# Dict takes more memory than list

# Youu need mathmatical operations
# (sum, average,etc. on values only)



# KEY (Label) → VALUE (Content)
kitchen = {
    "Sugar": "1 kg white sugar",      # "Sugar" is key, "1 kg white sugar" is value
    "Salt": "500 gm pink salt",        # "Salt" is key, "500 gm pink salt" is value
    "Tea": "Assam tea leaves"          # "Tea" is key, "Assam tea leaves" is value
}

# Get Sugar content using the key
sugar_content = kitchen["Sugar"]  # "1 kg white sugar"
print(sugar_content)

# What is mutuable 
# Mutuable means you can chnage/ modify the after creation 


# Dicitionaries Mutuabel 
student_name = {
    "name":"Deeksha",
    "age":20
}
print("Whole data print:", student_name)


# Change exisiting value 
student_name["age"] = 25
print("after update:",student_name)

student_name["city"] = "Gwalior"
print("Second Update :", student_name)

del student_name["city"]
print("Third Update :", student_name)

print(len(student_name))
xx = student_name.get("age")
print(xx)

print(student_name["name"],student_name["age"])
yz = student_name.keys()
print(yz)

mereko = "mein hu deeksha"
mujheto = mereko
print(mujheto)
mereko = "kuch kuch hota hai"
print(mereko)
print(mujheto)

# Create Dict
empty = {}
print(empty)
print(type(empty))
print(len(empty))


# Dict with string key 
students = {
    "name":"Deeksha Gupta",
    "age":25,
    "course": "Full Stack",
    "is_active":True
}
print(students)
print(students["name"])

# Dict with numberic key
students1 = {
    1:"One",
    2:"Two",
    3:"Three"
}
# mixed Types Data
mixedtypes_data = {
    "name":"Shubh Sharma",
    "age":19,
    "marks":[85,79,60],
    "address":{"city":"Delhi","pincode":23456},
    "is_active":True,
    "salary":50000.989

}
print(mixedtypes_data["address"]["city"])

# dict() cosntructor
# The dict() constructor create a dict from various user_data
# sources, keyword arguments list of tupels or two parallel 
# squence (using zip())


student123 = dict(names="Rohit",age= 30, city="Delhi")
print(student123)
# From List To Tupls
pairs = [("name", "Rohit"), ("age", 34)]
print(pairs)
students1234 = dict(pairs)
print(students1234)


# Key Values
keys = ["name","age","city"]
values = ["Rohit",28,"Delhi"]

ss123456 = dict(zip(keys,values))
print(keys)
print(ss123456)

#  From Genrator Expression 
squares = dict((x,x**2)for x in range(0,5))
print(squares)


# fromkeys() Same value for all keys
# formkeys() creates a new dictionary with keys from the 
# given squence and all values set to the same default value 

# formkeys ke naya dict banata hai jismein keys 
# given sequence se ati hain aur sabhi vakues ek he default value set hoti hai 
keys = ["name","age","city"]
default_dict = dict.fromkeys(keys,"Unknown")
print(keys)
print("Default Dict", default_dict)

# without default value none

keys1 = ['a','b','c']
emp_dict = dict.fromkeys(keys1)
print("emo_dic", emp_dict)

# From A String
result12 = dict.fromkeys("ABC",0)
print(result12)

# From A Range 
result13 = dict.fromkeys(range(1,10),"Empty")
print(result13)

# Dangerous - Mutuable default (All share smae object)
bad = dict.fromkeys(["a","b","c"],[])
print(bad)

# good wauy
good = {keys3:[] for keys3 in ["name","age","gender"]}
good["name"].append("Umang")
good["age"].append(30)
good["gender"].append("Male")
print("Umang to makkar h...", good)

# dictionary Comprehension
# Basic squres
squres = {x: x**2 for x in range(1,6)} 
print(squres)
even_squres = {x: x**2 for x in range(1,20) if x %2 == 0}
print(even_squres)
odd_squres = {x:x**2 for x in range(1,25) if x %2 ==1}
print(odd_squres)

# The items() method in a Python dictionary returns a view object 
# containing the dictionary's 
# key-value pairs as a list of tuples. 
# This method is primarily used to loop through a dictionary and 
# access both the keys and their corresponding values simultaneously.
# Syntax and Return ValueSyntax: dictionary.items()Parameters:
# NoneReturn Type: A dynamic dict_items view object. 
# This view automatically updates if the underlying dictionary changes.
prices = {"apple":100, "banana":50, "orange":45, "grapess": 120}
discounted = {item: price * 0.9 for item, price in prices.items()}
print(discounted)

high_price = {item: price for item,price in prices.items() if price > 70}
print(high_price)

# Swap value 
original1 = {"a":1,"b":2,"c":3}
swapped = {value: papakipari for papakipari,value in original1.items()}
print(swapped)

# Form the list wuth ZIP
# zip defination
# The Python zip() function takes multiple iterables (like lists, tuples, or strings) and aggregates 
# their corresponding elements into an iterator of tuples. 
# It acts like a physical zipper, locking matching elements together by their index

names = ["Rohit", "Falguni","Deeksha"]
ages = [29,26,29]
final = {name:age for name,age in zip(names,ages)}
print(final)

# Nested
matrix = {i:{i*j for j in range(1,9)} for i in range(1,4)}
print(matrix)

# with Enumerate
items1 = ["Apple","Banana", "Orange"]
index1 = {index: item for index,item in enumerate(items1)}
print(index1)
# Conditional Expression 

numbers12 = [1,2,3,4]
label = {x:"even" if x % 2 == 0 else "odd" for x in numbers12}
print(label)

# Method Default Dict No More KeyError
# defaultdic is a subclass of dict that provides a default value 
# for missing keys. When you access a missing key 
# it automatically creates it with default value

from collections import defaultdict
text12 = ["apple","banana","apple","orange","apple","banana"]
count12 = defaultdict(int)
# print(count12)
for wo in text12:
    count12[wo] += 1
print(count12)
# Grouping With list Default (list()->[])
data1 = [
    ("fruit", "apple"),
    ("fruit","banana"),
    ("veggie","carrot"),
    ("fruit","grapes"),
    ("veggie","raddish")

]

grouped_data1 = defaultdict(list)
for ram,item in data1:
    grouped_data1[ram].append(item)
print(grouped_data1)

# set default 
sets = defaultdict(set)
sets["fruits"].add("apple")
sets["veggies"].add("raddish")
sets["fruits"].add("banana")
sets["veggies"].add("carrot")
print(sets)

# Dict Default Factory
nested = defaultdict(dict)
nested["full"]["name"] = "Deeksha"
nested["full"]["age"] = 25
nested["full"]["city"] = "Gwalior"
nested["full"]["course"] = "Full Stack"
print(nested)

# Custom Default Factory
# def default_factory():
# return{"count":1,"items":[]}
# custom = defaultdict(default_factory)
# custom["fruits"]["items"].append("apple")
# custom["fruits"]["items"].append("banana")
# custom["veggies"]["items"].append("carrot")
# print(custom)
# isko hum dekh lenge jab hum def padhengye mtlb function padhengye


# Creatinhg From Other Data Types
# From list of lists
convert_dict = dict([["name","Deeksha"],["age",25],["city","Gwalior"]])
print(convert_dict)
# From list of tuples
convert_tuples = [("name","Falguni"),("age",25),("city","Gwalior")]
change_dict  = dict(convert_tuples)
print(change_dict)
# From Zip
keys1 = ["name","age","city"]
values1 = ["Tanisq",25,"Gwalior"]
zip_dict = dict(zip(keys1,values1))
print(zip_dict)
# From Json 
import json
json_data = '{"name":"Umang","age":25,"city":"Gwalior"}'
dict_from_json = json.loads(json_data)
print(dict_from_json)
# json.load () ek function hai jo json data ko python dict me convert karta hai


# Accessing Dict Elements
# The squre brackets dict[key] is the fatstes way 
# to access a value but it raises a KeyError if the key does not exist.
student_data = {
    "name":"Adarsh Jadon",
    "age":20,
    "city":"Edori"

}
print(student_data["name"])
# missing key find 
# print(student_data["phone"])

users_data1 = {
    "id":101,
    "name":"Shivam",
    "email":"shivam@example.com",
    "address":{
        "street":"123 Main St",
        "city":"Edori",
        "zip":12345
    }
}

print(users_data1["address"]["zip"])

# When to use []
# you are sure the key exists
# you want the program to crash if key ios missing 
# performance is criticial ([] is slightly faster)
# keys are perfom your owb device (constants configurations, etc.)
# Don't use []
# key might be missing (user input, API Data)
# Production code (unless guranted)
# you want to handle missing keys gracefully (default values, etc.)
 

# 4.2 Method 2: .get() Method Safe Access
# The .get(key,default = None) method returns the value for the key
# if its exists otherwise returns the default value (None if not specified)
# It never raises akeyerror
 
student_data1 = {
    
    "name":"Annu Sharma Pagal",
    "age":25,
    "city":"Datia"
}
annu_city = student_data1.get("city")
print(annu_city)
# Basic usage: Missing key returns None
annu_phone = student_data1.get("phone")
print(annu_phone)

# with default key  
annu_phonedevalur = student_data1.get("phone","Not Available")
print(annu_phonedevalur)

# with default for existing key 
annu_city1 = student_data1.get("city","Not Available")
print(annu_city1)

# Safe nested access (Chained.get())
user_data = {

    "id":101,
    "name":"Shivam",
    "email":"shivam@gmail.com",
    "address":{
        "street":"123 Main St",
        "city":"London",
        "zip":12345
    }
}

usercity = user_data.get("address",{}).get("city")
print(usercity)

# address is missing 
usercity1 = user_data.get("adress1",{}).get("city","Not Available")
print(usercity1)


# Lambda Function

def get_address():
    print("This is a normal function")
    return{"city":"Delhi"}
usercity1 = user_data.get("address",get_address())
print(usercity1)

# 4.3 Method 3: .setdefault() Method
# The .setdefault (key,default = None) method return the 
# value of the key if it exists. If the key 
# doesn't exists, it sets the key of the default value and return it

user_data2 = {
    "name":"Vijay Singh Bhadouriya",
    "age": 33,

}
# Existing key , Return and value doesn't change 
name1 = user_data2.setdefault("name","please enter your name")
print(name1) # Output : Vijay Singh Bhadouriya
print(user_data2) # Output : {'name': 'Vijay Singh Bhadouriya', 'age': 33}

# Missing key 
age1 = user_data2.setdefault("age",0)