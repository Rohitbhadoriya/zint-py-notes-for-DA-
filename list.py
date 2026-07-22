# List 4 Types
# daily_orders = []
# daily_orders = [440,450,453,986,900]
zomato_orders = [78456,"Rohit",123.09,True,"Bhopal"]
# jabi apko list ready krna hoga to []
print(zomato_orders)
numbers = list(range(10))
print(numbers)
other_bill = [100,200,300,400,500,600]
print(other_bill[0])
print(other_bill[3])
print(other_bill[-1])
print(other_bill[-3])
print(other_bill[::-1])   # is kya hoga poora reverse ho jata h 
print(other_bill[0:6])     # is se hum range de kar print karwa rhe 
print("kuch to bato ", other_bill[3:])      # last mein jitne bi index hogi wo sab a jayegi 
print(other_bill[::2])
print(other_bill)


# Questions => Slicing mein new list bnati h ya original 
# modify hoti hai 
# Ans: Naya list object banata hai. Original ko 
# unchnaged rkhta h 




#  What is append 
# List ke last mein ek value ko add krta hai
# list.append()
# Jab ek naya item add krete to use end mein add krna hota h 
# Zomato mein naya order aya to usey list mein add krna h 

chines_order = ["Garlic Naan","Sandwich","Sweet Corn","Haka Noodles","Momos"]
print(chines_order)
# store = chines_order.append("Kaddu")
chines_order.append("Kaddu")
print(chines_order)
# print(store)

# Interview append() vs extend() mein diff ky hai 
# append ek single value add krta hai.extend ek list 
# ke sarre elements add krta hai 

# Method 2 extend()
# El lisyt ke sare elemnets ko dusri list mein add krna 
# jab ek sath multiple values add krni ho 
# 
morning_order = [100,200,300,500.900]
eve_order = [900,890,780,678]
morning_order.extend(eve_order)
print(morning_order)
# extend kya krta hai : extend() original modify krta 
# hai nai list nhi banata hai 

# Insert
# Kisi specific positions (index) pe value insert krna hai 
# list.insert(index,value)
# jab order maintain krna  imp ho. kese jaise koi order 
# imp hai to iski indexing change kr denge 
# orders_1 = [123,234,456,789]
# orders_1.insert(1,1234567)
# print(orders_1)
restro_d = ["Sea Food","South Indian","Italian","Chinese"]
restro_d.insert(0,"Thai")
print(restro_d)

# Remove
# pheli occurence of value ko delete krta hai 
# jab speicfic value delete krni ho (uski position nhi pta ho)
# wo sirf first value he hta deta first value ka mtlb jo usey pheli mili
flipkart_order = [123,345,678,987,777,987,654,987]
flipkart_order.remove(987)
print(flipkart_order)
# Note: Agr value exist nhi krti h to wo value
# erorr dega 
# flipkart_order2 = [123,567,987]
# flipkart_order2.remove(777)
# print(flipkart_order2)

# Pop 
# Kisi index ki value ko remove krta h or return bi krta h 
# list.pop() - default index -1 (last)

last_order = [234,765,555,888,999]
# last_order.pop()
heloo_ji  = last_order.pop(1)
# print(last_order)
print(heloo_ji)
print(last_order)

# Interview Questions = pop(0) slow  kyu hota hai 
# kyu ki list andar se array hai . Index O remove karne ke baad
# sare elements ko ek position left shift krni pda - (o)n operation 


# clear 
# poorilist empty kar deta hai 
# jab sara data reset krna ho tab hum iska use krte hai 
ord1 = [234,987,444,666]
# ord3 = ord1.clear()
# print(ord3)
ord1.clear()
print(ord1)

# Index 
# value ki first occurence ka index batata hai 
# list.index(value, start,end)
# jaise ki maan lo aapko pta krna ki 10000 ki sindex pe hai 

