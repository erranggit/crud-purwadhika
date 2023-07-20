inventory = [
    ['CG010107','Rokok mild',17,24000, 'Cigarettes'],
    ['DR010107','Le minerale',15,5000, 'Water'],
    ['SN010107','Chittato',19,14000, 'Snack'],
    ['KP010107','Kapal api',12,6000, 'Coffee'],
    ['TH010107','Teh sosro',11,5000, 'Tea']
]       ## DATA

def show(): ## FUNCTION SHOW DATA MENU
        if len(inventory) == 0:
            print('No Stock Available')
        else:
            print('------------------------------------------------------------')
            print('Item\'s Code\tName\t\tStock\tPrice\tCategory')
            print('------------------------------------------------------------')
            for goods in inventory:
                print(f'{goods[0]}\t{goods[1]}\t{goods[2]}\t{goods[3]}\t{goods[4]}')

def menu(): ## FUNCTION MAIN MENU
    print('''
    Welcome to Our Mini Store

    List Menu :
    
    1. Show the Choice of The Item(s) Menu
    2. Add Item(s)
    3. Update Item(s)
    4. Delete Item(s)
    5. Buy Item(s)
    6. Exit Prorgam


    ''')

def read_menu():   ## FUNCTION CHOICE OF THE ITEM'S  / READ
    print('''

1. Show Menu
2. Search Data
3. Back to Menu

''')
    
def add_menu():   ## FUNCTION ADD DATA MENU
    print('''

1. Add an Item
2. Back to Menu

''')

def del_menu():   ## FUNCTION DEL DATA MENU
    print('''

1. Delete an Item
2. Back to Menu

''')

def update_menu():  ## FUNCTION UPDATE DATA MENU
    print('''

1. Update an Item
2. Back to Menu

''')
    
def update_column():    ## FUNCTION UPDATE COLUMN AFTER SHOW DATA THAT USER WANT TO UPDATE
         print('''

1. Item Code
2. Name
3. Stock
4. Price
5. Category

''')
    
def read():      # FIRST MENU OF MAIN MENU : SHOW THE CHOICE'S OF ITEM
    while True:
            read_menu()
            option_read = input('Please input the number of menu you want to choose:')
            if option_read == '1': # FIRST MENU : FIRST : SHOW ITEM
                show()
            elif option_read == '2': # FIRST MENU : SECOND : SEARCH DATA
                search_id()
            elif option_read == '3': # FIRST MENU : THIRD : BACK TO MENU 
                break
            else:
                print('The number you entered is invalid')

def add_data():     ## FUNCTION ADD DATA
    while True:
        add_menu()
        option_add = input('Please input the number of menu you want to choose:')
        if option_add == '1':
            while True:
                item_code = input('Please input the item\'s code : ').upper().strip()
                if item_code.isalnum():
                    break
                else:
                    print('The item\'s code should be contain with alphabet and numeric')
            found = True
            for i in inventory:
                if item_code == i[0]:
                    found = False
                    break
            if not found:
                print ('Data already exists')
            else:
                while True:
                    item_name = input('Please input item\'s Name : ').capitalize().strip()
                    if item_name.replace(' ','').isalpha():
                        break
                    else:
                        print('The name of item should be contain with alphabet')
                while True:
                    item_stock = input('Please input item\'s Stock : ')
                    if item_stock.isdigit():
                        break
                    else:
                        print('The number of stock should be contain in digit')
                while True:
                    item_price = input('Please input item\'s price : ')
                    if item_price.isdigit():
                        break
                    else:
                        print('The number of stock should be contain in digit')
                while True:
                    item_category = input('Please input item\'s category : ').capitalize().strip()
                    if item_category.isalpha():
                        break
                    else:
                        print('The category\'s name should be contain alphabet')
                data = [item_code, item_name, item_stock, item_price, item_category]
                while True:
                    confirm_add = input('Are you sure to continue the update ? (Yes/No)').capitalize().strip()
                    if confirm_add == 'Yes':
                        inventory.append(data)
                        print('\nData succesfully added')
                        break
                    elif confirm_add == 'No':
                        print('Add data cancelled')
                        break
                    else:
                        print('The value you entered is not valid')
                        break
        elif option_add == '2': # SECOND MENU : THIRD : BACK TO MENU 
            break
        else:
            print('The number you entered is invalid') 

