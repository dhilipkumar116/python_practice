'''

key value pair with key as a index
key should be unique

'''

user= {
    "name":"dhilip",
    "age":22,
    "isMarried":False
}

print(user)
print(type(user))
print(user["name"])
print(user.get("name"))
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items())

print("user:")
for x in user:
    print(x,"-",user[x])

print("keys:")
for x in user.keys():
    print(x)

print("values:")
for x in user.values():
    print(x)

print("items:")
for x,y in user.items():
    print(x,y)

if "age" in user:
    print("age is present")
else:
    print("age is not present")

# updating dictionary

user.update({"gender":"male"})
print(user)
user["age"] = 50
print(user)
user.pop("age")
print(user)


# nested dictionary

users = {
    "user1":{
        "name":"dhilip",
        "age":22,
        "isMarried":False
    },
    "user2":{
        "name":"sam",
        "age":45,
        "isMarried":True
    }
}
print(users)
print(users['user1']['name'])

'''
dic.clear()	Remove all the elements from the dictionary
dict.copy()	Returns a copy of the dictionary
dict.get(key, default = “None”)	 Returns the value of specified key
dict.items()  Returns a list containing a tuple for each key value pair
dict.keys()	 Returns a list containing dictionary’s keys
dict.update(dict2)	Updates dictionary with specified key-value pairs
dict.values()	 Returns a list of all the values of dictionary
pop()	 Remove the element with specified key
popItem()	Removes the last inserted key-value pair
dict.setdefault(key,default= “None”)	set the key to the default value if the key is not specified in the dictionary
dict.has_key(key)	returns true if the dictionary contains the specified key.
dict.get(key, default = “None”)	used to get the value specified for the passed key.
'''