ind1 = [999,9999,10000,11000,12000,13000,10000,98765,10000]
ind2 = ind1.index(10000) #agr aap ese use kr rhe h index ko tab 
#wo first value de rha h 
print(ind2)

ind3 = ind1.index(10000,8) # gar ese use kr rhe h to wo apko
# indexing bta rha h 
# (10000,3) to kya krega third index se 
# count krega jha apki value mil rhi wha ki wo indexing bta dega 
# agr value nhi milegei to kya hoga to wo valueerror ka msg de dega 

print(ind3)

# count
# list mein value kitni bar ayi 
# Frequency count ke liye 
# ha ye store krta h 
pizza_price_list = [456,765,999,234,888,765,999,1200,1201]
price_count = pizza_price_list.count(1201)
print("Kuch To Pta h", price_count)



# sort()
# list ko asecending / descending order mein sort krta h 
# Data ko sorted order dikhna ho jab use hota h 
# sort store nhi krtA h 
sortbills = [450,1200,899,2340,675]
# sortbills2 = sortbills.sort()
# print(sortbills2)
# sortbills.sort()
sortbills.sort(reverse=True)
print(sortbills)
# IMP sort () original list modifiy krta hai 
# AlterNative : sorted(list) = nayi sorted list reutrn krta hai , 
# orginial changed
sortedbills2 = sorted(sortbills)
print(sortedbills2)
# sort() or sorted mein diiference kya h
# sort() orginial list ko changed krta h or none return krta h .
# sorted() nayi list return krta h or original unchanged rhti h 



# reverese
# list ka order ulta kr deta h 
# jab last wala order hume first mein dekhna h 
reverslist = [123,456,789,987,654,321,237]
reverslist.reverse()
print(reverslist)


# copy
# list ki shallow copy bnata hai 
# orginal list ko protect krna h copy mein changes krne hai 
original = [1,2,3,4,5,6]
backup = original.copy()
backup.append(456)
print(original)
print(backup)
# Simple new = original se copy nhi hota h Dono smae list point krte h 

# wrong way
o1 = [1,2,3,4]
o2 = o1
o2.append(345)
print(o2)

# Built In Functions in lists
# len() Length
# sum() value add kr dega 
# max() wha max value nikal lega 
# min() wha min value niakl lega
# in check exists 

pizaa_hut_bills = [450,1200,899,2340,675,1500]
length_bills = len(pizaa_hut_bills)
total = sum(pizza_price_list)
maxx = max(pizaa_hut_bills)


minn = min(pizaa_hut_bills)
if 2000 in pizaa_hut_bills:
    print("High Value Order")
print(length_bills)
print(total)
print(maxx)
print(minn)

# List Comperhension 
# What is list comp
# Expression 
# Loop 
# condition 
# Syntax[expression for item in iterable if condition ]
# Why use list compernesion 
# Code short
# Faster
# Readable
# Normal Way

iterate = [234,546,789,987,211,1111,4567,7890]
new_iterate = []
for some in iterate:
    new_iterate.append(some + 100)
print(new_iterate)

# iterate = [234,546,789,987,211]
# new_iterate = []
# for some in range(len(iterate)):
#     iterate[some] = iterate[some] + 100

    # iterate.append(some + 100)
    # print(iterate)
# print(iterate)

new_iterate2 = [ramlal + 100 for ramlal in iterate]
print("kuch to ",new_iterate2)
high_bills = []
for high in iterate:
    if high > 700:
        high_bills.append(high)
print(high_bills)

list2345 = ["Rohit", "Falguni", "Rohit", "Falguni", "Rohit", "Falguni","Shyam", "Ramesh", "Deeksha"]

list23456=[]
for sita in list2345:
    if sita not in list23456:
        list23456.append(sita)
print(list23456)

# IF _ELSE
ttbills = [450,1200,899,2340,675,1500]
category = ["Low" if bill < 1000 else "High" for bill in ttbills ]
print(category)
suqrared = [x**2 for x in range(10)]
print(suqrared) 
sqt = [y**2 for y in [2,4,7,9,11,22,33,44,55]]
print(sqt)

