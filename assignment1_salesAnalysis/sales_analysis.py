# Stores the following values in variables:
shop_name = "3 NYC Coffee Shops"
number_of_drinks_sold = 176444 #calculated through the formula in EXCEL, I've sorted coffee, tea and drinking chocolate in the column of 'product_category' as drinks, and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
price_per_drink = 3.054142353 #calculated through the formula in EXCEL, I've sorted coffee, tea and drinking chocolate in the column of 'product_category' as drinks, and then used '=SUBTOTAL(101, H2:H149117)' in the column of 'unit_price'
number_of_pastries_sold = 6961 #calculated through the formula in EXCEL, I've sorted pastry in the column of 'product_type', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
price_per_pastry = 3.685979456 #calculated through the formula in EXCEL, I've sorted pastry in the column of 'product_type', and then used '=SUBTOTAL(101, H2:H149117)' in the column of 'unit_price'

# Calculates drink and pastry revenue:
drink_revenue = number_of_drinks_sold * price_per_drink
pastry_revenue = number_of_pastries_sold * price_per_pastry
total_revenue = drink_revenue + pastry_revenue

# Prints the written .txt file
with open("sales_analysis.txt", "r") as file:
    print(file.read())
