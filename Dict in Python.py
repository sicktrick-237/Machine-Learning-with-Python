# Dict have unique keys across it's elements
# Can be accessed by Key Value pair
# Keys can be accessed directly, Values will require which keys it's related to


i = 0
data = {}

while i<4:
    print("1. Add studs")
    print("2. Remove studs")
    print("3. Display studs")
    print("4. Exit")
    ch = int(input("Enter Your Selection"))

    if ch==1:
        ele = int(input("How many studs you want to add"))
        for each in range(ele):
            roll = input("Enter Roll: ")
            marks = float(input("Enter Marks: "))
            data[roll] = marks
        print(str(ele) + " Students Added")

    elif ch==2:
       ele = input("Student Roll")
       if ele in data:
            del data[ele]
       else:
            print("Student not in list") 
    elif ch==3:
        for each in data:
            print(each)
    elif ch==4:
        i = 9
    else:
        print("Invalid Selection")
