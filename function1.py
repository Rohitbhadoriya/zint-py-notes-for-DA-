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
log_errors("critical", "DB Down","Retry Failed","Sysytem unstable") 


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
# Internal Working
# Python sab extra keyword arguments uthata hai
# Unko ek dictionary mein pack krta hai
# app kwrgs.item() , kwrgs.get('key') use kr skte ho

# use kba krna chaiye 

# jab hume pta nhi ho ki kitne arguments pass hone wale h 
# jab flexible configuration chaiye ho 
# jab api forward compatiable rkhan ho
# jab dyanmic attributes add krne ho 

# Kb use na krein 
# jab parameteres specific ho mtlb ki define ho 
# jab type saftey chahiye ho 
# jab documentation imp ho 

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
# Jaha function call kiya tha wha value bhejta hai 
# return ke badd function excecution stop ho jata hai 
# Agr return nahi likha toh None return hota hai

# Return Vs Print

# Print
# Sirf screen pr dikhata hai    
# Use nhi kr skte ho 
#  side effect 
# Debugging ke liye 
# Return 
# Value provide krta hai 
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

# 3. Dictionary return
def get_user_profile():
    return {
        "name": "Rohit",
        "age": 25,
        "city": "Delhi",
        "active": True
    }
profile = get_user_profile()
print(profile["name"])  # Rohit


# 4. List return
def get_top_scores():
    return [95, 88, 76, 92, 84]

scores = get_top_scores()
print(scores[0])  # 95

# 5. None return (no return value)
def log_message(msg):
    print(f"LOG: {msg}")
    return  # None return

result = log_message("Hello")
print(result)  # None


# 6. Boolean return
def is_adult(age):
    return age >= 18

print(is_adult(20))  # True
print(is_adult(15))  # False




# ========== EARLY RETURN (Guard Clauses) ==========

def process_order(order_id):
    """
    Early return use karke validation.
    """
    # Validation 1
    if not order_id:
        return {"error": "Order ID required"}  # Early return
    
    # Validation 2
    if order_id <= 0:
        return {"error": "Invalid order ID"}  # Early return
    
    # Validation 3
    order = fetch_order(order_id)
    if not order:
        return {"error": "Order not found"}  # Early return
    
    # Main logic - tab hi execute hogi jab sab valid hai
    processed = process_order_data(order)
    return {"status": "success", "data": processed}



# 3.2 Return vs Print - INDUSTRY DECISION FRAMEWORK

# BAD - Print in function (can't use value)
def calculate_total_price(items):
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    print(total)  # 🔴 Print - value use nahi kar sakte

# GOOD - Return (can use value)
def calculate_total_price(items):
    total = 0
    for item in items:
        total += item["price"] * item["qty"]
    return total  # 🟢 Return - value use kar sakte ho



# PRINT (Display Only)                    RETURN (Provide)   
               
#     Screen pe dikhana                         Value dena           
#     Debugging                                Use karna            
#     Logging                                  Store karna          
#     Progress show karna                      Calculate karna      
#  User ko batana                           Pass to other funcs  │   • REPL/Testing                            • API responses  

#  GOLDEN RULE: 
# Functions should RETURN values, not PRINT them."
# If you need to display, print the RETURNED value 
# Functions = Computation (return)  
# Print = Display (use outside function)   


# BAD - Print in function
def get_user_data(user_id):
    user = db.fetch_user(user_id)
    print(user)  # Can't use this data anywhere!
    # Can't do anything else with the user data


    #  GOOD - Return
def get_user_data(user_id):
    user = db.fetch_user(user_id)
    return user  # Can use this data!


# Using the good function
user_data = get_user_data(101)  # Store
print(f"User: {user_data['name']}")  # Display when needed
process_user(user_data)  # Process
send_email(user_data["email"])  # Use in other functions

#  PART 4: SCOPE - VARIABLE KAHAN REHTI HAI
# 4.1 Local vs Global Scope - BILKUL SIMPLE

# ========== CODE ==========

# GLOBAL VARIABLE - sab jagah accessible
shop_name = "Rohit's Store"  # Global scope
tax_rate = 0.18              # Global scope

