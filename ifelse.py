# Comaprsion Operators
a = 10
b = 10
print(a ==b)
# List 
list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1
print(list1 == list2)
print(list1 is list2) # False because they are different objects in memory
print(list1 is list3) # True because they are the same object in memory


# Dev Code 
user_seesion  = None
if user_seesion is None:
    print("User is not logged in")

# Comprasion Table
# == Value comparison if user == 18
# != Value comparison if user != 18
# > Value comparison if user > 18
# < Value comparison if user < 18
# >= Value comparison if user >= 18
# <= Value comparison if user <= 18
# is identiy check if error is none
# in membership check if user in list

# Logic Operators
# and both conditions must be true
# or either condition can be true
# not negates the condition

# age = int(input("Enter your age: "))
age = 34
if age >= 18 and age <= 65:
    print("You are eligible to work")
else:
    print("You are not eligible to work")

# Industry Level 

is_in_stock = True
payment_successful = True
shipping_address = "123 Main St New Jersey"
pincode = 12344

if is_in_stock and payment_successful and shipping_address and pincode:
    print("Order Confirmed")
else:
    print("Order Failed check")
    if not is_in_stock:
        print("Out of stock")
    if not payment_successful:
        print("Payment Failed")
    if not shipping_address:
        print("No Shipping Address")


# OR Operator

day = "Sunday"
if day == "Staurday" or day == "Sunday":
    print("Holiday hai")

# Koi bi login system 
user_email = "rohit575@gmail.com"
user_phone = 123456789
username = None
if user_email or user_phone  or username:
    print("User Identity exists")
    identity =   user_phone  or username or user_email
    print(f"login with :{identity}")


# ==
# 1.1 == (Equality Operator)
# Kya hai: Do values ko compare karta hai ki equal hain ya nahi.

# Kab use karein:

# User input check karna

# Database se aayi value compare karna

# Status codes check karna

# Configuration values verify karna
# when use 

# 1. User Authentication
entered_password = "admin123"
stored_password = "admin123"
if entered_password == stored_password:
    print("Login successful")

# 2. Status Checking
order_status = "delivered"
if order_status == "delivered":
    print("Order completed")

# 3. Configuration Check
environment = "production"
if environment == "production":
    print("Using production database")
else:
    print("Using development database")

# 4. Form Validation
user_role = input("Enter role: ")
if user_role == "admin":
    print("Full access granted")
elif user_role == "editor":
    print("Edit access granted")
elif user_role == "viewer":
    print("Read-only access")
else:
    print("Invalid role")

# Kyu karein:
# Exact match check karne ke liye
# Data integrity verify karne ke liye
# Business rules enforce karne ke liye
# Agar use nahi karenge toh:


#  WRONG - Assignment operator use kiya
# if user_role = "admin":  # Syntax Error! Ye assignment hai, comparison nahi
    # print("Admin access")

#  WRONG - Wrong comparison
user_status = "active"
if user_status is "active":  # is works but should use == for values
    print("User active")

# Proper Example:
# E-commerce Product Validation
product_code = "PRD-001"
expected_code = "PRD-001"

if product_code == expected_code:
    print(" Product matched")
    # Proceed with product details
else:
    print(" Product not found")
    # Show error message

# 1.2 != (Not Equal Operator)

# Kya hai: Do values equal nahi hain toh True return karega.
# Kab use karein:
# Exception handling
# Block listing
# Invalid inputs reject karna
# Negative conditions check karna
# Kahan use karein:

# 1. Block List Check
blocked_ips = ["192.168.1.1", "10.0.0.1"]
user_ip = "192.168.1.2"
if user_ip != blocked_ips[0]:  # Not the first blocked IP
    print("IP not in block list")

# 2. Payment Processing
payment_status = "pending"
if payment_status != "completed":
    print("Payment pending, please wait")
else:
    print("Payment successful")

# 3. Data Validation
user_age = 25
if user_age != 0:  # Age 0 invalid hai
    print(f"Age: {user_age}")
else:
    print("Invalid age")

# 4. File Operations
file_name = "data.txt"
if file_name != "":  # Empty filename check
    print(f"Processing {file_name}")
else:
    print("No filename provided")

# Kyu karein:
# Negative conditions handle karne ke liye
# Specific values exclude karne ke liye
# Edge cases handle karne ke liye
# Agar use nahi karenge toh:

#  WRONG - Not using != leads to wrong logic
user_type = "guest"
if user_type == "admin":  # Guest admin nahi hai, toh yeh condition false hoga
    print("Admin access")
# Agar user_type "guest" hai toh admin check fail hoga, par guest check bhi nahi hai

#  CORRECT - Using !=
if user_type != "admin":
    print("Regular user access")
else:
    print("Admin access")

# Real Industry Example:

