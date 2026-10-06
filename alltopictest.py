Haan bhai 😄 **ab exact samajh gaya**. Tumhe sirf questions ki list nahi chahiye. Tumhe **minimum 20 proper industry-level Python interview questions + har question ka complete solution + code + output/logic + deep explanation + interview trap** chahiye.

Aur questions **mixed hone chahiye**, matlab ek question mein `list + dict + loop + if/else + function + set` naturally use ho, taaki **poora Python practically revise ho jaye**.

Neeche 20 master questions de raha hoon.

---

# 🔥 Python — 20 Industry-Level Master Interview Questions with Solutions

## Q1. Employee Salary Analysis

### Problem

```python
employees = [
    {"name": "Rohit", "dept": "Backend", "salary": 45000},
    {"name": "Aman", "dept": "Frontend", "salary": 38000},
    {"name": "Neha", "dept": "Backend", "salary": 60000},
    {"name": "Priya", "dept": "HR", "salary": 35000},
    {"name": "Raj", "dept": "Backend", "salary": 70000}
]
```

Program banao jo:

1. Backend employees find kare
2. Average salary calculate kare
3. Highest salary employee find kare
4. Salary ke basis par Junior/Mid/Senior classify kare
5. Unique departments nikale

### Solution

```python
def analyze_employees(employees):

    backend_employees = []
    departments = set()

    total_salary = 0
    highest_employee = employees[0]

    for employee in employees:

        departments.add(employee["dept"])
        total_salary += employee["salary"]

        if employee["dept"] == "Backend":
            backend_employees.append(employee)

        if employee["salary"] > highest_employee["salary"]:
            highest_employee = employee

    average_salary = total_salary / len(employees)

    print("Backend Employees:")
    for employee in backend_employees:
        print(employee["name"])

    print("\nAverage Salary:", average_salary)

    print(
        "Highest Salary:",
        highest_employee["name"],
        highest_employee["salary"]
    )

    print("\nDepartments:", departments)


analyze_employees(employees)
```

### Important concepts

Yahan:

* `list` → employees
* `dictionary` → individual employee
* `set` → unique departments
* `for` → iteration
* `if` → filtering
* `function` → reusable logic
* `sum` logic → salary calculation

### Interview trap

**Question:** Department ke liye list ki jagah set kyun?

Because duplicate department automatically remove ho jayenge.

---

# Q2. Student Result System

### Problem

```python
students = {
    "Rohit": [85, 90, 78],
    "Aman": [45, 50, 39],
    "Neha": [95, 92, 98]
}
```

Har student ka:

* Total
* Average
* Grade
* Pass/Fail

nikalo.

### Solution

```python
def calculate_grade(average):

    if average >= 90:
        return "A"

    elif average >= 75:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 40:
        return "D"

    else:
        return "F"


def student_result(students):

    for name, marks in students.items():

        total = sum(marks)
        average = total / len(marks)

        grade = calculate_grade(average)

        status = "Pass" if average >= 40 else "Fail"

        print(
            name,
            "Total:", total,
            "Average:", average,
            "Grade:", grade,
            "Status:", status
        )


student_result(students)
```

### Concepts

* Dictionary
* List
* Function
* `for`
* `if/elif/else`
* `sum()`
* `len()`
* conditional expression

---

# Q3. Duplicate Data Cleaning

### Problem

```python
users = [
    "Rohit",
    "rohit",
    " Aman ",
    "NEHA",
    "neha",
    "",
    None,
    "Aman"
]
```

Clean data:

```text
["rohit", "aman", "neha"]
```

### Solution

```python
def clean_users(users):

    result = []
    seen = set()

    for user in users:

        if user is None:
            continue

        user = user.strip().lower()

        if user == "":
            continue

        if user not in seen:
            result.append(user)
            seen.add(user)

    return result


users = [
    "Rohit",
    "rohit",
    " Aman ",
    "NEHA",
    "neha",
    "",
    None,
    "Aman"
]

print(clean_users(users))
```

### Output

```text
['rohit', 'aman', 'neha']
```

