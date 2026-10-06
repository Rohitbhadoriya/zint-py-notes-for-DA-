# 🐍 PYTHON FUNCTIONS — THE COMPLETE TEACHER'S MANUAL

> **Bhai, ab bilkul is pattern pe de raha hoon:**
> 1. Concept kya hai?
> 2. Why do we need it?
> 3. Real-life analogy
> 4. Syntax
> 5. Basic examples
> 6. Step-by-step execution
> 7. Internal working
> 8. Common mistakes
> 9. Debugging
> 10. Backend mein iska use
> 11. Real backend example
> 12. Interview questions
> 13. Student questions / doubts
> 14. Practice problems
> 15. Mini task/project
> 16. Teaching points — class mein kya explain karna hai

> **Har topic pe ye 16 points. Shuru se, poora. Kuch bhi beech se nahi.**

---

# 📖 TOPIC 1: FUNCTIONS

---

## 1. Concept Kya Hai?

Function ek **named block of code** hai jo ek specific kaam karta hai. Aap ise ek baar likhte ho, aur baar-baar use kar sakte ho.

**Technical:** A function is a **named, reusable block of code** that performs a specific task. It takes input (arguments), processes it, and optionally returns a value.

---

## 2. Why Do We Need It?

### Reason 1: Code Reusability (DRY)
```python
# ❌ BINA FUNCTION — 100 orders = 500 lines
order1_total = 100 * 2 * 1.18
order2_total = 200 * 3 * 1.18
order3_total = 150 * 1 * 1.18

# ✅ FUNCTION KE SAATH — 1 function, 100 calls
def calculate_total(price, qty, tax=0.18):
    return price * qty * (1 + tax)

print(calculate_total(100, 2))
print(calculate_total(200, 3))
print(calculate_total(150, 1))
```

### Reason 2: Modularity
Bade problem ko chhote functions mein todo.

### Reason 3: Abstraction
Andar ka logic chhupao, sirf kaam dikhao.

### Reason 4: Testability
Har function ko alag test kar sakte ho.

### Reason 5: Debugging Easy
Error aaya to pata chalega kaunsa function fail hua.

---

## 3. Real-Life Analogy

Socho aapke paas ek **chai banane ki recipe** hai:
- Pani garam karo
- Patti daalo
- Doodh daalo
- Sugar daalo
- Ubaalo
- Chhanno
- Cup mein daalo

Aap recipe **ek baar** likhte ho. Jab bhi chai banani ho, wahi recipe follow karte ho. Function bhi wahi hai — code ki recipe.

**Aur analogy:**
| Real Life | Function |
|-----------|----------|
| Chai recipe | Function definition |
| Chai banana | Function call |
| Doodh, patti, sugar | Arguments |
| Chai | Return value |
| Recipe book | Module |

---

## 4. Syntax

```python
def function_name(parameters):
    """Docstring"""
    # body
    return value
```

**Example:**
```python
def calculate_total(price, quantity, tax_rate=0.18):
    """Calculate total price with tax."""
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative")
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total
```

| Part | Kya Hai |
|------|---------|
| `def` | Keyword |
| `calculate_total` | Function name |
| `(price, quantity, tax_rate=0.18)` | Parameters |
| `:` | Body start |
| `"""..."""` | Docstring |
| `if price < 0` | Validation |
| `return total` | Output |

---

## 5. Basic Examples

### Example 1: No Parameter, No Return
```python
def greet():
    print("Hello, World!")

greet()
greet()
```

**Output:**
```
Hello, World!
Hello, World!
```

### Example 2: Parameter, No Return
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Rohit")
greet("Anchal")
```

**Output:**
```
Hello, Rohit!
Hello, Anchal!
```

### Example 3: Parameter, Return
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

**Output:**
```
8
```

### Example 4: Default Argument
```python
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

greet("Rohit")
greet("Rohit", "Hi")
```

**Output:**
```
Hello, Rohit!
Hi, Rohit!
```

---

## 6. Step-by-Step Execution

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

**Step-by-step:**
```
Step 1: Python `def add` dekhta hai
        → Memory mein function object banta hai
        → `add` naam se bind hota hai

Step 2: `add(5, 3)` call hota hai
        → Python function object dhundhta hai
        → Arguments evaluate karta hai (5, 3)
        → Naya local scope banata hai
        → a = 5, b = 3 bind karta hai

Step 3: Function body execute hoti hai
        → a + b = 8 compute hota hai

Step 4: return 8
        → Local scope destroy hota hai
        → 8 caller ko return hota hai

Step 5: result = 8
        → print(result) → 8
```

**Call Stack:**
```
Before call:  []
During call:  [add]
After call:   []
```

---

## 7. Internal Working

### Function Object Kaise Banta Hai
```python
def add(a, b):
    return a + b

print(type(add))        # <class 'function'>
print(add.__name__)     # add
print(add.__doc__)      # None
print(add.__code__)     # <code object add at ...>
```

### Local Scope Kaise Banta Hai
```python
def func():
    x = 10      # Local variable
    print(locals())   # {'x': 10}

func()
```

### Call Stack
```python
def a():
    print("a starts")
    b()
    print("a ends")

def b():
    print("b starts")
    c()
    print("b ends")

def c():
    print("c called")

a()
```

**Output:**
```
a starts
b starts
c called
b ends
a ends
```

**Stack visualization:**
```
[a] → [a, b] → [a, b, c] → [a, b] → [a] → []
```

---

## 8. Common Mistakes

### Mistake 1: `print` instead of `return`
```python
# ❌
def add(a, b):
    print(a + b)

result = add(2, 3)
print(result)   # None

# ✅
def add(a, b):
    return a + b
```

### Mistake 2: Missing return in some paths
```python
# ❌
def get_user(user_id):
    if user_id > 0:
        return {"id": user_id}
    # user_id <= 0 → None return

# ✅
def get_user(user_id):
    if user_id <= 0:
        return {"error": "Invalid ID"}
    return {"id": user_id}
```

### Mistake 3: No docstring
```python
# ❌
def calc(a, b, c):
    return a * b * (1 + c)

# ✅
def calculate_total(price, qty, tax_rate):
    """Calculate total price with tax."""
    return price * qty * (1 + tax_rate)
```

### Mistake 4: Too many responsibilities
```python
# ❌
def process_order(order):
    # validate + save + email + inventory + invoice + analytics
    pass

# ✅
def validate_order(order): ...
def save_order(order): ...
def process_order(order):
    validate_order(order)
    save_order(order)
```

---

## 9. Debugging

### Debugging 1: Print Statement
```python
def add(a, b):
    print(f"a={a}, b={b}")   # Debug
    result = a + b
    print(f"result={result}")  # Debug
    return result

add(5, 3)
```

### Debugging 2: `pdb` (Python Debugger)
```python
import pdb

def add(a, b):
    pdb.set_trace()   # Breakpoint
    return a + b

add(5, 3)
```

### Debugging 3: Traceback Padhna
```python
def a():
    return b()

def b():
    return c()

def c():
    return 1 / 0   # ZeroDivisionError

a()
```

**Traceback:**
```
Traceback (most recent call last):
  File "test.py", line 11, in <module>
    a()
  File "test.py", line 2, in a
    return b()
  File "test.py", line 5, in b
    return c()
  File "test.py", line 8, in c
    return 1 / 0
ZeroDivisionError: division by zero
```

**Kaise padhein:** Neeche se upar. `c()` mein error, `b()` ne call kiya, `a()` ne call kiya.

---

## 10. Backend Mein Iska Use

| Backend Area | Function Ka Use |
|--------------|-----------------|
| API Endpoints | Har endpoint ek function |
| Business Logic | Discount, tax calculation |
| Validation | Input check |
| Database Operations | CRUD functions |
| Authentication | Login, logout |
| Notifications | Email, SMS sending |
| Utilities | Date formatting, currency |

---

## 11. Real Backend Example

```python
def validate_order(order):
    """Validate order before processing."""
    if not order.get("items"):
        return False, "Order has no items"
    if order.get("total", 0) <= 0:
        return False, "Invalid total amount"
    return True, "Valid"

def save_to_database(order):
    """Save order to DB (simulated)."""
    print(f"[DB] Order {order['id']} saved")
    return True

def send_notification(order):
    """Notify user and restaurant."""
    print(f"[NOTIFY] User notified for order {order['id']}")
    return True

def process_order(order):
    """
    Complete order processing pipeline.
    Real-world: Zomato/Swiggy order flow.
    """
    # Step 1: Validate
    is_valid, message = validate_order(order)
    if not is_valid:
        return {"status": "error", "message": message}
    
    # Step 2: Save
    save_to_database(order)
    
    # Step 3: Notify
    send_notification(order)
    
    # Step 4: Response
    return {
        "status": "success",
        "order_id": order["id"],
        "message": "Order processed successfully"
    }

