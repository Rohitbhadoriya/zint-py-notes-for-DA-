# A function is block of code which only runs when it is called
# A function can return data and result
# A function helps avoiding code reptition
# In a python a function is defined using the def keyword 
# followed by a function name and paraentheses
# Scenario: 3 different orders ka total calculate karna hai

# Order 1 - Chai
items1 = [{"item": "Chai", "price": 20, "qty": 2}, {"item": "Samosa", "price": 15, "qty": 1}]
total1 = 0
for item in items1:
    total1 += item["price"] * item["qty"]
tax1 = total1 * 0.18
discount1 = 10 if total1 > 50 else 0
final1 = total1 + tax1 - discount1
print(f"Order 1 Total: {final1}")

# Order 2 - Coffee
items2 = [{"item": "Coffee", "price": 30, "qty": 1}, {"item": "Sandwich", "price": 45, "qty": 2}]
total2 = 0
for item in items2:  #  Same code dobara!
    total2 += item["price"] * item["qty"]
tax2 = total2 * 0.18
discount2 = 10 if total2 > 50 else 0
final2 = total2 + tax2 - discount2
print(f"Order 2 Total: {final2}")

# Order 3 - Pizza
items3 = [{"item": "Pizza", "price": 120, "qty": 1}]
total3 = 0
for item in items3:  #  Ek baar aur same code!
    total3 += item["price"] * item["qty"]
tax3 = total3 * 0.18
discount3 = 10 if total3 > 50 else 0
final3 = total3 + tax3 - discount3
print(f"Order 3 Total: {final3}")




# Function ke sath 

# EK BAAR FUNCTION BANAO
def calculate_order_total(items):
    # """
    # Order ka total calculate karo (tax + discount ke saath)
    
    # Ye function kya karta hai:
    # 1. Items ki price * qty karke subtotal nikalta hai
    # 2. 18% GST lagata hai
    # 3. Agar total ₹50 se zyada hai toh ₹10 discount deta hai
    # 4. Final total return karta hai
    # """
    # Step 1: Subtotal nikalna (sab items ka price * quantity)
    subtotal = 0
    for item in items:
        subtotal += item["price"] * item["qty"]
    
    # Step 2: Tax lagaana (18% GST)
    tax = subtotal * 0.18
    
    # Step 3: Discount apply karna (₹10 off agar ₹50+)
    discount = 10 if subtotal > 50 else 0
    
    # Step 4: Final total
    final_total = subtotal + tax - discount
    
    return final_total

# 🔁 AB FUNCTION KO BAAR BAAR USE KARO (Bina code duplicate kiye!)
order1_total = calculate_order_total(items1)  # Chai order
order2_total = calculate_order_total(items2)  # Coffee order
order3_total = calculate_order_total(items3)  # Pizza order

print(f"Order 1 Total: {order1_total}")
print(f"Order 2 Total: {order2_total}")
print(f"Order 3 Total: {order3_total}")


# E_commerece (Business Logic)
# Banking
# Healthcare


# How to make function 
def greet(name):
    message = f"Hello, {name}"
    return message
print(greet("rohit"))


# Function Parameter and arrguments

def create_profile(name,age,city):   # name,age,city  = Parameteres
    profile = {
        "name":name,
        "age":age,
        "city":city
    }
    return profile
user1 = create_profile("Sejal",19,"Panihar")
print(user1)
user2 = create_profile("Kushi",17,"Gwalior")
print(user2)
user3 = create_profile("Umang Singh Sikarwar",19,"Morena")
print(user3)

# Har Type ke paremeters
# Postional Parameter (order se value milna)
def create_stduent1(roll_no,name,grade):
    student12={
        "roll_no":roll_no,
        "name":name,
        "grade":grade
    }
    return student12
# firststudent = create_stduent1(101,"Sejal","A")
firststudent = create_stduent1("Sejal","A",101)

print(firststudent)

def create_product(name,price,catgeory,stock):
    return{
        "name":name,
        "price":price,
        "category":catgeory,
        "stock":stock
    }
product = create_product("Laptop",125000, "Electronice", 50)
print(product)

# Keyword Arguemnt (Name se value milta)

def create_employee(name,emp_id,dept,salary):
    employee = {
        "name":name,
        "emp_id":emp_id,
        "dept":dept,
        "salary":salary
    }
    return employee

emp2 = create_employee(
    name="Kanchan",
    emp_id="TA099",
    dept="Eng",
    salary=85000
)
print(emp2)





