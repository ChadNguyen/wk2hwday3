# 1) Build a Shopping Cart

# You can use either lists or dictionaries. The program should have the following capabilities:
# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list


# 2) Stores user input into a dictionary or list
shopping_cart = []

def cart():
    while True:
        user_input = input('Choose an Option (add/delete/checkout)')
        if user_input == 'add':
                add_items = input('what items do you want to add? ')
                shopping_cart.append(add_items)
        if user_input == 'remove':
                del_items = input('What items do you need to remove? ')
                shopping_cart.pop(del_items)
        if user_input == 'checkout':
            break
        print(shopping_cart)
    return
cart()