
products = {}

cart = []

i = 0

while i<4:
    print("1. Add Products to Stock")
    print("2. Add Products to Cart")
    print("3. Generate Invoice")
    print("4. Exit")
    
    try:
        ch = int(input("Enter your choice"))
    except ValueError:
        print("Invalid Choice")
        break
        
    if ch==1:
        iterator = int(input("How many Products to add in Stock"))
        if iterator != 0 or iterator !='':
            for each in range(iterator):
                company = input("Enter Company : ")
                product = input("Enter Product : ")
                cost = int(input("Enter Cost : "))
                productInsert = []
                productInsert.append(product)
                productInsert.append(cost)
                products[company] = productInsert
            print(products)
    
    elif ch==2:
        if products:
            qt = int(input("How many products to Purchase"))
            if qt != 0 or qt !='':
                for each in range(qt):
                    company = input("Enter Company : ")
                    product = input("Enter Product : ")
                    quantity = int(input("Enter Quantity : "))
                    productkeys = products.keys()
                    if company.lower() in str(productkeys).lower():                            
                            productInCart = []
                            productInCart.append(products[company][0])
                            price = quantity*products[company][1]
                            productInCart.append(price)
                            cart.append(productInCart)
                            print(cart)
                    else:
                        print("Company Not Found")
    elif ch==3:
        if cart:
            amount = 0
            for each in cart:
                amount += each[1]
            print("Total Bill : ",amount)
        else:
            print("\nPlease add items to cart\n")    
    elif ch==4:
        i = 4
    else:
        print("Wrong Choice")
    