# E-commerce - Validate coupon code
def validate_coupon(coupon_code, user_id):
    # Invalid coupon codes
    invalid_codes = ["EXPIRED", "USED", "INVALID"]
    
    if coupon_code in invalid_codes:
        return {"valid": False, "message": "Invalid coupon code"}
    
    # Check if user already used this coupon
    if user_id != "" and coupon_code not in used_coupons_by_user(user_id):
        return {"valid": True, "discount": 10}
    else:
        return {"valid": False, "message": "Coupon already used"}

# 1.3 > (Greater Than) & < (Less Than)
# Kya hai: Numerical values compare karna.
# Kab use karein:
# Threshold checks
# Pricing calculations
# Age verification
# Stock management
# Performance monitoring
# Kahan use karein:

# 1. Stock Management
stock_count = 5
minimum_stock = 10
if stock_count < minimum_stock:
    print(" Low stock! Reorder needed")
    # Trigger automatic reorder
else:
    print(" Stock sufficient")

# 2. Price Calculation
total_amount = 1500
if total_amount > 1000:
    discount = total_amount * 0.1  # 10% discount
    print(f"Discount applied: ₹{discount}")
else:
    print("No discount")

# 3. Age Verification
user_age = 17
if user_age >= 18:
    print("Adult content accessible")
else:
    print("Content blocked for minors")

# 4. Performance Monitoring
response_time = 250  # milliseconds
if response_time > 200:
    print(" Slow response time detected")
    # Send alert to dev team
else:
    print("✓ Performance good")

# 5. Credit Score Check
credit_score = 720
if credit_score > 700:
    print(" Loan approved with low interest")
elif credit_score > 650:
    print(" Loan approved with medium interest")
else:
    print(" Loan rejected")

# Kyu karein:
# Limits enforce karne ke liye
# Thresholds check karne ke liye
# Business rules apply karne ke liye
# Agar use nahi karenge toh:

# WRONG - Hardcoded values se compare nahi kiya
temperature = 38
if temperature == "hot":  # String compare - galat hai
    print("Turn on AC")
# Should be:
if temperature > 30:
    print("Turn on AC")

#  WRONG - Wrong direction
age = 16
if age < 18:  # Correct
    print("Minor")
else:
    print("Adult")
# Agar ulta kiya toh:
if age > 18:  # 16 > 18 False hoga, galat result
    print("Adult")
else:
    print("Minor")  # Minor print hoga, correct par logic galat

# Real Industry Example - Healthcare:
# Patient Health Monitor
def check_vitals(heart_rate, blood_pressure_sys, blood_pressure_dia, temperature):
    alerts = []
    
    # Heart Rate Check
    if heart_rate < 60:
        alerts.append(" Bradycardia: Heart rate too low")
    elif heart_rate > 100:
        alerts.append(" Tachycardia: Heart rate too high")
    else:
        alerts.append(" Heart rate normal")
    
    # Blood Pressure Check
    if blood_pressure_sys > 140 or blood_pressure_dia > 90:
        alerts.append(" High blood pressure detected")
    elif blood_pressure_sys < 90 or blood_pressure_dia < 60:
        alerts.append(" Low blood pressure detected")
    else:
        alerts.append("✓ Blood pressure normal")
    
    # Temperature Check
    if temperature > 100.4:
        alerts.append(" Fever detected")
    elif temperature < 95:
        alerts.append(" Hypothermia risk")
    else:
        alerts.append(" Temperature normal")
    
    return alerts


# 1.4 >= & <= (Greater/Equal & Less/Equal)
# Kya hai: Inclusive comparisons.

# Kab use karein:

# Minimum requirements check

# Maximum limits enforce

# Range validation

# Grade boundaries

# Kahan use karein:



# 1. Minimum Requirements
salary = 50000
if salary >= 40000:
    print(" Eligible for home loan")
else:
    print(" Salary below requirement")

# 2. Age Limits
age = 65
if age <= 60:
    print("Regular insurance rate")
else:
    print("Senior citizen rate")

# 3. Grade System
marks = 75
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

# 4. Battery Management
battery_level = 15
if battery_level <= 20:
    print(" Low battery! Please charge")
elif battery_level >= 80:
    print(" Battery high, good to go")
else:
    print(f"Battery: {battery_level}%")

# 5. Rate Limiting
api_requests = 980
if api_requests >= 1000:
    print(" Rate limit exceeded")
    # Block further requests
else:
    print(f" {1000 - api_requests} requests remaining")

# Kyu karein:
# Boundaries include karne ke liye
# Range checks ke liye
# Exact thresholds with inclusive limits
# Agar use nahi karenge toh:



# Agar use nahi karenge toh:


#  WRONG - Boundary missing
marks = 90
if marks > 90:  # 90 > 90 False hai, par 90 ko A+ milna chahiye
    grade = "A+"
elif marks > 80:
    grade = "A"
# Isme 90 ko "A" milega, galat

#  CORRECT - Using >=
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"

