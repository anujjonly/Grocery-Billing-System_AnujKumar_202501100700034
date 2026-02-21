# Grocery Store Billing System

# Taking input for three items
item1 = float(input("Enter price of Item 1: "))
item2 = float(input("Enter price of Item 2: "))
item3 = float(input("Enter price of Item 3: "))

# Calculating total cost
total = item1 + item2 + item3

# Initializing discount
discount = 0

# Applying 10% discount if total exceeds $50
if total > 50:
    discount = total * 0.10

# Calculating final amount
final_amount = total - discount

# Displaying results
print("\n----- BILL SUMMARY -----")
print("Original Total: $", total)
print("Discount Applied: $", discount)
print("Final Payable Amount: $", final_amount)
