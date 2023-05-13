fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_fruits = []
for fruit in fruits:
    if "a" in fruit:
        new_fruits.append(fruit)
print(new_fruits)


new_fruits = [fruit for fruit in fruits if "a" in fruit or "i" in fruit]
print(new_fruits)

# -----------------------------------

lst = [1,2,3,4,4]
set = {i for i in lst}
print(set)
print(type(set))

# -----------------------------------

lst = [1,2,3,4]
dic  = {i:i*i for i in lst}
print(dic)

# --------------------------------------

name = ['dhilip', 'kumar', 'naresh']
age = [10, 20, 30]
dic = {key:val for key, val in zip(name,age)}
print(dic)

zipped = zip(name, age)
print(zipped)
print(type(zipped))
name_z, age_z = zip(*zipped)
print(name_z)
print(age_z)
print(type(name_z))

# -----------------------------------------