def calculate_total(items):
    """
    Items ka total calculate karta hai.
    """
    subtotal = 0  # LOCAL variable - sirf function ke andar
    for item in items:
        subtotal += item["price"] * item["qty"]
    
    tax = subtotal * tax_rate  # Global variable access kar raha hai
    total = subtotal + tax
    return total

# ========== LINE-BY-LINE EXPLANATION ==========

"""
SCOPE (Variable ki visibility):

GLOBAL SCOPE:
- Function ke BAHAR defined variables
- Sab functions access kar sakte hain
- Program ke end tak exist karti hain
- Example: shop_name, tax_rate

 LOCAL SCOPE:
- Function ke ANDAR defined variables
- Sirf us function ke andar accessible
- Function khatam hote hi delete ho jati hain
- Example: subtotal, tax, total

IMPORTANT:
- Python function ke andar variable dhundhti hai:
  1. Pehle LOCAL scope mein
  2. Phir ENCLOSING scope mein (nested functions)
  3. Phir GLOBAL scope mein
  4. Phir BUILT-IN scope mein

ERROR:
def wrong_function():
    print(shop_name)  #  Global access - OK
    shop_name = "New Store"  #  Local variable ban raha hai
    # Python confuse ho jata hai - UnboundLocalError

 SOLUTION:
def correct_function():
    global shop_name  # "Mai global use kar raha hoon"
    print(shop_name)  #  Global access
    shop_name = "New Store"  #  Global modify
"""

# ========== INDUSTRY EXAMPLE ==========

#  COMPANY: Configuration file
# config.py
DATABASE_URL = "postgresql://localhost:5432/mydb"
API_KEY = "sk-1234567890"
MAX_RETRIES = 3
TIMEOUT = 30
DEBUG = True

# main.py
def connect_to_db():
    """Database connection function"""
    # Using global configuration
    print(f"Connecting to: {DATABASE_URL}")
    print(f"Timeout: {TIMEOUT}s")
    # Connection logic
    return {"status": "connected"}

def fetch_data(query):
    """Data fetch karna"""
    # Using global config
    print(f"Max retries: {MAX_RETRIES}")
    # Fetch logic
    
def set_debug_mode(enabled):
    """Debug mode set karna"""
    global DEBUG  # Need to modify global
    DEBUG = enabled
    print(f"Debug mode: {DEBUG}")

# Main execution
print(f"Starting app... ({DATABASE_URL})")
db = connect_to_db()
fetch_data("SELECT * FROM users")
set_debug_mode(False)



# 4.2 Global Keyword - Global Variable Modify Karna


# ========== CODE ==========

# Global variable
counter = 0
config = {"debug": True, "version": "1.0"}

def increment_counter():
    """
    Global counter increment karta hai.
    """
    global counter  # ← "Mai global counter use kar raha hoon"
    counter += 1
    print(f"Counter: {counter}")

def update_config(key, value):
    """
    Global config update karta hai.
    """
    global config  # ← "Mai global config use kar raha hoon"
    config[key] = value
    print(f"Config updated: {key} = {value}")

# ========== USE KARNA ==========
increment_counter()  # Counter: 1
increment_counter()  # Counter: 2
increment_counter()  # Counter: 3

update_config("debug", False)   # Config updated: debug = False
update_config("version", "2.0") # Config updated: version = 2.0

print(counter)  # 3
print(config)   # {'debug': False, 'version': '2.0'}

# ========== LINE-BY-LINE EXPLANATION ==========

"""
global KEYWORD:

KYA KARTA HAI:
- Function ke andar global variable modify karne ke liye
- Python ko batata hai ki "Naya variable mat banao, global use karo"

KYA HOGA BINA global KE:
counter = 0

def increment_counter():
    counter += 1  #  UnboundLocalError!
    # Python sochta hai: "counter local hai? par value toh nahi hai"

KYA HOGA global KE SAATH:
def increment_counter():
    global counter  # "Mai global wala counter use kar raha hoon"
    counter += 1    # Works!

WARNING:
- global ko HAMESHA function ke start mein likho
- Zyada global variables mat banao (tight coupling)
- Global variables test karna mushkil
- Industrial code mein global kam use karo
"""

# ========== INDUSTRY EXAMPLE ==========

#  Analytics counter
total_requests = 0
successful_requests = 0
failed_requests = 0

