# a = [10, 20, 30, 40, 50]
# b = a[1:4]
# b[0] = 999
# print(a)
# print(b)
# What will be printed? Why?
# Answer:
# [10, 20, 30, 40, 50]
# [999, 30, 40]
# Explanation: Slicing always creates a new list object. Changing b does not affect the original a. This is the key difference from assignment (b = a).


# 2. append vs extend – the classic trap
# x = [1, 2, 3]
# y = [4, 5]
# x.append(y)
# print(x)
# print(len(x))
# What is the output and length?
# Now change append to extend and answer again.
# Answer:
# With append: [1, 2, 3, [4, 5]] → length 4 (one nested list added)
# With extend: [1, 2, 3, 4, 5] → length 5
# Explanation: append adds the entire object as a single element. extend unpacks the iterable and adds each element individually. This is the most common interview trap.


# 3. Why is pop(0) slow? (O(n) question)
# orders = [100, 200, 300, 400, 500]
# orders.pop(0)
# Why do interviewers say list.pop(0) is expensive?
# Answer:

# Because a list is implemented as a dynamic array. Removing index 0 forces every remaining element to shift one position left. This is an O(n) operation.
# pop() or pop(-1) is O(1) because nothing needs to be shifted.

# 4. remove() vs pop() – subtle difference
data = [11, 22, 33, 22, 44]
data.remove(22)
print(data)

# What happens? What if the value does not exist?
# Answer:

# [11, 33, 22, 44] → only the first occurrence is removed.

# If the value is not present → ValueError.
# Extra trick: pop(index) returns the removed value, remove(value) returns None.

# 5. sort() vs sorted() – return value trap
bills = [450, 1200, 899, 2340]
result = bills.sort()
print(result)
print(bills)

# What will be printed?
# Answer:

# None

# [450, 899, 1200, 2340]
# Explanation:

# list.sort() sorts in-place and returns None.
# sorted(list) returns a new sorted list and leaves the original unchanged.
# This is one of the most frequent interview mistakes.

# 6. Shallow copy vs assignment
original = [1, 2, 3]
backup = original          # wrong way
backup.append(99)
print(original)

# What happens? How do you fix it?
# Answer:

# [1, 2, 3, 99] → both variables point to the same list object.
backup = original.copy()   # or list(original) or original[:]

# 7. index() with start parameter (tricky range)
nums = [10, 20, 30, 20, 40, 20, 50]
print(nums.index(20, 3))
# What does it return? What if you write nums.index(20, 6)?
# Answer:

# 3 (first 20 found starting from index 3)

# nums.index(20, 6) → ValueError because no 20 exists from index 6 onwards.

# 8. Combination question (real interview style)
orders = [100, 200, 300, 200, 400]
orders.remove(200)
orders.insert(0, 999)
orders.append([500, 600])
print(orders)
print(orders.count(200))
# Final output and count?
# Answer:

# [999, 100, 300, 200, 400, [500, 600]]

# count(200) → 1
# Explanation:

# remove deleted only the first 200
# insert(0, …) added at the beginning
# append added a nested list
# remaining 200 is still there → count is 1

# Slicing + reverse combination
nums = [10, 20, 30, 40, 50, 60]
print(nums[::-1][1:4])
print(nums)
# Output kya aayega?
# Answer:

# [50, 40, 30]

# Original list unchanged: [10, 20, 30, 40, 50, 60]
# Explanation: nums[::-1] pehle naya reversed list banata hai, phir uspe slicing hoti hai. Original list kabhi modify nahi hoti.
# copy() vs slicing vs assignment
a = [1, 2, 3]
b = a.copy()
c = a[:]
d = a
b.append(10)
c.append(20)
d.append(30)
print(a)
print(b)
print(c)
# Kya print hoga?
# Answer:

# [1, 2, 3, 30]

# [1, 2, 3, 10]

# [1, 2, 3, 20]
# Explanation:

# a.copy() aur a[:] dono nayi list banate hain → independent
# d = a same object point karta hai → change reflect hota hai