import json
import os

# Ensures inventory.json is always saved in the exact same directory as the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(BASE_DIR, "inventory.json")


def load_inventory():
    """Check if inventory.json exists and load data, else return empty list."""
    if os.path.exists(FILENAME):
        print(f"{FILENAME} found.")
        try:
            with open(FILENAME, "r") as f:
                inventory = json.load(f)
                print("Inventory loaded successfully.\n")
                return inventory
        except json.JSONDecodeError:
            print("Error reading JSON file. Starting with empty inventory.\n")
            return []
    else:
        print(f"{FILENAME} not found. Starting with empty inventory.\n")
        return []

def save_inventory(inventory, quiet=False):
    """Save the current inventory list back to inventory.json."""
    if not quiet:
        print("Saving inventory...")
    with open(FILENAME, "w") as f:
        json.dump(inventory, f, indent=4)
    if not quiet:
        print(f"Inventory saved successfully to {FILENAME}.\n")


def display_all(inventory):
    print("Current Inventory")
    if not inventory:
        print("No items in inventory.\n")
        return
    for item in inventory:
        print(
            f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}"
        )
    print()

def add_product(inventory):
    print("\nAdd New Product")
    prod_id = input("Product ID: ").strip()

    for item in inventory:
        if item["id"].upper() == prod_id.upper():
            print("Product ID already exists!\n")
            return

    name = input("Product Name: ").strip()
    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid numerical input.\n")
        return

    inventory.append(
        {"id": prod_id, "name": name, "price": price, "stock": stock}
    )
    print("Product added successfully!\n")

def update_stock(inventory):
    print("\nUpdate Stock")
    prod_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item["id"].upper() == prod_id.upper():
            print(
                f"\nProduct Found:\nName: {item['name']}\nCurrent Stock: {item['stock']}\n"
            )
            try:
                item["stock"] = int(input("New Stock Quantity: "))
                print("\nStock updated successfully!\n")
            except ValueError:
                print("Invalid stock quantity input.\n")
            return

    print("\nProduct not found.\n")


def search_product(inventory):
    print("\nSearch Product")
    prod_id = input("Enter Product ID: ").strip()

    for item in inventory:
        if item["id"].upper() == prod_id.upper():
            print("\nProduct Found")
            print("-" * 40)
            print(f"ID: {item['id']}")
            print(f"Name: {item['name']}")
            print(f"Price: ${item['price']:.2f}")
            print(f"Stock: {item['stock']}")
            print("-" * 40 + "\n")
            return

    print("\nProduct not found.\n")

def main():
    print("INVENTORY MANAGEMENT SYSTEM")
    inventory = load_inventory()

    while True:
        print("MENU")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")

        choice = input("Enter option: ").strip()

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            add_product(inventory)
        elif choice == "3":
            update_stock(inventory)
        elif choice == "4":
            search_product(inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory, quiet=True)
            print("Inventory saved successfully.\n")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    main()