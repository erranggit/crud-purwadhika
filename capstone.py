inventory = [
    ['CG010107','Rokok Mild',17,24000, 'Rokok'],
    ['DR010107','Le Minerale',15,5000, 'Mineral Water'],
    ['SN010107','Chittato',19,14000, 'Snack']
]       ## DATA

def show(): ## FUNCTION SHOW DATA MENU
        if len(inventory) == 0:
            print('No Stock Available')
        else:
            print('--------------------------------------------------------')
            print('Item_Code\tName\t\tStock\tPrice\tCategory')
            print('--------------------------------------------------------')
            for goods in inventory:
                print(f'{goods[0]}\t{goods[1]}\t{goods[2]}\t{goods[3]}\t{goods[4]}')

def menu(): ## FUNCTION MAIN MENU
    print('''
    Welcome to Our Mini Store

    List Menu :
    
    1. Show the Choice of The Item(s) Menu
    2. Add Item(s)
    3. Delete Item(s)
    4. Make Change for Item(s)
    5. Buy Item(s)
    6. Exit Prorgam


    ''')

def first_menu():   ## FUNCTION CHOICE OF THE ITEM'S MENU
    print('''

1. Show Menu
2. Search Data
3. Back to Menu

''')
    
def read():
    while True:
            first_menu()
            option_0 = input('Please Input the Number of Menu You Want to Choose:')
            if option_0 == '1':
                show()
            elif option_0 == '2': # SECOND MENU : SECOND : SEARCH DATA
                search_id()
            elif option_0 == '3': # SECOND MENU : THIRD : BACK TO MENU 
                print('Back to menu')
                break
            else:
                print('The Number You Entered is Invalid')

def add_data():     ## FUNCTION ADD DATA
    item_code = input('Please input the Item\'s Code : ')
    found = True
    for i in inventory:
         if item_code == i[0]:
              found = False
              break
    if not found:
         print ('Data Already Exists')
    else:
        item_name = input('Please input Item\'s Name : ')
        item_stock = input('Please input Item\'s Stock : ')
        item_price = input('Please input Item\'s Price : ')
        item_category = input('Please input Item\'s Category : ')

        data = [item_code, item_name, item_stock, item_price, item_category]
        inventory.append(data)

def search_id():    ## FUNCTION SEARCH DATA
    while True:
        if len(inventory) == 0:
            print('No Stock Available')
        else:
            stock_id = input('Please Input Item\'s Code : ').upper().strip()
            found_stock = ''
            for goods in inventory:
                            if stock_id == goods[0]:
                                  found_stock = goods
            if found_stock:
                print('-------------------------------------------------')
                print('Item_Code\tName\t\tStock\tPrice\tCategory')
                print('-------------------------------------------------')
                for val in found_stock:
                    print(val, end='\t')
                break
            else:
                    print('The Item\'s Code You Input is Not Found')

def del_data():     ## FUNCTION DEL DATA
      while True:
            item_code = None
            is_found = True
            deleted = input('Please Input Item\'s Code : ').upper().strip()
            for idx, list in enumerate(inventory):
                  if deleted == list[0]:
                        item_code = idx
                        is_found = False
                        break
            if is_found:
                  print('Data Not Found')
                  break
            else:
                  while True:
                        delete_notif = input('Are you sure to delete the data? (Yes/No)').capitalize().strip()
                        if delete_notif == 'No':
                                return False
                        elif delete_notif == 'Yes':
                                del inventory[item_code]
                                print('The Item Successfully Deleted')
                                return True
                        else:
                                print('The Value You Entered is Not Valid\n Please Input Again')

while True:
    menu()
    option = input('Please Input Number :')
    if option == '1':  # FIRST 5 MENU : SHOW THE ITEM'S MENU
        read()
    elif option == '2': # SECOND FROM 5 MENU : ADD ITEM(S)
        add_data() # FUNCTION ADD DATA( kurang opsi kalau udahh ada primary keluar kata2 data exist )
    elif option == '3':
        del_data() # THIRD MENU : DEL DATA
    elif option == '4': # FOURTH MENU : EDIT
        print('belum dibuat')
    elif option == '5': # BUY ITEMS
        print('belum dibuat')
    elif option == '6': # EXIT
        print('Thanks for visiting our Mini Store')
        break
    else: # INVALID INPUT
        print('The Value You Entered is Not Valid')