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

 

inventory = 0
failed_entries = 0
deliveries_processed = 0

while True:

    stock = get_valid_input()

    if stock == "quit":
        generate_report(deliveries_processed, failed_entries)
        break

    if stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)

    tax = calculate_tax(stock)

    print("Inventory:", inventory)
    print("Tax:", tax)

    deliveries_processed += 1

    if inventory > 500:
        print("ALERT: Inventory exceeds 500 units!")
        break