def track_request(success=True):
    """
    Request track karna.
    """
    global total_requests, successful_requests, failed_requests
    
    total_requests += 1
    
    if success:
        successful_requests += 1
    else:
        failed_requests += 1
    
    print(f"📊 Stats: Total={total_requests}, Success={successful_requests}, Failed={failed_requests}")

# Simulate requests
track_request(True)   # Stats: Total=1, Success=1, Failed=0
track_request(True)   # Stats: Total=2, Success=2, Failed=0
track_request(False)  # Stats: Total=3, Success=2, Failed=1
track_request(True)   # Stats: Total=4, Success=3, Failed=1



# Nonlocal Keyword - Enclosing Scope Modify Karna

# ========== CODE ==========

def outer_function():
    """
    Outer function - counter encloses inner function.
    """
    counter = 0  # Enclosing scope variable
    
    def inner_function():
        """
        Inner function - outer function ke variable modify karta hai.
        """
        nonlocal counter  # "Mai enclosing wala counter use kar raha hoon"
        counter += 1
        print(f"Inner counter: {counter}")
    
    inner_function()  # Inner counter: 1
    inner_function()  # Inner counter: 2
    inner_function()  # Inner counter: 3
    
    print(f"Outer counter: {counter}")  # Outer counter: 3
    
    return inner_function

# ========== USE KARNA ==========
func = outer_function()
func()  # Inner counter: 4
func()  # Inner counter: 5

# ========== LINE-BY-LINE EXPLANATION ==========

# """
# nonlocal KEYWORD:

# KYA KARTA HAI:
# - Nested function mein enclosing function ke variable modify karta hai
# - Outer function ke variable ko inner function mein change karta hai

def outer():
    counter = 0
    def inner():
        counter += 1  #  UnboundLocalError!
    inner()

# KYA HOGA nonlocal KE SAATH:
def outer():
    counter = 0
    def inner():
        nonlocal counter  # "Mai enclosing wala use kar raha hoon"
        counter += 1      #  Works!
    inner()


# WHEN TO USE:
#  Nested functions mein
#  Decorators mein
#  Closures mein
#  Function mein state maintain karna ho

# WHEN NOT TO USE:
#  Simple functions mein
#  Jab avoid kar sakte ho (use parameters instead)
#  Zyada nested functions mein (confusing)

# 5.1 Lambda Kya Hai? - SIMPLE EXPLANATION


# REGULAR FUNCTION: 
# def square(x):             
#     return x ** 2
# def keyword use karta hai
# Name hota hai
# Multiple statements
# Return explicitly 
# Documentation daal sakte
# Error handling kar sakte 
# Zyada complex logic  


# LAMBDA 
# lambda x: x ** 2
# def nahi use karta
# Anonymous (koi name nahi)
# Sirf ek expression
# Auto return
# Documentation nahi
# Error handling nahi
# Simple logic

# KYA HAI LAMBDA:
# Ek "anonymous function" (nam nahi hai)
# Short, one-line functions ke liye
# Expression automatically return hota hai
# Function ko function pass karte waqt use hota hai

# KAB USE KAREIN:
# Short one-line functions
# map, filter, sorted ke saath
# Function argument ke roop mein
# Quick operations

# KAB USE NA KAREIN:
# Complex logic ke liye
# Multiple statements ke liye
# Jab documentation chahiye
# Jab reusable function chahiye

# ========== CODE ==========

# Regular function
def square(x):
    """Number ka square nikalta hai"""
    return x ** 2

# Lambda function (anonymous)
square_lambda = lambda x: x ** 2

# ========== USE KARNA ==========
print(square(5))         # 25 - Regular function
print(square_lambda(5))  # 25 - Lambda function

# ========== LINE-BY-LINE EXPLANATION ==========

