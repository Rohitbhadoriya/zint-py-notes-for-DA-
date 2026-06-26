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
# Ans: Naya list object banata hai. Original ko unchnaged rkhta h 
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
# poorilist empt kar deta hai 
# jab sara data reset krna ho tab hum iska use krte hai 




