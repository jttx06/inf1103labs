inventory = 0
failed_entries = 0

# Keep asking for stock quantities continuously
while True:

    # Ask the user to enter a stock quantity
    stock = input("Enter stock quantity or 'quit': ")

    # Stop the loop if the user enters "quit"
    if stock == "quit":
        break
     # Check if the user entered a negative number
    if stock.startswith("-") and stock[1:].isdigit():
        print("Error: Negative numbers are not allowed.")
        
        # Add 1 to the failed entries count
        failed_entries += 1
        
        # Go back to the start of the loop
        continue

    # Check if the input is not a valid number
    if not stock.isdigit():
        print("Error: Invalid input.")
        
        # Add 1 to the failed entries count
        failed_entries += 1
        
        # Go back to the start of the loop
        continue

    # Convert the stock from a string to an integer
    stock = int(stock)

      # Add the stock quantity to the total inventory
    inventory += stock

    # Display the current inventory     
    print("Inventory:", inventory)

    # Check if the inventory exceeds 500 units
    if inventory > 500:
        print("ALERT: Inventory exceeds 500 units!")
        
        # Stop the loop immediately
        break
# Display the final report
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)