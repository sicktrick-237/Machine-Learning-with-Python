list1 = [1,2,3,4,5,6,7,8]
l = len(list1)

# FOR LOOPS

# Negative indexing accessing from last
#for each in range(-1,-(l+1),-1):
#                  print(list1[each])


# Negative accessing from start
# for each in range(-l,0,1):
#    print(list1[each])


# WHILE LOOPS
# To perform user interactive 

i = 0
elements = []


while i<5:
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Insert Item")
    print("4. Display Item")
    print("5. Exit")
    ch = int(input("Enter Your Selection"))

    if ch==1:
        ele = int(input("How many elements you want to add"))
        for each in range(ele):
            e = input("Enter Element: ")
            elements.append(i)
        print("Elements Added")
    elif ch==2:
        ele = input("Which Element")
        if ele in elements:
            element.remove(ele)
        else:
            print("Element not in list")
    elif ch==3:
        elein = int(input("At which pos."))
        ele = input("Element")
        elements.insert(elein,ele)
    elif ch==4:
        for each in elements:
            print(each)
    elif ch==5:
        i=6
        
