#  PART 1: FOUNDATION
## TOPIC 1: CONDITIONAL STATEMENTS KYA HAIN? (WHAT)

### Definition:
#"Conditional statements Python mein **decision-making** ke liye use hote hain. Ye program ko batate hain ki **kis condition mein kya karna hai**. Jaise real life mein — 'Agar barish ho rahi hai to chhata le lo, warna nahi.'"

### Real-Life Analogy:
#S"Socho aap **ATM** pe ho. Agar aapka balance 5000 hai aur aap 6000 nikalna chahte ho — ATM kahega 'Insufficient Balance'. Agar 4000 nikalna chahte ho — 'Cash Dispensed'. Ye decision **if-else** se hota hai."

### Simple Example:

age = 18

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


### Kyu Zaroori Hai:
"Bina conditional statements ke, program **linear** chalega — koi decision nahi lega. Real-world applications mein har jagah decisions hote hain — login check, payment validation, access control, recommendation."



## TOPIC 2: COMPARISON OPERATORS

### Definition:
#"Comparison operators do values ko compare karte hain aur **Boolean** (`True`/`False`) return karte hain."

### Operators Table:

# | Operator | Meaning | Example | Result |
# |----------|---------|---------|--------|
# | `==` | Equal to | `5 == 5` | True |
# | `!=` | Not equal | `5 != 3` | True |
# | `>` | Greater than | `5 > 3` | True |
# | `<` | Less than | `5 < 3` | False |
# | `>=` | Greater than or equal | `5 >= 5` | True |
# | `<=` | Less than or equal | `5 <= 3` | False |

### Basic Examples:

age = 20

print(age == 20)   # True
print(age != 18)   # True
print(age > 18)    # True
print(age < 25)    # True
print(age >= 18)   # True
print(age <= 20)   # True


###  `=` vs `==` (Bahut Important):

#  Assignment (value assign karta hai)
x = 5

# ✅ Comparison (compare karta hai)
x == 5  # True ya False


### Common Mistake:

#  SyntaxError
# if age = 18:
#     print("Adult")

#  Sahi
if age == 18:
    print("Adult")


### Industry Example — Age Verification:

user_age = 17
min_age = 18

if user_age >= min_age:
    print("Access granted")
else:
    print("Access denied")


## TOPIC 3: BOOLEAN VALUES

### Definition:
# "Boolean ek data type hai jiske sirf **2 values** hoti hain — `True` aur `False`. Ye comparison ka result hota hai."

### Example:

is_logged_in = True
is_admin = False

print(type(is_logged_in))  # <class 'bool'>
print(5 > 3)               # True
print(5 < 3)               # False


### Boolean Operations:

print(True and False)  # False
print(True or False)   # True
print(not True)        # False


### Industry Example:

is_premium = True
has_coupon = False

if is_premium or has_coupon:
    print("Discount applied")


## TOPIC 4: TRUTHY & FALSY VALUES (Bahut Important)

### Definition:
#"Python mein `if` ke andar **sirf `True`/`False` hi nahi**, koi bhi value aa sakti hai. Kuch values **automatically False** maani jaati hain (Falsy), baaki sab **True** (Truthy)."

### Falsy Values (Ye sab False hain):

# False
# None
# 0
# 0.0
# ""          # Empty string
# []          # Empty list
# ()          # Empty tuple
# {}          # Empty dict
# set()       # Empty set


### Truthy Values (Baaki sab):

# True
# 1, -1, 100
"hello", " ", "0"
[1, 2], (1,), {"a": 1}


### Examples:

name = "Rohit"
if name:
    print("Name exists")  #  Chalega

name = ""
if name:
    print("Name available")
else:
    print("Name is empty")  #  Chalega


### Industry Example — Empty List Check:

users = []

if users:
    print("Users found")
else:
    print("No users found")  # ✅ Chalega


### Industry Example — API Response:

response = {}

if response:
    print("Data received")
else:
    print("Empty response")  # ✅ Chalega


### Kab Use Karein:
# - Empty check karne ke liye
# - `None` check karne ke liye
# - Default values ke liye

### Common Mistake:

#  Verbose
if len(users) > 0:
    print("Users found")

# ✅ Pythonic
if users:
    print("Users found")


## TOPIC 5: `if` STATEMENT

### Definition:
#"`if` statement ek **condition** check karta hai. Agar condition **True** hai to andar ka code chalega. Agar **False** hai to skip ho jayega."

### Syntax:

# if condition:
    # code to execute if condition is True


### Diagram:

