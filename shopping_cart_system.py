product_list = []
user_list = []
cart_list = []
order_list = []

while True:
    print('='*10,'       SHOPPING CART SYSTEM     ','='*10)
    print('1. Admin')
    print('2. User')
    print('3. Exit')
    role = input('Enter your choice: ')
    # ADMIN SECTION
    if role == '1':
        while True:
            print('---------- ADMIN MENU ----------')
            print('1. Add Product')
            print('2. Update Product')
            print('3. Remove Product')
            print('4. View Products')
            print('5. View Users')
            print('6. view order History')
            print('7. Return to Main Menu')
            choice = input('Enter your choice: ')       
            # ADD PRODUCT
            if choice == '1':
                product = input('Enter product name: ')
                price = float(input('Enter product price: '))
                if price>0:
                    product_list.append([product, price])
                    print('Product added successfully')
                else:
                    print('price must be greater than zero')                
            # UPDATE PRODUCT
            elif choice == '2':
                if len(product_list) == 0:
                    print('No products available')
                else:
                    print('Available Products:')
                    i = 0
                    while i < len(product_list):
                        print(i + 1, product_list[i][0],product_list[i][1])
                        i = i + 1
                    number = int(input('Enter product number to update: '))
                    index = number - 1
                    if index >= 0 and index < len(product_list):
                        new_name = input('Enter new product name: ')
                        new_price = float(input('Enter new price: '))
                        if new_price>0:
                            product_list[index][0] = new_name
                            product_list[index][1] = new_price
                            print('Product updated successfully')
                        else:
                            print('price must be greater than zero')
                    else:
                        print('Invalid product number')                        
            # REMOVE PRODUCT
            elif choice == '3':
                if len(product_list) == 0:
                    print('No products available')
                else:
                    print('Available Products:')
                    i = 0
                    while i < len(product_list):
                        print(i + 1, product_list[i][0],product_list[i][1])
                        i = i + 1
                    number = int(input('Enter product number to remove: '))
                    index = number - 1
                    if index >= 0 and index < len(product_list):
                        removed_product = product_list.pop(index)
                        print('Removed', removed_product[0])
                    else:

                        print('Invalid product number')
            # VIEW PRODUCTS
            elif choice == '4':
                if len(product_list) == 0:
                    print('No products available')
                else:
                    print('========== PRODUCTS ==========')
                    i = 0
                    while i < len(product_list):
                        print(i + 1,product_list[i][0],product_list[i][1])
                        i = i + 1
            # VIEW USERS
            elif choice == '5':
                if len(user_list) == 0:
                    print('No users registered')
                else:
                    print('========== REGISTERED USERS ==========')
                    i = 0
                    while i < len(user_list):
                        print('User:',user_list[i][0])
                        print('Cart items:',len(user_list[i][1]))
                        i = i + 1
            # View Order History            
            elif choice == '6':
                if len(order_list) == 0:
                    print('No confirmed orders')
                else:
                    print('========== ORDER HISTORY ==========')
                    i = 0
                    while i < len(order_list):
                        print('Order Number:', i + 1)
                        print('Customer:', order_list[i][0])
                        print('Products:')
                        j = 0
                        while j < len(order_list[i][1]):
                            print(
                                order_list[i][1][j][0],order_list[i][1][j][1])
                            j = j + 1
                        print('Total: Rs.', order_list[i][2])
                        print('-------------------------')
                        i = i + 1
            # RETURN TO MAIN MENU
            elif choice == '7':
                print('Returning to Main Menu')
                break
            else:
                print('Invalid choice')            
    # USER SECTION
    elif role == '2':
        name = input("Enter your name: ")
        # FIND EXISTING USER
        user_index = 0
        while user_index < len(user_list):
            if user_list[user_index][0].lower() == name.lower():
                break
            user_index = user_index + 1
        # REGISTER NEW USER IF NOT FOUND
        if user_index == len(user_list):
            user_list.append([name, []])
            user_index = len(user_list) - 1
            print('New user registered successfully')
        else:
            print('Welcome back', user_list[user_index][0])
        # USE THIS USER'S OWN CART
        cart_list = user_list[user_index][1]
        while True:
            print('---------- USER MENU ----------')
            print('1. View Products')
            print('2. Add to Cart')
            print('3. Remove from Cart')
            print('4. View Cart')
            print('5. Checkout')
            print('6. Return to main Menu')
            choice = input('Enter your choice: ')
        # VIEW PRODUCTS
            if choice == '1':
                if len(product_list) == 0:
                    print('No products available')
                else:
                    print('========== PRODUCTS ==========')
                    i = 0
                    while i < len(product_list):
                        print(i + 1,product_list[i][0],product_list[i][1])
                        i = i + 1
        # ADD TO CART
            elif choice == '2':
                if len(product_list) == 0:
                    print('No products available')
                else:
                    print('========== PRODUCTS ==========')
                    i = 0
                    while i < len(product_list):
                        print(i + 1,product_list[i][0],product_list[i][1])
                        i = i + 1
                    number = int(input('Enter product number: '))
                    index = number - 1
                    if index >= 0 and index < len(product_list):
                        cart_list.append(product_list[index][0],product_list[index][1])
                        print(product_list[index][0],'added to cart')
                    else:
                        print('Invalid product number')
        # REMOVE FROM CART
            elif choice == '3':
                if len(cart_list) == 0:
                    print('Your cart is empty')
                else:
                    print('========== YOUR CART ==========')
                    i = 0
                    while i < len(cart_list):
                        print(i + 1,cart_list[i][0],cart_list[i][1])
                        i = i + 1
                    number = int(input('Enter item number to remove: '))
                    index = number - 1
                    if index >= 0 and index < len(cart_list):
                        removed = cart_list.pop(index)
                        print(removed[0], 'removed from cart')
                    else:
                        print('Invalid item number')
        # VIEW CART
            elif choice == '4':
                if len(cart_list) == 0:
                    print('Your cart is empty')
                else:
                    print('========== YOUR CART ==========')
                    total = 0
                    i = 0
                    while i < len(cart_list):
                        print(i + 1,cart_list[i][0],cart_list[i][1])
                        total = total + cart_list[i][1]
                        i = i + 1
                    print('------------------------------')
                    print('Total Amount = ', total)
        # CHECKOUT
            elif choice == '5':
                if len(cart_list) == 0:
                    print('Your cart is empty')
                    print('Please add products first')
                else:
                    total = 0
                    i = 0
                    print('========= CHECKOUT =========')
                    print('Customer:',user_list[user_index][0])
                    while i < len(cart_list):
                        print(cart_list[i][0],cart_list[i][1])
                        total = total + cart_list[i][1]
                        i = i + 1
                    print('Customer:', name)
                    print('Total Amount:', total)
                    confirm = input('Confirm order? (yes/no): ')
                    if confirm.lower() == 'yes':
                        order_list.append([user_list[user_index][0],cart_list[:],total])
                        print('Order placed successfully')
                        cart_list.clear()
                        print('your cart has been cleared')
                    else:
                        print('Order cancelled')
        # RETURN TO MAIN MENU
            elif choice == '6':
                print('Returning to Main Menu')
                break
            else:
                print('Invalid choice')
   # EXIT PROGRAM
    elif role == '3':
        print('Thank you for using Shopping Cart System')
        break
    else:
        print('Enter correct choice')