### Why not simply?

```python
list(set(users))
```

Because:

1. `None` problem ho sakta hai depending on processing
2. cleaning nahi hogi
3. order preservation ka reliable logic nahi rahega

Yahan `set` **duplicate checking** ke liye use hua hai.

---

# Q4. E-Commerce Cart

### Problem

```python
cart = [
    {"name": "Laptop", "price": 70000, "qty": 1},
    {"name": "Mouse", "price": 800, "qty": 2},
    {"name": "Keyboard", "price": 1500, "qty": 1}
]
```

Calculate:

```text
Subtotal
Discount
Tax
Final Amount
```

### Solution

```python
def calculate_bill(cart):

    subtotal = 0

    for item in cart:
        subtotal += item["price"] * item["qty"]

    if subtotal >= 50000:
        discount = subtotal * 0.15

    elif subtotal >= 20000:
        discount = subtotal * 0.10

    else:
        discount = subtotal * 0.05

    amount_after_discount = subtotal - discount

    tax = amount_after_discount * 0.18

    final_amount = amount_after_discount + tax

    return subtotal, discount, tax, final_amount


result = calculate_bill(cart)

print("Subtotal:", result[0])
print("Discount:", result[1])
print("Tax:", result[2])
print("Final:", result[3])
```

### Concepts

`list → dictionary → loop → arithmetic → if/elif → function → return → tuple`

Notice function multiple values return kar raha hai:

```python
return subtotal, discount, tax, final_amount
```

Python internally ise tuple ke form mein return karta hai.

---

# Q5. Login Authentication

### Problem

```python
users = {
    "rohit": {"password": "1234", "role": "admin"},
    "aman": {"password": "5678", "role": "user"},
    "neha": {"password": "9999", "role": "manager"}
}
```

Login system banao.

### Solution

```python
def login(username, password):

    if username not in users:
        return "User not found"

    user = users[username]

    if user["password"] != password:
        return "Invalid password"

    role = user["role"]

    match role:

        case "admin":
            return "Admin Dashboard"

        case "manager":
            return "Manager Dashboard"

        case "user":
            return "User Dashboard"

        case _:
            return "Unknown Role"


print(login("rohit", "1234"))
print(login("aman", "5678"))
print(login("aman", "1111"))
```

### Concepts

* Dictionary
* Nested dictionary
* Function
* Membership operator
* `if`
* `match-case`

---

# Q6. Inventory Management

### Problem

```python
products = [
    {"name": "Laptop", "price": 70000, "stock": 3},
    {"name": "Mouse", "price": 800, "stock": 0},
    {"name": "Keyboard", "price": 1500, "stock": 15}
]
```

Find:

* Out of stock
* Low stock
* Inventory value
* Most expensive product

### Solution

```python
def inventory_report(products):

    total_value = 0
    expensive_product = products[0]

    for product in products:

        total_value += product["price"] * product["stock"]

        if product["stock"] == 0:
            print("Out of stock:", product["name"])

        elif product["stock"] < 5:
            print("Low stock:", product["name"])

        if product["price"] > expensive_product["price"]:
            expensive_product = product

    print("Inventory Value:", total_value)
    print("Most Expensive:", expensive_product["name"])


inventory_report(products)
```

---

# Q7. Transaction Validation

### Problem

```python
transactions = [
    {"user": "Rohit", "amount": 5000},
    {"user": "Aman", "amount": -200},
    {"user": "Neha", "amount": "3000"},
    {"user": "Raj", "amount": 4500}
]
```

Invalid transactions ko reject karo.

### Solution

```python
def process_transactions(transactions):

    valid = []
    invalid = []

    for transaction in transactions:

        try:

            amount = float(transaction["amount"])

            if amount <= 0:
                raise ValueError("Amount must be positive")

            valid.append({
                "user": transaction["user"],
                "amount": amount
            })

        except (ValueError, TypeError) as error:

            invalid.append({
                "transaction": transaction,
                "error": str(error)
            })

    return valid, invalid


valid, invalid = process_transactions(transactions)

print("Valid:", valid)
print("Invalid:", invalid)
```

