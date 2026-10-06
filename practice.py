user = ["rohit","sujal","harsh"]
user.remove("rohit")
print(user)

anchal = [23,45,67,89,90]
anchal.sort()
print(anchal)

numbers = [1,2,3,4,5,6,7,8,9]
numbers.insert(3,99)
print(numbers)

original = [10,20,30,40,50,]
backup = original.copy()
backup.append(78)
print(original)
print(backup)

ind1 = ["momos","pizza","burger","pasta"]
ind2 = ind1.index("burger")
print(ind2)

fruits = ["lichi","apple","orange","mango"]
hii = fruits.pop(3)
print(hii)

myset = {
    "apple",
    "mango",
    "banana",
    "chiku"
}
print(type(myset))

a=[1,2,3,4,5,6]
print(a)

a=[1,2,3,4,5,6]
a.insert(7,6)
print(a)

a=[1,2,3,4,5,6]
a.remove(4)
print(a)

a=[1,2,3,4,5,6]
a.pop(1)
print(a)

a=[1,2,3,4,5,6]
a.clear()
print(a)

a=["tomato","potato"]
b=a.index("potato")
print(b)

a=["apple","banana","mango","banana"]
b=a.count("banana")
print(b)

a=[1,4,5,7,0,4]
b=a.sort()
print(a)

a=[1,4,5,7,0,4]
a.sort(reverse=True)
print(a)

a=[1,2,3,4,5,6]
a.reverse()
print(a)

a=[1,2,3,4,5,6]
b=a.copy()
print(b)

list1 = [100,200,300,400,500,600]
print(list1[::2])
