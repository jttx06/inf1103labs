inventory = 0
failed_entries = 0

# Keep asking for stock quantities continuously
while True:

    # Ask the user to enter a stock quantity
    stock = input("Enter stock quantity or 'quit': ")

    # Stop the loop if the user enters "quit"
    if stock == "quit":
        break