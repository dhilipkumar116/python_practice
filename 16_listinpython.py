
'''
sequence type, mutable
'''

a=[1,2,3,4,5,6]
print(a)
print(type(a))
a[0] = 100

print("splicing")
print(a[0:5])
print(a[0:])
print(a[2:])
print(a[-1])
print(a[-2])
print(a[:-1])
print("----------------------")

#array is not homogenous in python
a = [1,"dhilip",True,13.5,[1,2,3]]
print(type(a))
print(a[0]," type is ",type(a[0]))
print(a[1]," type is ",type(a[1]))
print(a[2]," type is ",type(a[2]))
print(a[3]," type is ",type(a[3]))
print(a[4]," type is ",type(a[4]))
print(a[4][2])
print("-------------------------")

#inbuild functions
a = [1,2,3,4,3,4,12]
b = a.copy()
print(b)
print(a.count(3)) # counts number of 3 in given array
print(a.index(1))
print(len(a))
print(max(a))
print(min(a))
a.pop(0) # remove value in specified index
print(a)
a.remove(2) # remove value
print(a)
print("------------------------")
name1 = ["ram"]
name1.append("kumar")
name1.append("ravi")
print(name1)
name2 = ["vasu"]
name1.extend(name2) # appendind list of values
print(name1)
name1.insert(0,"sam")
print(name1)

a.sort()
print(a)
a.sort(reverse=True)
print(a)
name1.sort(key=len) # sorting based on length of word
print(name1)



'''
Append()	Add an element to the end of the list
Extend()	Add all elements of a list to another list
Insert()	Insert an item at the defined index
Remove()	Removes an item from the list
Clear()	Removes all items from the list
Index()	Returns the index of the first matched item
Count()	Returns the count of the number of items passed as an argument
Sort()	Sort items in a list in ascending order
Reverse()	Reverse the order of items in the list
copy()	Returns a copy of the list
'''