#         ┌─────────────┐
#         │  Condition  │
#         └──────┬──────┘
#                │
#          ┌─────┴─────┐
#          │           │
#        True        False
#          │           │
#          ▼           ▼
#    ┌──────────┐  ┌──────────┐
#    │ Execute  │  │  Skip    │
#    │  Block   │  │  Block   │
#    └──────────┘  └──────────┘


### Basic Example:
age = 20

if age >= 18:
    print("You can vote")
    print("You are an adult")

print("Program ended")


# **Output:**

# You can vote
# You are an adult
# Program ended

### Line-by-Line Explanation:
# - `age = 20` → Variable assign
# - `if age >= 18:` → Condition check (True)
# - `print("You can vote")` → Andar ka code
# - `print("Program ended")` → Hamesha chalega (bahar hai)

### Industry Example — Login Check:

user_input = "admin"
password = "admin123"

if user_input == "admin" and password == "admin123":
    print("Login successful")


### Common Mistake:

#  IndentationError
if age >= 18:
print("You can vote")

#  Sahi
if age >= 18:
    print("You can vote")


## TOPIC 6: `if-else` STATEMENT

### Definition:
#"`if-else` do **alternate paths** deta hai. Agar condition True hai to `if` block, warna `else` block chalega."

### Syntax:

#if condition:
    # if True
#else:
    # if False


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
#    │ if block │  │else block│
#    └──────────┘  └──────────┘


### Basic Example:

age = 15

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


# **Output:**

# You cannot vote


### Industry Example — ATM Withdrawal:

balance = 5000
withdraw = 6000

if withdraw <= balance:
    print(f"₹{withdraw} dispensed")
    balance -= withdraw
else:
    print("Insufficient balance")

print(f"Current balance: ₹{balance}")


# **Output:**

# Insufficient balance
# Current balance: ₹5000




## TOPIC 7: MULTIPLE `if` vs `if-elif` (BAHUT IMPORTANT)

### Ye Beginners Ka Sabse Bada Confusion Hai:

### Multiple `if` — Independent Checks:

marks = 85

if marks >= 60:
    print("Pass")

if marks >= 80:
    print("Grade A")

if marks >= 90:
    print("Grade A+")


# **Output:**

# Pass
# Grade A

"Har `if` **independently** check hota hai. Multiple `if` = multiple independent checks."

### `if-elif` — One Decision Chain:

marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")


# **Output:**

# Grade A

"Pehla True mila, baaki skip. `if-elif` = one decision chain."

### Comparison Table:

# | Feature | Multiple `if` | `if-elif` |
# |---------|---------------|-----------|
# | **Checks** | Sab check hote hain | Pehla True mila, stop |
# | **Use Case** | Independent conditions | Mutually exclusive |
# | **Example** | Notifications, logs | Grade, discount |

### Student Ko Yaad Karwao:
# **Multiple `if` = multiple independent checks**
# **`if-elif` = one decision chain**



## TOPIC 8: `elif` STATEMENT

### Definition:
#"`elif` = **else if**. Jab multiple conditions check karni ho, tab `elif` use karte hain. Ye **top se bottom** check hota hai, jo pehla True mile wahi execute hota hai."

### Syntax:

# if condition1:
#     # block1
# elif condition2:
#     # block2
# elif condition3:
#     # block3
# else:
#     # default block


### Diagram:

#         ┌──────────────┐
#         │  Condition 1 │
#         └──────┬───────┘
#                │
#          ┌─────┴─────┐
#        True        False
#          │           │
#          ▼           ▼
#    ┌──────────┐  ┌──────────────┐
#    │ Block 1  │  │  Condition 2 │
#    └──────────┘  └──────┬───────┘
#                         │
#                   ┌─────┴─────┐
#                 True        False
#                   │           │
#                   ▼           ▼
#             ┌──────────┐  ┌──────────┐
#             │ Block 2  │  │  else    │
#             └──────────┘  └──────────┘


### Basic Example — Grade Calculator:

marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade F")


# **Output:**

# Grade A


### Line-by-Line Explanation:
# `marks = 85`
# `marks >= 90`? → False
# `marks >= 80`? → True → "Grade A" print
# Baaki conditions **skip**

### Industry Example — E-commerce Discount:

cart_total = 3500

if cart_total >= 5000:
    discount = 0.20
elif cart_total >= 3000:
    discount = 0.15
elif cart_total >= 1000:
    discount = 0.10
else:
    discount = 0

final_price = cart_total - (cart_total * discount)
print(f"Discount: {discount*100}%")
print(f"Final Price: ₹{final_price}")


# **Output:**

