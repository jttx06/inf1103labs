import json
import os

FILENAME = "inventory.json"


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


def display_all(inventory):
    print("Current Inventory")
    for item in inventory:
        print(
            f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}"
        )


if __name__ == "__main__":
    print("INVENTORY MANAGEMENT SYSTEM")
    inventory = load_inventory()
    display_all(inventory)

 # Initial Data Representation using a list of dictionaries
inventory = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]


def display_all(inventory):
    print("Current Inventory")
    for item in inventory:
        print(
            f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}"
        )


if __name__ == "__main__":
    display_all(inventory)