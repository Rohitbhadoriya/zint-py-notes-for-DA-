# A function is block of code which only runs when it is called
# A function can return data and result
# A function helps avoiding code reptition
# In a python a function is defined using the def keyword 
# followed by a function name and paraentheses
# welcomeback = "Hello Wlecomeback"
# kuchnaya = welcomeback * 10
# print(kuchnaya)
def my_function():
    print("Hello from a function")

my_function()
def sanamteriksm():
    print("This movie very closed to my heart")
list12 = [1,2,3,4,5,6]
print(list12)
my_function()
sanamteriksm()

temp1 = 77
celsius1 = (temp1 - 32) *5/9
print(celsius1)
temp2 = 92
celsius2 = (temp2 - 32) * 5/9
print(celsius2)
temp3 = 50
celsius3 = (temp3 - 32) * 5/9
print(celsius3)


def fahrenit_to_celsisus(fahrenheit):
   return(fahrenheit - 32) * 5/9
print(fahrenit_to_celsisus(77))
print(fahrenit_to_celsisus(55))
print(fahrenit_to_celsisus(77))

# Return : Functions can send data back to the code that called 
# them using the return statement
# When a function reaches a return statement it stops executing and sends teh result back 

def greet_msg():
    return "Hello a from function"
msg = greet_msg()
print(msg)
def greet2_msg():
    return "hello a from other function"
print(greet2_msg())

def my_function2(fname):
    print(fname + " Singh")
my_function2("Sejal")
my_function2("Khusi")
my_function2("Shivam")

# Parameters and arrguments
def my_argu(name):
    # this parammeter
    print(name + " kalra")
my_argu("Sejal")
my_argu("Shivam")
my_argu("prachi")
# isko bolte argument

def addtion_fu(n,n2):
    return n + n2
print(addtion_fu(4,5))
print(addtion_fu(4,0))
print(addtion_fu(97,5))

def sub(n,n2):
    return n - n2
print(sub(4,5))
print(sub(4,0))
print(sub(97,5))

def tw_argu(name,email):
    print(name + " " + email)
tw_argu("rohit","rohit@gmail.com")

def value_set(name = "Freind"):
    print("Hello", name)
value_set()
value_set("Sohan")


# items1 = [{"price":100,"qty":2},{"price":50,"qty":3}]
# total1 = 0
# for i in items1:
#     total1 += i["price"]*i["qty"]
# tax1 = total1 * 0.18
# discount1 = 50 if total1 > 500 else 0
# final1 = total1 + tax1-discount1
# print(final1)

# Ye hum jyda use nhi krnge kyu ki is se sqeuenxes ka pota nhi chlta h 
def create_user(name,age,gender):
    return{
        "name":name,
        "age":age,
        "gender":gender
    }
user12 = create_user("Rohit",25,"Male")
print("mein user12", user12)


# anoter method cretae user 
def another_user(name,age,std):
    return{
        "name":name,
        "age":age,
        "std":std
    }
user13 = another_user(name="Rohit",age=29,std=12)
print(user13)
user14 = another_user(std=11,age=26,name="Sejal")
print(user14)

# How it works 
# Python map argumnets name to parameter names
# Order doesn't matter - names are matched
# Each Paramater gets its value by name



def anotgher_item(item,items=[]):
    items.append(item)
    return items
print(anotgher_item("rohit"))
print(anotgher_item("Sejal ko bhoot a gaye"))
print(anotgher_item("khushi puch puch ke pareshan"))
print(anotgher_item("master puch puch ke pareshan bhoot naam kya"))
# print(anotgher_item())

def an_items(item,items=None):
    if items is None:
        items = []
        items.append(item)
        return items
# print(an_items())
print(an_items("Sejal ko Baba Rehmani pr le jao"))



def calculate_total(*tt):
    return sum(tt)
print(calculate_total(10,20,30))
print(calculate_total(45,56,78,98))

# def log_msg(level, *messages):
#     timestamp = datetime.now()

def create_user(**tcv):
    return tcv
user12 = create_user(name="Rohit",age=25)
print(user12)

# industires used 
# server create
def configure_server(host="localhost",port=8080, **options):
    config = {
        "host":host,
        "port":port,
        **options
    }
    return config
config12 = configure_server(host = "0.0.0.0", debug = "True", workers = 4, ssl = True)



# Method Posotional only parameters force postional argumnets

def create_rectangle(width,length,/,color = "red",outline=True):
    return{
        "width":width,
        "length":length,
        "color":color,
        "outline":outline


    }