# Usage
order = {"id": 101, "items": ["Pizza", "Coke"], "total": 310}
response = process_order(order)
print(response)
```

**Output:**
```
[DB] Order 101 saved
[NOTIFY] User notified for order 101
{'status': 'success', 'order_id': 101, 'message': 'Order processed successfully'}
```

---

## 12. Interview Questions

**Q1: Function kya hai?**
> Named, reusable block of code. Specific task karta hai.

**Q2: Function ke fayde?**
> Reusability, modularity, abstraction, testability, debugging.

**Q3: `return` vs `print`?**
> `return` value deta hai, `print` dikhata hai. Backend mein `return`.

**Q4: Function ke types?**
> Built-in, user-defined, lambda, recursive, generator, higher-order.

**Q5: Docstring kya hai?**
> Function documentation. `"""..."""`.

**Q6: Function overloading?**
> Python mein direct nahi. Default args, `*args`, `singledispatch`.

**Q7: First-class function?**
> Function ko variable mein store, pass, return kar sakte hain.

**Q8: Call stack kya hai?**
> Function calls ka record. LIFO.

**Q9: Pure function kya hai?**
> Same input → same output, no side effects.

**Q10: Higher-order function?**
> Function jo function leta/return karta hai.

---

## 13. Student Questions / Doubts

**Doubt 1: `print` aur `return` mein kya difference?**
> `print` sirf screen pe dikhata hai. `return` value ko bahar bhejta hai. Backend mein `return` use karo.

**Doubt 2: Function ke bina kaam nahi chal sakta?**
> Chal sakta hai, but code lamba, repeat, aur maintain karna mushkil hoga.

**Doubt 3: Function ka naam kya rakhun?**
> Verb-based, clear. `calculate_total`, `get_user`, `send_email`.

**Doubt 4: Docstring zaroori hai?**
> Zaroori nahi, but professional code mein likhna chahiye.

**Doubt 5: Function ke andar function bana sakte hain?**
> Haan, nested functions. Closures aur decorators isi pe based hain.

---

## 14. Practice Problems

**Q1:** Function banao jo 3 numbers ka average return kare.
```python
def average(a, b, c):
    return (a + b + c) / 3

print(average(10, 20, 30))   # 20.0
```

**Q2:** Function banao jo string mein vowels count kare.
```python
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in text if ch in vowels)

print(count_vowels("Hello World"))   # 3
```

**Q3:** Function banao jo prime check kare.
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))    # True
print(is_prime(10))   # False
```

**Q4:** Function banao jo second largest return kare.
```python
def second_largest(numbers):
    if len(numbers) < 2:
        return None
    unique = sorted(set(numbers), reverse=True)
    return unique[1] if len(unique) > 1 else None

print(second_largest([5, 2, 8, 1, 9, 9]))   # 8
```

**Q5:** Function banao jo string reverse kare bina slicing.
```python
def reverse_string(text):
    result = ""
    for char in text:
        result = char + result
    return result

print(reverse_string("hello"))   # olleh
```

---

## 15. Mini Task/Project

### Task: Simple Calculator

**Requirements:**
- `add(a, b)` — addition
- `subtract(a, b)` — subtraction
- `multiply(a, b)` — multiplication
- `divide(a, b)` — division (zero check)
- `calculator(operation, a, b)` — main function

**Solution:**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator(operation, a, b):
    operations = {
        "add": add,
        "sub": subtract,
        "mul": multiply,
        "div": divide
    }
    func = operations.get(operation)
    if not func:
        return f"Unknown operation: {operation}"
    return func(a, b)

# Test
print(calculator("add", 10, 5))    # 15
print(calculator("sub", 10, 5))    # 5
print(calculator("mul", 10, 5))    # 50
print(calculator("div", 10, 5))    # 2.0
print(calculator("div", 10, 0))    # Error
print(calculator("mod", 10, 5))    # Unknown
```

---

## 16. Teaching Points — Class Mein Kya Explain Karna Hai

### Point 1: Function = Recipe
> "Beta, jaise chai ki recipe hoti hai — ek baar likho, baar-baar use karo. Function wahi hai."

### Point 2: `return` vs `print`
> "`print` = screen pe dikhana. `return` = value bahar bhejna. Backend mein `return` use karte hain."

### Point 3: Naming Convention
> "Function ka naam verb se shuru karo — `get_`, `set_`, `calculate_`, `process_`."

### Point 4: Docstring
> "Har function pe docstring likho. Ye documentation hai."

### Point 5: Ek Function = Ek Kaam
> "Ek function sirf ek kaam kare. Agar 10 kaam kar raha hai, to todo."

### Blackboard Pe Kya Likhun
```
def calculate_total(price, qty, tax=0.18):
    return price * qty * (1 + tax)

calculate_total(100, 2)  →  236.0
calculate_total(200, 3)  →  708.0
```

### Class Activity
1. Students se ek function likhwao — `greet(name)`
2. Call karwao — `greet("Rohit")`
3. `return` vs `print` ka difference dikhao
4. Ek real-world example do — `calculate_total`
5. Homework: 5 functions likho

---

# 📖 TOPIC 2: `*args`

---

## 1. Concept Kya Hai?

`*args` ek special syntax hai jo function ko **kitne bhi positional arguments** lene deta hai. Jo bhi extra arguments aate hain, wo sab ek **tuple** mein pack ho jaate hain.

**Technical:** `*args` allows a function to accept any number of positional arguments. Inside the function, `args` is a tuple.

---

## 2. Why Do We Need It?

### Problem: Fixed Number of Arguments
```python
def add(a, b):
    return a + b

print(add(1, 2))        # 3
print(add(1, 2, 3))     # ❌ TypeError
```

Agar 3 numbers add karne hain, to naya function banana padega. 4 ke liye naya. 5 ke liye naya. **Impractical.**

### Solution: `*args`
```python
def add(*args):
    return sum(args)

print(add(1, 2))           # 3
print(add(1, 2, 3))        # 6
print(add(1, 2, 3, 4))     # 10
print(add(1, 2, 3, 4, 5))  # 15
```

**Ek function, kitne bhi arguments.**

---

## 3. Real-Life Analogy

Socho aapke paas ek **bag** hai. Aap usme:
- 2 cheezein daalo — bag le leta hai
- 5 daalo — bag le leta hai
- 10 daalo — bag le leta hai

Bag **sab le leta hai**. `*args` wahi bag hai. Jo bhi arguments do, sab ek tuple mein pack ho jaate hain.

---

## 4. Syntax

```python
def function_name(*args):
    # args is a tuple
    pass
```

**Example:**
```python
def total(*args):
    return sum(args)
```

**Naam `args` zaroori nahi:**
```python
def total(*numbers): ...
def total(*values): ...
def total(*items): ...
```

`*` star important hai, naam nahi.

---

## 5. Basic Examples

### Example 1: Basic Sum
```python
def total(*args):
    return sum(args)

print(total(1, 2, 3))         # 6
print(total(10, 20, 30, 40))  # 100
print(total())                # 0
```

### Example 2: Maximum Finder
```python
def find_max(*numbers):
    if not numbers:
        return None
    return max(numbers)

print(find_max(5, 2, 8, 1, 9))   # 9
print(find_max(10, 20))           # 20
print(find_max())                 # None
```

### Example 3: Logging
```python
def log_message(level, *messages):
    for msg in messages:
        print(f"[{level.upper()}] {msg}")

log_message("info", "User logged in", "Session created", "Token issued")
```

**Output:**
```
[INFO] User logged in
[INFO] Session created
[INFO] Token issued
```

### Example 4: Type Check
```python
def show_type(*args):
    print(type(args))   # <class 'tuple'>
    print(args)

show_type(1, "hello", 3.14, True)
# (1, 'hello', 3.14, True)
```

---

## 6. Step-by-Step Execution

```python
def total(*args):
    print(f"args = {args}")
    return sum(args)

result = total(1, 2, 3, 4)
print(result)
```

**Step-by-step:**
```
Step 1: Function call total(1, 2, 3, 4)
Step 2: Python dekhta hai *args
Step 3: Saare positional arguments collect karta hai
Step 4: Tuple banata hai: (1, 2, 3, 4)
Step 5: args = (1, 2, 3, 4)
Step 6: print(f"args = {args}") → args = (1, 2, 3, 4)
Step 7: sum(args) = 10
Step 8: return 10
Step 9: result = 10
Step 10: print(result) → 10
```

**Visualization:**
```
total(1, 2, 3, 4)
       ↓
args = (1, 2, 3, 4)   ← tuple
```

---

## 7. Internal Working

```python
def total(*args):
    print(type(args))    # <class 'tuple'>
    print(args)          # (1, 2, 3, 4)
    return sum(args)
```

**Internally:**
- `*args` ek tuple object banata hai
- Saare extra positional arguments us tuple mein daalta hai
- `args` variable us tuple ko refer karta hai

**Proof:**
```python
def func(*args):
    print(id(args))
    args = args + (5,)   # Naya tuple
    print(id(args))

func(1, 2, 3)
```

---

## 8. Common Mistakes

### Mistake 1: `*args` ke baad regular parameter
```python
# ❌
def func(*args, a):   # a keyword-only ban jaata hai
    pass