def search_id():    ## FUNCTION SEARCH DATA
    while True:
        if len(inventory) == 0:
            print('No stock available')
        else:
            stock_id = input('Please input item\'s code : ').upper().strip()
            found_stock = ''
            for goods in inventory:
                            if stock_id == goods[0]:
                                  found_stock = goods
            if found_stock:
                print('-------------------------------------------------')
                print('Item\'s Code\tName\t\tStock\tPrice\tCategory')
                print('-------------------------------------------------')
                for val in found_stock:
                    print(val, end='\t')
                break
            else:
                    print('The item\'s code you input is not found')

def del_data():     ## FUNCTION DEL DATA
      while True:
            del_menu()
            option_del = input('Please input the number of menu you want to choose:')
            if option_del == '1':
                item_index = ''
                is_not_found = True
                deleted = input('Please input item\'s code : ').upper().strip()
                is_deleted = ''
                for idx,goods in enumerate(inventory):
                        if deleted == goods[0]:
                             item_index = idx
                             is_deleted = goods
                             is_not_found = False
                             break      
                if not is_not_found:
                    print('\n---------------------------------------------------------')
                    print('Item\'s Code\tName\t\tStock\tPrice\tCategory')
                    print('---------------------------------------------------------')
                    for val in is_deleted:
                        print(val, end='\t')
                if is_not_found:
                    print('The data you are looking for does not exist')
                    continue
                else:
                    while True:
                            delete_notif = input('\n\nAre you sure to delete the data? (Yes/No)').capitalize().strip()
                            if delete_notif == 'No':
                                    print('Delete data cancelled')
                                    break
                            elif delete_notif == 'Yes':
                                    del inventory[item_index]
                                    print('\nData successfully deleted')
                                    break
                            else:
                                    print('The value you entered is not valid\n Please input again')
            elif option_del == '2': # SECOND MENU : THIRD : BACK TO MENU 
                break
            else:
                print('The number you entered is invalid')

def update_data():  # FUNCTION UPDATE DATA
    while True:
        update_menu()
        option_update = input('Please input the number of Menu you want to choose: ').upper().strip()
        new_item_code=''
        new_name=''
        new_price=''
        new_category=''
        new_stock=''       
        if option_update == '1':
                found_old_data = False
                if not inventory:
                    print('Data is not available')
                else:
                    item_code = input('Please input item\'s code : ').upper().strip()
                if not item_code.isalnum():
                    print('Item\'s code should contain number and alphabet')
                    continue

                found_data = ''
                for idx,goods_update in enumerate(inventory):
                    if goods_update[0] == item_code:
                        stock_idx = idx
                        found_data = goods_update
                if found_data:
                    print('-------------------------------------------------')
                    print('Item\'s Code\tName\t\tStock\tPrice\tCategory')
                    print('-------------------------------------------------')
                    for val in found_data:
                        print(val, end='\t')

                    while True:
                            update_notif = input('\n\nDo you want to update the data? (Yes/No)').lower().strip()
                            if update_notif == 'yes':
                                change_data = input('Please input the column data above that you want to update : ').lower().strip()
                                if change_data == 'item\'s code':
                                    while True:
                                        new_item_code = input('Please input the new item code : ').upper().strip()
                                        if new_item_code.isalnum() and new_item_code not in [goods_update[0] for goods_update in inventory]:
                                            break
                                        else:
                                            print('Item\'s code already exists or it should be contain numeric')
                                elif change_data == 'name':
                                    while True:
                                        new_name = input('Please input new name of item :').capitalize().strip()
                                        if new_name.replace(' ','').isalpha():
                                            break
                                        else:
                                            print('Item\'s name should be contain and has two words')
                                elif change_data == 'stock':
                                    while True:
                                        new_stock = input('Please input the stock that you want to input : ')
                                        if new_stock.isdigit():
                                            break
                                        else:
                                            print('The number of stock should be contain in digit')
                                elif change_data == 'price':
                                    while True:
                                        new_price = input('Please input the price of your new item : ')
                                        if new_price.isdigit():
                                            break
                                        else:
                                            print('The price of your new item should be contain in digit')
                                elif change_data == 'category':
                                    while True:
                                        new_category = input('Please input the category of your new item : ').capitalize().strip()
                                        if new_category.isalpha():
                                            break
                                        else:
                                            print('The cateory of your new item should be contain alphabet')
                                else:
                                    print('The data that you want to change is not valid')
                                    continue
                                while True:
                                    confirm = input('Are you sure to continue the update ? (Yes/No)').capitalize().strip()
                                    if confirm == 'Yes':
                                        if new_item_code != '':
                                            inventory[stock_idx][0] = new_item_code
                                        elif new_name != '':
                                            inventory[stock_idx][1] = new_name
                                        elif new_stock != '':
                                            inventory[stock_idx][2] = new_stock
                                        elif new_price != '':
                                            inventory[stock_idx][3] = new_price
                                        elif new_category != '':
                                            inventory[stock_idx][4] = new_category
                                        print('\nThe item successfully updated')
                                        break
                                    elif confirm == 'No':
                                        print('Update cancelled')
                                        break
                                    else:
                                        print('The value you entered is not valid')
                                break
                            elif update_notif == 'no':
                                print('Update cancelled')
                                break
                            else:
                                print('The value you entered is not valid\n Please input again')
                    
                    found_old_data = True

                if not found_old_data:
                    print('The item\'s code not found')                
        elif option_update == '2':
              break
        else:
            print('The number you entered is not valid')