#  WRONG - Upper bound missing
age = 65
if age < 60:  # 65 < 60 False, senior citizen check missing
    print("Regular")
elif age >= 60:  # Yeh correct hai
    print("Senior")


# Real Industry Example - Banking:


# Credit Card Eligibility Checker
def check_credit_card_eligibility(age, annual_income, credit_score, employment_type):
    # Minimum age requirement
    if age < 18:
        return {"eligible": False, "reason": "Minimum age 18 required"}
    
    # Maximum age limit
    if age > 70:
        return {"eligible": False, "reason": "Maximum age 70"}
    
    # Income threshold
    if annual_income < 250000:  # ₹2.5 Lakhs
        return {"eligible": False, "reason": "Minimum annual income ₹2.5L required"}
    
    # Credit score check
    if credit_score < 650:
        return {"eligible": False, "reason": "Minimum credit score 650 required"}
    
    # Employment type
    if employment_type not in ["salaried", "self_employed", "business"]:
        return {"eligible": False, "reason": "Invalid employment type"}
    
    # All checks passed
    credit_limit = 0
    if annual_income >= 1000000:  # ₹10 Lakhs
        credit_limit = 200000
    elif annual_income >= 500000:  # ₹5 Lakhs
        credit_limit = 100000
    else:
        credit_limit = 50000
    
    return {
        "eligible": True,
        "credit_limit": credit_limit,
        "interest_rate": 12.5 if credit_score >= 750 else 15.0
    }



# 2.1 and Operator
# Kya hai: Saari conditions True honi chahiye.

# Kab use karein:

# Multiple requirements check

# Multi-factor authentication

# Complex business rules

# Form validation

# Kahan use karein:



# 1. Multi-Factor Authentication
username = "admin"
password = "admin123"
is_active = True
is_locked = False

if username == "admin" and password == "admin123" and is_active and not is_locked:
    print("✅ Login successful - Full access")
else:
    print("❌ Login failed")

# 2. E-commerce Order Validation
def validate_order(order):
    has_items = len(order['items']) > 0
    has_address = bool(order.get('address'))
    has_payment = bool(order.get('payment_method'))
    is_verified = order.get('verified', False)
    
    if has_items and has_address and has_payment and is_verified:
        return {"valid": True, "message": "Order ready for processing"}
    else:
        missing = []
        if not has_items: missing.append("items")
        if not has_address: missing.append("address")
        if not has_payment: missing.append("payment")
        if not is_verified: missing.append("verification")
        return {"valid": False, "missing": missing}

# 3. User Permissions
def check_permission(user, action, resource):
    is_admin = user.get('role') == 'admin'
    has_permission = action in user.get('permissions', [])
    resource_accessible = resource in user.get('accessible_resources', [])
    
    if is_admin and (has_permission or resource_accessible):
        return True
    return False

# 4. Data Validation
def validate_user_data(user_data):
    name_exists = bool(user_data.get('name'))
    age_valid = 18 <= user_data.get('age', 0) <= 120
    email_valid = '@' in user_data.get('email', '') and '.' in user_data.get('email', '')
    phone_valid = len(str(user_data.get('phone', ''))) == 10
    
    if name_exists and age_valid and email_valid and phone_valid:
        return True, "All data valid"
    else:
        errors = []
        if not name_exists: errors.append("Name required")
        if not age_valid: errors.append("Age must be 18-120")
        if not email_valid: errors.append("Invalid email")
        if not phone_valid: errors.append("Phone must be 10 digits")
        return False, errors

# Kyu karein:

# All conditions must be satisfied

# Complex authorization logic

# Form validation

# Agar use nahi karenge toh:

#  WRONG - Nested ifs (hard to read)
if username == "admin":
    if password == "admin123":
        if is_active:
            if not is_locked:
                print("Login success")
# Nested ifs -> Hard to read, maintain, debug

#  CORRECT - Single condition with and
if username == "admin" and password == "admin123" and is_active and not is_locked:
    print("Login success")

# Real Industry Example - Insurance Claim:


class InsuranceClaim:
    def process_claim(self, claim_id, policy_number, claim_amount, incident_date):
        # Check 1: Valid policy
        policy_valid = self.policy_exists(policy_number) and not self.policy_expired(policy_number)
        
        # Check 2: Claim limits
        claim_valid = claim_amount > 0 and claim_amount <= self.get_policy_limit(policy_number)
        
        # Check 3: Time limit (within 30 days of incident)
        days_elapsed = (datetime.now() - incident_date).days
        time_valid = days_elapsed <= 30
        
        # Check 4: Claim not already filed
        not_duplicate = claim_id not in self.processed_claims
        
        if policy_valid and claim_valid and time_valid and not_duplicate:
            return self.approve_claim(claim_id)
        else:
            errors = []
            if not policy_valid:
                errors.append("Invalid or expired policy")
            if not claim_valid:
                errors.append("Claim amount exceeds policy limit")
            if not time_valid:
                errors.append(f"Claim must be filed within 30 days (current: {days_elapsed} days)")
            if not not_duplicate:
                errors.append("Duplicate claim detected")
            return {"status": "rejected", "errors": errors}

