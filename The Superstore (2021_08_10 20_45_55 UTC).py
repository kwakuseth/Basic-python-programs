import os
import sys
from time import time
# This is going to be the first of its kind in my program list by creating an online store
def home():
    choice = None
    while choice != "0":
        print(
            """
Please select an option: 
    1. Buy an item
    2. Sell an item
    3. Check item's price
    0. Exit
"""
            )
        choice = input("Select an option: ")
        if choice == "0":
            print("Closing application...")
            from winsound import Beep
            Beep(650,1700)
            sys.exit()
        elif choice=="1":
            buy_an_item()
        elif choice=="2":
            sell_an_item()
        elif choice=="3":
            item_price()
        else:
            print("Selection Invalid")

            
def buy_an_item():
    choice=None
    while choice != "0":
        print(
    """Item Categories
        1. Cosmetics
        2. Food items
        3. Clothing
        0. Back
    """
        )
        choice = input("Please select a category: ")
        if choice == "0":
            return(home())
        elif choice == "1":
            print("COSMETICS")
            cosmetics()
        elif choice == "2":
            print("FOOD ITEMS")
            food_items()
        elif choice == "3":
            print("CLOTHINGS")
            clothing()
        else:
            print()
            print("Invalid choice! Re-enter your category.")
            print()
            buy_an_item()

def cosmetics():
    itemp={"sure men":12.00,"explore":37.00,"cocoa butter":24.00,"professional aircream":12.00}
    itemp['nivea men']=13

    items={1:'sure men', 2:'explore', 3:'cocoa butter',4:'professional aircream',5:'nivea men'}

    print("""ITEM LIST""")

    for item in items:
        price=itemp[items[item]]
        print(items[item],"-------", price)
    print()
    input("Press Enter key to continue")
    print("You can press 0 to go back to the previous page.")
    _item=eval(input("Select an item from the list: "))
    if _item!=0 and items.get(_item) in itemp:
        price=itemp[items.get(_item)]
        qnty=eval(input('Qunatity: '))
        print()
        order1=print("You bought",qnty, "of",items.get(_item),'which costs GH¢',price*qnty,"in total.")
    elif _item==0:
        buy_an_item()
    else:
        print("""ITEM LIST""")
        for item in items:
            price=itemp[items[item]]
            print(items[item],price)
        print()
        input("Press Enter key to continue")
        print("You can press 0 to go back to the previous page.")
        _item=eval(input("Select an item from the list: "))
        if _item!=0:
            price=itemp[items[item]]
            print(items.get(_item),price)
        
##    print(items[_item])
##    if items[_item] in itemp:
##        price = itemp[items[_item]]
##        qty = int(input("Quantity: "))
##        print(item, ":US$", price*qty)
##    elif _item=="0":
##        buy_an_item()
##    else:
##        print()
##        print("Invalid choice! Re-enter your choice.")
##        print()
##        cosmetics()

def food_items():
    items={"sure men":12.00,"explore":37.00,"cocoa butter":24.00,"professional air cream":12.00}#Changes required with list
    print("""ITEM LIST""")
    for item in items:
        price=items[item]
        print(item,"----",price)
    print()
    input("Press Enter key to continue")
    print("You can select 0 to go back to the previous page.")
    item=input("Select an item from the list: ")
    item=item.lower()
    if item in items:
        price = items[item]
        qty = int(input("Quantity: "))
        print(item, ":US$", price*qty)
    elif item=="0":
        buy_an_item()
    else:
        print("Input Invalid")
        cosmetics()

def clothing():
    items={"sure men":12.00,"explore":37.00,"cocoa butter":24.00,"professional air cream":12.00}#Changes required here
    print("""ITEM LIST""")
    for item in items:
        price=items[item]
        print(item,"----",price)
    print()
    input("Press Enter key to continue")
    print("You can select 0 to go back to the previous page.")
    item=input("Select an item from the list: ")
    item=item.lower()
    if item in items:
        price = items[item]
        qty = int(input("Quantity: "))
        print(item, ":US$", price*qty)
    elif item=="0":
        buy_an_item()
    else:
        print("Input Invalid")
        cosmetics()


def sell_an_item():
    print(
        """
        Service Unavailable
        """
    )
    home()

def item_price():
    food={"rice":""}


#main
print(
    """DE-LUX SUPERSTORE
    """
)
customer_name=input("Name of customer: ")
print()
print("Hello ",customer_name,", you are welcome to DE-LUX SUPERSTORE")
home()