# Discount: 15.0%
# Final Price: ₹2975.0


### Important Rules:
# 1. `elif` **sirf** `if` ke baad
# 2. Ek `if` ke saath **multiple** `elif`
# 3. `else` **optional**
# 4. Pehla **True** mila → baaki skip



## TOPIC 9: NESTED `if`

### Definition:
#"Jab ek `if` ke andar doosra `if` likha jata hai, use **nested if** kehte hain. Ye tab use hota hai jab **multi-level decision** lena ho."

### Syntax:

# if condition1:
#     if condition2:
        # block
    # else:
        # block
else:
    # block


### Diagram:

#         ┌──────────────┐
#         │  Condition 1 │
#         └──────┬───────┘
#                │
#          ┌─────┴─────┐
#        True        False
#          │           │
#          ▼           ▼
#    ┌──────────────┐  ┌──────────┐
#    │ Condition 2  │  │ else     │
#    └──────┬───────┘  └──────────┘
#           │
#     ┌─────┴─────┐
#   True        False
#     │           │
#     ▼           ▼
# ┌────────┐  ┌────────┐
# │ Block  │  │ Block  │
# └────────┘  └────────┘


### Basic Example — Login + Admin Check:

is_logged_in = True
is_admin = True

if is_logged_in:
    print("Welcome!")
    if is_admin:
        print("You have admin access")
    else:
        print("You have user access")
else:
    print("Please login first")


# **Output:**

# Welcome!
# You have admin access


### Industry Example — Loan Approval:

age = 25
salary = 50000
credit_score = 750

if age >= 21:
    if salary >= 30000:
        if credit_score >= 700:
            print("Loan Approved")
        else:
            print("Loan Rejected: Low credit score")
    else:
        print("Loan Rejected: Low salary")
else:
    print("Loan Rejected: Underage")


# **Output:**

# Loan Approved


### ⚠️ Warning:
#"Nested if **zyada deep** mat karo. 3-4 level se zyada ho jaye to **refactor** karo."

### Alternative — Logical Operators:

#  Nested
if age >= 21:
    if salary >= 30000:
        if credit_score >= 700:
            print("Approved")

#  Better
if age >= 21 and salary >= 30000 and credit_score >= 700:
    print("Approved")


## TOPIC 10: LOGICAL OPERATORS

### Definition:
#"Logical operators **multiple conditions** ko combine karte hain. Python mein 3 hain — `and`, `or`, `not`."



### 10.1 `and` Operator

# **Kya:** Dono conditions **True** honi chahiye.

# **Truth Table:**
# | A | B | A and B |
# |---|---|---------|
# | True | True | True |
# | True | False | False |
# | False | True | False |
# | False | False | False |

# **Example:**

age = 25
salary = 50000

if age >= 21 and salary >= 30000:
    print("Eligible for loan")
else:
    print("Not eligible")


### 10.2 `or` Operator

# **Kya:** Koi bhi ek condition **True** ho to result True.

# **Truth Table:**
# | A | B | A or B |
# |---|---|--------|
# | True | True | True |
# | True | False | True |
# | False | True | True |
# | False | False | False |

# **Example:**

is_admin = False
is_moderator = True

if is_admin or is_moderator:
    print("You can delete posts")


### 10.3 `not` Operator

# **Kya:** Result ko **ulta** kar deta hai.

# **Truth Table:**
# | A | not A |
# |---|-------|
# | True | False |
# | False | True |

# **Example:**

is_logged_in = False

if not is_logged_in:
    print("Please login")


### 10.4  `and` / `or` Sirf Boolean Return Nahi Karte (Advanced)

"Python mein `and` aur `or` **operands return kar sakte hain**, sirf `True`/`False` nahi."


print(10 and 20)   # 20
print(0 and 20)    # 0
print(10 or 20)    # 10
print(0 or 20)     # 20


### Industry Use Case — Default Value:

name = ""
result = name or "Guest"
print(result)  # Guest



username = input("Enter name: ") or "Anonymous"
print(f"Hello, {username}")


### Kyu Useful Hai:
# - Default values set karna
# - Fallback chain
# - Short-circuit optimization



### 10.5 Short-Circuit Evaluation

#"Python **short-circuit** evaluation use karta hai."

# **`and` mein:** Pehli False → dusri **check hi nahi hoti**.

def check():
    print("Checking...")
    return True

if False and check():  # check() call nahi hoga
    print("Yes")


# **`or` mein:** Pehli True → dusri **check hi nahi hoti**.

if True or check():  # check() call nahi hoga
    print("Yes")


### Industry Use Case:

user = None

# Safe: user None hai, to user.name access nahi hoga
if user and user.name:
    print(user.name)


## TOPIC 11: MEMBERSHIP OPERATORS — `in` / `not in`

### Definition:
#"`in` operator check karta hai ki value collection mein hai ya nahi. `not in` ulta."

### Examples:

# **List:**

role = "admin"

if role in ["admin", "manager"]:
    print("Access granted")


# **String:**

email = "rohit@gmail.com"

if "@" in email:
    print("Valid email format")


# **Dictionary (keys check):**

user = {"name": "Rohit", "age": 21}

if "name" in user:
    print("Name exists")


### Industry Example — Role-Based Access:

allowed_roles = ["admin", "doctor", "accountant"]
user_role = "doctor"

if user_role in allowed_roles:
    print("Access granted")
else:
    print("Access denied")


### `not in` Example:

banned_users = ["spammer1", "spammer2"]

if "rohit" not in banned_users:
    print("Welcome!")


## TOPIC 12: IDENTITY OPERATORS — `is` / `is not` (Advanced)

### Definition:
#"`is` operator check karta hai ki do variables **same object** ko point karte hain ya nahi. `==` value compare karta hai, `is` identity compare karta hai."

### Difference:

a = [1, 2]
b = [1, 2]

print(a == b)   # True (values same)
print(a is b)   # False (different objects)


### `None` Checking:

user = None

if user is None:
    print("User not found")
else:
    print("User exists")


### Industry Example — API Response:

def get_user(user_id):
    # Database se user fetch
    return None  # agar nahi mila

user = get_user(101)

if user is None:
    print("User not found")


###  Important:
#"`None` check karne ke liye `is None` use karo, `== None` nahi."


#  Avoid
if user == None:
    pass

#  Prefer
if user is None:
    pass


### Kab Use Karein:
# - `None` check
# - Singleton objects (True, False, None)
# - Identity check

### Kab Avoid Karein:
# - Values compare karne ke liye (`==` use karo)


## TOPIC 13: OPERATOR PRECEDENCE

### Definition:
#"Jab ek expression mein multiple operators hote hain, Python **precedence** ke hisaab se evaluate karta hai."

### Precedence Order (High to Low):

# 1. ()          → Parentheses
# 2. not         → NOT
# 3. and         → AND
# 4. or          → OR


### Example:

if a or b and c:


# Python ise evaluate karega:

# if a or (b and c):


### Industry Example:

age = 20
is_verified = True
is_admin = False

if age >= 18 and is_verified or is_admin:
    # Python: (age >= 18 and is_verified) or is_admin
    print("Access granted")


###  Parentheses Readability Ke Liye:

# Confusing
if a or b and c:
    pass

#  Clear
if a or (b and c):
    pass


#"Parentheses readability improve karte hain aur logical expression clear banate hain."



## TOPIC 14: SHORTHAND `if` (Ternary Operator)

### Definition:
#"Shorthand `if` ek **single line** mein if-else likhne ka tarika hai. Ise **ternary operator** ya **conditional expression** bhi kehte hain."

### Syntax:

value_if_true if condition else value_if_false


### Diagram:

#    ┌────────────────┐
#    │  value_if_true │
#    └────────┬───────┘
#             │
#    ┌────────┴───────┐
#    │   if condition │
#    └────────┬───────┘
#             │
#    ┌────────┴────────┐
#    │ value_if_false  │
#    └─────────────────┘


### Basic Example:

age = 20

# Normal if-else
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Shorthand
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult


### Industry Example — Price Display:

price = 500
is_premium = True

final_price = price * 0.8 if is_premium else price
print(f"Final Price: ₹{final_price}")  # ₹400.0


### Function Ke Saath:

def get_status(age):
    return "Adult" if age >= 18 else "Minor"

print(get_status(20))  # Adult


###  Nested Shorthand (Avoid):

#  Confusing
result = "A" if m >= 90 else "B" if m >= 80 else "C" if m >= 70 else "F"

# ✅ Better
if m >= 90:
    result = "A"
elif m >= 80:
    result = "B"
elif m >= 70:
    result = "C"
else:
    result = "F"


### Kab Use Karein:
# - Simple conditions
# - Single line assignment
# - Return statements

### Kab Avoid Karein:
# - Complex conditions
# - Multiple elif



## TOPIC 15: GUARD CLAUSES / EARLY RETURN

### Definition:
#"Guard clause ek technique hai jisme hum **inverse condition** check karke **early return** kar dete hain. Isse nested if avoid hote hain."

### Bad (Nested):