# 2.2 or Operator
# Kya hai: Koi bhi condition True hona chahiye.

# Kab use karein:

# Multiple valid options

# Fallback values

# Quick checks

# Any conditions

# Kahan use karein:


# 1. Multiple Login Methods
user_email = "student@email.com"
user_phone = None
user_username = "student123"

if user_email or user_phone or user_username:
    login_method = user_email or user_phone or user_username  # First truthy value
    print(f"✅ Login with: {login_method}")
else:
    print("❌ No login method provided")

# 2. Discount Eligibility
def calculate_discount(user):
    is_premium = user.get('premium', False)
    is_student = user.get('student', False)
    is_senior = user.get('senior', False)
    is_employee = user.get('employee', False)
    
    if is_premium or is_student or is_senior or is_employee:
        return 15  # 15% discount
    return 0

# 3. Search Query Handling
query = search_input()
if query is None or query == "" or query.isspace():
    query = "default_search"  # Fallback

# 4. Error Handling
def get_user_data(user_id):
    # Try multiple data sources
    data = fetch_from_database(user_id) or fetch_from_cache(user_id) or fetch_from_api(user_id)
    
    if data:
        return data
    else:
        return {"error": "User not found in any source"}

# 5. Feature Flags
feature_new_ui = get_config('new_ui', False)
feature_beta = get_config('beta_features', False)
user_test_group = current_user.groups.contains('beta_tester')

if feature_new_ui or (feature_beta and user_test_group):
    render_new_ui()
else:
    render_old_ui()



# Kyu karein:

# Multiple valid options provide karna

# Fallback values provide karna

# Flexible conditions

# Agar use nahi karenge toh:


#  WRONG - Long if-elif chain
if user_email:
    login_method = user_email
elif user_phone:
    login_method = user_phone
elif user_username:
    login_method = user_username
else:
    login_method = None
# Bahut lengthy

#  CORRECT - Using or
login_method = user_email or user_phone or user_username

#  WRONG - Complex nested conditions
if not user_email:
    if not user_phone:
        if not user_username:
            print("No login method")
# Hard to read

#  CORRECT - Using or
if not (user_email or user_phone or user_username):
    print("No login method")

# Real Industry Example - Payment Processing:

class PaymentProcessor:
    def process_payment(self, amount, payment_methods):
        """
        Try multiple payment methods until one works
        """
        processed = False
        error_messages = []
        
        # Check if any payment method is available
        if not payment_methods:
            return {"status": "failed", "error": "No payment methods available"}
        
        # Try each method (OR logic)
        for method in payment_methods:
            try:
                if method['type'] == 'card':
                    result = self.process_card(amount, method['details'])
                elif method['type'] == 'upi':
                    result = self.process_upi(amount, method['details'])
                elif method['type'] == 'netbanking':
                    result = self.process_netbanking(amount, method['details'])
                elif method['type'] == 'wallet':
                    result = self.process_wallet(amount, method['details'])
                else:
                    continue
                
                if result['success']:
                    return {"status": "success", "method": method['type'], "transaction_id": result['id']}
                else:
                    error_messages.append(f"{method['type']}: {result['error']}")
                    
            except Exception as e:
                error_messages.append(f"{method['type']}: {str(e)}")
                continue
        
        # All methods failed
        return {
            "status": "failed", 
            "error": "All payment methods failed",
            "details": error_messages
        }

# 2.3 not Operator
# Kya hai: Condition ko reverse karta hai.

# Kab use karein:

# Negative checks

# Block lists

# Exclusion logic

# Fallback conditions

# Kahan use karein:

# 1. Ban Check
user_banned = True
if not user_banned:
    print("User can access platform")
else:
    print("User is banned")

# 2. Null Checks
user_data = None
if not user_data:
    print("No user data found")
else:
    print("Processing user data")

# 3. Status Check
is_processing = False
if not is_processing:
    print("Can start new operation")
else:
    print("Wait for current operation")

# 4. Permission Denied
def check_access(user, resource):
    if not user.has_permission('read', resource):
        return {"error": "Permission denied"}
    return {"status": "allowed"}

# 5. Empty Collection
orders = []
if not orders:
    print("No orders to process")
else:
    print(f"Processing {len(orders)} orders")

# Kyu karein:

# Negative conditions clear karte hain

# Code readability improve karte hain

# Edge cases handle karte hain

# Agar use nahi karenge toh:


#  WRONG - Unclear negative condition
if user_banned == False:
    print("User can access")
# == False is less readable

#  CORRECT - Using not
if not user_banned:
    print("User can access")

#  WRONG - Double negative
if not (not user_banned):  # Confusing
    print("Access denied")

