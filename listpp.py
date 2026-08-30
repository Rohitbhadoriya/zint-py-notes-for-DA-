chines_order = ["Garlic Naan","Sandwich","Sweet Corn","Haka Noodles","Momos"]
chines_order.append("Kuch kuch hota h")
print(chines_order)
# Value ko last indexing pr add kr deta h
morning_order = [100,200,300,500.900]
eve_order = [900,890,780,678]
morning_order.extend(eve_order)
print(morning_order)
restro_d = ["Sea Food","South Indian","Italian","Chinese"]
restro_d.insert(0,"Thai")
print(restro_d)

flipkart_order = [123,345,678,987,777,987,654,987]
flipkart_order.remove(987)
print(flipkart_order)

last_order = [234,765,555,888,999]
# last_order.pop()
heloo_ji  = last_order.pop(1)
# print(last_order)
print(heloo_ji)
print(last_order)

ord1 = [234,987,444,666]
# ord3 = ord1.clear()
# print(ord3)
ord1.clear()
print(ord1)


ind1 = [999,9999,10000,11000,12000,13000,10000,98765,10000]
ind2 = ind1.index(10000) #agr aap ese use kr rhe h index ko tab 
#wo first value de rha h 
print(ind2)
ind3 = ind1.index(10000,5)
print(ind3)


pizza_price_list = [456,765,999,234,888,765,999,1200,1201]
price_count = pizza_price_list.count(1201)
print("Kuch To Pta h", price_count)



sortbills = [450,1200,899,2340,675]
# sortbills2 = sortbills.sort()
# print(sortbills2)
# sortbills.sort()
sortbills.sort(reverse=True)
print(sortbills)

reverslist = [123,456,789,987,654,321,237]
reverslist.reverse()
print(reverslist)

original = [1,2,3,4,5,6]
backup = original.copy()
backup.append(456)
print(original)
print(backup)

pizaa_hut_bills = [450,1200,899,2340,675,1500]
length_bills = len(pizaa_hut_bills)
print(length_bills)
total = sum(pizza_price_list)
print(total)
maxx = max(pizaa_hut_bills)
print(maxx)


minn = min(pizaa_hut_bills)
print(minn)
print(4 in pizaa_hut_bills  )