# ✅
def func(a, *args):
    pass
```

### Mistake 2: `*args` ko list samajhna
```python
# ❌
def func(*args):
    args.append(5)   # AttributeError — tuple immutable

# ✅
def func(*args):
    args = list(args)
    args.append(5)
```

### Mistake 3: `*args` ke baad `**kwargs` order
```python
# ❌
def func(**kwargs, *args):   # SyntaxError
    pass

# ✅
def func(*args, **kwargs):
    pass
```

---

## 9. Debugging

### Debugging 1: Print args
```python
def total(*args):
    print(f"args = {args}")       # Debug
    print(f"type = {type(args)}")  # Debug
    return sum(args)

total(1, 2, 3)
```

### Debugging 2: Length check
```python
def total(*args):
    if not args:
        print("No arguments")   # Debug
        return 0
    return sum(args)
```

### Debugging 3: Type check
```python
def total(*args):
    for i, arg in enumerate(args):
        if not isinstance(arg, (int, float)):
            print(f"Invalid at index {i}: {arg}")
    return sum(args)
```

---

## 10. Backend Mein Iska Use

| Area | Use |
|------|-----|
| Bulk email | Kitne bhi recipients |
| Logging | Kitne bhi messages |
| Cart total | Kitne bhi items |
| Decorator wrapper | Forward args |
| Math operations | Kitne bhi numbers |
| Event handlers | Multiple payloads |

---

## 11. Real Backend Example

```python
def send_bulk_emails(subject, body, *recipients):
    """
    Send email to multiple recipients.
    Real-world: notification system, marketing emails.
    """
    print(f"Sending email: {subject}")
    print(f"Body: {body}")
    print(f"Recipients: {len(recipients)}")
    
    sent = []
    for email in recipients:
        print(f"  → Sent to {email}")
        sent.append(email)
    
    return {"total": len(sent), "recipients": sent}

# Usage
result = send_bulk_emails(
    "Welcome to Zomato",
    "Thanks for joining!",
    "rohit@x.com",
    "anchal@x.com",
    "shyam@x.com"
)

print(f"\nTotal sent: {result['total']}")
```

**Output:**
```
Sending email: Welcome to Zomato
Body: Thanks for joining!
Recipients: 3
  → Sent to rohit@x.com
  → Sent to anchal@x.com
  → Sent to shyam@x.com