#  CORRECT - Simplify
if user_banned:
    print("Access denied")

# Real Industry Example - Access Control System:


class AccessControl:
    def __init__(self):
        self.blacklisted_ips = set()
        self.blocked_countries = set()
        self.maintenance_mode = False
        
    def check_access(self, request):
        """Check if request should be allowed"""
        # Maintenance check
        if self.maintenance_mode:
            if not request.user.is_admin:
                return {"allowed": False, "reason": "System under maintenance"}
        
        # IP blacklist
        if request.ip in self.blacklisted_ips:
            if not request.user.is_admin:
                return {"allowed": False, "reason": "IP address blocked"}
        
        # Country block
        if request.country in self.blocked_countries:
            if not request.user.is_admin:
                return {"allowed": False, "reason": "Country blocked"}
        
        # Authentication check
        if not request.user.is_authenticated:
            return {"allowed": False, "reason": "Authentication required"}
        
        # Rate limiting
        if not request.user.is_admin:
            recent_requests = self.get_recent_requests(request.user.id)
            if len(recent_requests) >= 100:  # Limit 100 requests
                return {"allowed": False, "reason": "Rate limit exceeded"}
        
        # All checks passed
        return {"allowed": True}



# 3.1 if Statement - Everything You Need
# Complete Syntax:

# if condition:
#     # code block
#     # Must be indented (4 spaces)
#     # One or more lines
#     # All indented lines execute when condition is True

# Detailed Understanding:


# Example 1: Simple Check
temperature = 35
if temperature > 30:
    print("Temperature is high")
    print("Please stay hydrated")
    print("Use AC if available")
# All 3 lines execute when condition True

# Example 2: Single Line (Not Recommended)
if temperature > 30: print("Hot day")  # Avoid this

# Example 3: Multiple Conditions in One Line
if temperature > 30 and humidity > 70:
    print("Very uncomfortable weather")

# Example 4: Code Block
if user_logged_in:
    display_dashboard()
    load_user_data()
    update_activity_log()
    send_notification("Welcome back!")
# All functions called when logged in

# Example 5: Nested if
age = 25
has_id = True
if age >= 18:
    if has_id:
        print("Allowed entry")
    else:
        print("ID required")
# Nested if for multi-level checks

# When to use:

# Single condition check

# Simple validations

# Feature flags

# Optional operations

# What happens if not used:

#  WITHOUT IF - Always runs, even when shouldn't
# Would send notification to everyone, even inactive users
send_welcome_notification()  # Should only send to new users

# WITH IF
if user.is_new:
    send_welcome_notification()

# 3.2 if-else - Complete Guide

# if condition:
    # Runs when True
# else:
    # Runs when False


# Multiple Scenarios:


# 1. Binary Decision
def check_even(number):
    if number % 2 == 0:
        return "Even number"
    else:
        return "Odd number"

# 2. Validation
def process_order(order):
    if order.is_valid():
        # Process order
        confirm_order()
        send_invoice()
        update_inventory()
        return "Order processed"
    else:
        # Handle invalid
        return "Invalid order"
# 3. API Response
def handle_api_response(response):
    if response.status_code == 200:
        data = response.json()
        return {"success": True, "data": data}
    else:
        return {"success": False, "error": f"API Error: {response.status_code}"}

# 4. Configuration
def get_database_url():
    if environment == "production":
        return "prod-db.example.com"
    else:
        return "localhost:5432"

# 5. User Experience
def show_dashboard(user):
    if user.has_permission("view_dashboard"):
        render_dashboard()
        load_charts()
        display_metrics()
    else:
        render_access_denied()
        log_unauthorized_access(user.id)

# Why use else:

# Complete coverage of all cases

# Fallback behavior

# Error handling

# Default values

# What if not used:
#  WRONG - Only handles True case
def check_login(user):
    if user.is_authenticated:
        print("Welcome user!")
    # What if user not authenticated? Nothing happens!
    
#  CORRECT - Handles both
def check_login(user):
    if user.is_authenticated:
        print("Welcome user!")
    else:
        print("Please login")

# 3.3 elif - Multiple Conditions Mastery

# if condition1:
    # Check 1
# elif condition2:
    # Check 2 (only if condition1 False)
# elif condition3:
    # Check 3 (only if condition1 and 2 False)

# else:
    # All conditions False

# Real-World Examples:

# 1. Comprehensive Grade System
def calculate_grade(marks, attendance, projects):
    if marks >= 90:
        if attendance >= 75:
            return "A+ (Distinction)"
        else:
            return "A (Good, but improve attendance)"
    elif marks >= 80:
        if projects >= 2:
            return "A (Good projects)"
        else:
            return "B+ (Good, do more projects)"
    elif marks >= 70:
        if attendance >= 80:
            return "B (Good attendance)"
        else:
            return "C+ (Need improvement)"
    elif marks >= 60:
        return "C (Average)"
    elif marks >= 40:
        return "D (Below Average)"
    else:
        return "F (Failed)"