"""
lambda x: x ** 2
│       │
│       └─── Expression (automatically return ho jata hai)
└─── Parameters

REGULAR FUNCTION vs LAMBDA:
─────────────────────────────────────────────────
REGULAR FUNCTION:            LAMBDA:
─────────────────────────────────────────────────
def square(x):               lambda x: x ** 2
    return x ** 2
│                           │
- def keyword use karta hai  - def nahi use karta
- Name hota hai              - Anonymous (koi name nahi)
- Multiple statements         - Sirf ek expression
- Return explicitly           - Auto return
- Documentation daal sakte   - Documentation nahi
- Error handling kar sakte   - Error handling nahi
- Zyada complex logic         - Simple logic

KYA HAI LAMBDA:
- Ek "anonymous function" (nam nahi hai)
- Short, one-line functions ke liye
- Expression automatically return hota hai
- Function ko function pass karte waqt use hota hai

KAB USE KAREIN:
 Short one-line functions
map, filter, sorted ke saath
Function argument ke roop mein
Quick operations

KAB USE NA KAREIN:
 Complex logic ke liye
 Multiple statements ke liye
 Jab documentation chahiye
 Jab reusable function chahiye
"""

# ========== REAL INDUSTRY EXAMPLES ==========

# 1. SORTING WITH LAMBDA
users = [
    {"name": "Rohit", "age": 25, "salary": 50000},
    {"name": "Priya", "age": 30, "salary": 70000},
    {"name": "Amit", "age": 22, "salary": 45000},
    {"name": "Neha", "age": 28, "salary": 65000}
]

# Age ke hisaab se sort
sorted_by_age = sorted(users, key=lambda user: user["age"])
print("Age wise:")
for user in sorted_by_age:
    print(f"  {user['name']}: {user['age']} years")

# Salary ke hisaab se sort (descending)
sorted_by_salary = sorted(users, key=lambda user: user["salary"], reverse=True)
print("\nSalary wise (highest first):")
for user in sorted_by_salary:
    print(f"  {user['name']}: ₹{user['salary']}")

# 2. FILTERING WITH LAMBDA
numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50]

# Even numbers filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"\nEven numbers: {even_numbers}")

# Numbers > 25
greater_than_25 = list(filter(lambda x: x > 25, numbers))
print(f"Numbers > 25: {greater_than_25}")

# 3. MAPPING WITH LAMBDA
prices = [100, 200, 300, 400, 500]

# 10% discount apply
discounted = list(map(lambda price: price * 0.9, prices))
print(f"\nOriginal: {prices}")
print(f"Discounted: {discounted}")

# 4. REDUCING WITH LAMBDA
from functools import reduce

# Product of all numbers
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(f"\nProduct: {product}")  # 120

# 5. DATA TRANSFORMATION
orders = [
    {"id": 1, "items": [{"price": 100}, {"price": 200}]},
    {"id": 2, "items": [{"price": 50}, {"price": 75}, {"price": 25}]},
    {"id": 3, "items": [{"price": 300}]}
]

# Total of each order
totals = list(map(
    lambda order: sum(item["price"] for item in order["items"]),
    orders
))
print(f"\nOrder totals: {totals}")

# key=lambda kyu kiya?
# Dekho, sorted() function ko batana padta hai ki "Kis basis pe sort karna hai?"
# Bina key ke :
# sorted(users)
# Yeh error dega kyunki Python ko nahi pata ki tuple/list/dict ko kaise compare kare.

# Why lambda
# Lambda ek chhota, one-line function hai jo:
# Har user leta hai (user)
# Usme se "age" nikaalta hai (user["age"])
# Yeh value sorting key ban jaati hai

# Agar lambda nahi likhte toh?
# def get_age(user):
#     return user["age"]

# sorted(users, key=get_age)
# Lekin lambda short aur clean hai — ek hi baar use karna hai, toh alag function banane ki zaroorat nahi.






# Lambda vs Regular Function - DECISION GUIDE

"""
======================================================================
LAMBDA vs REGULAR FUNCTION - COMPLETE GUIDE (Simple Language)
======================================================================

YE SAMJHO: Function ek "kaam karne ka formula" hai
- Regular function = Bada dabba (naam ke saath)
- Lambda = Chhota dabba (bina naam ke)
"""

# ====================================================================
# PART 1: BASIC DIFFERENCE (Sabse zaroori baat)
# ====================================================================

print("=" * 50)
print("PART 1: BASIC DIFFERENCE")
print("=" * 50)

# REGULAR FUNCTION - Bada wala
def square_regular(x):
    """Number ka square nikalta hai"""
    return x * x

# LAMBDA - Chhota wala
square_lambda = lambda x: x * x

# Dono same kaam karte hain
print("Regular function:", square_regular(5))  # 25
print("Lambda function:", square_lambda(5))    # 25