highbill123 = [234,556,789,900,1001,1200,1500,2000,2500,3000,4000,5000]
result = [final_bill_list + 100 for final_bill_list in highbill123  if final_bill_list > 1000]
print(result)
result1 = []
for result2 in highbill123:
    if result2 > 1000:
        result1.append(result2 + 100)
print(result1)

guptajibill = [789,907,887,556,444,888,999]
cccvft = []
for golejibill in guptajibill:
    cccvft.append(golejibill + 100)
print(cccvft)
tanishk = []
for gupta in guptajibill:
    if gupta > 800:
        tanishk.append(gupta + 30)
print("Hello Ji mein hu makar", tanishk)
print("Hello Ji mein hu makar", guptajibill)

# even number 
even = [x for x in range(20) if x % 2 == 0]
print(even)
even1 = [x for x in [1,2,3,4,5,6,7,8,9,10] if x % 2 == 0]
print(even1)

odd = [x for x in range(20) if x % 2 != 0]
print(odd)


# gst with 5%
gstbiils = [100,200,300,400,500,600]
gst = [bill + (bill * 0.05) for bill in gstbiils]
print(gst)

# order s above average 

order123456 = [100,200,300,400,500,600]
average = sum(order123456) / len(order123456)
above_average = [order for order in order123456 if order > average]
print(above_average)

# convert string into list 
str_bills = ["200","300","400","500"]
int_bills = [int(bill) for bill in str_bills]
print(int_bills)






# Practiuce questions
zudio_bills = [100,200,300,400,500,600]
# for ttyls in zudio_bills[:]:
#     zudio_bills.append(ttyls + 100)
# print("Kuch to check kro ", zudio_bills)

# final_zuido_bills = [bill + 100 for bill in zudio_bills]
# print(final_zuido_bills)
# for zzz in zudio_bills:
#     print(zzz + 100)

# Ye infinite loop hoga kyu ki hum list 
# ke andar hi iterate kr rhe h or usi list mein append kr rhe h




# String Methods
# String Methods are built-in functions that can be used 
# to manipulate strings in Python.
# Some common string methods include:
# 1. upper(): Converts all characters in a string to uppercase.
# 2. lower(): Converts all characters in a string to lowercase.
# 3. strip(): Removes whitespace from the beginning and end of a string.
# 4. replace(): Replaces a specified substring with another substring.
# 5. split(): Splits a string into a list of substrings based on a specified delimiter.
# 6. join(): Joins a list of strings into a single string using a specified delimiter.
# 7. find(): Returns the index of the first occurrence of a specified substring in a string.
# 8. count(): Returns the number of occurrences of a specified substring in a string.
# 9. isalpha(): Returns True if all characters in a string are alphabetic, False otherwise.
# 10. isdigit(): Returns True if all characters in a

# strip
var_name = "                 Hello, World!            "
# print(var_name)
# print(var_name.strip())
var_name2 = var_name.strip()
print(var_name2)

# upper/lower()
print(var_name2.upper())
print(var_name2.lower())


# Title()
var_name3 = "satyam singh"
print(var_name3.title())


# split()
var_name4 = "Hello, World! Welcome to Python."
print(var_name4.split())
var_name5 = "apple,banana,cherry"
print(var_name5.split(","))


# join()
var_name6 = ["Hello", "World", "Welcome", "to", "Python"]
print(" ".join(var_name6))
var_name7 = ["apple", "banana", "cherry"]
print("+".join(var_name7))

# replace()
var_name8 = "+91-1234567890"
clean_number = var_name8.replace("+91-", "")
print(clean_number)

var_name9 = "Hello, World! Welcome to Python."
print(var_name9.replace("Python", "Programming"))


# find()
var_name10 = "Hello, World! Welcome to Python."
print(var_name10.find("World"))