# 2. Price Calculation Engine
def calculate_price(quantity, customer_type, has_coupon):
    base_price = 100
    
    # Customer tier
    if customer_type == "premium":
        tier_discount = 0.20  # 20%
    elif customer_type == "gold":
        tier_discount = 0.15
    elif customer_type == "silver":
        tier_discount = 0.10
    elif customer_type == "bronze":
        tier_discount = 0.05
    else:
        tier_discount = 0
    
    # Quantity discount
    if quantity >= 100:
        quantity_discount = 0.15
    elif quantity >= 50:
        quantity_discount = 0.10
    elif quantity >= 10:
        quantity_discount = 0.05
    else:
        quantity_discount = 0
    
    # Coupon discount
    coupon_discount = 0.10 if has_coupon else 0
    
    total_discount = tier_discount + quantity_discount + coupon_discount
    final_price = base_price * (1 - total_discount)
    
    # Ensure minimum price
    if final_price < 50:
        final_price = 50  # Minimum price guarantee
    
    return round(final_price, 2)

# 3. User Access Levels
def get_user_access(user):
    if user.is_admin:
        return ["all_permissions", "system_settings", "user_management"]
    elif user.is_manager:
        return ["view_reports", "team_management", "project_creation"]
    elif user.is_developer:
        return ["code_access", "deployment", "debug_logs"]
    elif user.is_tester:
        return ["test_cases", "bug_reporting", "qa_reports"]
    else:
        return ["read_only", "profile_edit"]

# Why order matters:
#  WRONG ORDER - Never reaches lower conditions
marks = 85
if marks >= 70:
    print("B Grade")  # 85 >= 70 True, runs here
elif marks >= 80:
    print("A Grade")  # Never runs
elif marks >= 90:
    print("A+ Grade")  # Never runs

#  CORRECT ORDER - Specific to general
if marks >= 90:
    print("A+ Grade")
elif marks >= 80:
    print("A Grade")
elif marks >= 70:
    print("B Grade")

# What if not using elif:

#  BAD - Multiple if statements
x = 3
if x == 1:
    print("One")  # Checks even if not needed
if x == 2:
    print("Two")
if x == 3:
    print("Three")
# All ifs checked -> Waste of CPU

#  GOOD - Using elif
if x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x == 3:
    print("Three")
# Stops at first match -> Efficient

# Nested Conditions - Advanced Patterns
# When to nest:

# Multi-level decisions

# Dependency between conditions

# Hierarchical logic

# Complex business rules

# Pattern 1: Sequential Checks
def validate_transaction(transaction):
    # Level 1: Basic validation
    if transaction.amount <= 0:
        return "Invalid amount"
    
    # Level 2: Account status
    if transaction.account.is_active:
        if transaction.account.balance >= transaction.amount:
            # Level 3: Additional checks
            if transaction.account.daily_limit >= transaction.amount:
                # Level 4: Security check
                if transaction.is_verified:
                    return "Transaction approved"
                else:
                    return "Transaction requires verification"
            else:
                return "Daily limit exceeded"
        else:
            return "Insufficient balance"
    else:
        return "Account inactive"

# Pattern 2: Guard Clauses (Better approach)
def validate_transaction_improved(transaction):
    # Guard clause 1
    if transaction.amount <= 0:
        return "Invalid amount"
    
    # Guard clause 2
    if not transaction.account.is_active:
        return "Account inactive"
    
    # Guard clause 3
    if transaction.account.balance < transaction.amount:
        return "Insufficient balance"
    
    # Guard clause 4
    if transaction.account.daily_limit < transaction.amount:
        return "Daily limit exceeded"
    
    # Guard clause 5
    if not transaction.is_verified:
        return "Transaction requires verification"
    
    # All checks passed
    return "Transaction approved"

# Real Industry Example - Booking System:

class FlightBookingSystem:
    def book_flight(self, booking_details):
        """
        Complex nested decision making
        """
        user = booking_details.user
        flight = booking_details.flight
        passengers = booking_details.passengers
        payment = booking_details.payment
        
        # Level 1: User validation
        if not user.is_verified:
            return {"status": "failed", "reason": "User not verified"}
        
        if user.is_banned:
            return {"status": "failed", "reason": "User banned"}
        
        # Level 2: Flight availability
        if not flight.has_available_seats(passengers):
            return {"status": "failed", "reason": "No seats available"}
        
        if flight.departure_date < datetime.now():
            return {"status": "failed", "reason": "Flight already departed"}
        
        # Level 3: Passenger details
        for passenger in passengers:
            if not passenger.has_valid_id():
                return {"status": "failed", "reason": f"Invalid ID for {passenger.name}"}
            
            if passenger.nationality != flight.country:
                if not passenger.has_valid_visa():
                    return {"status": "failed", "reason": f"Visa required for {passenger.name}"}
        
        # Level 4: Payment processing
        if payment.method == "card":
            if not self.process_card_payment(payment):
                return {"status": "failed", "reason": "Card payment failed"}
        elif payment.method == "wallet":
            if not self.process_wallet_payment(payment):
                return {"status": "failed", "reason": "Wallet payment failed"}
        else:
            return {"status": "failed", "reason": "Unsupported payment method"}
        
        # Level 5: Confirmation
        if payment.amount >= 50000:
            # High value transaction - extra verification
            if not self.send_otp_verification(user.phone):
                return {"status": "pending", "reason": "OTP verification required"}
        
        # All checks passed
        booking_id = self.create_booking(booking_details)
        self.send_confirmation_email(user.email, booking_id)
        
        return {
            "status": "success",
            "booking_id": booking_id,
            "pnr": self.generate_pnr(),
            "message": "Flight booked successfully"
        }