def buy_item():     # FUNCTION BUY ITEM
    cart = []

    while True:
        print('''
        1. View all items
        2. Add an item to cart
        3. Delete an item from cart
        4. View cart
        5. Pay
        6. Back to Menu
        ''')

        option_cart = input('Please input the number of menu you want to choose: ')
        if option_cart == '1':
            print('------------------------------------------------------------')
            print('Item\'s Code\tName\t\tStock\tPrice\tCategory')
            print('------------------------------------------------------------')
            for goods in inventory:
                print(f'{goods[0]}\t{goods[1]}\t{goods[2]}\t{goods[3]}\t{goods[4]}')

        elif option_cart == '2':
            item_code = input('Enter the item code of the item you want to buy: ').upper().strip()
            found_item = None
            for item in inventory:
                if item[0] == item_code:
                    found_item = item
                    break
            if found_item:
                quantity_available = found_item[2]
                quantity_needed = int(input('Enter the quantity you want to buy: '))
                while quantity_needed > quantity_available:
                    print(f'Only {quantity_available} units available for this item.')
                    quantity_needed = int(input('Enter a valid quantity: '))
                cart.append({'item': found_item, 'quantity': quantity_needed})
                print(f'{quantity_needed} units of {found_item[1]} added to the cart.')
            else:
                print('Item code not found in the inventory.')

        elif option_cart == '3':
            print('-------------------------------------------------------------------------------------')
            print('Index\tItem\'s Code\tName\t\tStock\tPrice\tCategory\tQuantity')
            print('-------------------------------------------------------------------------------------')
            for idx, item in enumerate(cart):
                print(f'{idx}\t{item["item"][0]}\t{item["item"][1]}\t{item["item"][2]}\t{item["item"][3]}\t{item["item"][4]}\t\t{item["quantity"]}')
            item_idx = int(input('Enter the index of the item you want to remove: '))
            if 0 <= item_idx < len(cart):
                item = cart.pop(item_idx)
                print(f'{item["quantity"]} units of {item["item"][1]} removed from the cart.')
            else:
                print('Invalid item index.')

        elif option_cart == '4':
            print('-------------------------------------------------------------------------------------')
            print('Index\tItem\'s Code\tName\t\tStock\tPrice\tCategory\tQuantity')
            print('-------------------------------------------------------------------------------------')
            for idx, item in enumerate(cart):
                print(f'{idx}\t{item["item"][0]}\t{item["item"][1]}\t{item["item"][2]}\t{item["item"][3]}\t{item["item"][4]}\t\t{item["quantity"]}')

        elif option_cart == '5':
            total_price = sum(item["item"][3] * item["quantity"] for item in cart)
            print(f'Total Price: {total_price}')
            amount_paid = int(input('Enter the amount you want to pay: '))
            while amount_paid < total_price:
                print('Amount paid is not sufficient. Please pay the exact total amount.')
                amount_paid = int(input('Enter the amount you want to pay: '))
            change = amount_paid - total_price
            print(f'Thank you for your purchase! Your change: {change}')
            for item in cart:
                item_code = item["item"][0]
                quantity_bought = item["quantity"]
                for inv_item in inventory:
                    if inv_item[0] == item_code:
                        inv_item[2] -= quantity_bought
                        break
            cart.clear()

        elif option_cart == '6':
            break

        else:
            print('Invalid option. Please try again.')

while True:
    menu()  # function MAIN MENU
    option = input('Please input the number of menu you want to choose :')
    if option == '1':
        read()          # function READ DATA
    elif option == '2': 
        add_data()      # function ADD DATA
    elif option == '3':
        update_data()   # function UPDATE DATA
    elif option == '4':
        del_data()      # function DEL DATA
    elif option == '5':
        buy_item()      # function BUY ITEM
    elif option == '6':
        print('Thanks for visiting our Mini Store')
        break           # EXIT
    else:
        print('The number you entered is not valid') # invalid input