def process_order(user):
    if user:
        if user.is_verified:
            if user.has_balance:
                print("Order processed")


### Good (Guard Clause):

def process_order(user):
    if not user:
        return

    if not user.is_verified:
        return

    if not user.has_balance:
        return

    print("Order processed")


### Industry Example — API Handler:

def handle_request(request):
    if not request:
        return {"error": "Empty request"}

    if not request.get("token"):
        return {"error": "Unauthorized"}

    if not request.get("data"):
        return {"error": "No data"}

    return {"status": "success", "data": request["data"]}


### Kyu Use Karein:
# - Nested conditions reduce
# - Code readable
# - Early exit

### Student Ko Yaad Karwao:
# "Guard clause = Inverse condition + Early return"



## TOPIC 16: `pass` STATEMENT

### Definition:
#  "`pass` ek **null statement** hai. Ye kuch nahi karta. Jab aapko syntactically kuch likhna ho par logically kuch nahi karna ho, tab `pass` use karte hain."

### Kyu Exist Karta Hai:
#"Python mein **empty block** allowed nahi hai. Agar aap `if` ke andar kuch nahi likhenge to **IndentationError** aayega."

### Basic Example:

age = 20

if age >= 18:
    pass  # Baad mein code add karenge


### Industry Use Cases:

# **1. Placeholder:**

def process_payment():
    pass  # TODO: Implement

def send_email():
    pass  # TODO: Implement


# **2. Empty Class:**

class User:
    pass


# **3. Exception Handling:**

try:
    result = 10 / 0
except ZeroDivisionError:
    pass  # Error ignore


### ⚠️ `pass` Return Value (Correction):
#"`pass` **khud koi value return nahi karta**. Agar kisi function ke andar sirf `pass` ho, to function **implicitly `None` return karega**."


def test():
    pass

print(test())  # None


### `pass` vs `...` (Ellipsis):

def func1():
    pass

def func2():
    ...  # Ellipsis literal


#"`pass` Python ka null statement hai, jabki `...` Ellipsis literal hai. Dono ko placeholder ki tarah use kiya ja sakta hai, lekin technically dono same cheez nahi hain."

### Kab Avoid Karein:

# ❌ Silent errors
try:
    risky_operation()
except Exception:
    pass  # Debugging mushkil

# ✅ Better
try:
    risky_operation()
except Exception as e:
    print(f"Error: {e}")


## TOPIC 17: `match` STATEMENT (Python 3.10+)

### Definition:
 #"`match` statement **structural pattern matching** ke liye use hota hai. Ye `switch-case` jaisa hai, par **zyada powerful**. Python 3.10 se introduce hua."

### Syntax:

# match value:
    #case pattern1:
        # block1
    #case pattern2:
        # block2
    #case _:
        # default


### Diagram:

#         ┌──────────────┐
#         │    value     │
#         └──────┬───────┘
#                │
#     ┌──────────┼──────────┐
#     │          │          │
#     ▼          ▼          ▼
# ┌───────┐  ┌───────┐  ┌───────┐
# │case 1 │  │case 2 │  │case _ │
# └───┬───┘  └───┬───┘  └───┬───┘
#     │          │          │
#   Match      Match      Default
#     │          │          │
#     ▼          ▼          ▼
# ┌───────┐  ┌───────┐  ┌───────┐
# │Block 1│  │Block 2│  │Block 3│
# └───────┘  └───────┘  └───────┘


### 17.1 Literal Patterns


status = 404

match status:
    case 200:
        print("OK")
    case 301:
        print("Moved Permanently")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown status")


# **Output:**

# Not Found


### 17.2 Multiple Patterns (OR)


day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")


### 17.3 Tuple Pattern


point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, 0):
        print(f"X-axis at {x}")
    case (x, y):
        print(f"Point at ({x}, {y})")


# **Output:**

# Y-axis at 5


### 17.4 List Pattern


command = ["move", "up", 10]

match command:
    case ["move", direction, steps]:
        print(f"Moving {direction} by {steps}")
    case ["stop"]:
        print("Stopped")


### 17.5 Dictionary Pattern


user = {"name": "Rohit", "role": "admin"}

match user:
    case {"role": "admin"}:
        print("Admin access")
    case {"role": "user"}:
        print("User access")


### 17.6 Guards


age = 25

match age:
    case n if n < 18:
        print("Minor")
    case n if n < 60:
        print("Adult")
    case _:
        print("Senior")


### 17.7 `_` Wildcard

# "`_` wildcard pattern hai. Ye **default case** hai. Koi bhi value match karta hai."