Total sent: 3
```

---

## 12. Interview Questions

**Q1: `*args` kya hai?**
> Variable positional arguments. Saare extra positional args ek tuple mein pack ho jaate hain.

**Q2: `args` ka type kya hai?**
> Tuple.

**Q3: `*args` ke baad kya aata hai?**
> `**kwargs`.

**Q4: `args` naam zaroori hai?**
> Nahi. `*` star important hai.

**Q5: `*args` kab use karte hain?**
> Bulk operations, logging, math.

**Q6: `*args` aur list mein difference?**
> `*args` function definition mein. List data structure.

---

## 13. Student Questions / Doubts

**Doubt 1: `*args` aur `*numbers` mein difference?**
> Kuch nahi. `*` important hai, naam nahi.

**Doubt 2: `*args` ke saath regular parameter?**
> Haan, `def func(a, *args):` — `a` fixed, `args` variable.

**Doubt 3: `*args` ke baad default?**
> Nahi. Order: positional → default → `*args` → `**kwargs`.

**Doubt 4: `*args` ko modify kar sakte hain?**
> Nahi, tuple immutable hai. List mein convert karo.

**Doubt 5: `*args` empty ho sakta hai?**
> Haan, `total()` → `args = ()`.

---

## 14. Practice Problems

**Q1:** Function banao jo `*args` se sum, average, min, max return kare.
```python
def stats(*numbers):
    if not numbers:
        return None
    return {
        "sum": sum(numbers),
        "avg": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

print(stats(10, 20, 30, 40))
# {'sum': 100, 'avg': 25.0, 'min': 10, 'max': 40}
```

**Q2:** Function banao jo `*args` se even numbers count kare.
```python
def count_evens(*numbers):
    return sum(1 for n in numbers if n % 2 == 0)

print(count_evens(1, 2, 3, 4, 5, 6))   # 3
```

**Q3:** Function banao jo `*args` se second largest return kare.
```python
def second_largest(*numbers):
    if len(numbers) < 2:
        return None
    unique = sorted(set(numbers), reverse=True)
    return unique[1] if len(unique) > 1 else None

print(second_largest(5, 2, 8, 1, 9, 9))   # 8
```

**Q4:** Function banao jo `*args` se string concatenate kare.
```python
def concat(*strings):
    return " ".join(strings)

print(concat("Hello", "World", "Python"))   # Hello World Python
```

**Q5:** Function banao jo `*args` se product return kare.
```python
from functools import reduce

def product(*numbers):
    if not numbers:
        return 1
    return reduce(lambda a, b: a * b, numbers)

print(product(2, 3, 4))   # 24
```

---

## 15. Mini Task/Project

### Task: Flexible Order Calculator

**Requirements:**
- `calculate_order(*items)` — kitne bhi items
- Har item dict: `{"name": ..., "price": ...}`
- Return total, item count, average

**Solution:**
```python
def calculate_order(*items):
    if not items:
        return {"total": 0, "count": 0, "average": 0}
    
    total = sum(item["price"] for item in items)
    count = len(items)
    
    return {
        "total": total,
        "count": count,
        "average": total / count,
        "items": [item["name"] for item in items]
    }

# Test
result = calculate_order(
    {"name": "Pizza", "price": 250},
    {"name": "Coke", "price": 60},
    {"name": "Brownie", "price": 120}
)
print(result)
# {'total': 430, 'count': 3, 'average': 143.33, 'items': ['Pizza', 'Coke', 'Brownie']}
```

---

## 16. Teaching Points — Class Mein Kya Explain Karna Hai

### Point 1: Bag Analogy
> "`*args` ek bag hai. Jo bhi do, sab le leta hai."

### Point 2: Tuple
> "`args` ek tuple hai. Immutable."

### Point 3: Naam Optional
> "`*` important hai, naam nahi. `*numbers`, `*values` bhi sahi."

### Point 4: Order
> "Positional → default → `*args` → `**kwargs`."

### Point 5: Real Use
> "Bulk email, logging, math operations."

### Blackboard Pe Kya Likhun
```
def total(*args):
    return sum(args)

total(1, 2, 3)  →  args = (1, 2, 3)  →  6
total(5, 10)    →  args = (5, 10)    →  15
total()         →  args = ()          →  0
```

### Class Activity
1. Students se `sum_all(*args)` likhwao
2. Call karwao — 2, 5, 10 arguments
3. `type(args)` print karwao
4. Homework: 5 functions likho `*args` ke saath

---

# 📖 TOPIC 3: `**kwargs`

---

## 1. Concept Kya Hai?

`**kwargs` ek special syntax hai jo function ko **kitne bhi keyword arguments** lene deta hai. Jo bhi extra keyword arguments aate hain, wo sab ek **dictionary** mein pack ho jaate hain.

**Technical:** `**kwargs` allows a function to accept any number of keyword arguments. Inside the function, `kwargs` is a dictionary.

---

## 2. Why Do We Need It?

### Problem: Fixed Keyword Arguments
```python
def create_user(name, email, age):
    return {"name": name, "email": email, "age": age}

print(create_user("Rohit", "r@x.com", 22))
# But agar city, phone, address bhi chahiye?
```

Har naya field ke liye function change karna padega. **Impractical.**

### Solution: `**kwargs`
```python
def create_user(**kwargs):
    return kwargs

print(create_user(name="Rohit", email="r@x.com", age=22))
print(create_user(name="Rohit", email="r@x.com", age=22, city="Bhopal"))
```

**Ek function, kitne bhi keyword arguments.**

---

## 3. Real-Life Analogy

Socho aapke paas ek **form** hai. Form mein aap:
- Naam, umar, shehar — kuch bhi likh sakte ho
- Har field ka ek **naam** aur **value** hoti hai

`**kwargs` wahi form hai. Jo bhi do, sab dictionary mein pack ho jaata hai.

---

## 4. Syntax

```python
def function_name(**kwargs):
    # kwargs is a dictionary
    pass
```

**Example:**
```python
def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

**Naam `kwargs` zaroori nahi:**
```python
def profile(**options): ...
def profile(**config): ...
def profile(**filters): ...
```

`**` double star important hai, naam nahi.

---

## 5. Basic Examples

### Example 1: Basic Profile
```python
def profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

profile(name="Rohit", age=22, city="Bhopal")
```

**Output:**
```
name: Rohit
age: 22
city: Bhopal
```

### Example 2: Dynamic Configuration
```python
def create_database(**config):
    defaults = {
        "host": "localhost",
        "port": 5432,
        "user": "admin",
        "database": "test"
    }
    defaults.update(config)
    return defaults

print(create_database())
print(create_database(host="prod-db.com", database="production"))
```

### Example 3: API Response Builder
```python
def build_response(status, message, **extra):
    response = {
        "status": status,
        "message": message,
        "timestamp": "2024-01-15T10:30:00"
    }
    response.update(extra)
    return response

print(build_response("success", "User created"))
print(build_response("success", "Order placed", order_id=101, amount=450))
```

### Example 4: Type Check
```python
def show_type(**kwargs):
    print(type(kwargs))   # <class 'dict'>
    print(kwargs)

show_type(name="Rohit", age=22)
# {'name': 'Rohit', 'age': 22}
```

---

## 6. Step-by-Step Execution

```python
def profile(**kwargs):
    print(f"kwargs = {kwargs}")
    return kwargs

result = profile(name="Rohit", age=22)
print(result)
```

**Step-by-step:**
```
Step 1: Function call profile(name="Rohit", age=22)
Step 2: Python dekhta hai **kwargs
Step 3: Saare keyword arguments collect karta hai
Step 4: Dictionary banata hai: {'name': 'Rohit', 'age': 22}
Step 5: kwargs = {'name': 'Rohit', 'age': 22}
Step 6: print(f"kwargs = {kwargs}")
Step 7: return kwargs
Step 8: result = {'name': 'Rohit', 'age': 22}
```

**Visualization:**
```
profile(name="Rohit", age=22)
       ↓
kwargs = {'name': 'Rohit', 'age': 22}   ← dict
```

---

## 7. Internal Working

```python
def profile(**kwargs):
    print(type(kwargs))    # <class 'dict'>
    print(kwargs)          # {'name': 'Rohit', 'age': 22}
    return kwargs
```

**Internally:**
- `**kwargs` ek dictionary object banata hai
- Saare extra keyword arguments us dictionary mein daalta hai
- `kwargs` variable us dictionary ko refer karta hai

**Proof:**
```python
def func(**kwargs):
    print(id(kwargs))
    kwargs["new"] = "value"   # Modify ho sakta hai
    print(id(kwargs))

func(a=1, b=2)
```

---

## 8. Common Mistakes

### Mistake 1: `**kwargs` ke baad regular parameter
```python
# ❌
def func(**kwargs, a):   # SyntaxError
    pass

# ✅
def func(a, **kwargs):
    pass
```

### Mistake 2: `**kwargs` ko positional samajhna
```python
# ❌
def func(**kwargs):
    print(kwargs[0])   # KeyError

# ✅
def func(**kwargs):
    print(kwargs["name"])
```

### Mistake 3: `**kwargs` ke baad `*args`
```python
# ❌
def func(**kwargs, *args):   # SyntaxError
    pass

# ✅
def func(*args, **kwargs):
    pass
```

---

## 9. Debugging

### Debugging 1: Print kwargs
```python
def profile(**kwargs):
    print(f"kwargs = {kwargs}")       # Debug
    print(f"type = {type(kwargs)}")    # Debug
    print(f"keys = {list(kwargs.keys())}")  # Debug
    return kwargs

profile(name="Rohit", age=22)
```

### Debugging 2: Key check
```python
def profile(**kwargs):
    if "name" not in kwargs:
        print("Name missing")   # Debug
    return kwargs
```

### Debugging 3: Type check
```python
def profile(**kwargs):
    for key, value in kwargs.items():
        if not isinstance(value, (str, int, float, bool)):
            print(f"Invalid type for {key}: {type(value)}")
    return kwargs
```

---

## 10. Backend Mein Iska Use

| Area | Use |
|------|-----|
| API response | Flexible fields |
| Database filter | Dynamic conditions |
| Configuration | Optional settings |
| User profile | Variable fields |
| Decorator wrapper | Forward keyword args |
| Query builder | Dynamic SQL |

---

## 11. Real Backend Example

```python
def filter_products(**filters):
    """
    Dynamic filtering for e-commerce.
    Real-world: Django ORM, SQL query builder.
    """
    if not filters:
        return "SELECT * FROM products"
    
    conditions = []
    for key, value in filters.items():
        if key.endswith("__lt"):
            field = key[:-4]
            conditions.append(f"{field} < {value}")
        elif key.endswith("__gt"):
            field = key[:-4]
            conditions.append(f"{field} > {value}")
        else:
            conditions.append(f"{key} = '{value}'")
    
    where = " AND ".join(conditions)
    return f"SELECT * FROM products WHERE {where}"

# Usage
print(filter_products())
print(filter_products(category="electronics"))
print(filter_products(category="electronics", price__lt=1000))
print(filter_products(category="electronics", price__lt=1000, in_stock=True))
```

**Output:**
```
SELECT * FROM products
SELECT * FROM products WHERE category = 'electronics'
SELECT * FROM products WHERE category = 'electronics' AND price < 1000
SELECT * FROM products WHERE category = 'electronics' AND price < 1000 AND in_stock = 'True'
```

---

## 12. Interview Questions

**Q1: `**kwargs` kya hai?**
> Variable keyword arguments. Saare extra keyword args ek dictionary mein pack ho jaate hain.

**Q2: `kwargs` ka type kya hai?**
> Dictionary.

**Q3: `**kwargs` ke baad kya aata hai?**
> Kuch nahi. Ye last mein aata hai.

**Q4: `kwargs` naam zaroori hai?**
> Nahi. `**` double star important hai.

**Q5: `**kwargs` kab use karte hain?**
> API response, config, dynamic filters.

**Q6: `**kwargs` aur dict mein difference?**
> `**kwargs` function definition mein. Dict data structure.

---

## 13. Student Questions / Doubts

**Doubt 1: `**kwargs` aur `*args` mein difference?**
> `*args` = tuple of positional. `**kwargs` = dict of keyword.

**Doubt 2: `**kwargs` ke saath regular parameter?**
> Haan, `def func(a, **kwargs):` — `a` fixed, `kwargs` variable.

**Doubt 3: `**kwargs` modify kar sakte hain?**
> Haan, dictionary mutable hai.

**Doubt 4: `**kwargs` empty ho sakta hai?**
> Haan, `profile()` → `kwargs = {}`.

**Doubt 5: `**kwargs` aur `**options` mein difference?**
> Kuch nahi. `**` important hai, naam nahi.

---

## 14. Practice Problems

**Q1:** Function banao jo `**kwargs` se full name build kare.
```python
def build_name(**parts):
    return " ".join(parts.values())

print(build_name(first="Rohit", middle="Kumar", last="Sharma"))
# Rohit Kumar Sharma
```

**Q2:** Function banao jo `**kwargs` se filter kare.
```python
def filter_data(**filters):
    return filters

print(filter_data(status="active", role="admin"))
# {'status': 'active', 'role': 'admin'}
```

**Q3:** Function banao jo `**kwargs` se config merge kare.
```python
def merge_config(**kwargs):
    defaults = {"debug": False, "port": 8000}
    defaults.update(kwargs)
    return defaults

print(merge_config(debug=True))
# {'debug': True, 'port': 8000}
```

**Q4:** Function banao jo `**kwargs` se total price calculate kare.
```python
def total_price(**items):
    return sum(items.values())

print(total_price(pizza=250, coke=60, brownie=120))   # 430
```

**Q5:** Function banao jo `**kwargs` se key count kare.
```python
def count_keys(**kwargs):
    return len(kwargs)

print(count_keys(a=1, b=2, c=3))   # 3
```

---

## 15. Mini Task/Project

### Task: User Registration System

**Requirements:**
- `register_user(**data)` — flexible user data
- Required fields check: name, email
- Optional fields: age, city, phone
- Return structured response

**Solution:**
```python
def register_user(**data):
    """
    Register user with flexible fields.
    """
    required = ["name", "email"]
    
    # Check required
    missing = [field for field in required if field not in data]
    if missing:
        return {"status": "error", "message": f"Missing: {missing}"}
    
    # Build user
    user = {
        "name": data["name"],
        "email": data["email"],
        "age": data.get("age"),
        "city": data.get("city"),
        "phone": data.get("phone"),
        "status": "active"
    }
    
    return {"status": "success", "user": user}

# Test
print(register_user(name="Rohit", email="r@x.com"))
print(register_user(name="Anchal", email="a@x.com", age=22, city="Bhopal"))
print(register_user(name="Shyam"))
```

**Output:**
```
{'status': 'success', 'user': {'name': 'Rohit', 'email': 'r@x.com', 'age': None, ...}}
{'status': 'success', 'user': {'name': 'Anchal', 'email': 'a@x.com', 'age': 22, ...}}
{'status': 'error', 'message': "Missing: ['email']"}
```

---

## 16. Teaching Points — Class Mein Kya Explain Karna Hai

### Point 1: Form Analogy
> "`**kwargs` ek form hai. Jo bhi field bharo, sab dictionary mein aata hai."

### Point 2: Dictionary
> "`kwargs` ek dictionary hai. Mutable."

### Point 3: Naam Optional
> "`**` important hai, naam nahi."

### Point 4: Last Mein Aata Hai
> "`**kwargs` hamesha last mein."

### Point 5: Real Use
> "API response, config, dynamic filters."

### Blackboard Pe Kya Likhun
```
def profile(**kwargs):
    return kwargs

profile(name="Rohit", age=22)
       ↓
kwargs = {'name': 'Rohit', 'age': 22}
```

### Class Activity
1. Students se `show_info(**kwargs)` likhwao
2. Call karwao — 2, 4 keyword args
3. `type(kwargs)` print karwao
4. Homework: 5 functions likho `**kwargs` ke saath

---

# 📖 TOPIC 4: LAMBDA

---

## 1. Concept Kya Hai?

Lambda ek **chhota, anonymous function** hai jo **ek hi line** mein likha jaata hai. Iska koi naam nahi hota. Iska sirf ek expression hota hai.

**Technical:** A lambda function is a small, anonymous, single-expression function. It is defined using the `lambda` keyword.

---

## 2. Why Do We Need It?

### Problem: Chhota Function, Baar-Baar Nahi Chahiye
```python
def square(x):
    return x ** 2

# Ye function sirf ek jagah use hoga
# Naam dena zaroori nahi
```

### Solution: Lambda
```python
square = lambda x: x ** 2
```

### Kab Use Hoga
- `sorted()` ka key
- `filter()` condition
- `map()` transform
- `reduce()` accumulate
- One-time use

---

## 3. Real-Life Analogy

Lambda ek **chhota helper** hai bina naam ke. Jaise ek chhota worker jo ek hi kaam karta hai. `def` bada function hai — multiple lines. Lambda chhota — ek line.

---

## 4. Syntax

```python
lambda arguments: expression
```

| Part | Matlab |
|------|--------|
| `lambda` | Keyword |
| `arguments` | Input params |
| `:` | Separator |
| `expression` | Single line return |

---

## 5. Basic Examples

### Example 1: Basic Lambda
```python
square = lambda x: x ** 2
print(square(5))   # 25

add = lambda a, b: a + b
print(add(3, 4))   # 7

is_even = lambda x: x % 2 == 0
print(is_even(10))   # True
```

### Example 2: Lambda with `sorted`
```python
users = [
    {"name": "Rohit", "age": 25},
    {"name": "Anchal", "age": 22},
    {"name": "Shyam", "age": 30}
]

by_age = sorted(users, key=lambda u: u["age"])
for u in by_age:
    print(u)
```

### Example 3: Lambda with `filter` and `map`
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8]

