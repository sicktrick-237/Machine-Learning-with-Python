#print("Hello")

val = 'Hey'

# a = input(val) #input function will consider everything as a string.
# Input will print out the value of the variable

# print(type(a)) # Checks the type of the specified Datatype

import time
#------------------TypeCasting-------------------

a1 = int(input("Value 1 : ")) # input function will consider everything as a string.
a2 = int(input("Value 2 : ")) # unless explicitly typecasted
res = a1 + a2

if res < 0: # Indentation specifies the start of a control block 
    print("Value is -ve")
elif res == 0:
    print("Value is Zero")
else:
    print("Value is +ve")

print("Added values are : ",res)

#---------------------Errors-------------------
# For type errors : TypeError | For value errors : ValueError

#--------------------Assignment-------------------
name = input("Enter your name: ")
by = int(input("Enter Year of Birth: "))
gender = input("Enter Your Gender: ")
age = time.localtime().tm_year - by # tm_year is a param from localtime method

print("Hey,",name)
if (gender == 'F' and age > 18) or (gender == 'M' and age > 21):
    print("You're eligible")
elif (gender == 'F'):
    if(age < 18):
        print("You're eligible after ",18-age)
else:
    if(age < 21):
        print("You're eligible after ",21-age)
