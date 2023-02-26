# VARIABLES
product = input("Product: ")
count = int(input("Product count: "))
date = int(input("December: "))
date_state = ""
disscount = 0

# FIRST NEED TO CHECK IF BEFORE/AFTER 15 DEC
if (date <= 15):
    date_state = "before_15"
if (date > 15):
    date_state = "after_15"

    
# HOLD PRODUCTS PRICES TABLE
products = { "Cake": {'before_15': 24.00, 'after_15': 28.70},
          "Souffle": {'before_15': 06.66, 'after_15': 09.80},
          "Baklava": {'before_15': 12.60, 'after_15': 16.98}
           }

# HOLD THE CURRENT TEMP PRICE
current_price = count * products[product][date_state]

# ADD DISSCOUNTS
if (date <= 22):
    if current_price > 100 and current_price <= 200:
        current_price = current_price - (current_price * 0.15)
        
    if (current_price > 200):
        current_price = current_price - (current_price * 0.25)
        
    if (date <= 15):
        current_price = current_price - (current_price * 0.1)
    
print(current_price)