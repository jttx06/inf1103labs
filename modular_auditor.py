inventory = 0
failed_entries = 0
deliveries_processed = 0

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