squares = list(map(lambda x: x ** 2, numbers))
print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64]
```

### Example 4: Multi-Key Sort
```python
orders = [
    {"id": 1, "amount": 500, "priority": "low"},
    {"id": 2, "amount": 1500, "priority": "high"},
    {"id": 3, "amount": 800, "priority": "high"},
]

sorted_orders = sorted(
    orders,
    key=lambda o: (
        0 if o["priority"] == "high" else 1,
        -o["amount"]
    )
)

for o in sorted_orders:
    print(o)
```

---

## 6. Step-by-Step Execution

```python
square = lambda x: x ** 2
result = square(5)
print(result)
```

**Step-by-step:**
```
Step 1: lambda expression evaluate hota hai
Step 2: Ek anonymous function object banta hai
Step 3: square variable us object ko bind karta hai
Step 4: square(5) call → x=5
Step 5: x ** 2 = 25
Step 6: return 25
Step 7: result = 25
```

---

## 7. Internal Working

```python
square = lambda x: x ** 2
print(type(square))       # <class 'function'>
print(square.__name__)    # <lambda>
```

**Internally:**
- Lambda bhi ek function object hai
- Bas uska naam `<lambda>` hota hai
- Same internal structure

**Proof:**
```python
def normal(x):
    return x ** 2

lam = lambda x: x ** 2

print(normal(5))   # 25
print(lam(5))      # 25
print(type(normal))  # <class 'function'>
print(type(lam))     # <class 'function'>
```

---

## 8. Common Mistakes

### Mistake 1: Multiple statements
```python
# ❌
lambda x: print(x); return x   # SyntaxError

# ✅
lambda x: x + 1
```

### Mistake 2: Complex logic
```python
# ❌
lambda x: x if x > 0 else -x if x < 0 else 0

# ✅
def sign(x):
    if x > 0:
        return x
    elif x < 0:
        return -x
    return 0
```

### Mistake 3: Lambda with no args
```python
# ❌ — allowed but useless
f = lambda: 5

# ✅
f = lambda x: x + 5
```

---

## 9. Debugging

### Debugging 1: Print lambda result
```python
square = lambda x: x ** 2
print(square(5))   # Debug
```

### Debugging 2: Check type
```python
square = lambda x: x ** 2
print(type(square))   # <class 'function'>
```

### Debugging 3: Convert to def
```python
# Lambda
square = lambda x: x ** 2

# Def equivalent (debugging ke liye)
def square(x):
    return x ** 2
```

---

## 10. Backend Mein Iska Use

| Area | Use |
|------|-----|
| Sorting | `sorted(key=lambda ...)` |
| Filtering | `filter(lambda ...)` |
| Mapping | `map(lambda ...)` |
| Reducing | `reduce(lambda ...)` |
| DRF serializers | Field functions |
| Django | Query expressions |

---

## 11. Real Backend Example

```python
orders = [
    {"id": 1, "amount": 500, "priority": "low", "date": "2024-01-15"},
    {"id": 2, "amount": 1500, "priority": "high", "date": "2024-01-14"},
    {"id": 3, "amount": 800, "priority": "high", "date": "2024-01-16"},
    {"id": 4, "amount": 2000, "priority": "low", "date": "2024-01-13"},
]

# Pehle priority (high first), phir amount (high first)
sorted_orders = sorted(
    orders,
    key=lambda o: (
        0 if o["priority"] == "high" else 1,
        -o["amount"]
    )
)

for o in sorted_orders:
    print(f"ID: {o['id']}, Priority: {o['priority']}, Amount: {o['amount']}")
```

**Output:**
```
ID: 2, Priority: high, Amount: 1500
ID: 3, Priority: high, Amount: 800
ID: 4, Priority: low, Amount: 2000
ID: 1, Priority: low, Amount: 500
```

---

## 12. Interview Questions

**Q1: Lambda kya hai?**
> Anonymous single-expression function.

**Q2: Lambda vs def?**
> Lambda single expression, anonymous. `def` multi-line, named.

**Q3: Lambda kahan use karte hain?**
> `sorted()`, `filter()`, `map()`, `reduce()`.

**Q4: Lambda mein multiple statements?**
> Nahi. Sirf single expression.

**Q5: Lambda ko variable mein store?**
> Haan, but PEP 8 kehta hai `def` use karo.

**Q6: Lambda closure?**
> Haan, lambda bhi closure bana sakta hai.

---

## 13. Student Questions / Doubts

**Doubt 1: Lambda ka naam kyu nahi hota?**
> Anonymous function hai. Ek baar use karna ho to naam ki zaroorat nahi.

**Doubt 2: Lambda mein `return` likhna?**
> Nahi. Expression automatically return hota hai.

**Doubt 3: Lambda mein loop?**
> Nahi. Single expression only.

**Doubt 4: Lambda aur def mein speed?**
> Same. Lambda sirf syntax sugar hai.

**Doubt 5: Lambda kahan nahi use karna?**
> Complex logic, multiple statements, debugging.

---

## 14. Practice Problems

**Q1:** Lambda se list ko square karo.
```python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)   # [1, 4, 9, 16, 25]
```

**Q2:** Lambda se even numbers filter karo.
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6, 8]
```

**Q3:** Lambda se dict ko value se sort karo.
```python
data = {"a": 3, "b": 1, "c": 2}
sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_data)   # {'b': 1, 'c': 2, 'a': 3}
```

**Q4:** Lambda se list of tuples ko second element se sort karo.
```python
students = [("Rohit", 85), ("Anchal", 92), ("Shyam", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_students)
# [('Anchal', 92), ('Rohit', 85), ('Shyam', 78)]
```

**Q5:** Lambda se string length se sort karo.
```python
words = ["python", "is", "awesome", "programming"]
sorted_words = sorted(words, key=lambda w: len(w))
print(sorted_words)
# ['is', 'python', 'awesome', 'programming']
```

---

## 15. Mini Task/Project

### Task: Product Sorting System

**Requirements:**
- `sort_products(products, key, reverse)` — flexible sorting
- Key options: name, price, rating
- Return sorted list

**Solution:**
```python
def sort_products(products, key="name", reverse=False):
    """
    Sort products by various keys.
    """
    key_funcs = {
        "name": lambda p: p["name"],
        "price": lambda p: p["price"],
        "rating": lambda p: p["rating"]
    }
    
    func = key_funcs.get(key)
    if not func:
        return {"error": f"Invalid key: {key}"}
    
    return sorted(products, key=func, reverse=reverse)

# Test
products = [
    {"name": "Laptop", "price": 50000, "rating": 4.5},
    {"name": "Phone", "price": 20000, "rating": 4.8},
    {"name": "Tablet", "price": 15000, "rating": 4.2},
]

print(sort_products(products, "price"))
print(sort_products(products, "rating", reverse=True))
```

---

