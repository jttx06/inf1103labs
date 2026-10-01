def get_valid_input():
    stock = input("Enter stock quantity or 'quit': ")

    if stock == "quit":
        return "quit"

    if stock.startswith("-") and stock[1:].isdigit():
        print("Error: Negative numbers are not allowed.")
        return None

    if not stock.isdigit():
        print("Error: Invalid input.")
        return None

    return int(stock)

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(total_deliveries, failed_attempts):
    print("Total Deliveries Processed:", total_deliveries)
    print("Number of Failed/Rejected Entries:", failed_attempts)


def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            lines = file.readlines()

            inventory = int(lines[0].strip())

            history = []
            for line in lines[1:]:
                if line.strip():
                    history.append(int(line.strip()))

            return inventory, history

    except FileNotFoundError:
        return 0, []

def save_inventory(inventory, history):
    with open("inventory.txt", "w") as file:
        file.write(str(inventory) + "\n")

        for transaction in history:
            file.write(str(transaction) + "\n")
    print("Inventory and transaction history saved to inventory.txt.")
 
inventory, transaction_history = load_inventory()
failed_entries = 0
deliveries_processed = 0

while True:

    stock = get_valid_input()

    if stock == "quit":
        print("Current Stock:", inventory)
        print("New Stock Added:", 0)
        print("Updated Inventory:", inventory)
        print("Tax:", tax)

        
        generate_report(deliveries_processed, failed_entries)
        save_inventory(inventory, transaction_history)
        break

    if stock is None:
        failed_entries += 1
        continue

    current_stock = inventory
    inventory = process_delivery(inventory, stock)
    transaction_history.append(stock)

    tax = calculate_tax(stock)
    
    print("Current Stock:", current_stock)
    print("New Stock Added:", stock)
    print("Updated Inventory:", inventory)
    print("Tax:", tax)

    deliveries_processed += 1

    if inventory > 500:
        print("ALERT: Inventory exceeds 500 units!")
        break

