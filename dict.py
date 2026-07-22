# what is dictonary 
# A Dictonary is a built in python types that stores date in key and value pairs
#  It is and unordered list (Python 3.7+ maintains insertion orders). mutubale are indexed collection 


phonebook = {
    "Hitler Mom": 9987654321,
    "Father Shab": 8889968914,
    "Mitr": 2345678901,

}
print(phonebook)

# Why Dict Exists 

names = ["Rohit","Falguni","Kanchan","Deeksha","Punisha","Arpita","Archit","Mohit"]
ages = [30,27,31,30,32,32,30,31]
city = ["Gwalior","London","California","Delhi","Canda","Punjab","Chennai","Gwalior"]
archit_index = names.index("Archit")
# print(archit_index)
archit_age = ages[archit_index]
print(archit_age)


# sloutions with dictonary

dost = {
    "Rohit":{"age":25,"city":"Gwalior"},
    "Falguni":{"age":27,"city":"London"},
    "Kanchan":{"age":31,"city":"California"}
}


# falni_singh = dost["Kanchan"]["age"]
# print(falni_singh)
print(dost["Kanchan"]["age"])

# When to use dict

school_students = {
    "name":"deeksha Gupta",
    "age": 78
}

user_data={
    "id":101,
    "name":"Shivam"
}

product_db = {
    "P001":{"name":"laptop","price":23456}
}

# api in json 
api_response = {
    "status":"success",
    "data":[{}]
}

gropued_data = {
    "fruits":{"apple","banana","grapess"},
    "veggies":{"carrot","raddish"}
}


# Don't use Dict
fruits = ["apple","grappes","Papaya"]
days = ["Monday","Tuesday"]
num1 = [1,2,3,4]

for i in range(50):
    print(i)

# Memory is very limited
# Dict takes more memory than list

# Youu need mathmatical operations
# (sum, average,etc. on values only)



# KEY (Label) → VALUE (Content)
kitchen = {
    "Sugar": "1 kg white sugar",      # "Sugar" is key, "1 kg white sugar" is value
    "Salt": "500 gm pink salt",        # "Salt" is key, "500 gm pink salt" is value
    "Tea": "Assam tea leaves"          # "Tea" is key, "Assam tea leaves" is value
}

# Get Sugar content using the key
sugar_content = kitchen["Sugar"]  # "1 kg white sugar"
print(sugar_content)

# What is mutuable 
# Mutuable means you can chnage/ modify the after creation 


# Dicitionaries Mutuabel 
student_name = {
    "name":"Deeksha",
    "age":20
}
print("Whole data print:", student_name)


# Change exisiting value 
student_name["age"] = 25
print("after update:",student_name)

student_name["city"] = "Gwalior"
print("Second Update :", student_name)

del student_name["city"]
print("Third Update :", student_name)

print(len(student_name))
xx = student_name.get("age")
print(xx)

print(student_name["name"],student_name["age"])
yz = student_name.keys()
print(yz)

mereko = "mein hu deeksha"
mujheto = mereko
print(mujheto)
mereko = "kuch kuch hota hai"
print(mereko)
print(mujheto)



