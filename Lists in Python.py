list1 = [] # List Definition
list2 = [1,'2',3.0,-4]
print(type(list2))

list2.append('Hey') # Append() Will append at the end of the list
print(list2)

list2.remove(3.0) # Remove() will be based on type
print(list2)

list2.insert(2,'This') # Insert() Specify Index and value/object
print(list2)

# To check elements in list

if 7 in list2:
    list2.remove(7)
else:
    print("Not Found")

print(list2.index(-4)) # Index() will return the index of the specified value