## 16. Teaching Points — Class Mein Kya Explain Karna Hai

### Point 1: Chhota Helper
> "Lambda ek chhota helper hai bina naam ke. Ek line, ek kaam."

### Point 2: Single Expression
> "Sirf ek expression. Multiple statements nahi."

### Point 3: `sorted`, `filter`, `map`
> "Inke saath common use."

### Point 4: Complex Logic?
> "`def` use karo, lambda nahi."

### Point 5: PEP 8
> "Agar naam dena hai, `def` use karo."

### Blackboard Pe Kya Likhun
```
lambda x: x ** 2
       ↓
  anonymous
  single line
  returns expression
```

### Class Activity
1. Students se `lambda x: x + 1` likhwao
2. `sorted()` mein use karwao
3. `filter()` mein use karwao
4. Homework: 5 lambda examples

---

# 📖 TOPIC 5: MAP

---

## 1. Concept Kya Hai?

`map()` ek function hai jo **har element pe ek function apply** karta hai aur **naya iterable** return karta hai.

**Technical:** `map(function, iterable)` applies the given function to each item of the iterable and returns a map object.

---

## 2. Why Do We Need It?

### Problem: Manual Loop
```python
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
print(squares)   # [1, 4, 9, 16, 25]
```

### Solution: Map
```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)   # [1, 4, 9, 16, 25]
```

**Chhota, clean, functional.**

---

## 3. Real-Life Analogy

Socho aapke paas ek **machine** hai. Aap usme 5 raw items daalo, machine har ek pe kaam karti hai, 5 finished items deti hai. `map` wahi machine hai.

---

## 4. Syntax

```python
map(function, iterable)
```

---

## 5. Basic Examples

### Example 1: Basic
```python
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)   # [1, 4, 9, 16, 25]
```

### Example 2: Multiple Iterables
```python
a = [1, 2, 3]
b = [10, 20, 30]

result = list(map(lambda x, y: x + y, a, b))
print(result)   # [11, 22, 33]
```

### Example 3: Strings
```python
names = ["rohit", "anchal", "shyam"]
capitalized = list(map(str.capitalize, names))
print(capitalized)   # ['Rohit', 'Anchal', 'Shyam']
```

### Example 4: Price with GST
```python
def add_gst(price):
    return round(price * 1.18, 2)

product_prices = [100, 250, 500, 1000, 1500]
prices_with_gst = list(map(add_gst, product_prices))

print("Original:", product_prices)
print("With GST:", prices_with_gst)
```

---

## 6. Step-by-Step Execution

```python
numbers = [1, 2, 3]
squares = list(map(lambda x: x ** 2, numbers))
```

**Step-by-step:**
```
Step 1: map() call hota hai
Step 2: Lambda function set hota hai
Step 3: Har element pe lambda apply:
        x=1 → 1
        x=2 → 4
        x=3 → 9
Step 4: Map object banta hai: <map object>
Step 5: list() se list: [1, 4, 9]
```

---

## 7. Internal Working

```python
numbers = [1, 2, 3]
m = map(lambda x: x ** 2, numbers)
print(type(m))   # <class 'map'>
```

**Internally:**
- `map` ek iterator return karta hai
- Lazy evaluation — ek time pe ek value
- `list()` se convert

**Proof:**
```python
numbers = [1, 2, 3]
m = map(lambda x: x ** 2, numbers)
print(next(m))   # 1
print(next(m))   # 4
print(next(m))   # 9
```

---

## 8. Common Mistakes

### Mistake 1: Direct print
```python
# ❌
numbers = [1, 2, 3]
print(map(lambda x: x ** 2, numbers))
# <map object at 0x...>

# ✅
print(list(map(lambda x: x ** 2, numbers)))
```

### Mistake 2: Multiple use
```python
# ❌
m = map(lambda x: x ** 2, [1, 2, 3])
print(list(m))   # [1, 4, 9]
print(list(m))   # [] — exhausted

# ✅
numbers = [1, 2, 3]
print(list(map(lambda x: x ** 2, numbers)))
print(list(map(lambda x: x ** 2, numbers)))
```

### Mistake 3: Different lengths
```python
# map stops at shortest
a = [1, 2, 3, 4, 5]
b = [10, 20]
result = list(map(lambda x, y: x + y, a, b))
print(result)   # [11, 22]
```

---

## 9. Debugging

### Debugging 1: Print map object
```python
numbers = [1, 2, 3]
m = map(lambda x: x ** 2, numbers)
print(m)   # <map object>
print(list(m))   # [1, 4, 9]
```

### Debugging 2: Convert to loop
```python
numbers = [1, 2, 3]
for n in numbers:
    print(n ** 2)   # Debug
```

### Debugging 3: Named function
```python
def square(x):
    return x ** 2

numbers = [1, 2, 3]
print(list(map(square, numbers)))
```

---

## 10. Backend Mein Iska Use

| Area | Use |
|------|-----|
| Price calculation | GST, discount |
| Data transformation | API response |
| Bulk operations | Multiple items |
| String processing | Uppercase, strip |
| Type conversion | Str → Int |

---

## 11. Real Backend Example

```python
def calculate_discount(price):
    """Apply 10% discount."""
    return round(price * 0.9, 2)

product_prices = [100, 250, 500, 1000, 1500]
discounted = list(map(calculate_discount, product_prices))

print("Original:", product_prices)
print("Discounted:", discounted)
```

**Output:**
```
Original: [100, 250, 500, 1000, 1500]
Discounted: [90.0, 225.0, 450.0, 900.0, 1350.0]
```

---

## 12. Interview Questions

**Q1: Map kya hai?**
> Har element pe function apply, naya iterable return.

**Q2: Map ka return type?**
> Map object. `list()` se list.

**Q3: Map vs list comprehension?**
> Map functional, list comp Pythonic. List comp faster.

**Q4: Map multiple iterables?**
> Haan, `map(func, list1, list2)`.

**Q5: Map kab use karte hain?**
> Jab har element ko transform karna ho.

**Q6: Map aur filter mein difference?**
> Map transform, filter condition.

---

## 13. Student Questions / Doubts

**Doubt 1: Map aur loop mein difference?**
> Map clean, functional. Loop traditional.

**Doubt 2: Map lazy hai?**
> Haan, iterator return karta hai. `list()` se convert.

**Doubt 3: Map ke saath lambda zaroori?**
> Nahi. Named function bhi.

**Doubt 4: Map se index milta?**
> Nahi. `enumerate` use karo.

**Doubt 5: Map exhausted?**
> Haan, ek baar use karne ke baad. Dobara call karo.

---

## 14. Practice Problems

**Q1:** Map se list ke saare numbers double karo.
```python
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(doubled)   # [2, 4, 6, 8, 10]
```

**Q2:** Map se strings uppercase karo.
```python
words = ["hello", "world"]
upper = list(map(str.upper, words))
print(upper)   # ['HELLO', 'WORLD']
```

**Q3:** Map se do lists add karo.
```python
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
print(result)   # [11, 22, 33]
```

**Q4:** Map se string lengths nikalo.
```python
words = ["python", "is", "awesome"]
lengths = list(map(len, words))
print(lengths)   # [6, 2, 7]
```

**Q5:** Map se Celsius to Fahrenheit.
```python
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)   # [32.0, 50.0, 68.0, 86.0, 104.0]
```

---

## 15. Mini Task/Project

### Task: Price Transformer

**Requirements:**
- `transform_prices(prices, operation)` — flexible transform
- Operations: gst, discount, round
- Return transformed list

**Solution:**
```python
def transform_prices(prices, operation="gst"):
    ops = {
        "gst": lambda p: round(p * 1.18, 2),
        "discount": lambda p: round(p * 0.9, 2),
        "round": lambda p: round(p, 0)
    }
    
    func = ops.get(operation)
    if not func:
        return {"error": f"Invalid operation: {operation}"}
    
    return list(map(func, prices))

# Test
prices = [100, 250, 500, 1000]
print(transform_prices(prices, "gst"))
print(transform_prices(prices, "discount"))
```

---

## 16. Teaching Points — Class Mein Kya Explain Karna Hai

### Point 1: Machine Analogy
> "Map ek machine hai. Raw items daalo, finished items nikalo."

### Point 2: Lazy
> "Map lazy hai. `list()` se convert."

### Point 3: Multiple Iterables
> "Do lists parallel."

### Point 4: Lambda ke Saath
> "Common combo."

### Point 5: Real Use
> "Price calculation, data transformation."

### Blackboard Pe Kya Likhun
```
map(func, [1, 2, 3])
       ↓
  [func(1), func(2), func(3)]
```

### Class Activity
1. Students se `map(lambda x: x*2, [1,2,3])` likhwao
2. `list()` se convert karwao
3. Named function se bhi karwao
4. Homework: 5 map examples

---

# 📖 TOPIC 6: FILTER

---

## 1. Concept Kya Hai?

`filter()` ek function hai jo **condition pass karne wale elements** rakhta hai aur baaki hata deta hai.

**Technical:** `filter(function, iterable)` returns an iterator with only those items for which the function returns True.