print("\n--- FARAK KYA HAI? ---")
print("1. Regular ka naam hai 'square_regular'")
print("2. Lambda ka naam nahi hai (anonymous)")
print("3. Regular mein 'return' likhna padta hai")
print("4. Lambda mein auto return hota hai")
print("5. Regular mein documentation daal sakte ho")
print("6. Lambda mein nahi daal sakte")

# ====================================================================
# PART 2: KAB KYA USE KAREIN? (Decision Guide)
# ====================================================================

print("\n" + "=" * 50)
print("PART 2: KAB KYA USE KAREIN?")
print("=" * 50)

# SCENARIO 1: Simple kaam (Square)
print("\n[SCENARIO 1] Simple kaam - Square nikaalna")
print("-" * 40)

#  Lambda - Best (1 line mein kaam ho gaya)
square = lambda x: x ** 2
print(" Lambda use karo:", square(5))

# Regular - Overkill (zyada likhna pada)
def square_regular2(x):
    return x ** 2
print(" Regular zaroorat se zyada hai")

print(" DECISION: Lambda use karo (simple hai)")

# SCENARIO 2: Complex logic (Zyada conditions)
print("\n[SCENARIO 2] Complex logic - Multiple conditions")
print("-" * 40)

#  Lambda - Bahut mushkil (ghanshyam ho jaata hai)
# process = lambda data: [item for item in data if item["status"] == "active" and item["age"] > 18 and item["salary"] > 50000]

#  Regular - Clean (sabko samajh aata hai)
def process_active_high_earners(data):
    """Active users jo 18+ hain aur salary 50000 se zyada"""
    result = []
    for item in data:
        if item["status"] == "active" and item["age"] > 18 and item["salary"] > 50000:
            result.append(item)
    return result

# Test data
test_data = [
    {"name": "Rohit", "status": "active", "age": 25, "salary": 60000},
    {"name": "Priya", "status": "active", "age": 30, "salary": 70000},
    {"name": "Amit", "status": "inactive", "age": 22, "salary": 40000}
]

result = process_active_high_earners(test_data)
print(" Regular function result:", result)

print(" DECISION: Regular function use karo (complex hai)")

# SCENARIO 3: Multiple statements (Zyada kaam)
print("\n[SCENARIO 3] Multiple statements - Zyada kaam")
print("-" * 40)

#  Lambda - Possible hi nahi
# process = lambda x: print(x); return x**2  #  Error

#  Regular - Aaram se kaam karega
def process_and_log(x):
    print(f"  Processing: {x}")
    result = x ** 2
    print(f"  Result: {result}")
    return result

print(" Regular function:")
result = process_and_log(5)

print(" DECISION: Regular function use karo (multiple statements)")

# SCENARIO 4: Quick inline use (map, filter, sorted)
print("\n[SCENARIO 4] Quick inline use - map/filter/sorted")
print("-" * 40)

users = [
    {"name": "Rohit", "age": 25},
    {"name": "Priya", "age": 30},
    {"name": "Amit", "age": 22}
]
numbers = [1, 2, 3, 4, 5]

#  Lambda - Perfect (1 line mein kaam)
users.sort(key=lambda user: user["age"])
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
doubled = list(map(lambda x: x * 2, numbers))

print("Sorted users:", users)
print("Even numbers:", even_numbers)
print("Doubled numbers:", doubled)

print(" DECISION: Lambda use karo (inline)")

# ====================================================================
# PART 3: INDUSTRY BEST PRACTICE (Real company mein kaise)
# ====================================================================

print("\n" + "=" * 50)
print("PART 3: INDUSTRY BEST PRACTICE")
print("=" * 50)

employees = [
    {"name": "Rohit", "age": 25, "salary": 50000, "dept": "Eng"},
    {"name": "Priya", "age": 30, "salary": 70000, "dept": "HR"},
    {"name": "Amit", "age": 22, "salary": 45000, "dept": "Sales"},
    {"name": "Neha", "age": 28, "salary": 60000, "dept": "Eng"}
]

print("\n[BAD PRACTICE] Complex lambda - mat karo")
print("-" * 40)
print(" Yeh mat karo (bahut complicated):")
print("   list(filter(lambda u: u['age'] > 25 and u['salary'] > 50000")
print("   and u['dept'] in ['Eng', 'HR'], employees))")
print("   → Kisi ko samajh nahi aayega")