match status:
    case 200:
        print("OK")
    case _:
        print("Unknown")


### ⚠️ Important: `_` Optional Hai
# "`_` **mandatory nahi hai**. Agar unmatched values ke liye kuch nahi karna, to skip kar sakte ho."


match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
# 500 ke liye kuch nahi hoga


### ⚠️ `match` Mein `else` Nahi Hota:
#"`match` mein `else` nahi hota; fallback ke liye `case _:` use hota hai."



### 17.8 Variable Capture (Advanced)

# "`case x:` mein `x` koi fixed value nahi hai — ye value ko **capture** karega."

value = 42

match value:
    case 200:
        print("Literal 200")
    case x:
        print(f"Captured: {x}")  # 42


# **Difference:**

# case 200:   # Literal match
# case x:     # Capture (kuch bhi match)


### 17.9 `match` vs `if-elif`

# | Feature | `if-elif` | `match` |
# |---------|-----------|---------|
# | **Python Version** | Sab | 3.10+ |
# | **Pattern Matching** | Nahi | Haan |
# | **Readability** | Complex | Clean |
# | **Use Case** | General conditions | Structured data |
# | **Performance** | Similar | Similar |

### ⚠️ Important:
# "`match` **simply switch-case nahi** hai. Ye **structural pattern matching** hai. Simple conditions ke liye `if-elif` often natural hota hai."


# ❌ match unnecessarily complex
match age:
    case n if n >= 18:
        print("Adult")

# ✅ if-elif natural
if age >= 18:
    print("Adult")


### Kab Use Karein:
# - Multiple values check
# - Structured data match
# - API responses
# - Command parsing
# - State machines



## TOPIC 18: CONDITION DRY RUN TECHNIQUE

### Definition:
#"Dry run = code ko **manually step-by-step** evaluate karna."

### Example:

age = 22
is_student = True
has_id = False

if age >= 18 and has_id:
    print("Allowed")
elif is_student:
    print("Student access")
else:
    print("Denied")


### Dry Run Table:

# | Expression | Result |
# |-----------|--------|
# | `age >= 18` | True |
# | `has_id` | False |
# | `True and False` | False |
# | `is_student` | True |
# | `elif` executes | Yes |

# **Output:** `Student access`

### Kyu Useful Hai:
# - Debugging
# - Logic verify
# - Interview preparation



## TOPIC 19: CONDITIONAL STATEMENTS + FUNCTIONS

### Example:

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

result = check_age(20)
print(result)  # Adult


### Industry Example:

def calculate_discount(cart_total, is_premium):
    if is_premium or cart_total >= 5000:
        return 0.20
    elif cart_total >= 3000:
        return 0.15
    elif cart_total >= 1000:
        return 0.10
    else:
        return 0

discount = calculate_discount(3500, False)
print(f"Discount: {discount*100}%")  # 15.0%


### Teaching Point:
#"Conditions **sirf print karne ke liye nahi hoti** — actual application logic mein decision lekar value return karti hain."



## TOPIC 20: CONDITIONS WITH STRINGS / LISTS / DICTIONARIES

### String:

username = "Rohit"

if username:
    print("Username available")


### List:

cart = ["Laptop", "Mouse"]

if cart:
    print("Cart has products")


### Dictionary:

user = {"name": "Rohit"}

if user:
    print("User data available")



#  "Truthy/Falsy ke saath ye practical section students ki Python understanding kaafi strong karega."


## TOPIC 21: `if` / `elif` / `else` CHAIN STRUCTURE

### Rules:

# if condition1:
#     ...
# elif condition2:
#     ...
# elif condition3:
#     ...
# else:
#     ...


# - `if` → **maximum one**
# - `elif` → **zero or more**
# - `else` → **zero or one**
# - `else` always **last**



#  PART 2: REAL-WORLD USE CASES

### 1. Login System

username = "admin"
password = "admin123"

if username == "admin" and password == "admin123":
    print("Login successful")
elif username == "admin":
    print("Wrong password")
else:
    print("User not found")


### 2. Payment Gateway

amount = 5000
balance = 10000
is_verified = True

if amount <= balance and is_verified:
    print("Payment processed")
elif not is_verified:
    print("Please verify your account")
else:
    print("Insufficient balance")


### 3. Age Verification

age = 17
has_parental_consent = True

if age >= 18:
    print("Access granted")
elif age >= 13 and has_parental_consent:
    print("Access granted with parental consent")
else:
    print("Access denied")


### 4. Grade Calculator

marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Grade: {grade}")


### 5. Weather Recommendation