---

## 2. Why Do We Need It?

### Problem: Manual Loop
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)   # [2, 4, 6]
```

### Solution: Filter
```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6]
```

**Chhota, clean.**

---

## 3. Real-Life Analogy

Socho aap chawal mein se **kankar chhaante** ho. Chawal rakhte ho, kankar hata dete ho. `filter` wahi channi hai.

---

## 4. Syntax

```python
filter(function, iterable)
```

---

## 5. Basic Examples

### Example 1: Even Numbers
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8]
```

### Example 2: Non-Empty Strings
```python
words = ["hello", "", "world", "", "python", ""]
non_empty = list(filter(None, words))
print(non_empty)   # ['hello', 'world', 'python']
```

### Example 3: Complex Condition
```python
users = [
    {"name": "Rohit", "age": 25, "active": True},
    {"name": "Anchal", "age": 22, "active": False},
    {"name": "Shyam", "age": 30, "active": True}
]

active_adults = list(filter(
    lambda u: u["active"] and u["age"] >= 25,
    users
))
print(active_adults)
```

### Example 4: High-Value Orders
```python
orders = [
    {"id": 1, "amount": 500, "status": "paid"},
    {"id": 2, "amount": 1500, "status": "pending"},
    {"id": 3, "amount": 2500, "status": "paid"},
    {"id": 4, "amount": 800, "status": "cancelled"},
    {"id": 5, "amount": 3000, "status": "paid"}
]

def is_high_value_paid(order):
    return order["amount"] >= 1000 and order["status"] == "paid"

high_value_paid = list(filter(is_high_value_paid, orders))

for o in high_value_paid:
    print(f"ID: {o['id']}, Amount: ₹{o['amount']}")
```

**Output:**
```
ID: 3, Amount: ₹2500
ID: 5, Amount: ₹3000
```

---

## 6. Step-by-Step Execution

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
```

**Step-by-step:**
```
Step 1: filter() call hota hai
Step 2: Lambda function set hota hai
Step 3: Har element pe lambda apply:
        x=1 → False
        x=2 → True
        x=3 → False
        x=4 → True
        x=5 → False
        x=6 → True
Step 4: True wale elements rakho
Step 5: Filter object banta hai
Step 6: list() se list: [2, 4, 6]
```

---

## 7. Internal Working

```python
numbers = [1, 2, 3, 4]
f = filter(lambda x: x % 2 == 0, numbers)
print(type(f))   # <class 'filter'>
```

**Internally:**
- `filter` iterator return karta hai
- Lazy evaluation
- `list()` se convert

---

## 8. Common Mistakes

### Mistake 1: Direct print
```python
# ❌
print(filter(lambda x: x > 2, [1, 2, 3]))
# <filter object>

# ✅
print(list(filter(lambda x: x > 2, [1, 2, 3])))
```

### Mistake 2: `None` ka misuse
```python
# filter(None, iterable) — falsy values hata deta hai
words = ["hello", "", "world"]
print(list(filter(None, words)))   # ['hello', 'world']

# But ye bhi:
nums = [0, 1, 2, 0, 3]
print(list(filter(None, nums)))   # [1, 2, 3]
```

### Mistake 3: Multiple use
```python
# ❌
f = filter(lambda x: x > 2, [1, 2, 3, 4])
print(list(f))   # [3, 4]
print(list(f))   # [] — exhausted
```

---

## 9. Debugging

### Debugging 1: Print filter object
```python
numbers = [1, 2, 3, 4]
f = filter(lambda x: x % 2 == 0, numbers)
print(f)   # <filter object>
print(list(f))   # [2, 4]
```

### Debugging 2: Convert to loop
```python
numbers = [1, 2, 3, 4]
for n in numbers:
    if n % 2 == 0:
        print(n)   # Debug
```

### Debugging 3: Named function
```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4]
print(list(filter(is_even, numbers)))
```

---

## 10. Backend Mein Iska Use

| Area | Use |
|------|-----|
| Order filter | Status, amount |
| User filter | Active, role |
| Product filter | Category, price |
| Email filter | Valid, domain |
| Log filter | Error, warning |

---

## 11. Real Backend Example

```python
def is_high_value_paid(order):
    return order["amount"] >= 1000 and order["status"] == "paid"

orders = [
    {"id": 1, "amount": 500, "status": "paid"},
    {"id": 2, "amount": 1500, "status": "pending"},
    {"id": 3, "amount": 2500, "status": "paid"},
    {"id": 4, "amount": 800, "status": "cancelled"},
    {"id": 5, "amount": 3000, "status": "paid"}
]

high_value_paid = list(filter(is_high_value_paid, orders))

for o in high_value_paid:
    print(f"ID: {o['id']}, Amount: ₹{o['amount']}")
```

**Output:**
```
ID: 3, Amount: ₹2500
ID: 5, Amount: ₹3000
```

---

## 12. Interview Questions

**Q1: Filter kya hai?**
> Condition pass karne wale elements rakhta hai.

**Q2: Filter ka return type?**
> Filter object. `list()` se list.

**Q3: Filter vs list comprehension?**
> Filter functional, list comp Pythonic. List comp faster.

**Q4: Filter mein `None`?**
> Falsy values hata deta hai.

**Q5: Filter kab use karte hain?**
> Jab condition ke hisaab se elements nikalne ho.

**Q6: Map aur filter mein difference?**
> Map transform, filter condition.

---

## 13. Student Questions / Doubts

**Doubt 1: Filter aur loop mein difference?**
> Filter clean, functional. Loop traditional.

**Doubt 2: Filter lazy hai?**
> Haan, iterator return karta hai.

**Doubt 3: Filter ke saath lambda zaroori?**
> Nahi. Named function bhi.

**Doubt 4: Filter se index milta?**
> Nahi. `enumerate` use karo.

**Doubt 5: Filter exhausted?**
> Haan, ek baar use karne ke baad.

---

## 14. Practice Problems

**Q1:** Filter se positive numbers nikalo.
```python
nums = [-1, 2, -3, 4, -5, 6]
positives = list(filter(lambda x: x > 0, nums))
print(positives)   # [2, 4, 6]
```

**Q2:** Filter se odd numbers nikalo.
```python
nums = [1, 2, 3, 4, 5, 6]
odds = list(filter(lambda x: x % 2 != 0, nums))
print(odds)   # [1, 3, 5]
```

**Q3:** Filter se long words nikalo.
```python
words = ["hi", "hello", "hey", "wonderful"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)   # ['hello', 'wonderful']
```

**Q4:** Filter se active users nikalo.
```python
users = [
    {"name": "Rohit", "active": True},
    {"name": "Anchal", "active": False},
    {"name": "Shyam", "active": True}
]
active = list(filter(lambda u: u["active"], users))
print(active)
```

# **Q5:** Filter se prime numbers nikalo.

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = list(filter(is_prime, nums))
print(primes)   # [2, 3, 5, 7]


## 15. Mini Task/Project

### Task: Order Filter System

# **Requirements:**
# - `filter_orders(orders, **criteria)` — flexible filtering
# - Criteria: status, min_amount, max_amount
# - Return filtered list

# **Solution:**

def filter_orders(orders, **criteria):
    """
    Filter orders by multiple criteria.
    """
    result = orders
    
    if "status" in criteria:
        result = list(filter(lambda o: o["status"] == criteria["status"], result))
    
    if "min_amount" in criteria:
        result = list(filter(lambda o: o["amount"] >= criteria["min_amount"], result))
    
    if "max_amount" in criteria:
        result = list(filter(lambda o: o["amount"] <= criteria["max_amount"], result))
    
    return result

# Test
orders = [
    {"id": 1, "amount": 500, "status": "paid"},
    {"id": 2, "amount": 1500, "status": "pending"},
    {"id": 3, "amount": 2500, "status": "paid"},
    {"id": 4, "amount": 800, "status": "paid"}
]

print(filter_orders(orders, status="paid", min_amount=1000))


## 16. Teaching Points — Class Mein Kya Explain Karna Hai

# ### Point 1: Channi Analogy
# > "Filter channi hai. Jo chahiye wo rakho, baaki hatao."

# ### Point 2: Lazy
# > "Filter lazy hai. `list()` se convert."

# ### Point 3: `None` Special
# > "`filter(None, iterable)` — falsy values hatao."

# ### Point 4: Lambda ke Saath
# > "Common combo."

# ### Point 5: Real Use
# > "Order filter, user filter."

### Blackboard Pe Kya Likhun

# filter(func, [1, 2, 3, 4])
#        ↓
#   [x for x in list if func(x)]


### Class Activity
# 1. Students se `filter(lambda x: x > 2, [1,2,3,4])` likhwao
# 2. `list()` se convert karwao
# 3. Named function se bhi karwao
# 4. Homework: 5 filter examples



#  TOPIC 7: REDUCE

## 1. Concept Kya Hai?

# `reduce()` ek function hai jo **iterable ke saare elements ko ek single value mein combine** karta hai.

# **Technical:** `reduce(function, iterable)` applies a function of two arguments cumulatively to the items of an iterable, from left to right, reducing the iterable to a single value.



## 2. Why Do We Need It?

### Problem: Manual Accumulation

numbers = [1, 2, 3, 4, 5]
total = 0
for n in numbers:
    total += n
print(total)   # 15


### Solution: Reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numbers)
print(total)   # 15


# **Clean, functional.**


## 3. Real-Life Analogy

Socho aap ek **dher ko ek-ek karke jodte** ho. Pehle 2, phir 3, phir 4... aakhir mein ek number. `reduce` wahi karta hai.



## 4. Syntax


from functools import reduce
reduce(function, iterable)


## 5. Basic Examples

### Example 1: Sum

from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numbers)
print(total)   # 15


### Example 2: Product

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda a, b: a * b, numbers)
print(product)   # 120


### Example 3: Maximum

from functools import reduce

numbers = [5, 2, 8, 1, 9, 3]
max_val = reduce(lambda a, b: a if a > b else b, numbers)
print(max_val)   # 9


### Example 4: Total Cart Value

from functools import reduce

cart = [
    {"name": "Pizza", "price": 250, "qty": 2},
    {"name": "Coke", "price": 60, "qty": 3},
    {"name": "Brownie", "price": 120, "qty": 1}
]

def add_item_total(acc, item):
    return acc + (item["price"] * item["qty"])

total = reduce(add_item_total, cart, 0)
print(f"Cart Total: ₹{total}")   # ₹800


## 6. Step-by-Step Execution


from functools import reduce

numbers = [1, 2, 3, 4, 5]
total = reduce(lambda acc, x: acc + x, numbers)


# **Step-by-step:**

# Step 1: acc = 1 (pehla element)
# Step 2: acc = acc + 2 = 3
# Step 3: acc = acc + 3 = 6
# Step 4: acc = acc + 4 = 10
# Step 5: acc = acc + 5 = 15
# Step 6: return 15


# **Visualization:**
# ```
# reduce(func, [1, 2, 3, 4])
#        ↓
# func(func(func(1, 2), 3), 4)
#        ↓
# func(func(3, 3), 4)
#        ↓
# func(6, 4)
#        ↓
# 10


