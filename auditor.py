inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity or 'quit': ")

    if stock == "quit":
        break

    if stock.isdigit():
        stock = int(stock)

        if stock < 0:
            print("Error: Negative numbers are not allowed.")
            failed_entries += 1
            continue

        inventory += stock
        print("Inventory:", inventory)

        if inventory > 500:
            print("ALERT: Inventory exceeds 500 units!")
            break

    else:
        print("Error: Invalid input.")
        failed_entries += 1
        continue

print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)