### Important

Yahan `"3000"` string ko:

```python
float("3000")
```

se number mein convert kar diya.

---

# Q8. Word Frequency Analyzer

### Problem

```python
text = "python is easy python is powerful python"
```

Expected:

```python
{
    "python": 3,
    "is": 2,
    "easy": 1,
    "powerful": 1
}
```

### Solution

```python
def word_frequency(text):

    words = text.lower().split()

    frequency = {}

    for word in words:

        frequency[word] = frequency.get(word, 0) + 1

    return frequency


print(word_frequency(text))
```

### Important interview concept

```python
frequency.get(word, 0)
```

Agar key exist nahi karti:

```text
0
```

return karega.

Phir:

```python
+ 1
```

kar diya.

---

# Q9. Department-wise Employee Count

```python
employees = [
    ("Rohit", "Backend"),
    ("Aman", "Frontend"),
    ("Neha", "Backend"),
    ("Raj", "Backend"),
    ("Priya", "HR")
]
```

### Solution

```python
def department_count(employees):

    result = {}

    for name, department in employees:

        result[department] = result.get(department, 0) + 1

    return result


print(department_count(employees))
```

Output:

```python
{
    "Backend": 3,
    "Frontend": 1,
    "HR": 1
}
```

### Concepts

Yahan tuple unpacking ho raha hai:

```python
for name, department in employees:
```

---

# Q10. Find Second Highest Number

### Problem

```python
numbers = [10, 50, 20, 80, 80, 40]
```

Second highest **unique** number find karo.

### Solution

```python
def second_highest(numbers):

    unique_numbers = set(numbers)

    if len(unique_numbers) < 2:
        return None

    sorted_numbers = sorted(unique_numbers, reverse=True)

    return sorted_numbers[1]


print(second_highest(numbers))
```

Output:

```text
50
```

### Concepts

* List
* Set
* `len`
* `sorted`
* `reverse`
* Function

---

# Q11. List Comprehension Based Filtering

Numbers:

```python
numbers = range(1, 21)
```

Find:

* even numbers
* squares of even numbers
* numbers > 10

### Solution

```python
numbers = range(1, 21)

even_numbers = [
    number for number in numbers
    if number % 2 == 0
]

even_squares = [
    number ** 2
    for number in numbers
    if number % 2 == 0
]

greater_than_10 = [
    number
    for number in numbers
    if number > 10
]

print(even_numbers)
print(even_squares)
print(greater_than_10)
```

### Interview question

Normal loop aur comprehension mein difference?

Comprehension mainly **concise collection creation** ke liye useful hai.

---

# Q12. `*args` and `**kwargs`

### Problem

Ek billing function banao jo unlimited prices aur optional configuration accept kare.

```python
calculate_bill(
    1000,
    500,
    200,
    discount=10,
    tax=18
)
```

### Solution

```python
def calculate_bill(*prices, **options):

    subtotal = sum(prices)

    discount = options.get("discount", 0)
    tax = options.get("tax", 0)

    discount_amount = subtotal * discount / 100

    after_discount = subtotal - discount_amount

    tax_amount = after_discount * tax / 100

    final_amount = after_discount + tax_amount

    return final_amount


result = calculate_bill(
    1000,
    500,
    200,
    discount=10,
    tax=18
)

print(result)
```

### Core concept

```python
*prices
```

→ tuple

```python
**options
```

→ dictionary

---

# Q13. Lambda + Sorting

### Problem

```python
employees = [
    {"name": "Rohit", "salary": 45000},
    {"name": "Aman", "salary": 70000},
    {"name": "Neha", "salary": 55000}
]
```

Salary descending order mein sort karo.

### Solution

```python
employees_sorted = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)

for employee in employees_sorted:
    print(employee)
```

### Output

```text
{'name': 'Aman', 'salary': 70000}
{'name': 'Neha', 'salary': 55000}
{'name': 'Rohit', 'salary': 45000}
```

### Interview understanding

```python
lambda employee: employee["salary"]
```

ka matlab:

> Har employee dictionary se salary lekar sorting ke liye use karo.

---

# Q14. `map`, `filter`, `reduce`

### Problem

```python
numbers = [10, 15, 20, 25, 30]
```

1. Sabko double karo
2. Sirf even numbers rakho
3. Sabka total nikalo

### Solution

```python
from functools import reduce

numbers = [10, 15, 20, 25, 30]

doubled = list(
    map(lambda x: x * 2, numbers)
)

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

total = reduce(
    lambda x, y: x + y,
    numbers
)

print(doubled)
print(even_numbers)
print(total)
```

### Difference

```text
map    → transform
filter → select
reduce → combine
```

---

# Q15. `match-case` Order Status System

### Problem

Order status ke basis par message return karo.

```python
status = "shipped"
```

### Solution

```python
def order_message(status):

    match status:

        case "pending":
            return "Order is waiting"

        case "paid":
            return "Payment successful"

        case "shipped":
            return "Order shipped"

        case "delivered":
            return "Order delivered"

        case "cancelled":
            return "Order cancelled"

        case _:
            return "Invalid status"


print(order_message("shipped"))
```

### Important

Last:

```python
case _:
```

default case hai.

Ye roughly traditional:

```python
else
```

jaisa fallback provide karta hai.

---

# Q16. File Handling + Error Handling

### Problem

`users.txt` read karo aur valid users count karo.

### Solution

```python
def read_users(filename):

    users = []

    try:

        with open(filename, "r") as file:

            for line in file:

                username = line.strip()

                if username:
                    users.append(username)

    except FileNotFoundError:

        print("File does not exist")

    return users
```

### `with open()` kyun?

File automatically close ho jaati hai.

Manual:

```python
file.close()
```

karne ki zarurat nahi.

---

# Q17. Mutable vs Immutable

### Problem

Explain output:

```python
a = [10, 20]
b = a

b.append(30)

print(a)
print(b)
```

### Solution

Output:

```text
[10, 20, 30]
[10, 20, 30]
```

Because:

```python
b = a
```

copy nahi banata.

Dono same list object ko reference karte hain.

### Correct independent copy

```python
a = [10, 20]

b = a.copy()

b.append(30)

print(a)
print(b)
```

Output:

```text
[10, 20]
[10, 20, 30]
```

### Interview concept

Yahan test ho raha hai:

* mutable object
* reference
* shallow copy
* `.copy()`

---

# Q18. OOP — Employee System

### Problem

Employee class banao.

Developer aur Manager inherit karein.

### Solution

```python
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return self.salary * 0.05


class Developer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.10


class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.20


employees = [
    Developer("Rohit", 50000),
    Manager("Neha", 80000)
]

for employee in employees:

    print(
        employee.name,
        employee.calculate_bonus()
    )
```

### Yahan kya hua?

`Employee` → parent class

`Developer`, `Manager` → child classes

Same method:

```python
calculate_bonus()
```

different behavior de raha hai.

Ye **polymorphism** ka example hai.

---

# Q19. Banking System — Multiple Concepts Together

### Problem

Bank account:

```python
account = {
    "name": "Rohit",
    "balance": 50000,
    "transactions": []
}
```

Deposit aur withdraw functions banao.

### Solution

```python
def deposit(account, amount):

    if amount <= 0:
        raise ValueError("Amount must be positive")

    account["balance"] += amount

    account["transactions"].append({
        "type": "deposit",
        "amount": amount
    })


def withdraw(account, amount):

    if amount <= 0:
        raise ValueError("Amount must be positive")

    if amount > account["balance"]:
        raise ValueError("Insufficient balance")

    account["balance"] -= amount

    account["transactions"].append({
        "type": "withdraw",
        "amount": amount
    })


account = {
    "name": "Rohit",
    "balance": 50000,
    "transactions": []
}

try:

    deposit(account, 5000)
    withdraw(account, 2000)

except ValueError as error:

    print("Error:", error)


print(account)
```

### Concepts

Ek hi problem mein:

* dictionary
* list
* function
* condition
* exception
* mutation
* nested data