print("\n[GOOD PRACTICE] Regular function - karo")
print("-" * 40)

def is_eligible_employee(emp):
    """Employee eligible hai ya nahi check karo"""
    if emp["age"] <= 25:
        return False
    if emp["salary"] <= 50000:
        return False
    if emp["dept"] not in ["Eng", "HR"]:
        return False
    return True

eligible = list(filter(is_eligible_employee, employees))
print(" Eligible employees:", eligible)
print("   → Sabko samajh aata hai, documentation bhi hai")

# ====================================================================
# PART 4: COMPLETE DECISION GUIDE (Yaad rakhne wali baat)
# ====================================================================

print("\n" + "=" * 50)
print("PART 4: DECISION GUIDE - YAAD RAKHO")
print("=" * 50)

print("""
LAMBDA USE KARO JAB:
-------------------
1. Kaam 1 line mein ho
2. Simple operation ho (jaise square, double)
3. map/filter/sorted ke saath use karna ho
4. Quick inline kaam ho
5. Documentation ki zaroorat nahi
6. Reusable nahi banana

REGULAR FUNCTION USE KARO JAB:
----------------------------
1. Multiple lines likhni ho
2. Complex logic ho (zyada conditions)
3. Documentation chahiye
4. Reusable banana hai (dusri jagah bhi use karna)
5. Error handling chahiye (try/except)
6. Side effects ho (jaise print, file write)

GOLDEN RULE (Zindagi ka mantra):
--------------------------------
"AGAR LAMBDA EK LINE SE ZYADA KA HAI,
 TOH REGULAR FUNCTION USE KARO"

READABILITY > SHORT CODE
""")

# ====================================================================
# PART 5: REAL-LIFE EXAMPLES (Company mein kaise use karte hain)
# ====================================================================

print("=" * 50)
print("PART 5: REAL-LIFE EXAMPLES")
print("=" * 50)

# Example 1: Employee sorting
print("\n[EXAMPLE 1] Sorting employees by salary")
print("-" * 40)

employees2 = [
    {"name": "Rohit", "salary": 50000},
    {"name": "Priya", "salary": 70000},
    {"name": "Amit", "salary": 45000}
]

# Lambda use karo - 1 line mein kaam
sorted_by_salary = sorted(employees2, key=lambda emp: emp["salary"], reverse=True)
print("Highest salary first:", sorted_by_salary)

# Example 2: Filtering products
print("\n[EXAMPLE 2] Filtering expensive products")
print("-" * 40)

products = [
    {"name": "Laptop", "price": 80000},
    {"name": "Phone", "price": 30000},
    {"name": "Tablet", "price": 45000}
]

# Lambda use karo
expensive = list(filter(lambda p: p["price"] > 40000, products))
print("Expensive products:", expensive)

# Example 3: Data transformation
print("\n[EXAMPLE 3] Data transformation")
print("-" * 40)

prices = [100, 200, 300, 400]
# Lambda use karo - 10% discount
discounted = list(map(lambda p: p * 0.9, prices))
print("Original:", prices)
print("After 10% discount:", discounted)

# Example 4: Complex business logic
print("\n[EXAMPLE 4] Complex business logic")
print("-" * 40)

orders = [
    {"id": 1, "items": [{"price": 100}, {"price": 200}]},
    {"id": 2, "items": [{"price": 50}, {"price": 75}, {"price": 25}]},
    {"id": 3, "items": [{"price": 300}]}
]

# Regular function use karo (complex hai)
def calculate_order_total(order):
    """Har order ka total calculate karo"""
    total = 0
    for item in order["items"]:
        total += item["price"]
    return total

totals = []
for order in orders:
    totals.append(calculate_order_total(order))

print("Order totals:", totals)

print("\n" + "=" * 50)
print("BAS YEHI HAI - SIMPLE AUR CLEAN")
print("=" * 50)

"""
======================================================================
SUMMARY (Ek line mein yaad rakho)
======================================================================

LAMBDA = Chhota dabba (1 line ka kaam)
REGULAR = Bada dabba (complex kaam)

Rule: Agar 1 line se zyada hai toh regular function use karo.
======================================================================
"""




