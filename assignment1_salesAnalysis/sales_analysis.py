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

# Uses an if/else statement to print whether total revenue is at least $500:
if total_revenue >= 500:
    print(f"Total revenue is ${total_revenue:,.2f}, which is equal or above $500.")
else:
    print(f"Total revenue is ${total_revenue:,.2f}, which is less than $500.")

# Produces the data per the recommendations:
# Recommendation 1: Promote Mobile Pre-Ordering to improve Service efficiency
transaction_6am_7am = 2612 #calculated through the formula in EXCEL, I've sorted 6:00:00-7:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_7am_8am = 7852 #calculated through the formula in EXCEL, I've sorted 7:00:00-8:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_8am_9am = 10543 #calculated through the formula in EXCEL, I've sorted 8:00:00-9:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_9am_10am = 10669 #calculated through the formula in EXCEL, I've sorted 9:00:00-10:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_10am_11am = 10867 #calculated through the formula in EXCEL, I've sorted 10:00:00-11:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_11am_12pm = 5664 #calculated through the formula in EXCEL, I've sorted 11:00:00-12:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_12pm_1pm = 4843 #calculated through the formula in EXCEL, I've sorted 12:00:00-13:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_1pm_2pm = 5135 #calculated through the formula in EXCEL, I've sorted 13:00:00-14:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_2pm_3pm = 5119 #calculated through the formula in EXCEL, I've sorted 14:00:00-15:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_3pm_4pm = 5248 #calculated through the formula in EXCEL, I've sorted 15:00:00-16:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_4pm_5pm = 5499 #calculated through the formula in EXCEL, I've sorted 16:00:00-17:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_5pm_6pm = 4940 #calculated through the formula in EXCEL, I've sorted 17:00:00-18:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_6pm_7pm = 4245 #calculated through the formula in EXCEL, I've sorted 18:00:00-19:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_7pm_8pm = 3597 #calculated through the formula in EXCEL, I've sorted 19:00:00-20:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
transaction_8pm_9pm = 326 #calculated through the formula in EXCEL, I've sorted 20:00:00-21:00:00 in the column of 'transaction_time', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'

hourly_transaction = [transaction_6am_7am, transaction_7am_8am, transaction_8am_9am, transaction_9am_10am, transaction_10am_11am, transaction_11am_12pm, 
                      transaction_12pm_1pm, transaction_1pm_2pm, transaction_2pm_3pm, transaction_3pm_4pm, transaction_4pm_5pm,
                      transaction_5pm_6pm, transaction_6pm_7pm, transaction_7pm_8pm, transaction_8pm_9pm]
morning_transactions = (transaction_7am_8am + transaction_8am_9am + transaction_9am_10am + transaction_10am_11am)
total_transactions = sum (hourly_transaction)
morning_share = morning_transactions / total_transactions

print(f"Morning transactions (7am-11am): {morning_transactions:,}")
print(f"Share of the day: {morning_share:.1%}")

# Recommendation 2: Offer Breakfast Bundles to Increase Average Order Value
item_1 = 87159 #calculated through the formula in EXCEL, I've sorted 1 item in the column of 'transaction_qty', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty'
item_2 = 58642 #calculated through the formula in EXCEL, I've sorted 2 items in the column of 'transaction_qty', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty' and divided by 2 to see the real transaction people
item_3 = 3279 #calculated through the formula in EXCEL, I've sorted 3 items in the column of 'transaction_qty', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty' and divided by 3 to see the real transaction people
item_4 = 23 #calculated through the formula in EXCEL, I've sorted 4 items in the column of 'transaction_qty', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty' and divided by 4 to see the real transaction people
item_6 = 3 #calculated through the formula in EXCEL, I've sorted 6 items in the column of 'transaction_qty', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty' and divided by 6 to see the real transaction people
item_8 = 10 #calculated through the formula in EXCEL, I've sorted 8 items in the column of 'transaction_qty', and then used '=SUBTOTAL(9,D2:D149117)' in the column of 'transaction_qty' and divided by 8 to see the real transaction people

items = [item_1, item_2, item_3, item_4, item_6, item_8]
total_items = sum (items)
item_1_share = item_1 / total_items
item_2_share = item_2 / total_items
share_1_or_2 = (item_1 + item_2) / total_items

print(f"People buying 1 item: {item_1:,} ({item_1_share:.1%})")
print(f"People buying 2 items: {item_2:,} ({item_2_share:.1%})")
print(f"People buying 1-2 items: {share_1_or_2:.1%}")