# PART 4: INDUSTRY BEST PRACTICES
# Practice 1: Readable Code
#  BAD - Unreadable
if x>10 and y<20 or z==30 and not w: print("Yes")

#  GOOD - Readable
if (x > 10 and y < 20) or (z == 30 and not w):
    print("Yes")

#  EVEN BETTER - Named conditions
is_valid_range = x > 10 and y < 20
is_special_case = z == 30 and not w
if is_valid_range or is_special_case:
    print("Yes")


# Practice 2: Magic Numbers Avoid

# BAD - Magic numbers
if user_age >= 18:
    print("Adult")

#  GOOD - Constants
ADULT_AGE = 18
if user_age >= ADULT_AGE:
    print("Adult")

#  BAD
if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
# What are 90, 80? Magic numbers!

#  GOOD
GRADE_A_PLUS = 90
GRADE_A = 80
GRADE_B = 70

if marks >= GRADE_A_PLUS:
    grade = "A+"
elif marks >= GRADE_A:
    grade = "A"
elif marks >= GRADE_B:
    grade = "B"

# Practice 3: Early Returns
#  BAD - Deep nesting
def process(order):
    if order:
        if order.items:
            if order.payment:
                if order.address:
                    # Process
                    return "Success"
                else:
                    return "No address"
            else:
                return "No payment"
        else:
            return "No items"
    else:
        return "No order"

#  GOOD - Early returns
def process(order):
    if not order:
        return "No order"
    if not order.items:
        return "No items"
    if not order.payment:
        return "No payment"
    if not order.address:
        return "No address"
    
    # Process
    return "Success"

# Practice 4: Defensive Programming

def safe_divide(a, b):
    # Check both inputs
    if a is None or b is None:
        return {"error": "None values not allowed"}
    
    # Check types
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return {"error": "Invalid input types"}
    
    # Check division by zero
    if b == 0:
        return {"error": "Division by zero"}
    
    # Safe operation
    try:
        result = a / b
        return {"success": True, "result": result}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}




# Complete E-commerce Checkout System:
"""
Complete E-commerce Checkout with all decision making concepts
"""