temperature = 35
is_raining = False

if temperature > 30 and not is_raining:
    print("Wear light clothes")
elif is_raining:
    print("Take umbrella")
else:
    print("Normal clothes")


### 6. E-commerce Discount

cart_total = 3500
is_premium = True

if is_premium or cart_total >= 5000:
    discount = 0.20
elif cart_total >= 3000:
    discount = 0.15
elif cart_total >= 1000:
    discount = 0.10
else:
    discount = 0

final = cart_total - (cart_total * discount)
print(f"Final: ₹{final}")


### 7. API Response Handler (match)

response = {"status": 200, "data": {"user": "Rohit"}}

match response:
    case {"status": 200, "data": data}:
        print(f"Success: {data}")
    case {"status": 404}:
        print("Not Found")
    case {"status": 500}:
        print("Server Error")
    case _:
        print("Unknown")


### 8. Command Parser (match)

command = input("Enter command: ").split()

match command:
    case ["help"]:
        print("Available commands: help, add, remove")
    case ["add", item]:
        print(f"Added {item}")
    case ["remove", item]:
        print(f"Removed {item}")
    case _:
        print("Unknown command")


### 9. Guard Clause — Order Processing

def process_order(user):
    if not user:
        return {"error": "No user"}

    if not user.get("is_verified"):
        return {"error": "Not verified"}

    if not user.get("has_balance"):
        return {"error": "No balance"}

    return {"status": "success", "message": "Order processed"}


### 10. Role-Based Access Control

allowed_roles = ["admin", "doctor", "accountant"]
user_role = "doctor"

if user_role in allowed_roles:
    print("Access granted")
else:
    print("Access denied")


# ⚠️ PART 3: COMMON MISTAKES

### Mistake 1: Indentation Error

# 
if age >= 18:
print("Adult")

# 
if age >= 18:
    print("Adult")


### Mistake 2: Assignment Instead of Comparison

#  SyntaxError
if age = 18:
    print("Adult")

# ✅
if age == 18:
    print("Adult")


### Mistake 3: Forgetting Colon

# ❌
if age >= 18
    print("Adult")

# ✅
if age >= 18:
    print("Adult")
```

### Mistake 4: elif Without if

# ❌ SyntaxError
elif age >= 18:
    print("Adult")
```

### Mistake 5: Nested if Too Deep

# ❌
if a:
    if b:
        if c:
            if d:
                if e:
                    print("Too deep!")

# ✅
if a and b and c and d and e:
    print("Better")


### Mistake 6: Shorthand Overuse

# ❌ Confusing
result = "A" if m >= 90 else "B" if m >= 80 else "C" if m >= 70 else "F"


### Mistake 7: `pass` Silent Error

# ❌
try:
    risky()
except:
    pass

# ✅
try:
    risky()
except Exception as e:
    print(f"Error: {e}")


### Mistake 8: Multiple `if` vs `elif` Confusion

# ❌ Ye dono chalenge
if marks >= 60:
    print("Pass")
if marks >= 80:
    print("Grade A")

# ✅ Ye sirf ek chalega
if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Pass")


### Mistake 9: `and`/`or` Precedence

# ❌ Confusing
if a or b and c:  # (a) or (b and c)

# ✅ Clear
# if a or (b and c):
#     pass


### Mistake 10: `== None` vs `is None`

# ❌ Avoid
if user == None:
    pass

# ✅ Prefer
if user is None:
    pass


# 🎤 PART 4: INTERVIEW QUESTIONS

### Q1: `if` aur `elif` mein difference?
# "`if` pehla condition check karta hai. `elif` tab check hota hai jab pehla `if` False ho."

### Q2: Multiple `if` vs `if-elif`?
# "Multiple `if` = multiple independent checks. `if-elif` = one decision chain."

### Q3: `if-else` aur shorthand `if` mein difference?
# "`if-else` statement hai, kuch return nahi karta. Shorthand `if` expression hai, value return karta hai."

### Q4: Nested if kab use karte hain?
#"Jab multi-level decision lena ho — jaise login check, phir admin check."

### Q5: `and`, `or`, `not` ka use?
# "`and` — dono True. `or` — koi ek True. `not` — invert."

### Q6: Short-circuit evaluation kya hai?
# "`and` mein pehli False ho to dusri check nahi. `or` mein pehli True ho to dusri check nahi."

### Q7: `and` / `or` Boolean return karte hain?
# "Nahi. Ye **operands return kar sakte hain**. `10 and 20` → 20."

### Q8: `pass` statement kya karta hai?
# "Kuch nahi karta. Placeholder hai."

