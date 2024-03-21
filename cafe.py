# Read the README.txt file for the code explanation

#======================     Code    ========================

# Menu list
menu = ["Americano", "Cappuccino", "Latte", "Flat white"]

# Stock dictionary with stock value for each item
stock = {
    "Americano": 30,
    "Cappuccino": 40,
    "Latte": 40,
    "Flat white": 30,
}

# Price dictionary with price of each order of the menu item
price = {
    "Americano": 3.00,
    "Cappuccino": 4.25,
    "Latte": 4.50,
    "Flat white": 4.00,
}

# Sets a variable for total stock value in the sop as 0
total_stock = 0

# Uses a for loop to get each item value in the shop
# Then adds that item to the total value to get the final value
# of all the stock in the shop

for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

# Finally prints out the total value of the stock in the shop
print(f"The total stock value in the shop is: £{total_stock}")