class ECommerceCheckout:
    def __init__(self):
        self.MINIMUM_ORDER = 100
        self.FREE_SHIPPING_THRESHOLD = 500
        self.DISCOUNT_TIERS = {
            "premium": 0.20,
            "gold": 0.15,
            "silver": 0.10,
            "basic": 0.05
        }
        self.RESTRICTED_COUNTRIES = ["North Korea", "Iran", "Syria", "Cuba"]
        self.MAX_QUANTITY_PER_ITEM = 10
        
    def validate_cart(self, cart, user):
        """Validate all items in cart"""
        errors = []
        
        # Check if cart empty
        if not cart or len(cart['items']) == 0:
            return {"valid": False, "error": "Cart is empty"}
        
        # Check each item
        for item in cart['items']:
            # Quantity check
            if item['quantity'] > self.MAX_QUANTITY_PER_ITEM:
                errors.append(f"Cannot order more than {self.MAX_QUANTITY_PER_ITEM} of {item['name']}")
            
            # Stock check
            if item['quantity'] > item['stock']:
                errors.append(f"Insufficient stock for {item['name']}")
            
            # Price check
            if item['price'] <= 0:
                errors.append(f"Invalid price for {item['name']}")
        
        if errors:
            return {"valid": False, "error": errors}
        
        return {"valid": True}
    
    def calculate_discounts(self, cart_total, user):
        """Apply all applicable discounts"""
        discount = 0
        discount_reasons = []
        
        # Tier discount
        user_tier = user.get('tier', 'basic')
        if user_tier in self.DISCOUNT_TIERS:
            tier_discount = cart_total * self.DISCOUNT_TIERS[user_tier]
            discount += tier_discount
            discount_reasons.append(f"{user_tier} tier discount: {tier_discount:.2f}")
        
        # Bulk discount
        if cart_total >= 1000:
            bulk_discount = cart_total * 0.08  # 8% bulk discount
            discount += bulk_discount
            discount_reasons.append(f"Bulk order discount: {bulk_discount:.2f}")
        
        # New user discount
        if user.get('is_new', False):
            new_user_discount = cart_total * 0.10
            discount += new_user_discount
            discount_reasons.append(f"New user discount: {new_user_discount:.2f}")
        
        # Festival offer
        if cart_total >= 2000 and not user.get('used_festival_offer', False):
            festival_discount = cart_total * 0.05
            discount += festival_discount
            discount_reasons.append(f"Festival offer: {festival_discount:.2f}")
        
        return {
            "total_discount": discount,
            "final_amount": cart_total - discount,
            "reasons": discount_reasons
        }
    
    def process_checkout(self, cart, user, shipping_address, payment_method):
        """
        Complete checkout process with all decision logic
        """
        # Step 1: Validate cart
        cart_validation = self.validate_cart(cart, user)
        if not cart_validation['valid']:
            return {
                "status": "failed",
                "step": "cart_validation",
                "error": cart_validation['error']
            }
        
        # Step 2: Calculate total
        cart_total = sum(item['price'] * item['quantity'] for item in cart['items'])
        
        # Step 3: Apply discounts
        discount_result = self.calculate_discounts(cart_total, user)
        
        # Step 4: Shipping calculation
        if shipping_address['country'] in self.RESTRICTED_COUNTRIES:
            return {
                "status": "failed",
                "step": "shipping",
                "error": "Shipping not available to this country"
            }
        
        # Free shipping check
        if discount_result['final_amount'] >= self.FREE_SHIPPING_THRESHOLD:
            shipping_charge = 0
            shipping_reason = "Free shipping (order above threshold)"
        else:
            shipping_charge = 50
            shipping_reason = "Standard shipping charge"
        
        # Step 5: Payment validation
        if payment_method['type'] not in ['credit_card', 'debit_card', 'upi', 'netbanking', 'wallet']:
            return {
                "status": "failed",
                "step": "payment",
                "error": "Unsupported payment method"
            }
        
        # Step 6: Final amount calculation
        final_amount = discount_result['final_amount'] + shipping_charge
        
        # Step 7: Security check (high value orders)
        if final_amount > 50000:
            # Require additional verification
            if not user.get('verified', False):
                return {
                    "status": "pending",
                    "step": "verification",
                    "message": "High value order requires verification",
                    "amount": final_amount
                }
        
        # Step 8: Process payment
        payment_processed = self.process_payment(final_amount, payment_method)
        if payment_processed['status'] != 'success':
            return {
                "status": "failed",
                "step": "payment_processing",
                "error": payment_processed.get('error', 'Payment failed')
            }
        
        # Step 9: Create order
        order_id = self.create_order(cart, user, shipping_address, final_amount)
        
        # Step 10: Send notifications
        self.send_order_confirmation(user.email, order_id)
        
        # Step 11: Update inventory
        self.update_inventory(cart['items'])
        
        # Step 12: Complete
        return {
            "status": "success",
            "order_id": order_id,
            "final_amount": final_amount,
            "discount_applied": discount_result['total_discount'],
            "discount_reasons": discount_result['reasons'],
            "shipping_charge": shipping_charge,
            "shipping_reason": shipping_reason,
            "payment_method": payment_method['type'],
            "estimated_delivery": self.calculate_delivery_date(shipping_address),
            "message": "Order placed successfully!"
        }
    
    def process_payment(self, amount, payment_method):
        """Payment processing with multiple methods"""
        # Implementation would connect to payment gateways
        return {"status": "success", "transaction_id": "TXN123456"}
    
    def create_order(self, cart, user, address, amount):
        """Create order in database"""
        return "ORD-2024-001"
    
    def send_order_confirmation(self, email, order_id):
        """Send confirmation email"""
        pass
    
    def update_inventory(self, items):
        """Update stock levels"""
        pass
    
    def calculate_delivery_date(self, address):
        """Calculate delivery date based on location"""
        from datetime import datetime, timedelta
        # Business logic for delivery estimation
        return (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")

# Usage Example
checkout = ECommerceCheckout()
cart = {
    'items': [
        {'name': 'Laptop', 'price': 45000, 'quantity': 1, 'stock': 5},
        {'name': 'Mouse', 'price': 500, 'quantity': 2, 'stock': 10}
    ]
}
user = {
    'id': 'user123',
    'tier': 'gold',
    'is_new': False,
    'verified': True,
    'email': 'user@example.com',
    'used_festival_offer': False
}
address = {
    'city': 'Mumbai',
    'state': 'Maharashtra',
    'country': 'India',
    'pincode': '400001'
}
payment = {
    'type': 'credit_card',
    'card_number': '****1234',
    'expiry': '12/25'
}

result = checkout.process_checkout(cart, user, address, payment)
print(result)