### Q9: `pass` return value?
# "`pass` khud koi value return nahi karta. Function with only `pass` implicitly `None` return karta hai."

# ### Q10: `pass` vs `...`?
# > "`pass` null statement hai. `...` Ellipsis literal hai. Placeholder ke liye dono use ho sakte hain."

# ### Q11: `match` statement kya hai?
# > "Python 3.10+ ka **structural pattern matching** feature."

# ### Q12: `match` vs `if-elif`?
# > "`match` structured data ke liye better. `if-elif` general conditions ke liye."

# ### Q13: `match` mein `_` kya hai?
# > "Wildcard pattern. Default case. Optional hai."

# ### Q14: `match` mein `else` hota hai?
# > "Nahi. Fallback ke liye `case _:` use hota hai."

# ### Q15: `match` mein variable capture kya hai?
# > "`case x:` mein `x` value capture karta hai. Literal match `case 200:` alag hai."

# ### Q16: `is` vs `==`?
# > "`==` value compare. `is` identity compare."

# ### Q17: `None` check kaise?
# > "`is None` use karo, `== None` nahi."

# ### Q18: Truthy/Falsy kya hai?
# > "Python mein kuch values automatically False maani jaati hain — `0`, `None`, `""`, `[]`, `{}`, `set()`. Baaki sab Truthy."

# ### Q19: Operator precedence?
# > "`()` > `not` > `and` > `or`"

# ### Q20: Guard clause kya hai?
# > "Inverse condition check karke early return. Nested if avoid."

# ### Q21: `match` Python ke kaunse version se aaya?
# > "Python 3.10 se."

# ### Q22: Ternary operator kya hai?
# > "`value_if_true if condition else value_if_false`"

# ### Q23: `if 18 <= age <= 60` valid hai?
# > "Haan, Python chained comparison support karta hai."

# ### Q24: `in` operator kaise kaam karta hai?
# > "List, string, dict mein membership check karta hai."

# ### Q25: `if x = 5` valid hai?
# > "Nahi, `=` assignment hai, `==` comparison."

# ---

# # 📝 PART 5: PRACTICE QUESTIONS

# ### Beginner:
# 1. Check karo number positive, negative, ya zero hai.
# 2. Check karo number even ya odd hai.
# 3. Do numbers mein se bada find karo.
# 4. Check karo year leap year hai ya nahi.
# 5. Grade calculator banao.
# 6. Check karo person vote kar sakta hai ya nahi.
# 7. Login system banao.
# 8. Check karo triangle valid hai ya nahi.
# 9. Truthy/Falsy check karo — empty list, string, dict.
# 10. Comparison operators practice karo.

# ### Intermediate:
# 11. BMI calculator banao.
# 12. Tax calculator (income slabs).
# 13. E-commerce discount calculator.
# 14. ATM withdrawal system.
# 15. Check karo character vowel hai ya consonant.
# 16. Simple calculator (match use karke).
# 17. Rock-Paper-Scissors game.
# 18. Check karo string palindrome hai ya nahi.
# 19. Membership operator se role-based access.
# 20. Guard clause se validation function.

# ### Advanced:
# 21. Loan approval system (age, salary, credit score).
# 22. Multi-role access control.
# 23. API response handler (match).
# 24. Command parser (match).
# 25. State machine banao (match).
# 26. Traffic light system.
# 27. Quiz application with scoring.
# 28. Banking system.
# 29. Guard clause se order processing.
# 30. Dry run technique practice.

# ---

# # ✅ PART 6: SUMMARY

# | Topic | Key Point |
# |-------|-----------|
# | **Comparison Operators** | `==`, `!=`, `>`, `<`, `>=`, `<=` |
# | **Boolean** | `True`, `False` |
# | **Truthy/Falsy** | `0`, `None`, `""`, `[]`, `{}` → False |
# | **`if`** | Single condition check |
# | **`if-else`** | Two paths |
# | **Multiple `if` vs `elif`** | Independent vs chain |
# | **`elif`** | Multiple conditions |
# | **Nested `if`** | Multi-level |
# | **`and`/`or`/`not`** | Combine conditions |
# | **`and`/`or` operand return** | Boolean nahi, operands |
# | **`in`/`not in`** | Membership |
# | **`is`/`is not`** | Identity |
# | **Precedence** | `()` > `not` > `and` > `or` |
# | **Short-circuit** | Lazy evaluation |
# | **Ternary** | Single line |
# | **Guard clause** | Early return |
# | **`pass`** | Null statement |
# | **`match`** | Pattern matching (3.10+) |

# ---