rect1 = create_rectangle(10,20)
print(rect1)
rect2 = create_rectangle(10,20, color="blue")
print(rect2)

# Keyword only argument
def create_user(name,*,age=None, city=None, phone=None):
    user34 = {"name":name}
    if age is not None:
        user34["age"] = age
    if city is not None:
        user34["city"] = city
    if phone is not None:
        user34["phone"] = phone
    return user34
userr = create_user("Rohit",age=29,city = "Hyderabad")
print(userr)


# Return Statement - Complete guide
# return x (when to use: simple output) easy to use
# return x,y Multiples values unpacking
# return [1,2,3] multiple values ietraiion
# return {"a":1} Names values Readable
# return or return None No output side effects
# yield x large data memory effuency 

def add(a,b):
    return a+b
resultr = add(2,3)
print(resultr)

def get_user_stats(user_id):
    return user_id,"Rohit",25,"active"
user_id,name,age,status = get_user_stats(104)
print(f"User {user_id}:{name},{age}years,{status}")

# Default Parameters (optional values)
def insta_user(name,age=18, city="unknown",active=True):
    return{
        "name":name,
        "age":age,
        "city":city,
        "active":active
    }
isnta1 = insta_user("rohit-123")
print(isnta1)
inst2 = insta_user("priya_dev",age=25,city="Mumbai")
print(inst2)
inst3 = insta_user("amit_007",age=43,active=False)
print(inst3)

# *args Unknown Number of Positional Arguments

def calculate_avg(*args):
    if not args:
        return 0
    total  = sum(args)
    avg = total/len(args)
    return avg
print(calculate_avg(10,20,30))

# *args el tuple (list jaisa banata hai)
# sab postional agruments us tuple atte hain
# args ka naam kuch bi ho skta h (par *args  he use krte hain)

# Python sab ectra positional argumnets utahta hai
# Unko ek tuple mein pack krta hai
# Function ko wo tuple milta hai
# Aap args ko iterrate kr skte hai index use kr skte ho

# *args Use kab kre
# jab hume pta nhi ho ki kitne arguments pass hone wale h 
# jab number of arguments variable hai
# jab wrapper  function bana rha ho
# jab exsiting function modify krna ho 
# 
# One example bank software

def sum_transicitions(*ammounts):
    return sum(ammounts)

print(sum_transicitions(100,345.67,234,45,6,7,8,90))

# Data Science 

def calculate_stats(*numbers):
    if not numbers:
        return None
    return{
        "min":min(numbers),
        "max":max(numbers),
        "avg":sum(numbers)/len(numbers),
        "count":len(numbers)
    }
stats = calculate_stats(10,20,30,40,50,60,7080)
print(stats)

# Logging error handling

def log_errors(error_level, *msg):
    print(f"[{error_level}]")
    for msgs in msg:
        print(f"{msgs}")
log_errors("crictical", "DB Down","Retry Failed","Sysytem unstable") 


# **kwargs Unknown Number of keyword arguments
def create_user_profile(**kwargs):
    """
    Keyword arguments se user profile banata hai.
    
    **kwargs = Variable number of keyword arguments
    """
    # Default values
    profile = {
        "name": "Unknown",
        "age": 0,
        "city": "Unknown"
    }
    
    # Update with provided values
    for key, value in kwargs.items():
        profile[key] = value
    
    return profile

# ========== ALAG-ALAG TAREEKE SE CALL KARNA ==========

user1 = create_user_profile(name="Rohit", age=25, city="Delhi")
print(user1)  # {'name': 'Rohit', 'age': 25, 'city': 'Delhi'}
# **kwargs ek dict banata hai 
# sab keyword arguments us dict mein ate hai
# IOnternal Woprking
# Python sab extra keyword arguments uthata hai
# Unko ek dictionary mein pack krta hai
# app kwrgs.item() , kwrgs.get('key') use kr skte ho

# use kba krna chaiye 

# jab hume pta nhi ho ki kitne arguments pass hone wale h 
# jab flexible configuration chaiye ho 
# jab api forward compatiable rkhan ho
# jab dyanmic attributes add krne ho 

# Kb use na krein 
# jab parameteres secific ho mtlb ki define ho 
# jab type saftey chaiye ho 
# jab documnetation imp ho 