sab aa gaye.

---

# Q20. 🔥 FINAL MASTER — Mini Banking Application

Ab ye **proper interview-level question** hai.

### Requirement

Banking system banao:

```text
1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. Check Balance
6. Transaction History
7. Exit
```

### Solution

```python
accounts = {}


def create_account(account_id, name, balance=0):

    if account_id in accounts:
        print("Account already exists")
        return

    if balance < 0:
        print("Invalid balance")
        return

    accounts[account_id] = {
        "name": name,
        "balance": balance,
        "transactions": []
    }

    print("Account created successfully")


def deposit(account_id, amount):

    if account_id not in accounts:
        print("Account not found")
        return

    if amount <= 0:
        print("Invalid amount")
        return

    account = accounts[account_id]

    account["balance"] += amount

    account["transactions"].append({
        "type": "deposit",
        "amount": amount,
        "balance_after": account["balance"]
    })

    print("Deposit successful")


def withdraw(account_id, amount):

    if account_id not in accounts:
        print("Account not found")
        return

    if amount <= 0:
        print("Invalid amount")
        return

    account = accounts[account_id]

    if amount > account["balance"]:
        print("Insufficient balance")
        return

    account["balance"] -= amount

    account["transactions"].append({
        "type": "withdraw",
        "amount": amount,
        "balance_after": account["balance"]
    })

    print("Withdrawal successful")


def transfer(sender_id, receiver_id, amount):

    if sender_id not in accounts:
        print("Sender account not found")
        return

    if receiver_id not in accounts:
        print("Receiver account not found")
        return

    if amount <= 0:
        print("Invalid amount")
        return

    sender = accounts[sender_id]
    receiver = accounts[receiver_id]

    if amount > sender["balance"]:
        print("Insufficient balance")
        return

    sender["balance"] -= amount
    receiver["balance"] += amount

    sender["transactions"].append({
        "type": "transfer_sent",
        "amount": amount,
        "to": receiver_id,
        "balance_after": sender["balance"]
    })

    receiver["transactions"].append({
        "type": "transfer_received",
        "amount": amount,
        "from": sender_id,
        "balance_after": receiver["balance"]
    })

    print("Transfer successful")


def check_balance(account_id):

    if account_id not in accounts:
        print("Account not found")
        return

    print(
        "Balance:",
        accounts[account_id]["balance"]
    )


def transaction_history(account_id):

    if account_id not in accounts:
        print("Account not found")
        return

    transactions = accounts[account_id]["transactions"]

    if not transactions:
        print("No transactions")
        return

    for transaction in transactions:
        print(transaction)
```

### Example

```python
create_account(101, "Rohit", 50000)

create_account(102, "Aman", 25000)

deposit(101, 5000)

withdraw(102, 2000)

transfer(101, 102, 10000)

check_balance(101)

transaction_history(101)
```

---

# 🔥 Ab Interviewer Tumse Ye Follow-up Pooch Sakta Hai

### 1. Accounts ke liye dictionary kyun?

```python
accounts[101]
```

se account direct access ho sakta hai.

### 2. Transactions ke liye list kyun?

Because transaction history ordered collection hai aur multiple transactions store karne hain.

### 3. Account ID unique kaise rakhi?

```python
if account_id in accounts:
```

### 4. Set kahan use kar sakte ho?

For example unique transaction types:

```python
types = {
    transaction["type"]
    for transaction in transactions
}
```

### 5. Tuple kahan useful ho sakta hai?

Immutable data ke liye, for example:

```python
coordinates = (23.25, 77.41)
```

### 6. `match-case` kahan laga sakte ho?

Menu handling:

```python
match choice:

    case 1:
        create_account()

    case 2:
        deposit()

    case 3:
        withdraw()

    case _:
        print("Invalid option")
```

### 7. 10 lakh accounts ho jaayein to?

Tab in-memory dictionary ko permanent database se replace karna hoga.

Example architecture:

```text
Python Application
       ↓
Service Layer
       ↓
Repository
       ↓
Database
```

---