def send_email(
    to_email,
    subject,
    body,
    cc=None,
    bcc=None,
    attachments=None,
    priority="normal"
):
    print(f"Sending to Email: {to_email}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    print(f"Priority: {priority}")

    if cc:
        print(f"CC: {cc}")


send_email(
    to_email="rohit@company.com",
    subject="Meeting Tomorrow",
    body="Meeting At 10 AM",
    cc="manager@gmail.com",
    priority="High",
    attachments=["agenda.pdf"]
)

    
# Default Paramteer

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
rect1 = create_rectangle(10,20)
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

# How take input in function 
def twovalueadd(q,w):
    result12 = q + w
    return result12
print(twovalueadd(9,9))

def citydef1(city="Japan"):
    print(city)
citydef1("India")
citydef1()

# def studentin():
#     name = input("Enter Your Name")
#     age = input("Enter Your age")
#     city = input("Enter your city")
#     print("name",name)
#     print("age",age)
#     print("city",city)
# studentin()

# def addtion234():
#     a = int(input("Enter your number"))
#     b = int(input("Engter your second number"))
#     print(a + b)
# addtion234()

# 2.8 Mixed Parameters = All types Together

def complex_function(required_param,*args,reuired_keyword,  default_keyword = "default", **kwargs,):
    # sab type ke paramters ek sath 
    # Order of parameters
    # Postional keyword reuired
    # *args (variable postional)
    # keyword only (rquired + optional)
    # **kwargs (varibale keyword)
    print(f"Required: {required_param}")
    print(f"Args: , {args}")
    print(f"Required Keyword: {reuired_keyword}")
    print(f"Default keyword: {default_keyword}")
    print(f"kwargs:{kwargs}")
    return{
        "required":required_param,
        "args":args,
        "required_keyword":reuired_keyword,
        "default_keyword":default_keyword,
        "kwargs": kwargs
    }

result55 = complex_function(
    "hello",
    10,20,30,
    reuired_keyword = "world",
    default_keyword = "custom",
    extra1 = "value1",
    extra2 = "value2"


)


# ye function banane ke rule hota h 
# Order is imp (Paramters is order mein ana chaiye )
# Def complex_function(
# required_param => Required (postional/kyword)
# *args => varibale positional
# reuired_keyword, => keyword onolie reuired
# default_keyword = "default",  => keyword only optional
# **kwargs variable keywword
# )
# Pehele required paramterres
# phir *args
# phir required-only-paramterss
# 4 Phir **kwargs

# Wrong order
# def wrong_function(*args, required_param) Error
# def wrong_function(**kwargs, required_param) Error
# def wrong_function(required_param, **kwargs, default) Error

# Rules 
# *args ke bad kbhi **kwargs nhi a skta h 
# **kwargs humesha last mein ayega 
# Postional-Only(/) se phele *args nhi a skta h 
print(result55)

def created_advanced_user(
        username,
        *groups,
        email = None,
        phone = None,
        active = True,
        **extra_data
):
    solaraixuser = {
        "username":username,
        "groups":list(groups) if groups else [],
        "active":active,
        "email":email,
        "phone":phone
    }
    solaraixuser.update(extra_data)
    return solaraixuser
user = created_advanced_user(
    "Mohan Singh Bhadoriya",
    "admins","managers","Developers",
    email="mohan@gmail.com",
    phone=6268135064,
    active=True,
    department="Engineering",
    emp_id = "SL101",
    join_date = "2026-08-29",
    skills = ["Python","Aws"]
)
print("Rohit ki compnay ka emplouyee hu",user)

# Reutrn Kya h kaise kaam krta h 

def add_numbers(a,b):
    result = a + b
    return result
print("mein ek return hu", add_numbers(4,5))

# return Keyword
# Function se output bhejta hai 
# Jahna function call kiya tha wha value bhejta hai 
# return ke badd function excecution stop ho jata hai 
# Agr return nahi likha toh None return hota hai

# Return Vs Print

# Print
# Sirf screen pr dikhata hai    
# Use nhi kr skte ho 
#  side effect 
# Debugging ke liye 
# Return 
# Vlaue provide kkrta hai 
# Use kar skte ho 
# Actual output
# Production code mein

# Return Types 
# Single value return 
def square(x):
    return x ** 2
print(square(5))


# Muliple values (Tuple)
def get_user_info():
    return "Rohit" ,20, "Delhi"
name,age,city = get_user_info()
print(name,age,city)