## 7. Internal Working


from functools import reduce

numbers = [1, 2, 3]
total = reduce(lambda a, b: a + b, numbers)


# **Internally:**
# - `reduce` pehle 2 elements leta hai
# - Function apply karta hai
# - Result ko agle element ke saath combine karta hai
# - Aakhir mein single value return



## 8. Common Mistakes

### Mistake 1: Import bhool jana

# ❌
reduce(lambda a, b: a + b, [1, 2, 3])   # NameError

# ✅
from functools import reduce
reduce(lambda a, b: a + b, [1, 2, 3])


### Mistake 2: Empty iterable without initial

# ❌
reduce(lambda a, b: a + b, [])   # TypeError

# ✅
reduce(lambda a, b: a + b, [], 0)   # 0


### Mistake 3: Single element without initial

# Single element — no function call, element return
reduce(lambda a, b: a + b, [5])   # 5


## 9. Debugging

### Debugging 1: Print steps

from functools import reduce

def add(acc, x):
    print(f"acc={acc}, x={x}")
    return acc + x

reduce(add, [1, 2, 3, 4])


**Output:**

acc=1, x=2
acc=3, x=3
acc=6, x=4


### Debugging 2: Initial value

from functools import reduce
reduce(lambda a, b: a + b, [1, 2, 3], 100)


### Debugging 3: Named function

from functools import reduce

def add(a, b):
    return a + b

print(reduce(add, [1, 2, 3, 4]))


## 10. Backend Mein Iska Use

# | Area | Use |
# |------|-----|
# | Cart total | Sum of items |
# | Product total | Multiply values |
# | Max/min | Find extreme |
# | String concat | Join strings |
# | Data aggregation | Reports |



## 11. Real Backend Example


from functools import reduce

cart = [
    {"name": "Pizza", "price": 250, "qty": 2},
    {"name": "Coke", "price": 60, "qty": 3},
    {"name": "Brownie", "price": 120, "qty": 1}
]

def add_item_total(acc, item):
    """Add item total to accumulator."""
    item_total = item["price"] * item["qty"]
    print(f"Adding {item['name']}: {item_total}")
    return acc + item_total

total = reduce(add_item_total, cart, 0)
print(f"\nCart Total: ₹{total}")


# **Output:**

# Adding Pizza: 500
# Adding Coke: 180
# Adding Brownie: 120

# Cart Total: ₹800


## 12. Interview Questions

# **Q1: Reduce kya hai?**
# > Iterable ko single value mein combine karta hai.

# **Q2: Reduce kahan se aata hai?**
# > `functools` module se.

# **Q3: Reduce vs sum?**
# > `sum` built-in, `reduce` custom function.

# **Q4: Reduce ka initial value?**
# > `reduce(func, iterable, initial)` — optional.

# **Q5: Reduce kab use karte hain?**
# > Jab iterable ko single value mein combine karna ho.

# **Q6: Reduce empty iterable pe?**
# > Initial value ke bina error. Initial ke saath initial return.



## 13. Student Questions / Doubts

# **Doubt 1: Reduce aur loop mein difference?**
# > Reduce functional, loop traditional.

# **Doubt 2: Reduce deprecated?**
# > Python 3 mein `functools` mein move hua. Deprecated nahi.

# **Doubt 3: Reduce ke saath lambda zaroori?**
# > Nahi. Named function bhi.

# **Doubt 4: Reduce se string concat?**
# > Haan, `reduce(lambda a, b: a + b, ["a", "b", "c"])` → "abc".

# **Doubt 5: Reduce aur sum mein speed?**
# > `sum` faster (built-in). `reduce` flexible.


## 14. Practice Problems

# **Q1:** Reduce se sum nikalo.

# from functools import reduce
nums = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, nums))   # 15


# **Q2:** Reduce se product nikalo.

# from functools import reduce
nums = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a * b, nums))   # 120


# **Q3:** Reduce se max nikalo.

# from functools import reduce
nums = [5, 2, 8, 1, 9, 3]
print(reduce(lambda a, b: a if a > b else b, nums))   # 9


# **Q4:** Reduce se string concat karo.

# from functools import reduce
words = ["Hello", "World", "Python"]
print(reduce(lambda a, b: a + " " + b, words))
# Hello World Python


# **Q5:** Reduce se dict merge karo.

# from functools import reduce

dicts = [{"a": 1}, {"b": 2}, {"c": 3}]
merged = reduce(lambda a, b: {**a, **b}, dicts)
print(merged)   # {'a': 1, 'b': 2, 'c': 3}


## 15. Mini Task/Project

### Task: Cart Total Calculator

# **Requirements:**
# - `calculate_cart(cart)` — total, item count, average
# - Use `reduce`

# **Solution:**

from functools import reduce

def calculate_cart(cart):
    if not cart:
        return {"total": 0, "count": 0, "average": 0}
    
    def add_item(acc, item):
        return acc + (item["price"] * item["qty"])
    
    total = reduce(add_item, cart, 0)
    count = reduce(lambda acc, item: acc + item["qty"], cart, 0)
    
    return {
        "total": total,
        "count": count,
        "average": round(total / count, 2) if count else 0
    }

# Test
cart = [
    {"name": "Pizza", "price": 250, "qty": 2},
    {"name": "Coke", "price": 60, "qty": 3},
    {"name": "Brownie", "price": 120, "qty": 1}
]

print(calculate_cart(cart))
# {'total': 800, 'count': 6, 'average': 133.33}


## 16. Teaching Points — Class Mein Kya Explain Karna Hai

### Point 1: Dher Analogy
# > "Reduce ek dher ko jodta hai. Ek-ek karke."

### Point 2: `functools` Import
# > "`from functools import reduce` zaroori."

### Point 3: Two Arguments
# > "Reduce ka function 2 arguments leta hai — accumulator aur current."

### Point 4: Initial Value
# > "Optional. Bina initial ke empty pe error."

### Point 5: Real Use
# > "Cart total, sum, product."

### Blackboard Pe Kya Likhun

# reduce(func, [1, 2, 3, 4])
#        ↓
# func(func(func(1, 2), 3), 4)
#        ↓
# 10


### Class Activity
# 1. Students se `reduce(lambda a, b: a + b, [1,2,3])` likhwao
# 2. Print steps karwao
# 3. Initial value ke saath karwao
# 4. Homework: 5 reduce examples



# # 📌 FINAL SUMMARY

# | Topic | Kya Hai | Kab Use | Return Type |
# |-------|---------|---------|-------------|
# | Function | Named reusable block | Har jagah | Kuch bhi |
# | `*args` | Variable positional | Bulk ops | Tuple |
# | `**kwargs` | Variable keyword | Flexible config | Dict |
# | Lambda | Anonymous single-line | Short ops | Expression |
# | Map | Transform each | Har element pe | Iterator |
# | Filter | Condition pass | Elements filter | Iterator |
# | Reduce | Combine to single | Sum, product | Single value |





