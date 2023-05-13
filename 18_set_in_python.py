
'''

set is a unordered and unindexed data structure
it does not allow duplicate elements
elements are enclosed in curly brace - {1,2,3}
we can add ,delete elements but we cannot change(edit) element

'''

myset = set(["a", "b", "c"])
myset.add("d")
print(myset)

names = {'dhilip','kumar','ram'}
print(type(names))

#accessing values
for name in names:
    print(name,end=" ")

print()
#adding new name
names.add('ganesh')
print(names)

#add another set of data
a = {'laksh','sita'}
names.update(a)
print(names)

print('laksh' in names)


# remove values
#names.remove('Dhilip') # remove func will throw error if element is not present in set
#print(names)

# to avoid that we have to use dicard func
# it delete if element present , otherwise nothing will happen
names.discard('dhilip')
print(names)
a.clear()
print(a)


# getting common element in 2 sets
a = {1,2,3,4,5}
b = {4,5,6,7,8,9}
c = a.intersection(b)
print(c)
#a.intersection_update(b) # storing result in "a" set
#print(a)

# storing uncommon values
c = a.symmetric_difference(b)
print(c)

# ------------------------------------------
'''
Frozen sets in Python are immutable objects 
that only support methods and operators that 
produce a result without affecting the frozen 
set or sets to which they are applied.
'''
frozen_set = frozenset(["e", "f", "g"])
# Uncommenting below line would cause error as
# we are trying to add element to a frozen set
# frozen_set.add("h")