# Positional -  only paramters
# ========== CODE ==========
def create_rectangle(width, height, /, color="red", outline=True):
    """
    Rectangle banata hai.
    
    width aur height POSITIONAL-ONLY hain (name se nahi de sakte)
    color aur outline keyword se de sakte ho
    """
    return {
        "width": width,
        "height": height,
        "color": color,
        "outline": outline
    }

# ========== SAHI CALLS ==========

#  width aur height positional dena (mandatory)
rect1 = create_rectangle(10, 20)
print(rect1)  # {'width': 10, 'height': 20, 'color': 'red', 'outline': True}

# color aur outline keyword se de sakte ho
rect2 = create_rectangle(10, 20, color="blue", outline=False)
print(rect2)  # {'width': 10, 'height': 20, 'color': 'blue', 'outline': False}

# ========== GALAT CALLS ==========

#  width aur height keyword se nahi de sakte
# rect3 = create_rectangle(width=10, height=20)  # TypeError!

#  width/height ke baad / hai, isliye positional hi honge
# rect4 = create_rectangle(10, 20, color="blue")  # Works! color keyword hai

# ========== LINE-BY-LINE EXPLANATION ==========

"""

KYA HOTA HAI POSITIONAL-ONLY MEIN:

1. Parameter name use karke value nahi de sakte
2. Sirf position se value milegi
3. Function ke ANDAR toh name se use kar sakte ho

KYON USE KAREIN:
1. Order enforce karna - order matters hai toh
2. API future-proof - parameter rename kar sakte ho
3. Mathematical functions - sin, cos mein order important hai
4. Parameter names meaningless hain toh

KAB USE KAREIN:
 Jab order critically important hai
 Jab parameter names meaningful nahi hain
 Jab mathematical operations hain
 Jab API backward compatibility chahiye

KAB USE NA KAREIN:
Jab readability important hai (keyword arguments zyada clear hain)
 Jab zyada parameters hain
 Jab optional parameters hain
 Jab code review mein clarity chahiye
"""

# ========== INDUSTRY EXAMPLE ==========

#  MATHEMATICAL OPERATIONS
def distance(x1, y1, x2, y2, /):
    """
    Do points ke beech distance calculate karta hai.
    
    Points ke coordinates positional-only hain.
    Kyunki order important hai - x1, y1 pehla point, x2, y2 dusra point
    """
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

#  SAHI
d = distance(0, 0, 3, 4)  # (0,0) se (3,4) tak distance
print(d)  # 5.0

#  GALAT - Keyword nahi de sakte
# d = distance(x1=0, y1=0, x2=3, y2=4)  # TypeError!

# GEOMETRY
def point(x, y, /, label="P"):
    """
    Point create karta hai.
    x, y positional-only hain, label optional hai.
    """
    return {"x": x, "y": y, "label": label}

p1 = point(3, 4)
p2 = point(5, 6, label="Q")
print(p1)  # {'x': 3, 'y': 4, 'label': 'P'}
print(p2)  # {'x': 5, 'y': 6, 'label': 'Q'}


#  Keyword-Only Parameters (*) - Force Keyword Arguments

def create_user(name, *, age=None, city=None, phone=None, email=None):
    """
    User create karta hai.
    
    name positional hai (required)
    baaki sab KEYWORD-ONLY hain (name se hi de sakte ho)
    """
    user = {"name": name}
    
    # Optional fields add karo
    if age is not None:
        user["age"] = age
    if city is not None:
        user["city"] = city
    if phone is not None:
        user["phone"] = phone
    if email is not None:
        user["email"] = email
    
    return user

# ========== SAHI CALLS ==========

# name positional, baaki keyword
user17 = create_user("Rohit", age=25, city="Delhi", phone="1234567890")
print(user17)  # {'name': 'Rohit', 'age': 25, 'city': 'Delhi', 'phone': '1234567890'}

# Sirf name do, baaki optional
user2 = create_user("Priya")
print(user2)  # {'name': 'Priya'}

# Kisi bhi order mein keyword de sakte ho
user3 = create_user(
    "Amit",
    email="amit@mail.com",
    city="Mumbai",
    age=30
)
print(user3)  # {'name': 'Amit', 'age': 30, 'city': 'Mumbai', 'email': 'amit@mail.com'}

# ========== GALAT CALLS ==========

#  age keyword nahi de sakte (positional nahi chalega)
# user4 = create_user("Rohit", 25, "Delhi")  # TypeError!

# city keyword nahi de sakte
# user5 = create_user("Rohit", "Delhi")  # TypeError!
